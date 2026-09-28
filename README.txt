========================================================================
BÀI 2: MÔ PHỎNG CẢM BIẾN NHIỆT ĐỘ VÀ ĐỘ ẨM BẰNG MQTT
========================================================================

1. THÔNG TIN SINH VIÊN:
- Họ và tên: Họ tên
- Mã sinh viên: Mã SV

2. BROKER SỬ DỤNG:
- Tên Broker: Local Eclipse Mosquitto Broker
- Host / IP: localhost
- Cổng (Port): 1883
- Topic: iot/lab/sensor01/data

3. CÁCH CHẠY TỪNG CHƯƠNG TRÌNH:
(Mở 2 cửa sổ Terminal)

- Terminal 1: Chạy Monitoring Subscriber để lắng nghe và cảnh báo
  Lệnh chạy: python monitor_subscriber_bai2.py

- Terminal 2: Chạy Sensor Publisher để gửi dữ liệu cảm biến định kỳ
  Lệnh chạy: python sensor_publisher_bai2.py

4. KẾT QUẢ ĐẠT ĐƯỢC:
- Dữ liệu cảm biến được đóng gói chuẩn định dạng JSON gồm các trường:
  {"device_id": "sensor01", "temperature": 28.5, "humidity": 65.2}
- Tần suất gửi dữ liệu: Định kỳ tuần hoàn 3 giây/lần.
- Subscriber phân tích chính xác chuỗi JSON và hiển thị trực quan thông số nhiệt độ, độ ẩm.
- Kiểm tra ngưỡng và đưa ra cảnh báo chính xác:
  + Nếu nhiệt độ > 35°C  -> In cảnh báo ">>> CANH BAO: Nhiet do cao <<<".
  + Nếu độ ẩm < 40%      -> In cảnh báo ">>> CANH BAO: Do am thap <<<".
========================================================================
