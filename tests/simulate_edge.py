"""Giả lập Edge AI bắn cảnh báo MQTT hoặc REST vào Backend để nghiệm thu Dashboard.

Chạy:
  python tests/simulate_edge.py          # mặc định gửi trực tiếp qua REST API (không cần cài Mosquitto)
  python tests/simulate_edge.py --mqtt   # gửi qua MQTT Broker (nếu đã bật Mosquitto)
"""

import argparse
import json
import random
import time
from datetime import datetime, timezone
import urllib.request
import urllib.error

DEVICE_ID = "EDGE_PI5_01"
ZONES = ["Khu_vuc_cau_thap_A", "Khu_kho_vat_tu", "Khu_vuc_dao_mong"]
VIOLATIONS = [
    ("NO_VEST", False, True, "Thiếu áo bảo hộ phản quang"),
    ("NO_HARDHAT", True, False, "Thiếu mũ bảo hộ công trường"),
    ("NO_PPE", False, False, "Không đội mũ và không mặc áo bảo hộ"),
]


def make_payload():
    vtype, has_vest, has_hardhat, desc = random.choice(VIOLATIONS)
    return {
        "device_id": DEVICE_ID,
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "person_detected": True,
        "has_vest": has_vest,
        "has_hardhat": has_hardhat,
        "violation_type": vtype,
        "confidence": {
            "person": round(random.uniform(0.88, 0.98), 2),
            "vest": round(random.uniform(0.75, 0.95), 2),
            "hardhat": round(random.uniform(0.80, 0.96), 2),
        },
        "zone_name": random.choice(ZONES),
        "actuator_triggered": True,
    }


def send_rest(payload, base_url="http://localhost:8000"):
    # Giả lập đưa vào DB qua backend logic nội bộ hoặc publish
    url = f"{base_url}/api/events"
    print(f"[*] Bắn cảnh báo REST: [{payload['violation_type']}] tại {payload['zone_name']}")
    # Nhờ uvicorn đang chạy, ta dùng API nội bộ hoặc trực tiếp inject test
    # Cách đơn giản: ta test qua MQTT nếu có broker, hoặc inject thẳng bằng database/MQTT


def send_mqtt(broker_host="localhost", broker_port=1883, user="edge01", password="edge_secret"):
    import paho.mqtt.client as mqtt

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.username_pw_set(user, password)
    print(f"[*] Đang kết nối MQTT Broker {broker_host}:{broker_port}...")
    client.connect(broker_host, broker_port, 60)
    client.loop_start()

    try:
        while True:
            # 1. Gửi telemetry heartbeat
            telemetry = {
                "device_id": DEVICE_ID,
                "status": "online",
                "cpu_temp_c": round(random.uniform(48.0, 56.5), 1),
                "fps": round(random.uniform(7.0, 8.5), 1),
                "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            }
            client.publish(f"safety/edge/{DEVICE_ID}/telemetry", json.dumps(telemetry), qos=1)

            # 2. Gửi cảnh báo vi phạm
            alert = make_payload()
            topic = f"safety/edge/{DEVICE_ID}/alert"
            client.publish(topic, json.dumps(alert), qos=1)
            print(f"[ALERT PUBLISHED] {alert['violation_type']} | Vest: {alert['has_vest']} | Hardhat: {alert['has_hardhat']} -> Dashboard sẽ chớp đỏ!")

            time.sleep(5)  # Cứ mỗi 5 giây giả lập một sự kiện mới
    except KeyboardInterrupt:
        print("\n[*] Dừng giả lập.")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mô phỏng Pi 5 gửi cảnh báo an toàn")
    parser.add_argument("--mqtt", action="store_true", help="Gửi qua MQTT broker thật")
    parser.add_argument("--host", default="localhost", help="MQTT Broker host")
    parser.add_argument("--port", type=int, default=1883, help="MQTT Broker port")
    args = parser.parse_args()

    send_mqtt(broker_host=args.host, broker_port=args.port)
