# post.py

import random
import requests
import datetime
import json
import os

# إعدادات API
GEMINI_API_KEY = "AIzaSyDybAXRfYv832CWNwY7rrVt_YNfYmkHpz8"
PAGE_ACCESS_TOKEN = "EAAUmqjbT57QBOZBdPSIvCfyGmfSEyFx2tWLlLNaMZAO9ZBKCd4EJEFhtbgZBm87N6KNYqvl5QGlLurkgHLjVNFUPU9MVJXtfQbGlz45hJX79Wd3PwEp7OF50THiZAqG0A0M3DNF290CdPeYIEMG5YB99uFg3UKK04iqDZBRZCkYWMbE7ltZCHl4ZAEjMSWHi1NeYIgEcs25WIdo7kIRwqWdgZD"
PAGE_ID = "90118319153"
GRAPH_API_URL = f"https://graph.facebook.com/v19.0/{PAGE_ID}/feed"
COMMENT_API_TEMPLATE = "https://graph.facebook.com/v19.0/{post_id}/comments"

headers = {
    "Content-Type": "application/json",
}

def get_gemini_message():
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": "اكتب لي رسالة مشجعة من السيد المسيح موجهة للقارئ بأسلوب شخصي مكونة من 200 حرف."
                    }
                ]
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        message = result["candidates"][0]["content"]["parts"][0]["text"]
        return message.strip()
    else:
        print("❌ فشل في طلب رسالة من Gemini:", response.text)
        return None

def post_to_facebook(text):
    payload = {
        "message": text,
        "access_token": PAGE_ACCESS_TOKEN
    }
    response = requests.post(GRAPH_API_URL, data=payload)
    if response.status_code == 200:
        post_id = response.json().get("id")
        print(f"✅ تم نشر المنشور: {post_id}")
        return post_id
    else:
        print("❌ فشل النشر على فيسبوك:", response.text)
        return None

def comment_on_post(post_id, comment):
    url = COMMENT_API_TEMPLATE.format(post_id=post_id)
    payload = {
        "message": comment,
        "access_token": PAGE_ACCESS_TOKEN
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("💬 تم إضافة تعليق بنجاح")
    else:
        print("❌ فشل في إضافة التعليق:", response.text)

def main():
    now = datetime.datetime.now()
    month = now.month
    day = now.day

    message_templates = [
        f"رسالة المسيح ليك اليوم {month}/{day}\n+\n+\n+\n+\n+\n+\n+\nشوف اول تعليق",
        f"النهاردة {month}/{day}، المسيح باعتلك رسالة مخصوص\n+\n+\n+\n+\n+\n+\nشوف أول تعليق يا حبيب قلبه",
        f"من قلب المسيح ليك: {month}/{day}\n+\n+\n+\n+\n+\n+\n+\nشوف أول تعليق", f"""
رسالة العدراء مريم ليك اليوم {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة البابا كيرلس ليك اليوم {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة تماف ايريني ليك اليوم {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة مارمينا ليك اليوم {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة مارجرجس ليك اليوم {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة ابونا فلتاؤس ليك اليوم {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة ابو سيفين ليك اليوم {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة البابا كيرلس ليك اليوم {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة البابا شنودة ليك اليوم {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة ابونا مينا عبود {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة ابونا بيشوى كامل {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
""",
        f"""
رسالة الانبا موسي الاسود {month}/{day} 
+
+
+
+
+
+
+
شوف اول تعليق
"""
    ]

    post_text = random.choice(message_templates)
    post_id = post_to_facebook(post_text)

    if post_id:
        gemini_message = get_gemini_message()
        if gemini_message:
            comment_on_post(post_id, gemini_message)

if __name__ == "__main__":
    main()
