import os
import random
import requests
from datetime import datetime

# إعداد المتغيرات
ACCESS_TOKEN = "EAAUmqjbT57QBOZBdPSIvCfyGmfSEyFx2tWLlLNaMZAO9ZBKCd4EJEFhtbgZBm87N6KNYqvl5QGlLurkgHLjVNFUPU9MVJXtfQbGlz45hJX79Wd3PwEp7OF50THiZAqG0A0M3DNF290CdPeYIEMG5YB99uFg3UKK04iqDZBRZCkYWMbE7ltZCHl4ZAEjMSWHi1NeYIgEcs25WIdo7kIRwqWdgZD"
PAGE_ID = "90118319153"
GEMINI_API_KEY ="AIzaSyDybAXRfYv832CWNwY7rrVt_YNfYmkHpz8"

def get_encouraging_message():
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {
                "parts": [
                    {"text": "اكتب لي رسالة مشجعة ومليانة بالحب كأنها من المسيح إلى الإنسان، باللغة العربية، لا تذكر أنها من ذكاء اصطناعي"}
                ]
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.ok:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    else:
        return "الرب معك ويشجعك في كل طريق."

def get_last_post_id():
    url = f"https://graph.facebook.com/v19.0/{PAGE_ID}/posts?access_token={ACCESS_TOKEN}&limit=1"
    res = requests.get(url)
    return res.json()['data'][0]['id'] if res.ok else None

def comment_on_post(post_id, message):
    url = f"https://graph.facebook.com/v19.0/{post_id}/comments"
    data = {"message": message, "access_token": ACCESS_TOKEN}
    return requests.post(url, data=data)

def main():
    post_id = get_last_post_id()
    if not post_id:
        print("❌ فشل في الحصول على ID آخر منشور")
        return
    message = get_encouraging_message()
    print("🔹 رسالة:", message)
    res = comment_on_post(post_id, message)
    if res.ok:
        print("✅ تم إضافة التعليق بنجاح")
    else:
        print("❌ فشل في التعليق", res.text)

if __name__ == "__main__":
    main()
