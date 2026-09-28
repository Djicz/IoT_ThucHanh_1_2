import time
import json
import random
import paho.mqtt.client as mqtt

# Cau hinh broker
BROKER = "localhost"
PORT = 1883
TOPIC = "iot/lab/sensor01/data"
DEVICE_ID = "sensor01"
INTERVAL = 3  # Giay

# Tao Client
try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="Sensor_Publisher_Bai2")
except AttributeError:
    client = mqtt.Client(client_id="Sensor_Publisher_Bai2")

def on_connect(client, userdata, flags, rc, *args, **kwargs):
    if rc == 0:
        print(f"[*] Ket noi thanh cong toi Broker: {BROKER}:{PORT}")
    else:
        print(f"[!] Ket noi that bai, ma loi: {rc}")

client.on_connect = on_connect

print("Dang ket noi toi MQTT Broker...")
client.connect(BROKER, PORT, keepalive=60)
client.loop_start()

time.sleep(1)
print(f"[*] Bat dau gui du lieu cam bien dinh ky moi {INTERVAL}s len topic '{TOPIC}'...")
print("[*] Nhan Ctrl+C de dung chuong trinh.\n" + "="*40)

try:
    count = 1
    while True:
        # Sinh du lieu nhiet do (20.0 - 42.0 C) va do am (30.0 - 85.0 %)
        # Co ty le vuot nguong de test canh bao
        temperature = round(random.uniform(20.0, 42.0), 1)
        humidity = round(random.uniform(30.0, 85.0), 1)

        payload_dict = {
            "device_id": DEVICE_ID,
            "temperature": temperature,
            "humidity": humidity
        }
        
        # Chuyen dictionary sang chuoi JSON
        payload_json = json.dumps(payload_dict)

        print(f"[{count}] Gui du lieu: {payload_json}")
        client.publish(TOPIC, payload_json, qos=1)

        count += 1
        time.sleep(INTERVAL)

except KeyboardInterrupt:
    print("\n[*] Nguoi dung da dung chuong trinh.")
finally:
    client.loop_stop()
    client.disconnect()
    print("[*] Da ngat ket noi.")
