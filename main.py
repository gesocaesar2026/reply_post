import requests
import json
import random
import os

ACCESS_TOKEN = "EAAUmqjbT57QBOZBdPSIvCfyGmfSEyFx2tWLlLNaMZAO9ZBKCd4EJEFhtbgZBm87N6KNYqvl5QGlLurkgHLjVNFUPU9MVJXtfQbGlz45hJX79Wd3PwEp7OF50THiZAqG0A0M3DNF290CdPeYIEMG5YB99uFg3UKK04iqDZBRZCkYWMbE7ltZCHl4ZAEjMSWHi1NeYIgEcs25WIdo7kIRwqWdgZD"
PAGE_ID = "90118319153"
REPLIED_FILE = "replied_posts.json"

# تحميل الرسائل
with open("messages.txt", "r", encoding="utf-8") as f:
    MESSAGES = [line.strip() for line in f if line.strip()]

# تحميل المنشورات التي تم الرد عليها
if os.path.exists(REPLIED_FILE):
    with open(REPLIED_FILE, "r") as f:
        replied_posts = json.load(f)
else:
    replied_posts = []

def get_last_posts():
    url = f"https://graph.facebook.com/v19.0/{PAGE_ID}/posts"
    params = {
        "access_token": ACCESS_TOKEN,
        "limit": 5
    }
    response = requests.get(url, params=params)
    return response.json().get("data", [])

def reply_to_post(post_id, message):
    url = f"https://graph.facebook.com/v19.0/{post_id}/comments"
    payload = {
        "message": message,
        "access_token": ACCESS_TOKEN
    }
    response = requests.post(url, data=payload)
    return response.status_code == 200

def save_replied():
    with open(REPLIED_FILE, "w") as f:
        json.dump(replied_posts, f)

def main():
    posts = get_last_posts()
    for post in posts:
        post_id = post["id"]
        if post_id in replied_posts:
            continue
        message = random.choice(MESSAGES)
        success = reply_to_post(post_id, message)
        if success:
            print(f"✅ Replied to: {post_id}")
            replied_posts.append(post_id)
        else:
            print(f"❌ Failed to reply: {post_id}")
    save_replied()

if __name__ == "__main__":
    main()
