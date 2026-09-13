# KHUNG ĐỀ TÀI IoT THEO HƯỚNG DESIGN THINKING

## 1. Mục tiêu chung

Đề tài IoT được triển khai theo nguyên tắc:

**Vấn đề/người dùng → nhu cầu → ý tưởng → thiết kế hệ thống IoT → prototype → thử nghiệm → đánh giá → cải tiến**

Không bắt đầu từ việc “có cảm biến gì thì làm đề tài đó”.

Một đề tài đạt yêu cầu phải chứng minh được cả:

- giá trị đối với người dùng;
- kiến trúc IoT end-to-end;
- khả năng triển khai prototype;
- khả năng kiểm thử và đánh giá;
- có ít nhất một vòng phản hồi/cải tiến theo Design Thinking.

---

# 2. Khung tổng thể đề tài

| Phần | Nội dung phải có | Yêu cầu cần đạt |
|---|---|---|
| 1. Problem & Context | Bối cảnh, đối tượng, vấn đề thực tế | Chứng minh có vấn đề thực, không bắt đầu từ công nghệ |
| 2. Empathize | Người dùng, quan sát/phỏng vấn, pain point | Có dữ liệu từ người dùng thực hoặc tình huống thực |
| 3. Define | Problem Statement, Persona, POV/HMW | Vấn đề đủ hẹp, rõ, đo được |
| 4. Ideate | Các phương án và lý do chọn giải pháp | Có ít nhất 3 ý tưởng, có tiêu chí lựa chọn |
| 5. IoT Solution Design | Use case, kiến trúc, sensor/actuator, network, platform, data | Kiến trúc end-to-end hợp lý |
| 6. Prototype | Prototype phần cứng + phần mềm | Có hệ thống chạy được, không chỉ mockup |
| 7. Test & Evaluation | Functional test + user test + technical metrics | Có số liệu và tiêu chí pass/fail |
| 8. Iteration & Final Result | Phản hồi, cải tiến, hạn chế, hướng mở rộng | Có ít nhất một vòng lặp cải tiến |

---

# 3. PHẦN 1 — Problem & Context

## 3.1. Bối cảnh

Phải trả lời được:

- Vấn đề xảy ra ở đâu?
- Ai gặp vấn đề?
- Khi nào?
- Hiện tại họ xử lý bằng cách nào?
- Điểm bất tiện, rủi ro hoặc tốn kém là gì?

### Ví dụ không nên viết

> Nhóm xây dựng hệ thống IoT đo nhiệt độ bằng DHT11.

### Nên viết theo hướng

> Trong phòng thiết bị X, người vận hành hiện kiểm tra nhiệt độ thủ công. Việc kiểm tra không liên tục nên không phát hiện sớm tình trạng nhiệt độ vượt ngưỡng.

## 3.2. Mục tiêu ban đầu

Nêu kết quả mong muốn đối với người dùng, chưa đi sâu vào công nghệ.

Ví dụ:

> Giúp người quản lý phát hiện sớm tình trạng nhiệt độ bất thường và có thể kiểm tra trạng thái phòng từ xa.

## 3.3. Yêu cầu cần đạt

Phải xác định được:

**User → Problem → Context → Consequence**

Không chấp nhận đề tài chỉ có:

> Sensor + Raspberry Pi + MQTT + Dashboard

mà không giải thích tại sao người dùng cần hệ thống đó.

---

# 4. PHẦN 2 — EMPATHIZE

## 4.1. Stakeholder

Xác định ít nhất:

- Primary user;
- Secondary user;
- người quản lý hoặc bảo trì nếu có.

## 4.2. Thu thập thông tin

Có thể sử dụng:

- phỏng vấn;
- quan sát;
- questionnaire;
- contextual inquiry;
- nhật ký sử dụng;
- khảo sát hiện trường.

Với đề tài sinh viên, khoảng 3–5 người dùng thực sự phù hợp có thể đủ cho một vòng nghiên cứu ban đầu.

## 4.3. Persona

Tối thiểu phải có:

- vai trò;
- mục tiêu;
- hành vi;
- khó khăn;
- nhu cầu.

## 4.4. Pain Point

Nên xác định khoảng 3–5 pain point chính.

Ví dụ:

1. Không biết trạng thái thiết bị từ xa.
2. Chỉ phát hiện sự cố khi đã xảy ra.
3. Phải kiểm tra thủ công.
4. Không có dữ liệu lịch sử.

## 4.5. Yêu cầu cần đạt

Mỗi chức năng quan trọng của hệ thống sau này phải truy ngược được về ít nhất một:

**User Need / Pain Point**

---

# 5. PHẦN 3 — DEFINE

## 5.1. Problem Statement

Nên theo mẫu:

**[User] cần [Need] vì [Insight].**

Ví dụ:

> Nhân viên quản lý phòng thiết bị cần biết sớm khi nhiệt độ tăng bất thường vì việc kiểm tra thủ công theo ca không đủ để phát hiện sự cố giữa hai lần kiểm tra.

## 5.2. POV — Point of View

Có thể dùng:

**User + Need + Insight**

## 5.3. HMW — How Might We?

Ví dụ:

> How might we help the operator detect abnormal room conditions early without requiring continuous manual monitoring?

## 5.4. Tiêu chí thành công

Phải chuyển nhu cầu thành tiêu chí đo được.

| Requirement | Target |
|---|---:|
| Cập nhật nhiệt độ | ≤ 10 s |
| Phát hiện vượt ngưỡng | ≤ 15 s |
| Tỷ lệ nhận dữ liệu | ≥ 95% |
| Người dùng xem trạng thái | ≤ 3 thao tác |
| Lưu dữ liệu lịch sử | ≥ 24 giờ |

## 5.5. Yêu cầu cần đạt

Vấn đề phải:

- cụ thể;
- có người dùng;
- có bối cảnh;
- có thể kiểm chứng;
- không chứa sẵn lời giải.

---

# 6. PHẦN 4 — IDEATE

## 6.1. Sinh ý tưởng

Yêu cầu tối thiểu **3 phương án**.

Ví dụ:

- A. Cảnh báo tại chỗ bằng còi/LED.
- B. Gửi trạng thái lên smartphone.
- C. IoT monitoring + cảnh báo + lịch sử dữ liệu.

## 6.2. Ma trận lựa chọn

Ví dụ:

| Tiêu chí | Trọng số |
|---|---:|
| Giá trị cho người dùng | 30% |
| Khả thi kỹ thuật | 25% |
| Chi phí | 15% |
| Thời gian thực hiện | 15% |
| Khả năng mở rộng | 15% |

## 6.3. Concept được chọn

Phải trả lời:

> Vì sao phương án này tốt hơn các phương án còn lại?

## 6.4. Yêu cầu cần đạt

Không đánh giá ý tưởng chỉ dựa trên:

> Nhóm biết Raspberry Pi nên dùng Raspberry Pi.

---

# 7. PHẦN 5 — THIẾT KẾ GIẢI PHÁP IoT

Kiến trúc tối thiểu phải thể hiện được:

```text
Physical World
    ↓
Sensor
    ↓
Edge / Device
    ↓
Network
    ↓
Backend / IoT Platform
    ↓
Data / Database
    ↓
Application / Dashboard
    ↓
User
    ↓
Action / Decision
```

## 7.1. Use Case

Bắt buộc có khoảng 2–5 use case chính.

Ví dụ:

- UC01 — View current temperature
- UC02 — Receive high-temperature alert
- UC03 — View historical data
- UC04 — Turn cooling device on/off

## 7.2. Input — Processing — Output

Mỗi chức năng cần xác định:

```text
Input
  ↓
Processing
  ↓
Decision
  ↓
Output / Action
```

Ví dụ:

```text
Temperature
    ↓
Compare threshold
    ↓
T > 35 °C?
  /       \
No        Yes
           ↓
         Alert
           ↓
          User
```

## 7.3. Sensor

Phải giải thích:

- đo đại lượng gì;
- range;
- accuracy;
- sampling rate;
- vị trí sensor;
- lý do chọn.

Không chỉ liệt kê tên cảm biến.

## 7.4. Actuator

Nếu bài toán có điều khiển, phải mô tả:

- LED;
- relay;
- motor;
- buzzer;
- smart plug;
- display;
- actuator khác.

Phải chỉ rõ:

**Trigger → Action → Feedback**

## 7.5. Edge / Device

Ví dụ:

- ESP32;
- Raspberry Pi;
- old smartphone;
- simulator.

Phải giải thích vai trò:

- sampling;
- preprocessing;
- communication;
- local control.

## 7.6. Communication

Phải chỉ rõ:

- Wi-Fi / BLE / Serial / khác;
- TCP / UDP nếu liên quan;
- MQTT / HTTP / REST / khác;
- topic hoặc endpoint chính.

## 7.7. IoT Platform / Backend

Có thể sử dụng:

- Node.js;
- Express;
- Node-RED;
- Mobius4;
- openHAB;
- SmartThings;
- backend tự xây dựng.

Phải nêu rõ vai trò của backend/platform trong hệ thống.

## 7.8. Database

Tối thiểu phải mô tả:

- dữ liệu gì được lưu;
- timestamp;
- device ID;
- measurement;
- command/state nếu có.

## 7.9. Visualization

Không chỉ đưa screenshot dashboard.

Phải trả lời:

> Người dùng nhìn dashboard này để đưa ra quyết định gì?

## 7.10. Security

Tối thiểu:

- authentication;
- credential management;
- không hard-code password/token;
- phân quyền nếu có;
- network exposure.

---

# 8. PHẦN 6 — PROTOTYPE

## 8.1. Prototype 1 — Concept Prototype

Có thể là:

- sketch;
- storyboard;
- Figma;
- mock dashboard;
- paper prototype.

Mục tiêu:

> Kiểm chứng luồng sử dụng.

## 8.2. Prototype 2 — Functional Prototype

Phải có:

```text
Sensor / Device
      ↓
Communication
      ↓
Processing / Platform
      ↓
UI / Dashboard
```

## 8.3. Prototype 3 — Integrated IoT Prototype

Hệ thống end-to-end.

Ví dụ:

```text
Sensor
  ↓
ESP32
  ↓
MQTT
  ↓
Node.js
  ↓
PostgreSQL
  ↓
Grafana
  ↓
User
```

hoặc kiến trúc tương đương.

## 8.4. Yêu cầu tối thiểu

Không được chỉ:

> Đọc sensor và print ra terminal.

Tối thiểu phải chứng minh được một luồng IoT hoàn chỉnh.

---

# 9. PHẦN 7 — TEST & EVALUATION

Cần tách thành hai nhóm.

## 9.1. Technical Testing

Ví dụ:

| Test | Chỉ số |
|---|---|
| Sensor | Sai số |
| Network | Packet success |
| MQTT/HTTP | Message success |
| System | Latency |
| Database | Data completeness |
| Alert | Detection time |
| Reliability | Runtime |

Ví dụ tiêu chí:

```text
100 messages sent
≥ 95 messages received
→ PASS
```

## 9.2. User Testing

Thực hiện lại với người dùng.

Ví dụ nhiệm vụ:

- Task 1: kiểm tra nhiệt độ hiện tại.
- Task 2: xác định phòng nào đang có cảnh báo.
- Task 3: xem dữ liệu 1 giờ gần nhất.

Đánh giá:

- task completion;
- time on task;
- error;
- user feedback;
- satisfaction.

## 9.3. Yêu cầu cần đạt

Phải phân biệt:

**Technical Success ≠ User Success**

Hệ thống kỹ thuật hoạt động tốt nhưng người dùng không sử dụng hiệu quả thì thiết kế vẫn chưa đạt.

---

# 10. PHẦN 8 — ITERATION

Phải có ít nhất một vòng cải tiến:

```text
Prototype
    ↓
Test
    ↓
Feedback
    ↓
Problem Found
    ↓
Change
    ↓
Prototype v2
```

Nên lập bảng:

| Phản hồi | Nguyên nhân | Thay đổi |
|---|---|---|
| Không nhận biết cảnh báo | Màu sắc chưa nổi bật | Thêm alarm banner |
| Update quá chậm | Polling quá lâu | Giảm chu kỳ / dùng event |
| Khó xem trên mobile | Dashboard quá rộng | Responsive layout |

## Yêu cầu cần đạt

Phải chứng minh được:

**Prototype v1 → Feedback → Change → Prototype v2**

Đây là bằng chứng chính cho việc áp dụng Design Thinking.

---

# 11. Kết quả cuối cùng bắt buộc

Mỗi nhóm phải nộp tối thiểu các artefact sau:

1. Problem Statement
2. Persona
3. Pain Point / User Need
4. POV + HMW
5. Ít nhất 3 concept và ma trận lựa chọn
6. Use Case
7. IoT Architecture
8. Prototype hoạt động
9. Technical Test + User Test
10. Iteration: v1 → feedback → v2

Ngoài ra nên có:

- source code trên Git;
- README;
- sơ đồ phần cứng;
- cấu hình hệ thống;
- dữ liệu thử nghiệm;
- video demo 3–5 phút.

---

# 12. Definition of Done

Một đề tài chỉ được coi là hoàn chỉnh nếu trả lời được 6 câu hỏi sau.

## 12.1. WHO?

**Ai là người dùng?**

Không trả lời được → chưa phải Design Thinking.

## 12.2. WHY?

**Họ đang gặp vấn đề gì?**

Không trả lời được → đề tài đang technology-driven.

## 12.3. WHAT?

**Giải pháp tạo giá trị gì?**

Không trả lời được → IoT chưa trở thành service.

## 12.4. HOW?

**Dữ liệu đi qua hệ thống thế nào?**

```text
Sensor → Device → Network → Platform → Data → Application
```

Không trả lời được → kiến trúc IoT chưa rõ.

## 12.5. HOW WELL?

**Hệ thống tốt đến mức nào?**

Phải có metric.

Không có metric → chỉ là demo.

## 12.6. SO WHAT?

**Người dùng thử xong thì kết quả thế nào và nhóm đã sửa gì?**

Không có feedback/iteration → chưa hoàn chỉnh vòng Design Thinking.

---

# 13. Mức yêu cầu đề xuất

| Mức | Yêu cầu |
|---|---|
| Đạt | Problem rõ + sensor/device + network + backend + UI + chạy end-to-end |
| Khá | + database + dashboard + technical test + user test |
| Tốt | + actuator/control + notification + reliability/security |
| Xuất sắc | + ít nhất 1 vòng Design Thinking iteration + định lượng cải thiện + kiến trúc/chất lượng kỹ thuật tốt |

Không bắt buộc AI trong mọi đề tài.

AI chỉ nên được sử dụng khi thực sự giải quyết được vấn đề.

Các thành phần nên bắt buộc:

- user need;
- sensing;
- connectivity;
- data;
- service;
- testing;
- iteration.

---

# 14. Khung báo cáo cuối cùng

```text
1. Introduction
   1.1 Context
   1.2 Problem
   1.3 Objectives
   1.4 Scope

2. Empathize
   2.1 Stakeholders
   2.2 User Research
   2.3 Persona
   2.4 Pain Points
   2.5 Insights

3. Define
   3.1 Problem Statement
   3.2 POV
   3.3 HMW
   3.4 Success Criteria

4. Ideate
   4.1 Alternative Ideas
   4.2 Evaluation Criteria
   4.3 Selected Concept

5. IoT System Design
   5.1 Use Cases
   5.2 Functional Requirements
   5.3 System Architecture
   5.4 Sensors & Actuators
   5.5 Edge Device
   5.6 Communication
   5.7 Backend / IoT Platform
   5.8 Database
   5.9 Application / Dashboard
   5.10 Security

6. Prototype
   6.1 Prototype v1
   6.2 Hardware
   6.3 Software
   6.4 Integration

7. Test & Evaluation
   7.1 Functional Tests
   7.2 Performance Tests
   7.3 User Tests
   7.4 Results

8. Iteration
   8.1 Feedback
   8.2 Changes
   8.3 Prototype v2

9. Final Evaluation
   9.1 Achievement against Requirements
   9.2 Limitations
   9.3 Future Work

10. Conclusion

Appendix
- Source code
- Schematics
- API / Topics
- Test data
- User research evidence
```

---

# 15. Tiêu chí cốt lõi để giao đề tài

Một đề tài IoT theo Design Thinking phải chứng minh được đồng thời:

1. Có người dùng cụ thể.
2. Có vấn đề thực tế.
3. Có nhu cầu và insight.
4. Có nhiều phương án trước khi chọn giải pháp.
5. Có kiến trúc IoT end-to-end.
6. Có prototype chạy được.
7. Có dữ liệu và metric để đánh giá.
8. Có user test.
9. Có phản hồi.
10. Có ít nhất một vòng cải tiến.
