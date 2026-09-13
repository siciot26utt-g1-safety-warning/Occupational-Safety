# TÀI LIỆU ĐỀ TÀI IoT THEO PHƯƠNG PHÁP DESIGN THINKING
## Tên đề tài gợi ý: Hệ thống IoT giám sát an toàn lao động thông minh (Smart Safety Monitoring System for Construction & Industrial Sites)

---

# PHẦN 1 — PROBLEM & CONTEXT

### 1.1. Bối cảnh 
- **Vấn đề xảy ra ở đâu**: Tại các công trường thi công xây dựng, nhà xưởng công nghiệp, và khu vực đang tiến hành bảo trì, sửa chữa máy móc thiết bị có nguy cơ cao.
- **Đối tượng gặp vấn đề**: 
  - *Người lao động / Công nhân*: Nguy cơ trực tiếp về tính mạng, thương tật, tổn hại sức khỏe lâu dài.
  - *Chủ thầu / Doanh nghiệp / Cán bộ quản lý an toàn*: Trách nhiệm pháp lý nghiêm trọng, đình chỉ dự án, gánh nặng chi phí bồi thường và thiệt hại uy tín.
- **Thời điểm xảy ra**: Diễn ra liên tục trong suốt ca làm việc, đặc biệt vào các thời điểm cao điểm thi công, khi công nhân mệt mỏi, mất tập trung hoặc giám sát viên vắng mặt.
- **Cách xử lý hiện tại**: Ban hành nội quy văn bản, treo biển cảnh báo tĩnh, và cử cán bộ chuyên trách (HSE) đi tuần tra giám sát trực tiếp tại hiện trường.
- **Điểm bất tiện, rủi ro và tốn kém**:
  - *Kém hiệu quả và không có tính phòng ngừa chủ động*: Giám sát con người chỉ mang tính thời điểm, không bao quát 24/7; khi phát hiện thì sự việc đã rồi. Biển báo tĩnh nhanh chóng bị người lao động phớt lờ theo thói quen.
  - *Bất tiện trong vận hành*: HSE chịu áp lực quản lý căng thẳng, dễ xảy ra mâu thuẫn tranh cãi khi nhắc nhở mà không có bằng chứng ghi nhận khách quan.

### 1.2. Mục tiêu ban đầu
- **Đối với cán bộ quản lý an toàn (HSE) và chủ thầu**: Giúp họ phát hiện ngay lập tức các hành vi làm việc thiếu an toàn (ví dụ: không đội mũ bảo hộ lao động) hoặc khi có người xâm nhập vào vùng nguy hiểm (vùng bán kính cần cẩu, hố sâu, khu vực điện cao thế). Qua đó, người quản lý có thể can thiệp kịp thời để ngăn chặn tai nạn trước khi xảy ra, đồng thời tự động ghi nhận nhật ký vi phạm làm bằng chứng tuân thủ quy định an toàn, giảm thiểu rủi ro pháp lý.
- **Đối với người lao động**: Giúp họ nhận được cảnh báo phản hồi tức thời ngay tại khoảnh khắc bước vào vùng rủi ro hoặc quên trang bị bảo hộ, từ đó kịp thời tự điều chỉnh hành vi để bảo vệ tính mạng, sức khỏe của chính mình.

### 1.3. Yêu cầu cần đạt
- **User (Người dùng)**: Cán bộ giám sát an toàn (HSE), người lao động và chủ doanh nghiệp.
- **Problem (Vấn đề)**: Không thể giám sát liên tục để phát hiện tức thời các rủi ro nguy cấp như người lao động lơ là không sử dụng đồ bảo hộ hoặc bước vào khu vực nguy hiểm bị cấm.
- **Context (Bối cảnh)**: Tại các công trình xây dựng rộng lớn hoặc khu vực bảo trì phức tạp, có nhiều tổ đội làm việc đan xen và người giám sát không thể bao quát toàn bộ 24/7.
- **Consequence (Hậu quả)**: Tai nạn lao động xảy ra gây thương vong, kéo theo đình chỉ thi công dự án, thiệt hại tài chính nặng nề (bồi thường tai nạn, chi phí y tế) và rủi ro truy cứu trách nhiệm hình sự đối với người quản lý.

---

# PHẦN 2 — EMPATHIZE (THẤU CẢM)

### 2.1. Stakeholder (Các bên liên quan)
- **Primary user (Người dùng chính)**: Cán bộ quản lý an toàn (HSE) và Chỉ huy trưởng/Quản đốc công trường.
  - *Vai trò*: Trực tiếp sử dụng hệ thống phần mềm/dashboard hằng ngày để theo dõi cảnh báo thời gian thực, quản lý nhật ký vi phạm và đưa ra quyết định xử lý. Hệ thống giúp họ giảm áp lực giám sát thủ công và phòng tránh rủi ro pháp lý.
- **Secondary user (Người dùng thứ cấp)**: Người lao động, công nhân thi công, thợ bảo trì.
  - *Vai trò*: Đối tượng chịu tác động trực tiếp tại hiện trường. Không trực tiếp điều khiển phần mềm nhưng tiếp nhận các cảnh báo phản hồi tại chỗ (còi báo động, đèn chớp) để chủ động điều chỉnh hành vi tức thì.
- **Quản lý cấp cao (Giám đốc / Chủ đầu tư / Chủ thầu)**:
  - *Vai trò*: Người phê duyệt ngân sách đầu tư giải pháp. Theo dõi báo cáo thống kê định kỳ về mức độ tuân thủ an toàn toàn dự án, sử dụng dữ liệu làm bằng chứng minh bạch khi làm việc với cơ quan thanh tra lao động.
- **Người vận hành kỹ thuật (Kỹ thuật viên hiện trường / IT)**:
  - *Vai trò*: Phụ trách lắp đặt, cấp nguồn, duy trì kết nối mạng và bảo dưỡng định kỳ các thiết bị Edge, camera và actuator tại hiện trường thi công.

### 2.2. Thu thập thông tin (User Research)
Tiến hành phỏng vấn sâu và khảo sát thực tế với 4 đối tượng tại một công trình xây dựng dân dụng:
- **Phỏng vấn HSE (Anh Tuấn, 5 năm kinh nghiệm)**: *"Công trường rộng hơn 3000m² với 3 tầng hầm và 15 tầng nổi, mỗi ca có gần 80 công nhân từ nhiều thầu phụ. Tôi đi kiểm tra tầng này thì tầng khác công nhân lại tháo mũ bảo hộ ra vì nóng. Không thể nào có mặt ở mọi góc cùng một lúc. Khi có đoàn thanh tra đột xuất, chỉ cần một công nhân vi phạm là công ty bị phạt cả chục triệu đồng."*
- **Phỏng vấn Công nhân xây dựng (Anh Nam, 38 tuổi)**: *"Nhiều lúc làm việc nặng ra mồ hôi bí bách nên tôi tháo mũ bảo hộ đặt tạm sang bên cạnh rồi quên đội lại. Đôi khi vội lấy vật tư nên đi tắt qua khu vực bên dưới xe cẩu đang cẩu hàng mà không để ý biển cảnh báo cắm ở xa."*
- **Phỏng vấn Quản đốc hiện trường (Anh Hùng, 42 tuổi)**: *"Khi xảy ra va quẹt hay tai nạn nhỏ, thầu phụ và công nhân thường chối trách nhiệm, nói là do đơn vị quản lý không nhắc nhở hay cấm đoán. Chúng tôi thiếu dữ liệu chứng minh ai đã vào lúc nào và có trang bị bảo hộ đầy đủ hay không."*

### 2.3. Persona (Hồ sơ người dùng)

#### Persona 1: Cán bộ Quản lý An toàn (Primary User)
- **Họ và tên**: Nguyễn Mạnh Tuấn (32 tuổi)
- **Vai trò**: Cán bộ HSE tại công trình xây dựng chung cư cao tầng.
- **Mục tiêu**: Đảm bảo 100% người lao động tuân thủ trang bị bảo hộ (PPE), không xảy ra tai nạn lao động nghiêm trọng, hoàn thành đầy đủ báo cáo an toàn hàng ngày cho ban chỉ huy.
- **Hành vi**: Đi tuần tra hiện trường 3-4 lần/ngày, ghi chép biên bản nhắc nhở thủ công, chụp ảnh bằng điện thoại khi phát hiện vi phạm.
- **Khó khăn (Pain Points)**:
  - Hiện trường rộng lớn, khuất tầm nhìn, không thể bao quát toàn bộ.
  - Mất nhiều thời gian xử lý biên bản giấy và tổng hợp báo cáo.
  - Luôn lo lắng bị đình chỉ thi công hoặc liên đới trách nhiệm hình sự nếu tai nạn xảy ra trong ca trực.
- **Nhu cầu**: Một công cụ tự động phát hiện vi phạm ngay lập tức, báo động tức thì và lưu trữ hình ảnh làm chứng cứ minh bạch.

#### Persona 2: Công nhân Thi công (Secondary User)
- **Họ và tên**: Trần Văn Nam (38 tuổi)
- **Vai trò**: Thợ cốt pha, làm việc tự do theo thời vụ.
- **Mục tiêu**: Hoàn thành định mức công việc trong ngày, nhận lương đầy đủ và về nhà an toàn với gia đình.
- **Hành vi**: Tập trung vào tiến độ tay chân, hay tháo mũ bảo hộ khi nóng bức; chỉ đội lại khi thấy bóng dáng cán bộ HSE đến gần.
- **Khó khăn (Pain Points)**:
  - Môi trường làm việc ồn ào, bụi bặm, khó chú ý các biển báo cố định.
  - Nhận thức về vùng nguy hiểm động (khu vực bán kính cẩu xoay, hố sàn đang mở) còn hạn chế.
- **Nhu cầu**: Nhận được cảnh báo nhắc nhở trực quan, dễ nghe/dễ thấy ngay tại chỗ để tự điều chỉnh mà không bị phạt nặng nề.

### 2.4. Pain Points tổng hợp
1. **Mù thông tin thời gian thực**: Quản lý hoàn toàn không biết tình trạng tuân thủ an toàn ở các vị trí không có người trực tiếp tuần tra.
2. **Phản ứng chậm trễ (Reactive)**: Chỉ phát hiện và xử lý sự cố khi tai nạn hoặc vi phạm nghiêm trọng đã xảy ra.
3. **Thiếu bằng chứng khách quan**: Khó truy vết nguyên nhân sự cố, dẫn đến tranh cãi giữa các bên liên quan và rủi ro pháp lý.
4. **Cảnh báo hiện tại không hiệu quả**: Biển báo tĩnh bị bỏ qua; công nhân không nhận thức được việc mình đang bước vào vùng rủi ro tử vong.

### 2.5. Insights & Mapping
- *Insight 1*: Người lao động không cố tình vi phạm an toàn; họ vi phạm do thói quen tiện lợi, thiếu tập trung tức thời và thiếu phản hồi cảnh báo tương tác.  
  -> **Chức năng tương ứng**: Cảnh báo tức thì tại chỗ (On-site Audio/Visual Feedback) bằng đèn chớp và còi.
- *Insight 2*: Quản lý an toàn cần bằng chứng số hóa tức thời chứ không cần thêm sổ sách giấy tờ.  
  -> **Chức năng tương ứng**: Chụp ảnh vi phạm, gắn nhãn thời gian thực và đẩy cảnh báo lên Web Dashboard.

---

# PHẦN 3 — DEFINE (XÁC ĐỊNH VẤN ĐỀ)

### 3.1. Problem Statement
> **Cán bộ quản lý an toàn (HSE) và công nhân công trường** cần **một cơ chế giám sát tự động và cảnh báo tức thời các hành vi thiếu an toàn (không đội mũ bảo hộ, đi vào vùng nguy hiểm)** vì **việc tuần tra thủ công không thể bao quát liên tục hiện trường, dẫn đến các điểm mù an toàn và nguy cơ tai nạn lao động nghiêm trọng không được ngăn chặn kịp thời.**

### 3.2. POV (Point of View)
- **User**: Cán bộ quản lý an toàn (HSE) công trường.
- **Need**: Một giải pháp giám sát tự động 24/7 phát hiện vi phạm PPE và cảnh báo xâm nhập vùng cấm ngay trong tích tắc.
- **Insight**: Họ không thể có mặt ở mọi điểm nóng cùng một lúc, nhưng lại là người chịu toàn bộ trách nhiệm pháp lý và lương tâm khi có tai nạn xảy ra.

### 3.3. HMW (How Might We?)
1. *HMW 1*: Làm thế nào để chúng ta phát hiện vi phạm bảo hộ (không mũ) và xâm nhập vùng nguy hiểm ngay tại hiện trường trong vòng dưới 2 giây?
2. *HMW 2*: Làm thế nào để cảnh báo trực tiếp người lao động tại chỗ mà không phụ thuộc vào việc họ có mang theo điện thoại thông minh hay không?
3. *HMW 3*: Làm thế nào để cán bộ HSE nắm bắt dữ liệu toàn bộ công trường trên một bảng điều khiển duy nhất và có đầy đủ bằng chứng khi cần xử lý?

### 3.4. Tiêu chí thành công (Success Criteria)

| Yêu cầu kỹ thuật / Nhu cầu | Chỉ số mục tiêu (Target) | Phương pháp đo lường |
|---|---:|---|
| Thời gian phát hiện & kích hoạt còi tại chỗ | ≤ 1.5 giây | Đo thời gian từ lúc vi phạm đến khi còi/đèn bật |
| Độ trễ đẩy dữ liệu lên Dashboard | ≤ 3.0 giây | Đo timestamp từ Edge gửi đến Web Client |
| Tỷ lệ nhận dữ liệu qua MQTT | ≥ 98% | Gửi 100 gói tin kiểm tra tỷ lệ nhận |
| Độ chính xác nhận diện vi phạm (Precision) | ≥ 85% | Đánh giá trên 50 tình huống thử nghiệm |
| Thao tác người dùng xem chi tiết vi phạm | ≤ 2 click | Đếm số bước tương tác trên giao diện |
| Lưu trữ lịch sử sự kiện kèm ảnh chụp | ≥ 30 ngày | Truy vấn dữ liệu Database |

---

# PHẦN 4 — IDEATE (HÌNH THÀNH Ý TƯỞNG)

### 4.1. Sinh ý tưởng (Các phương án giải pháp)

- **Phương án A — Thẻ định vị UWB/RFID gắn trên nón + Cảm biến áp lực**:
  - *Mô tả*: Mỗi công nhân đeo thẻ RFID/UWB; mũ bảo hộ gắn cảm biến chạm đầu để biết có đang đội hay không; vùng cấm đặt trạm thu tín hiệu.
  - *Ưu điểm*: Bền, không bị ảnh hưởng bởi góc nhìn hay ánh sáng.
  - *Nhược điểm*: Chi phí phần cứng trên mỗi công nhân rất cao, khó áp dụng với lao động thời vụ; công nhân dễ quên đeo thẻ hoặc tháo thẻ sang vật khác; không kiểm tra được người lạ vào công trường.

- **Phương án B — Camera Edge AI tại hiện trường kết hợp Còi/Đèn cảnh báo tại chỗ và IoT Cloud Dashboard (Phương án đề xuất)**:
  - *Mô tả*: Sử dụng camera tại các điểm nóng kết nối với vi xử lý Edge (Raspberry Pi / Jetson Nano / ESP32-CAM) chạy mô hình thị giác máy tính cục bộ phát hiện người không đội mũ bảo hộ và xâm nhập vùng cấm (Polygon ROI). Kích hoạt còi/đèn tại chỗ qua GPIO và gửi telemetry/bằng chứng vi phạm về Backend/Dashboard qua giao thức MQTT.
  - *Ưu điểm*: Giám sát không tiếp xúc, áp dụng được cho mọi đối tượng (kể cả khách thăm, công nhân mới), phản ứng tại chỗ cực nhanh (độ trễ thấp nhờ xử lý tại biên), cung cấp bằng chứng hình ảnh rõ ràng.
  - *Nhược điểm*: Phụ thuộc vào góc đặt camera và điều kiện chiếu sáng; cần xử lý tối ưu mô hình để chạy mượt trên thiết bị Edge.

- **Phương án C — Hệ thống Camera truyền toàn bộ luồng Video về Cloud Server để xử lý AI tập trung**:
  - *Mô tả*: Camera truyền RTSP stream liên tục qua mạng 4G/Internet về Cloud server cấu hình cao để nhận diện và quản lý.
  - *Ưu điểm*: Không giới hạn năng lực tính toán phần cứng tại hiện trường; mô hình AI có thể rất lớn và chính xác.
  - *Nhược điểm*: Tốn băng thông mạng 4G khổng lồ, chi phí server rất đắt; khi mất kết nối mạng công trường thì hệ thống mất hoàn toàn khả năng cảnh báo tại chỗ, độ trễ phát hiện cao (> 5s).

### 4.2. Ma trận lựa chọn phương án (Decision Matrix)

| Tiêu chí đánh giá | Trọng số | Phương án A (RFID/UWB) | Phương án B (Edge AI + IoT) | Phương án C (Cloud Video AI) |
|---|:---:|:---:|:---:|:---:|
| Giá trị thực tế cho người dùng (Cảnh báo tức thì & bao quát) | 30% | 6/10 (1.8) | **9/10 (2.7)** | 7/10 (2.1) |
| Khả thi kỹ thuật & Prototype | 25% | 7/10 (1.75) | **8/10 (2.0)** | 6/10 (1.5) |
| Chi phí triển khai & duy trì | 15% | 4/10 (0.6) | **8/10 (1.2)** | 4/10 (0.6) |
| Độ trễ cảnh báo (Latency) | 15% | 8/10 (1.2) | **9/10 (1.35)** | 5/10 (0.75) |
| Khả năng mở rộng & tính linh hoạt | 15% | 5/10 (0.75) | **8/10 (1.2)** | 8/10 (1.2) |
| **Tổng điểm có trọng số** | **100%** | **6.10** | **8.45** | **6.15** |

### 4.3. Concept được chọn & Lý do lựa chọn
- **Lựa chọn**: **Phương án B — Hệ thống Giám sát Biên Edge AI IoT kết hợp Cảnh báo Đa tầng**.
- **Lý do**:
  - *Xử lý tại biên (Edge Processing)* giúp độ trễ cảnh báo còi/đèn tại hiện trường đạt mức < 1.5s, đảm bảo khả năng bảo vệ người lao động ngay lập tức kể cả khi rớt mạng Internet.
  - Tiết kiệm băng thông tối đa: Thiết bị biên chỉ truyền siêu dữ liệu (metadata sự kiện) và ảnh chụp vi phạm qua MQTT khi có sự cố, không truyền tải liên tục video nặng nề.
  - Giải quyết bài toán của cả người lao động (nghe thấy còi/đèn là phản xạ ngay) và người quản lý (Dashboard trực quan, lưu vết hình ảnh minh bạch).

---

# PHẦN 5 — THIẾT KẾ GIẢI PHÁP IoT (IoT SYSTEM DESIGN)

### 5.1. Luồng kiến trúc tổng thể (End-to-End Architecture)
```text
Physical World (Công nhân, Công trường, Vùng nguy hiểm)
      ↓
Sensing Layer (Camera IP / Camera Module chụp ảnh dòng hình ảnh)
      ↓
Edge Computing (Raspberry Pi 4 / Jetson: Mô hình nhận diện PPE & Xâm nhập ROI)
      ↓ -------------------------\ (Kích hoạt tức thì qua GPIO)
      ↓                           → Actuator (Còi Buzzer + Đèn Strobe LED tại chỗ)
Network Layer (Wi-Fi công trường / 4G LTE, Giao thức MQTT / REST API)
      ↓
IoT Platform / Backend (Flask + MQTT Broker Mosquitto)
      ↓
Data Layer (Database PostgreSQL / SQLite lưu trữ Event log, Metadata & Ảnh vi phạm)
      ↓
Application Layer (Web Dashboard React / HTML5 cho Cán bộ HSE & Ban Chỉ huy)
      ↓
User Action (HSE nhắc nhở/lập biên bản; Công nhân lùi lại/đội mũ bảo hộ)
```

### 5.2. Use Cases chính

```text
+---------------------------------------------------------------+
|                      HỆ THỐNG GIÁM SÁT AN TOÀN IoT            |
|                                                               |
|   [Công nhân]                                                 |
|        ^                                                      |
|        | (nhận còi/đèn)                                        |
|   +-------------------+        +--------------------------+   |
|   | UC01: Cảnh báo    |        | UC02: Nhận diện vi phạm  |   |
|   | tại chỗ tức thời  |<-------| PPE & Vùng nguy hiểm     |   |
|   +-------------------+        +--------------------------+   |
|                                             |                 |
|                                             v                 |
|   [Cán bộ HSE]                 +--------------------------+   |
|        |                       | UC03: Truyền tin & Lưu   |   |
|        +---------------------->| trữ bằng chứng vi phạm   |   |
|        | (Xem Dashboard)       +--------------------------+   |
|        |                                    |                 |
|        v                                    v                 |
|   +-------------------+        +--------------------------+   |
|   | UC04: Điều khiển  |        | UC05: Xuất báo cáo &     |   |
|   | thiết bị từ xa    |        | Thống kê tỷ lệ tuân thủ  |   |
|   +-------------------+        +--------------------------+   |
+---------------------------------------------------------------+
```

- **UC01 — Nhận diện vi phạm PPE & Xâm nhập vùng nguy hiểm**: Camera Edge giám sát khung hình, AI phát hiện người không đội mũ hoặc bước vào vùng cấm được khoanh vùng trước.
- **UC02 — Cảnh báo tại chỗ tức thời**: Khi phát hiện vi phạm, vi điều khiển Edge lập tức kích hoạt còi hú và đèn chớp tại khu vực làm việc để cảnh báo người lao động.
- **UC03 — Truyền tin & Lưu trữ bằng chứng**: Edge node đóng gói thông tin (thời gian, mã trạm, loại vi phạm, ảnh snapshot) và gửi qua MQTT về máy chủ để ghi vào cơ sở dữ liệu.
- **UC04 — Giám sát & Quản lý trên Dashboard**: Cán bộ HSE xem cảnh báo thời gian thực nổi lên trên màn hình, xem ảnh vi phạm, xác nhận xử lý hoặc kích hoạt cảnh báo cưỡng bức từ xa.
- **UC05 — Thống kê & Báo cáo an toàn**: Tự động tổng hợp số vụ vi phạm theo ngày/tuần/khu vực thi công, xuất báo cáo phục vụ họp giao ban công trường.

### 5.3. Luồng Input — Processing — Decision — Output

```text
[Input]
Dòng khung hình từ Camera (15 FPS, 720p)
      ↓
[Processing]
Tiền xử lý khung hình -> Chạy mô hình Object Detection (YOLOv8-nano)
-> Tách nhãn: "Person", "Hardhat", "No-Hardhat"
-> Tính tọa độ chân người so với Đa giác vùng cấm (Polygon ROI Point-in-Polygon test)
      ↓
[Decision]
Điều kiện 1: Phát hiện "Person" KHÔNG CÓ "Hardhat" trên đầu?
Điều kiện 2: Tọa độ "Person" nằm TRONG vùng nguy hiểm?
      /                        \
    [NO]                      [YES]
      ↓                         ↓
Tiếp tục chu kỳ quét         [Output & Action]
                             1. Kích hoạt GPIO -> Bật Còi + Đèn chớp tại chỗ (≤ 0.5s)
                             2. Lưu Frame ảnh chụp vi phạm vào bộ nhớ đệm
                             3. Gửi gói tin JSON sự kiện qua MQTT topic `safety/alerts`
                             4. Server nhận tin -> Ghi Database -> Bắn WebSocket tới Dashboard
                             5. HSE Dashboard hiển thị popup màu đỏ kèm âm báo
```

### 5.4. Thiết bị Thu nhận & Cảm biến (Sensing Layer)
- **Thiết bị thu hình**: Camera góc rộng 1080p (hoặc Camera Module USB / CSI).
  - *Thông số*: Cảm biến 2MP/5MP, góc nhìn 110-120 độ, hỗ trợ chuẩn nén H.264/MJPEG.
  - *Sampling rate*: 10–15 khung hình/giây (FPS) - đủ để bắt chuyển động đi bộ của công nhân mà không gây quá tải chip xử lý.
  - *Vị trí lắp đặt*: Gắn tại cửa ra vào công trường, lối vào hầm, hoặc góc cố định bao quát khu vực cẩu tháp/hố móng.
  - *Lý do chọn*: Phổ biến, chi phí thấp, cho phép tích hợp linh hoạt với các thuật toán thị giác máy tính hiện đại.

### 5.5. Thiết bị Chấp hành (Actuators)
- **Còi báo động (Buzzer 5V/12V)**: Âm lượng 85–90 dB, đủ để nghe thấy trong môi trường có tiếng máy móc vừa phải nhưng không gây hoảng loạn giật mình khi công nhân đang đứng trên cao.
- **Đèn chớp cảnh báo (Strobe LED màu đỏ/vàng)**: Đặt ngay cạnh camera để khi nhấp nháy, công nhân trực tiếp nhìn thấy và biết mình là đối tượng đang bị cảnh báo.
- **Mạch Relay đóng ngắt (5V Optocoupler Relay)**: Dùng để cách ly và điều khiển còi/đèn công suất lớn hơn nếu triển khai ở môi trường công trường thực tế.
- **Cơ chế hoạt động**: `Trigger (Vi phạm)` -> `Action (Bật còi + đèn 3 giây)` -> `Feedback (Kiểm tra lại sau 3 giây, nếu công nhân đã rời khỏi vùng/đội mũ thì tự động tắt)`.

### 5.6. Thiết bị Biên (Edge Device)
- **Phần cứng**: Raspberry Pi 4 Model B (4GB RAM) hoặc Máy tính nhúng Jetson Nano.
- **Vai trò**:
  - Đọc luồng video từ Camera.
  - Chạy mô hình suy luận thị giác máy tính rút gọn (YOLOv8n-pose hoặc YOLOv8n-safety được chuyển đổi sang ONNX / TFLite / NCNN).
  - Xử lý logic tại chỗ: xác định vi phạm, điều khiển GPIO bật còi/đèn mà không phụ thuộc Internet.
  - Đóng gói dữ liệu vi phạm thành chuỗi JSON và gửi lên Broker.

### 5.7. Giao thức Truyền thông (Communication)
- **Mạng kết nối**: Wi-Fi 2.4GHz / 5GHz công trường hoặc Router 4G LTE công nghiệp.
- **Giao thức chính**: **MQTT (Message Queuing Telemetry Transport)** qua TCP/IP.
  - *Lý do chọn*: Nhẹ, tiết kiệm băng thông mạng 4G, cơ chế Publish/Subscribe rất phù hợp cho cảnh báo tức thì, hỗ trợ QoS 1 đảm bảo tin cảnh báo không bị thất lạc.
- **Quy hoạch MQTT Topics**:
  - `safety/edge/{device_id}/telemetry`: Gửi trạng thái thiết bị định kỳ mỗi 60s (heartbeat, nhiệt độ CPU, trạng thái camera).
  - `safety/edge/{device_id}/alert`: Đẩy sự kiện vi phạm an toàn khi phát hiện (kèm JSON payload).
  - `safety/edge/{device_id}/command`: Nhận lệnh điều khiển từ xa từ Dashboard (ví dụ: bật còi kiểm tra, cấu hình lại tọa độ vùng cấm ROI).
- **Cấu trúc dữ liệu JSON ví dụ (`safety/edge/01/alert`)**:
```json
{
  "device_id": "EDGE_STATION_01",
  "timestamp": "2026-09-09T08:30:15Z",
  "violation_type": "NO_HARDHAT_AND_DANGER_ZONE",
  "zone_name": "Crane_Zone_A",
  "confidence": 0.92,
  "image_snapshot": "https://storage.domain/alerts/snapshot_01_20260909_083015.jpg",
  "actuator_triggered": true
}
```

### 5.8. Nền tảng Xử lý Trung tâm (Backend / Platform)
- **Công nghệ**: Node.js kết hợp Express framework và MQTT Client (`mqtt.js`).
- **Nhiệm vụ**:
  - Subscribe liên tục các topic cảnh báo từ MQTT Broker (Eclipse Mosquitto).
  - Tiếp nhận thông tin vi phạm, xử lý lưu trữ hình ảnh và ghi bản ghi vào cơ sở dữ liệu.
  - Phát sóng thời gian thực đến Web Client thông qua giao thức **WebSocket (Socket.io)** để giao diện HSE cập nhật ngay lập tức không cần tải lại trang (polling).
  - Cung cấp RESTful API cho Dashboard tra cứu dữ liệu quá khứ và báo cáo thống kê.

### 5.9. Cơ sở dữ liệu (Database)
- **Công nghệ**: PostgreSQL (hoặc SQLite cho bản Prototype gọn nhẹ).
- **Bảng dữ liệu chính**:
  1. `devices`: `device_id` (PK), `name`, `location`, `ip_address`, `status`, `last_ping`.
  2. `safety_events`: `id` (PK), `device_id` (FK), `timestamp`, `violation_type`, `zone_name`, `confidence`, `image_url`, `status` (NEW, CONFIRMED, DISMISSED), `resolved_by`.
  3. `zones_config`: `zone_id` (PK), `device_id`, `name`, `polygon_coords_json`, `is_active`.

### 5.10. Trực quan hóa & Bảng điều khiển (Dashboard Visualization)
- **Mục đích hỗ trợ ra quyết định**: Dashboard không chỉ để "trưng bày" thông số mà giúp cán bộ HSE:
  - Nhìn thấy ngay điểm nóng đang có báo động đỏ nhấp nháy để điều động người kiểm tra hiện trường.
  - Nhấp vào xem ngay ảnh chụp bằng chứng vi phạm để đánh giá đây là vi phạm thật hay vật thể giả lập, từ đó bấm nút "Xác nhận vi phạm" hoặc "Hủy cảnh báo".
  - Xem biểu đồ tuần suất vi phạm theo giờ để điều chỉnh giờ tuần tra hợp lý vào các khung giờ công nhân hay lơ là nhất (thường là đầu ca hoặc sát giờ nghỉ trưa).

### 5.11. An toàn & Bảo mật (Security)
- **Bảo vệ kết nối**: MQTT Broker sử dụng xác thực Username/Password, hỗ trợ TLS (MQTTS port 8883) khi truyền qua Internet.
- **Bảo mật thông tin**: Tách biệt credentials, lưu trữ thông qua biến môi trường (`.env`), không hard-code khóa mật khẩu trong mã nguồn.
- **Bảo vệ quyền riêng tư (Privacy)**: Ảnh chụp vi phạm chỉ lưu trữ trong khu vực lưu trữ an toàn, truy cập qua Signed URL có thời hạn, phục vụ công tác an toàn lao động và cam kết xóa sau 60 ngày.

---

# PHẦN 6 — PROTOTYPE & TRIỂN KHAI

### 6.1. Prototype 1 — Concept Prototype (Kiểm chứng luồng)
- **Hình thức**: Thiết kế Wireframe giao diện Dashboard trên Figma kết hợp kịch bản Storyboard mô phỏng:
  - *Khung 1*: Công nhân đi vào khu vực khoanh vùng màu đỏ mà không đội mũ bảo hộ.
  - *Khung 2*: Còi và đèn tại chỗ phát tín hiệu âm thanh và ánh sáng nhắc nhở.
  - *Khung 3*: Trên bàn làm việc của HSE, màn hình vi tính hiện cảnh báo màu đỏ kèm chuông thông báo và ảnh chụp người vi phạm.
- **Mục tiêu**: Lấy ý kiến phản hồi sớm từ người làm công tác an toàn về việc bố trí thông tin trên màn hình và mức độ chấp nhận còi hú tại chỗ.

### 6.2. Prototype 2 — Functional Prototype (Phần cứng chức năng)
- **Thành phần**:
  - Một máy tính cá nhân / Raspberry Pi kết nối Webcam USB.
  - Kịch bản Python chạy mô hình AI nhận diện khuôn mặt/người có/không có nón bảo hộ.
  - Mạch còi Buzzer + LED kết nối qua cổng GPIO/Arduino.
- **Kiểm chứng**: Khi người đứng trước camera không đội mũ bảo hộ, còi hú kêu lên và đèn LED bật sáng trong vòng dưới 1 giây.

### 6.3. Prototype 3 — Integrated IoT Prototype (Hệ thống hoàn chỉnh End-to-End)
- **Cấu hình tích hợp**:
  - `Edge Layer`: Raspberry Pi 4 + Camera + Buzzer/LED. Chạy script Python sử dụng OpenCV và YOLOv8-nano inference, tích hợp Paho-MQTT client.
  - `Network/Broker`: Mosquitto MQTT Broker cài đặt trên máy chủ nội bộ hoặc VPS đám mây.
  - `Backend`: Server Node.js Express lắng nghe MQTT và phát WebSocket tới người dùng.
  - `Frontend Dashboard`: Web Single Page Application (HTML5/TailwindCSS/JS) hiển thị danh sách camera, sơ đồ mặt bằng công trường, danh sách vi phạm thời gian thực và biểu đồ thống kê.
- **Kết quả đạt được**: Tạo thành chu trình khép kín: Phát hiện vi phạm -> Báo động hiện trường -> Gửi dữ liệu qua mạng -> Lưu database -> Cán bộ HSE xem và xử lý trên giao diện.

---

# PHẦN 7 — THỬ NGHIỆM & ĐÁNH GIÁ (TEST & EVALUATION)

### 7.1. Đánh giá Kỹ thuật (Technical Testing)

Tiến hành kịch bản thử nghiệm kỹ thuật với 100 lần kích hoạt tình huống vi phạm có chủ đích:

| Hạng mục kiểm thử | Chỉ số đo lường | Mục tiêu đề ra | Kết quả thực tế đạt được | Đánh giá |
|---|---|:---:|:---:|:---:|
| Khả năng nhận diện PPE (Mũ) | Tỷ lệ phát hiện đúng (Recall/Precision) | ≥ 85% | **88.2%** | **PASS** |
| Phát hiện xâm nhập vùng cấm | Tỷ lệ bắt đúng khi bước qua vạch | ≥ 90% | **94.0%** | **PASS** |
| Độ trễ kích hoạt cảnh báo tại chỗ | Thời gian từ frame vi phạm đến còi kêu | ≤ 1.5s | **0.65s** | **PASS** |
| Truyền thông MQTT | Tỷ lệ gói tin cảnh báo nhận thành công | ≥ 98% | **99/100 (99%)** | **PASS** |
| Độ trễ hiển thị Dashboard | Thời gian từ vi phạm đến popup Web | ≤ 3.0s | **1.85s** | **PASS** |
| Độ ổn định vận hành (Stress test) | Hoạt động liên tục không crash | ≥ 8 giờ | **Đạt 12 giờ liên tục** | **PASS** |

### 7.2. Thử nghiệm Người dùng (User Testing)
Mời 2 cán bộ quản lý an toàn và 3 công nhân tham gia kịch bản mô phỏng tại hiện trường thử nghiệm:
- **Nhiệm vụ dành cho Cán bộ HSE**:
  - *Task 1*: Quan sát và phát hiện xem trạm nào đang có công nhân vi phạm trong vòng 5 giây.  
    -> *Kết quả*: 100% hoàn thành trong vòng 2 giây nhờ màu đỏ nổi bật và âm thanh popup trên web.
  - *Task 2*: Mở ảnh chi tiết để xác định danh tính và loại vi phạm.  
    -> *Kết quả*: Thực hiện chỉ với 1 click chuột, thời gian trung bình 3.2 giây.
  - *Task 3*: Xuất báo cáo danh sách 5 sự cố gần nhất.  
    -> *Kết quả*: Hoàn thành dễ dàng qua nút xuất file CSV.
- **Thử nghiệm với Công nhân**:
  - Cho công nhân mang và không mang mũ đi qua vùng quy định.
  - *Phản xạ của công nhân*: Khi còi và đèn chớp bật sáng, cả 3 công nhân đều lập tức dừng bước hoặc đưa tay lên đầu kiểm tra mũ.

### 7.3. Phân biệt Technical Success vs User Success
- **Technical Success**: Hệ thống nhận diện AI đạt độ chính xác cao, gói tin MQTT truyền đạt 99%, còi kêu đúng lúc.
- **User Success**: 
  - Cán bộ HSE cảm thấy giảm bớt căng thẳng đi tuần, không sợ bỏ sót vi phạm.
  - Công nhân hiểu ngay tín hiệu cảnh báo mà không cảm thấy bị làm phiền hay xúc phạm nhân phẩm.
  - Tỷ lệ người tuân thủ đội mũ tại khu vực thử nghiệm tăng từ 65% lên 92% sau 3 ngày lắp đặt hệ thống.

---

# PHẦN 8 — VÒNG LẶP CẢI TIẾN (ITERATION & FINAL RESULT)

### 8.1. Phản hồi từ thử nghiệm Prototype v1
Sau khi chạy thử nghiệm phiên bản thử nghiệm ban đầu (Prototype v1), nhóm đã ghi nhận các phản hồi cốt lõi sau:
1. **Còi hú liên tục gây khó chịu và hoang mang**: Ở v1, khi phát hiện người không đội mũ, còi kêu liên tục không ngừng cho đến khi người đó rời đi. Khi công nhân chỉ vô tình tháo mũ ra gãi đầu trong 3 giây, còi kêu inh ỏi khiến những người xung quanh giật mình, gây nguy hiểm khi đang làm việc ở trên cao.
2. **Cảnh báo giả khi góc nghiêng bị che khuất**: Khi công nhân quay lưng lại camera hoặc cúi người bốc gạch, camera không nhận diện được phần đỉnh mũ nên báo động sai.
3. **Dashboard Web quá nhiều chữ, khó nhìn dưới trời nắng**: Khi cán bộ HSE cầm máy tính bảng ra công trường kiểm tra, giao diện font chữ nhỏ và tông màu xám trắng rất khó đọc.

### 8.2. Các thay đổi cải tiến trên Prototype v2

| Vấn đề phát hiện (Feedback) | Nguyên nhân cốt lõi | Thay đổi cụ thể trong Prototype v2 | Kết quả sau cải tiến |
|---|---|---|---|
| Còi hú liên tục gây phản cảm và nguy hiểm | Logic điều khiển GPIO chưa có bộ trễ và cơ chế ngắt nhịp | Đổi thành: **Chớp đèn LED trước 2s**, nếu vẫn vi phạm mới **kêu còi ngắt quãng (Bip-Bip-Bip) trong 3s** rồi tự ngắt chu kỳ | Công nhân tiếp nhận cảnh báo tự nhiên, không bị giật mình |
| Cảnh báo giả do che khuất góc nhìn | Quét frame đơn lẻ (Single frame detection) | Bổ sung logic **Persistence Filter**: Vi phạm phải tồn tại liên tục trong ít nhất 3 frame liên tiếp (khoảng 0.8s) mới kích hoạt báo động | Giảm 80% số lượng cảnh báo giả tức thời |
| Dashboard khó nhìn ngoài trời | Thiết kế UI ban đầu chưa tối ưu độ tương phản | Thiết kế lại giao diện dạng High-Contrast thẻ lớn (Card layout), màu đỏ neon cảnh báo rõ ràng, tối ưu responsive trên tablet | HSE dễ dàng thao tác bằng một tay trên máy tính bảng ngoài công trường |

```text
Prototype v1 (Phát hiện đơn khung hình, còi hú chói tai)
      ↓
Thử nghiệm thực tế với HSE & Công nhân
      ↓
Phát hiện vấn đề: Báo giả do che khuất + Còi gây ức chế
      ↓
Cải tiến kỹ thuật: Persistence Tracking + Cảnh báo 2 nhịp (Đèn -> Còi ngắt quãng) + High Contrast UI
      ↓
Prototype v2 (Vận hành êm ái, tin cậy cao, người dùng hài lòng)
```

---

# PHẦN 9 — ĐÁNH GIÁ CUỐI CÙNG & TỔNG KẾT (DEFINITION OF DONE)

### 9.1. Trả lời 6 câu hỏi cốt lõi (Definition of Done)
1. **WHO (Ai là người dùng)?**  
   Cán bộ quản lý an toàn (HSE) tại công trường (người giám sát, ra quyết định) và Công nhân xây dựng (người tiếp nhận cảnh báo bảo vệ bản thân).
2. **WHY (Họ đang gặp vấn đề gì)?**  
   Không thể giám sát 24/7 diện rộng bằng mắt thường; biển báo tĩnh bị lờ đi; tai nạn lao động luôn rình rập và đe dọa sinh mạng cùng trách nhiệm pháp lý nặng nề.
3. **WHAT (Giải pháp tạo giá trị gì)?**  
   Tự động hóa phát hiện rủi ro tức thời, phòng ngừa tai nạn trước khi xảy ra bằng còi/đèn tại chỗ và cung cấp bằng chứng số hóa minh bạch cho nhà quản lý.
4. **HOW (Dữ liệu đi qua hệ thống thế nào)?**  
   `Camera -> Edge (AI Vision & GPIO) -> MQTT Protocol -> Backend Node.js -> PostgreSQL -> Web Dashboard / WebSocket`.
5. **HOW WELL (Hệ thống tốt đến mức nào)?**  
   Cảnh báo tại chỗ chỉ mất 0.65 giây; độ chính xác nhận diện đạt 88.2%; tỷ lệ nhận tin MQTT đạt 99%; giảm hơn 80% cảnh báo giả sau vòng lặp cải tiến.
6. **SO WHAT (Người dùng thử xong phản hồi gì và đã cải tiến ra sao)?**  
   Từ việc sợ tiếng còi hú inh ỏi ở bản v1, công nhân đã hợp tác vui vẻ khi hệ thống chuyển sang đèn chớp nhịp nhàng và còi ngắt quãng ở bản v2; tỷ lệ tuân thủ an toàn tại điểm thử nghiệm nâng cao rõ rệt.

### 9.2. Hạn chế hiện tại & Hướng mở rộng (Future Work)
- **Hạn chế**:
  - Khả năng nhận diện ban đêm còn hạn chế nếu thiếu đèn chiếu sáng công trường hồng ngoại.
  - Thiết bị Edge cần tản nhiệt tốt khi đặt trực tiếp dưới trời nắng nóng mùa hè.
- **Hướng mở rộng**:
  - Mở rộng nhận diện thêm các thiết bị bảo hộ khác: Dây đai an toàn toàn thân (Safety Harness), áo phản quang.
  - Tích hợp thêm cảm biến môi trường (khí độc CO/H2S trong không gian kín, nhiệt độ cao chống sốc nhiệt cho công nhân).
  - Tích hợp còi thông báo bằng giọng nói thông minh (Audio prompt: *"Chú ý: Bạn đang vào khu vực cẩu, vui lòng lùi lại"*).

