from flask import Flask, request
import requests
import io

app = Flask(__name__)

BOT_TOKEN = "8620142253:AAH8TFYy219PdSiRaVx6et_WE04alYjXaVk"
CHAT_ID = "6315170436"

@app.route('/upload', methods=['POST'])
def upload():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    
    if 'file' in request.files:
        file_to_send = request.files['file']
        requests.post(url, data={"chat_id": CHAT_ID}, files={"document": file_to_send})
    else:
        file_data = request.get_data()
        if file_data:
            file_to_send = io.BytesIO(file_data)
            requests.post(url, data={"chat_id": CHAT_ID}, files={"document": ("AL-Rasheed.backup", file_to_send)})
        else:
            return "No data received", 400

    return "OK", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
