# Truemoney webhook gateway but Python
ระบบ Truemoney Webhook

พัฒนาต่อจาก Repo หลักของ [DearTanakorn](https://github.com/DearTanakorn/truemoney-webhook-gateway)

## Requirement

- Python 3.9++
- JWT Secret ของ Webhook

## Prerequisites

1. หลังจากได้ Server แล้ว รันไฟล์ระบบและ ทำการตั้งค่าลิ้งค์ Webhook ไปที่ URL ของท่านแล้วตามด้วย /webhook เช่น http://example.com/webhook
<img src="https://user-images.githubusercontent.com/43856376/171544028-77e2a972-312f-439b-9d1c-053397fc73af.jpg" height="500">

3. เมื่อตั้งค่าลิ้งค์เสร็จเรียบร้อยแล้ว ให้นำ Secret ที่ได้รับหลังจากนั้นมาใส่ใน .env ตรง JWT_SECRET
<img src="https://user-images.githubusercontent.com/43856376/171543646-18566f5b-4ab2-4403-96d5-5d228cf58051.png" height="500">


## Installation

1. ทำการ Clone repo นี้ลงไปใน Server ที่ต้องการ
2. ติดตั้ง Package ต่าง ๆ
   ```
    pip install -r requirements.txt
   ```
3. เปลี่ยนชื่อจาก '.env.example' เป็น '.env'
4. แก้ไข SECRET_KEY ใน `.env` ที่ได้รับหลังจากตั้งค่า Webhook เสร็จเรียบร้อยแล้ว
   ```
    SECRET_KEY=jwt_token
   ```

## How to run

1. เปิด CMD หรือ Bash ขึ้นมา
2. พิมพ์คำสั่ง `py main.py`

## Contributing

สำหรับใครที่ต้องการแก้ไขหรือมีข้อเสนอต่าง ๆ สามารถเปิด Issue หรือ Pull request มาได้เลยนะครับ เนื่องจากไม่ค่อยได้เขียน Repo เป็นสาธารณะมากสักเท่าไหร + ค่อนข้างเมา ๆ ตอนเขียนด้วย ฮ่า ๆ


