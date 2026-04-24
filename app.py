from flask import Flask, request
import requests
import io
import os

app = Flask(__name__)

# بيانات البوت الخاصة بك
BOT_TOKEN = "8620142253:AAH8TFYy219PdSiRaVx6et_WE04alYjXaVk"
CHAT_ID = "6315170436"

@app.route('/upload', methods=['POST'])
def upload():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    data = request.get_data()
    
    if data:
        file_io = io.BytesIO(data)
        # نرسل الملف للتليجرام
        r = requests.post(url, data={"chat_id": CHAT_ID}, files={"document": ("AL-Rasheed.backup", file_io)})
        return f"Done: {r.status_code}", 200
    
    return "No Data", 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
