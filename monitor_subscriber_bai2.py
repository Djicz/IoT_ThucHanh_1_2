import json
import paho.mqtt.client as mqtt

# Cau hinh broker
BROKER = "localhost"
PORT = 1883
TOPIC = "iot/lab/sensor01/data"

# Tao Client
try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="Monitor_Subscriber_Bai2")
except AttributeError:
    client = mqtt.Client(client_id="Monitor_Subscriber_Bai2")

def on_connect(client, userdata, flags, rc, *args, **kwargs):
    if rc == 0:
        print(f"[*] Ket noi thanh cong toi Broker: {BROKER}:{PORT}")
        print(f"[*] Dang theo doi du lieu tu topic: '{TOPIC}'...")
        print("[*] Nhan Ctrl+C de dung chuong trinh.\n" + "="*40)
        client.subscribe(TOPIC, qos=1)
    else:
        print(f"[!] Ket noi that bai, ma loi: {rc}")

def on_message(client, userdata, msg):
    try:
        payload_str = msg.payload.decode("utf-8")
        data = json.loads(payload_str)

        device_id = data.get("device_id", "Unknown")
        temp = data.get("temperature", 0)
        hum = data.get("humidity", 0)

        print("\n" + "-"*35)
        print(f"Device: {device_id}")
        print(f"Temperature: {temp} C")
        print(f"Humidity: {hum} %")

        # Kiem tra nguong va canh bao
        if temp > 35:
            print(">>> CANH BAO: Nhiet do cao <<<")
        if hum < 40:
            print(">>> CANH BAO: Do am thap <<<")
        print("-"*35)

    except json.JSONDecodeError:
        print(f"[!] Loi: Khong the parse JSON tu payload: {msg.payload}")
    except Exception as e:
        print(f"[!] Loi xu ly: {e}")

client.on_connect = on_connect
client.on_message = on_message

print("Dang ket noi toi MQTT Broker...")
client.connect(BROKER, PORT, keepalive=60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\n[*] Nguoi dung da dung chuong trinh.")
    client.disconnect()
    print("[*] Da ngat ket noi.")
