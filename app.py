from flask import Flask, request
import requests
import io
import os

app = Flask(__name__)

BOT_TOKEN = "8620142253:AAH8TFYy219PdSiRaVx6et_WE04alYjXaVk"
CHAT_ID = "6315170436"

@app.route('/upload', methods=['POST'])
def upload():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    
    # تصحيح: قراءة البيانات الخام مباشرة من المايكروتك
    data = request.data  
    
    if data:
        # تحويل البيانات إلى ملف ليرسله التليجرام
        file_io = io.BytesIO(data)
        files = {'document': ('AL-Rasheed.backup', file_io)}
        
        # إرسال الملف إلى التليجرام
        r = requests.post(url, data={'chat_id': CHAT_ID}, files=files)
        
        if r.status_code == 200:
            return "File Sent Successfully!", 200
        else:
            return f"Telegram Error: {r.text}", r.status_code
            
    return "No Data Received", 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
