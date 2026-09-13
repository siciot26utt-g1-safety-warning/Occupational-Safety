# Smart Safety Monitoring System — Hệ thống Giám sát An toàn Lao động IoT

Capstone IoT theo phương pháp Design Thinking. Chi tiết thiết kế xem `doc.md`.

## Kiến trúc

```text
[Camera USB] → [Pi 5: YOLOv8 + GPIO còi/đèn] → MQTT → [Backend FastAPI + PostgreSQL] → [Web Dashboard]
```

## Cấu trúc thư mục

```
edge/          Chạy trên Raspberry Pi 5 (Python + OpenCV + YOLOv8)
backend/       FastAPI + MQTT subscriber + PostgreSQL + WebSocket
dashboard/     Web UI (HTML + TailwindCSS, high-contrast cho ngoài trời)
tests/         simulate_edge.py - mô phỏng Edge device không cần phần cứng
```

## Cài đặt & Chạy demo

### 1. Cài Mosquitto MQTT broker

```bash
# Windows: tải từ mosquitto.org, chạy:
mosquitto -v
# Pi 5:
sudo apt install mosquitto mosquitto-clients
```

Tạo user `edge01` / `edge_secret`:
```bash
mosquitto_passwd -c passwd.txt edge01   # nhập edge_secret
# thêm vào mosquitto.conf: password_file passwd.txt, allow_anonymous false
```

### 2. Chạy Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 3. Test bằng simulator (không cần phần cứng)

```bash
cd tests
pip install paho-mqtt
python simulate_edge.py
# Mở http://localhost:8000 — Dashboard sẽ nhận cảnh báo realtime
```

### 4. Chạy Edge thật trên Pi 5

```bash
cd edge
pip install -r requirements.txt
python detection.py   # cần config.json trỏ đúng broker + camera_index
```

## Tuần tự triển khai trên Pi 5 (theo lộ trình)

1. **Bước 1**: Cài Raspberry Pi OS 64-bit + OpenCV + Ultralytics. Test webcam: `python -c "import cv2; cap=cv2.VideoCapture(0); print(cap.isOpened())"`
2. **Bước 2**: Tải YOLOv8n pretrain, test nhận diện `person`. Sau đó fine-tune với dataset PPE (hardhat) — khuyến nghị dataset có sẵn: [PPE Detection on Roboflow](https://public.roboflow.com/object-detection/hard-hat-workers)
3. **Bước 3**: Nối GPIO (LED pin 17, Buzzer pin 27 theo `edge/detection.py`), test `trigger_alert()`
4. **Bước 4**: Chạy end-to-end: Edge + Mosquitto + Backend + Dashboard

## API chính

| Endpoint | Mô tả |
|---|---|
| `GET /api/events` | Danh sách sự kiện vi phạm |
| `POST /api/events/{id}/resolve?action=CONFIRMED\|DISMISSED` | HSE xác nhận/hủy cảnh báo |
| `GET /api/events/export` | Xuất CSV báo cáo |
| `GET /api/stats/daily` | Thống kê vi phạm 7 ngày |
| `GET /api/devices` | Trạng thái Edge devices |
| `WS /ws` | WebSocket nhận cảnh báo realtime |

## MQTT Topics

- `safety/edge/{device_id}/telemetry` — heartbeat 60s
- `safety/edge/{device_id}/alert` — cảnh báo vi phạm
- `safety/edge/{device_id}/command` — lệnh điều khiển từ xa (chưa dùng ở demo)
