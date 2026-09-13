# KẾ HOẠCH TRIỂN KHAI — SMART SAFETY MONITORING SYSTEM (EDGE AI & IOT)

> **Tham chiếu nghiệp vụ**: [doc.md](doc.md)  
> **Kiến trúc cốt lõi**: `Camera USB` ➔ `Pi 5 (AI nhận dạng Người -> Áo -> Mũ)` ➔ `Logic quyết định & Cảnh báo còi/đèn tại chỗ` ➔ `MQTT Broker (Payload JSON)` ➔ `Backend (FastAPI + PostgreSQL)` ➔ `WebSocket Broadcast` ➔ `Web Dashboard realtime`

---

# PHẦN A — KIẾN TRÚC VÀ LUỒNG HOẠT ĐỘNG CHI TIẾT

## 1. Sơ đồ luồng xử lý toàn hệ thống

```text
  [ CAMERA USB ]
        │  (Khung hình video /dev/video0)
        ▼
┌────────────────────────────────────────────────────────────────────────┐
│  RASPBERRY PI 5 (EDGE AI & CONTROLLER)                                 │
│                                                                        │
│  1. Nhận dạng thị giác phân tầng (Hierarchical Inference):             │
│     [Phát hiện Người (Person)]                                         │
│            │                                                           │
│            ├── Có người ──► Cắt vùng thân trên (Upper-body ROI)        │
│            │                      │                                    │
│            │                      ├── Nhận diện Áo bảo hộ (Vest)?      │
│            │                      └── Nhận diện Mũ bảo hộ (Hardhat)?   │
│            │                                                           │
│  2. Phân tích & Quyết định (Decision Engine):                          │
│     - Kiểm tra trạng thái: has_vest (true/false), has_hardhat (true/false)
│     - Bộ lọc chống nhiễu (Persistence Filter): vi phạm liên tục ≥ 3 frame│
│     - Bật actuator cảnh báo tức thì: LED đỏ chớp + Còi buzzer ngắt quãng│
│                                                                        │
│  3. Đóng gói & Xuất bản (MQTT Client):                                │
│     - Topic: safety/edge/EDGE_01/alert                                 │
│     - Payload: JSON { person, has_vest, has_hardhat, status... }       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                         Mạng Wi-Fi / LAN (MQTT QoS 1)
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  CENTRAL PLATFORM (BACKEND & DATABASE)                                 │
│                                                                        │
│  1. Mosquitto MQTT Broker: Xác thực user/pass, nhận & định tuyến tin   │
│  2. FastAPI Service (Python):                                          │
│     - MQTT Subscriber nhận chuỗi JSON từ Edge                          │
│     - Ghi nhận vi phạm vào PostgreSQL (chống trùng lặp - Dedup)        │
│     - Đẩy bản tin realtime qua WebSocket                              │
│     - Cung cấp REST API cho Dashboard tra cứu/xác nhận vi phạm         │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                         WebSocket / HTTP REST
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  HSE WEB DASHBOARD                                                     │
│                                                                        │
│  - Popup cảnh báo vi phạm chớp đỏ tức thì kèm âm thanh báo động        │
│  - Hiển thị trực quan trạng thái từng công nhân: Áo (Đạt/Lỗi), Mũ (Đạt/Lỗi)│
│  - Ảnh chụp bằng chứng (Snapshot) lúc vi phạm                          │
│  - Nút Xác nhận (CONFIRMED) hoặc Hủy báo động giả (DISMISSED)          │
│  - Báo cáo thống kê vi phạm theo ngày/giờ                              │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Đặc tả gói tin dữ liệu MQTT (JSON Payloads)

### 2.1. Cảnh báo vi phạm an toàn (`safety/edge/{device_id}/alert`)
Đúng theo luồng nghiệp vụ: Nhận diện Người ➔ Áo ➔ Mũ:
```json
{
  "device_id": "EDGE_PI5_01",
  "timestamp": "2026-09-12T08:30:15Z",
  "person_detected": true,
  "has_vest": false,
  "has_hardhat": true,
  "violation_type": "NO_VEST",
  "confidence": {
    "person": 0.95,
    "vest": 0.88,
    "hardhat": 0.92
  },
  "zone_name": "Khu_vuc_cau_thap_A",
  "actuator_triggered": true,
  "image_snapshot": "snapshot_EDGE_01_20260912_083015.jpg"
}
```
*Quy ước `violation_type`:*
- `NO_VEST`: Có người, có mũ, không áo
- `NO_HARDHAT`: Có người, có áo, không mũ
- `NO_PPE`: Có người, thiếu cả áo và mũ
- `DANGER_ZONE`: Xâm nhập khu vực cấm

### 2.2. Trạng thái thiết bị định kỳ (`safety/edge/{device_id}/telemetry`)
Gửi mỗi 60 giây để giám sát tình trạng Pi 5:
```json
{
  "device_id": "EDGE_PI5_01",
  "status": "online",
  "cpu_temp_c": 52.4,
  "fps": 7.5,
  "timestamp": "2026-09-12T08:31:00Z"
}
```

---

# PHẦN B — KẾ HOẠCH TRIỂN KHAI CHI TIẾT (8 TUẦN)

> **Chiến lược thông minh**: *Phần mềm & Simulator trước ➔ AI & Camera trên PC ➔ Port lên Pi 5 + Còi/Đèn ➔ Tích hợp trọn gói.* Giúp việc debug nhanh gọn, không bị phụ thuộc phần cứng ở những bước đầu.

```text
Tuần 1-2: Backend (FastAPI + PostgreSQL) + Dashboard Web (Test bằng Simulator)
Tuần 3-4: Xây dựng bộ nhận dạng AI (Người -> Áo -> Mũ) trên PC bằng Webcam
Tuần 5  : Port lên Raspberry Pi 5 + Đấu nối GPIO Còi/Đèn LED
Tuần 6  : Tích hợp toàn hệ thống End-to-End & Thử nghiệm liên tục
Tuần 7  : Đo đạc chỉ số kỹ thuật & Đánh giá người dùng (Design Thinking)
Tuần 8  : Hoàn thiện vòng lặp v2, làm báo cáo & Quay video demo
```

---

## Giai đoạn 0 — Chuẩn bị môi trường & Thiết bị (Đầu tuần 1)

| Hạng mục | Chi tiết thực hiện |
|---|---|
| **Máy tính cá nhân** | Cài Python 3.11+, PostgreSQL, Mosquitto MQTT Broker, VS Code |
| **Cơ sở dữ liệu** | Cài PostgreSQL, chạy lệnh tạo DB: `createdb safety_events` |
| **Phần cứng sẵn có** | Raspberry Pi 5 (8GB hoặc 4GB RAM) kèm nguồn chuẩn 27W USB-C PD |
| **Phần cứng mua bổ sung** | - USB Webcam UVC (Plug & Play, 720p/1080p, ~400k - 600k)<br>- Breadboard, 1 LED đỏ 5mm, 1 điện trở 220Ω, 1 Còi Active Buzzer 5V, dây cắm Dupont (~50k) |
| **Dữ liệu huấn luyện AI** | Dataset PPE gồm 3 nhãn: `person`, `vest`, `hardhat` (Roboflow PPE Dataset) |

---

## Giai đoạn 1 — Xây dựng Backend & Cơ sở dữ liệu PostgreSQL (Tuần 1 - 2)

Mục tiêu: Xây dựng trung tâm tiếp nhận MQTT, lưu trữ vi phạm vào PostgreSQL và phát WebSocket lên UI.

| Bước | Nội dung công việc | File đích | Đầu ra kiểm tra |
|---|---|---|---|
| **1.1** | Tạo cấu trúc bảng PostgreSQL (Devices, Zones, SafetyEvents, Telemetry) | `backend/database.py` | Chạy script tạo bảng thành công trong PostgreSQL |
| **1.2** | Cấu hình Broker Mosquitto & xác thực kết nối | `mosquitto.conf`, `.env` | Kết nối MQTT bảo mật bằng user/password |
| **1.3** | Dịch vụ MQTT Subscriber xử lý chuỗi JSON `has_vest`, `has_hardhat` | `backend/mqtt_service.py` | Bóc tách đúng JSON, lưu bản ghi và ảnh snapshot |
| **1.4** | Cơ chế chống trùng tin (QoS 1 Dedup) & WebSocket Bridge | `backend/main.py` | Đẩy sự kiện realtime tới các client kết nối `/ws` |
| **1.5** | REST API tra cứu danh sách vi phạm, xử lý Xác nhận/Hủy, xuất CSV | `backend/routes.py` | Gọi test API qua Swagger UI (`http://localhost:8000/docs`) |

---

## Giai đoạn 2 — Giao diện Web Dashboard trực quan (Tuần 2 - 3)

Mục tiêu: Cán bộ giám sát an toàn (HSE) nhận cảnh báo tức thời, xem trạng thái vi phạm áo/mũ và thao tác xác nhận.

| Bước | Nội dung công việc | Giao diện / Chức năng |
|---|---|---|
| **2.1** | Giao diện tương phản cao (High-contrast Dark Mode) cho công trường | `dashboard/index.html` (TailwindCSS) |
| **2.2** | Khung Banner cảnh báo khẩn cấp (Pulsing Red) + Âm thanh bip khi có vi phạm mới | Banner đỏ nhảy ra hiển thị vị trí, loại vi phạm (`Thiếu mũ`/`Thiếu áo`) |
| **2.3** | Thẻ vi phạm chi tiết: Ảnh bằng chứng + Tag trạng thái `Áo: FAIL`, `Mũ: FAIL` | Thể hiện trực quan rõ ràng từng mục trang bị an toàn |
| **2.4** | Thao tác xử lý sự cố 1 chạm cho cán bộ HSE | 2 nút bấm: `Xác nhận vi phạm` (CONFIRMED) & `Bỏ qua/Cảnh báo giả` (DISMISSED) |
| **2.5** | Kịch bản kiểm thử giả lập không cần phần cứng | Chạy `tests/simulate_edge.py` đẩy dữ liệu giả lập để nghiệm thu toàn bộ Web |

---

## Giai đoạn 3 — Xây dựng mô hình AI nhận diện (Người ➔ Áo ➔ Mũ) trên PC (Tuần 3 - 4)

Mục tiêu: Xây dựng luồng thị giác máy tính chính xác, kiểm tra ngay trên webcam máy tính cá nhân trước khi nạp vào Pi.

```text
Luồng xử lý trên từng khung hình (Frame):
1. Detect Person: Xác định bounding box người (x1, y1, x2, y2)
2. Crop ROI Thân trên & Đầu của người đó
3. Classify/Detect PPE:
   - Vùng đầu: Có mũ (hardhat: true/false)?
   - Vùng ngực/thân: Có áo phản quang (vest: true/false)?
4. Persistence Check: Vi phạm kéo dài ≥ 3 frame liên tiếp -> Xác nhận Vi phạm thật!
```

| Bước | Công việc chi tiết | Ghi chú kỹ thuật |
|---|---|---|
| **3.1** | Lấy luồng video từ Webcam qua OpenCV | `cv2.VideoCapture(0)` ổn định, tốc độ khung hình 15-30 FPS |
| **3.2** | Tải và cấu hình model YOLOv8 PPE (Person, Vest, Hardhat) | Sử dụng YOLOv8-nano (`yolov8n.pt`) để tối ưu tốc độ |
| **3.3** | Xây dựng logic phân tầng (Hierarchical Inference) | Chỉ khi phát hiện `person` mới quét tiếp `vest` và `hardhat` trong phạm vi box người |
| **3.4** | Tích hợp thuật toán lọc nhiễu khung hình (Persistence Filter) | Tránh trường hợp camera chớp khung hình hoặc người cúi đầu bị báo sai |
| **3.5** | Đóng gói JSON và Publish bản tin MQTT lên Broker | `paho-mqtt` gửi chuỗi `has_vest`, `has_hardhat` kèm ảnh snapshot |

**Tiêu chí hoàn thành**: Ngồi trước Webcam máy tính:
- Bỏ mũ / cởi áo bảo hộ ➔ Màn hình console in ra: `[ALERT] has_vest: false, has_hardhat: true`
- Gói tin MQTT tự động gửi về Backend ➔ Dashboard lập tức chớp đỏ cảnh báo.

---

## Giai đoạn 4 — Port mã nguồn lên Raspberry Pi 5 & Đấu nối GPIO Còi/Đèn (Tuần 5)

Mục tiêu: Chuyển toàn bộ mã nguồn sang chạy độc lập trên phần cứng Pi 5 ngoài hiện trường.

| Bước | Nội dung công việc | Sơ đồ & Chỉ dẫn kỹ thuật |
|---|---|---|
| **4.1** | Cài đặt hệ điều hành Raspberry Pi OS (64-bit) & môi trường Python | Cài đặt OpenCV, Ultralytics, Paho-MQTT, RPi.GPIO |
| **4.2** | Cắm USB Webcam vào Pi 5 và kiểm tra luồng video | Lệnh kiểm tra: `v4l2-ctl --list-devices` |
| **4.3** | Đấu nối phần cứng Còi & Đèn báo động: | - **LED đỏ**: Pin GPIO 17 (Chân vật lý 11) nối tiếp trở 220Ω ➔ Anode (+), GND (Chân 9) ➔ Cathode (-)<br>- **Buzzer 5V**: Pin GPIO 27 (Chân vật lý 13) ➔ VCC/Signal, GND (Chân 14) ➔ GND |
| **4.4** | Lập trình logic báo động 2 pha (Thiết kế theo phản hồi thực tế): | - **Pha 1**: Đèn LED đỏ nhấp nháy 2 giây (Cảnh báo thị giác tại chỗ)<br>- **Pha 2**: Còi Buzzer kêu ngắt quãng bip...bip...bip trong 3 giây (Cảnh báo âm thanh) |
| **4.5** | Tối ưu hóa hiệu năng trên Pi 5 | Chuyển đổi mô hình sang ONNX runtime (`imgsz=416`), duy trì FPS từ 6 - 9 FPS |

---

## Giai đoạn 5 — Đóng gói, Vận hành tự động & Tích hợp hoàn chỉnh (Tuần 6)

| Bước | Nội dung công việc | Chi tiết |
|---|---|---|
| **5.1** | Viết file cấu hình dịch vụ tự khởi động (Systemd Services) | Khi bật nguồn Pi 5 hoặc Server, hệ thống tự động chạy ngầm mà không cần gõ lệnh |
| **5.2** | Thử nghiệm độ bền (Stress test 12 giờ) | Chạy camera liên tục 12 tiếng để kiểm tra nhiệt độ CPU của Pi 5 và việc tràn bộ nhớ RAM |
| **5.3** | Đóng hộp bảo vệ vật lý cho Raspberry Pi 5 | Gắn quạt tản nhiệt chủ động (Active Cooler) cho Pi 5 tránh quá nhiệt khi chạy AI liên tục |
| **5.4** | Quay video minh chứng hoạt động (Demo Video 3 - 5 phút) | Thể hiện đầy đủ luồng từ phát hiện người, kiểm tra áo/mũ, còi hú tại chỗ đến dashboard cập nhật |

---

## Giai đoạn 6 — Đo lường kỹ thuật & Đánh giá theo Design Thinking (Tuần 7)

Thực hiện đo đạc các số liệu thực tế để đưa vào báo cáo nghiệm thu đồ án:

| Chỉ số đánh giá | Cách thức đo lường | Mục tiêu kỳ vọng |
|---|---|---|
| **Độ chính xác phát hiện (Precision/Recall)** | Đóng giả 50 lần vi phạm (quên mũ, quên áo, đi vào khu vực cấm) | Đạt ≥ 85% độ chính xác |
| **Độ trễ cảnh báo tại chỗ (Local Latency)** | Từ lúc vi phạm đến khi còi/đèn tại Pi kích hoạt | Dưới 1.0 giây |
| **Độ trễ truyền mạng lên Dashboard** | Từ lúc vi phạm đến khi Web Dashboard chớp đỏ | Dưới 1.5 giây |
| **Tỷ lệ thất thoát tin nhắn MQTT** | Kiểm tra số sự kiện ghi nhận tại Backend so với số lần phát hiện | 100% nhờ cơ chế MQTT QoS 1 |
| **Khảo sát trải nghiệm người dùng (UX)** | Cho 2 cán bộ HSE và 3 người đóng vai công nhân tương tác thử | Đánh giá mức độ rõ ràng của âm thanh và giao diện |

---

## Giai đoạn 7 — Hoàn thiện Báo cáo v2 & Bảo vệ Capstone (Tuần 8)

1. Tổng hợp bảng đối chiếu chỉ số kỹ thuật đạt được so với mục tiêu ban đầu.
2. Hoàn thiện tài liệu thuyết minh đồ án (`doc.md`) theo chuẩn phương pháp Design Thinking.
3. Xuất file báo cáo lịch sử vi phạm ra định dạng Excel/CSV làm bằng chứng nghiệm thu.
4. Chuẩn bị Slide thuyết trình bảo vệ đồ án trước hội đồng.

---

# PHẦN C — THIẾT KẾ CƠ SỞ DỮ LIỆU POSTGRESQL

## C.1. Sơ đồ thực thể quan hệ (ERD)

```text
┌─────────────────────────────────────────────────────────┐
│                       devices                           │  (Trạm Edge Pi 5 tại hiện trường)
│  PK device_id                                           │
│     name, location, ip_address, status, last_ping       │
└──────────────────────────┬──────────────────────────────┘
                           │ 1
                           │
                           │ n
┌──────────────────────────┴──────────────────────────────┐
│                    safety_events                        │  (Bảng trung tâm lưu sự kiện vi phạm)
│  PK id (Identity)                                       │
│  FK device_id ──────────────────────────────────────────┘
│     timestamp, violation_type                           │
│     person_detected (bool), has_vest (bool), has_hardhat (bool)
│     confidence, zone_name, image_url                    │
│     status ('NEW', 'CONFIRMED', 'DISMISSED')            │
│     resolved_by (text), resolved_at                     │
│     UNIQUE(device_id, timestamp, violation_type)        │  (Chống trùng tin do mạng chập chờn)
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                      telemetry                          │  (Nhật ký nhiệt độ/FPS của Pi 5)
│  PK id (Identity)                                       │
│  FK device_id                                           │
│     timestamp, cpu_temp_c, fps, status                  │
└─────────────────────────────────────────────────────────┘
```

## C.2. Tập lệnh khởi tạo DDL (PostgreSQL)

```sql
-- 1. Bảng quản lý trạm Edge Pi 5
CREATE TABLE devices (
    device_id        TEXT PRIMARY KEY,
    name             TEXT NOT NULL,
    location         TEXT,
    ip_address       TEXT,
    firmware_version TEXT,
    status           TEXT DEFAULT 'offline',
    last_ping        TIMESTAMP,
    created_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Bảng cấu hình vùng nguy hiểm (Polygon chuẩn hóa 0.0 - 1.0)
CREATE TABLE zones_config (
    zone_id             TEXT PRIMARY KEY,
    device_id           TEXT REFERENCES devices(device_id),
    name                TEXT NOT NULL,
    polygon_coords_json TEXT NOT NULL,
    is_active           BOOLEAN DEFAULT TRUE,
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Bảng lưu trữ chi tiết sự kiện vi phạm (Đúng logic Người -> Áo -> Mũ)
CREATE TABLE safety_events (
    id              GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    device_id       TEXT NOT NULL REFERENCES devices(device_id),
    timestamp       TIMESTAMP NOT NULL,
    person_detected BOOLEAN DEFAULT TRUE,
    has_vest        BOOLEAN NOT NULL,
    has_hardhat     BOOLEAN NOT NULL,
    violation_type  TEXT NOT NULL,
    confidence      REAL,
    zone_name       TEXT,
    image_url       TEXT,
    status          TEXT DEFAULT 'NEW' CHECK (status IN ('NEW', 'CONFIRMED', 'DISMISSED')),
    resolved_by     TEXT,
    resolved_at     TIMESTAMP,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Ràng buộc chống trùng lặp dữ liệu từ MQTT QoS 1
    CONSTRAINT uidx_event_dedup UNIQUE (device_id, timestamp, violation_type)
);

CREATE INDEX idx_events_timestamp ON safety_events(timestamp DESC);
CREATE INDEX idx_events_status ON safety_events(status);
CREATE INDEX idx_events_device_time ON safety_events(device_id, timestamp);

-- 4. Bảng dữ liệu viễn trắc (Giám sát sức khỏe phần cứng Pi 5)
CREATE TABLE telemetry (
    id         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    device_id  TEXT REFERENCES devices(device_id),
    timestamp  TIMESTAMP NOT NULL,
    cpu_temp_c REAL,
    fps        REAL,
    status     TEXT
);

CREATE INDEX idx_telemetry_time ON telemetry(timestamp DESC);
```

---

# PHẦN D — QUẢN TRỊ RỦI RO & PHƯƠNG ÁN XỬ LÝ

| Rủi ro kỹ thuật | Mức độ | Biện pháp giảm thiểu |
|---|---|---|
| **Pi 5 chạy nhận diện nhiều nhãn (người, áo, mũ) bị giật lag (< 4 FPS)** | Cao | 1. Chỉ chạy mô hình YOLOv8-nano.<br>2. Xuất sang định dạng ONNX Runtime tối ưu CPU ARM64.<br>3. Giảm kích thước ảnh đầu vào về 416x416.<br>4. Chỉ nhận diện áo/mũ sau khi đã tìm thấy `person`. |
| **Báo động giả do công nhân cúi người khuất mũ/áo** | Trung bình | Dùng thuật toán **Persistence Filter**: Vi phạm phải tồn tại liên tục trong 3 khung hình liên tiếp mới kích hoạt còi/đèn và gửi MQTT. |
| **Mất kết nối mạng Wi-Fi ngoài công trường** | Thấp | Pi 5 xử lý AI và kích hoạt Còi/Đèn hoàn toàn tại chỗ (Edge). Khi có mạng trở lại, tin nhắn MQTT QoS 1 sẽ tự động đồng bộ về máy chủ. |
| **Nhiệt độ Pi 5 tăng cao gây giảm xung nhịp (Thermal Throttling)** | Trung bình | Trang bị vỏ nhôm tản nhiệt có quạt điều tốc tự động (Active Cooler). Bảng `telemetry` liên tục giám sát nhiệt độ CPU. |
