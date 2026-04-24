from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = "8620142253:AAH8TFYy219PdSiRaVx6et_WE04alYjXaVk"
CHAT_ID = "6315170436"

@app.route('/test', methods=['POST', 'GET'])
def test():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': '✅ تم الاتصال بالسيرفر الوسيط بنجاح يا بشمهندس رشيد! السيرفر جاهز لاستقبال البك أب.'
    }
    r = requests.post(url, data=payload)
    return "Test Sent", 200

@app.route('/upload', methods=['POST'])
def upload():
    file_data = request.get_data()
    if not file_data: return "No data", 400
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    files = {'document': ('AL-Rasheed.backup', file_data)}
    requests.post(url, data={'chat_id': CHAT_ID}, files=files)
    return "Done", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
