from flask import Flask, request
import requests
import io
import os

app = Flask(__name__)

# تأكد أن هذه البيانات صحيحة 100%
BOT_TOKEN = "8620142253:AAH8TFYy219PdSiRaVx6et_WE04alYjXaVk"
CHAT_ID = "6315170436"

@app.route('/upload', methods=['POST'])
def upload():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    
    # جلب البيانات الخام من المايكروتك
    data = request.get_data()
    
    if not data:
        print("Error: No data received from MikroTik")
        return "No Data", 400

    try:
        # تحويل البيانات إلى ملف افتراضي
        file_io = io.BytesIO(data)
        file_io.name = "AL-Rasheed.backup" # تسمية الملف داخل السيرفر
        
        # إرسال الملف للتليجرام
        files = {'document': file_io}
        payload = {'chat_id': CHAT_ID}
        
        r = requests.post(url, data=payload, files=files)
        
        print(f"Telegram Response: {r.text}") # سيظهر في سجلات Render
        
        if r.status_code == 200:
            return "OK", 200
        else:
            return f"Telegram Error: {r.status_code}", 400
            
    except Exception as e:
        print(f"System Error: {str(e)}")
        return "Internal Error", 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
