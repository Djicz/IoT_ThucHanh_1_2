# BÀI 2: MÔ PHỎNG CẢM BIẾN NHIỆT ĐỘ VÀ ĐỘ ẨM BẰNG MQTT

## 1. Broker sử dụng
- **Tên Broker:** Local Eclipse Mosquitto Broker
- **Host / IP:** `localhost`
- **Port:** `1883`
- **Giao thức:** MQTT TCP
- **Topic:** `iot/lab/sensor01/data`

---

## 2. Cách chạy từng chương trình

Mở **2 cửa sổ Terminal**:

1. **Terminal 1 - Chạy Monitoring Subscriber (Giám sát & Cảnh báo):**
   ```bash
   python monitor_subscriber_bai2.py
   ```
   *Chương trình kết nối tới Broker, subscribe topic `iot/lab/sensor01/data` và chờ dữ liệu cảm biến.*

2. **Terminal 2 - Chạy Sensor Publisher (Mô phỏng cảm biến):**
   ```bash
   python sensor_publisher_bai2.py
   ```
   *Chương trình tự động sinh ngẫu nhiên nhiệt độ & độ ẩm, đóng gói định dạng JSON và gửi tuần hoàn mỗi 3 giây.*

---

## 3. Kết quả đạt được

### Output tại Terminal Sensor Publisher:
```text
Dang ket noi toi MQTT Broker...
[*] Ket noi thanh cong toi Broker: localhost:1883
[*] Bat dau gui du lieu cam bien dinh ky moi 3s len topic 'iot/lab/sensor01/data'...
[*] Nhan Ctrl+C de dung chuong trinh.
========================================
[1] Gui du lieu: {"device_id": "sensor01", "temperature": 28.5, "humidity": 65.2}
[2] Gui du lieu: {"device_id": "sensor01", "temperature": 36.8, "humidity": 37.4}
[3] Gui du lieu: {"device_id": "sensor01", "temperature": 31.2, "humidity": 55.0}
```

### Output tại Terminal Monitoring Subscriber:
```text
Dang ket noi toi MQTT Broker...
[*] Ket noi thanh cong toi Broker: localhost:1883
[*] Dang theo doi du lieu tu topic: 'iot/lab/sensor01/data'...
[*] Nhan Ctrl+C de dung chuong trinh.
========================================

-----------------------------------
Device: sensor01
Temperature: 28.5 C
Humidity: 65.2 %
-----------------------------------

-----------------------------------
Device: sensor01
Temperature: 36.8 C
Humidity: 37.4 %
>>> CANH BAO: Nhiet do cao <<<
>>> CANH BAO: Do am thap <<<
-----------------------------------
```

### Đánh giá:
- Payload gửi đi tuân thủ 100% chuẩn định dạng JSON (`device_id`, `temperature`, `humidity`).
- Dữ liệu được gửi đều đặn chu kỳ 3 giây/lần.
- Subscriber parse JSON chính xác, hiển thị trực quan và kích hoạt cảnh báo đúng điều kiện:
  + Nhiệt độ > 35°C: hiển thị cảnh báo nhiệt độ cao.
  + Độ ẩm < 40%: hiển thị cảnh báo độ ẩm thấp.
