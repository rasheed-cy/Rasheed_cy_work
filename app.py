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
    
    # تصحيح: قراءة البيانات الخام من المايكروتك (src-path)
    # المايكروتك يرسل الملف كـ byte stream
    file_data = request.get_data()
    
    if not file_data:
        return "No data found", 400

    try:
        # تحويل البيانات إلى ملف ليفهمه التليجرام
        file_io = io.BytesIO(file_data)
        file_io.name = "AL-Rasheed.backup"
        
        # إرسال الملف للتليجرام
        response = requests.post(
            url, 
            data={'chat_id': CHAT_ID}, 
            files={'document': file_io}
        )
        
        if response.status_code == 200:
            return "Success", 200
        else:
            # إذا كان الخطأ من التليجرام، السيرفر سيرد عليك بـ 400
            return f"Telegram Error: {response.text}", 400
            
    except Exception as e:
        return f"Server Error: {str(e)}", 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
