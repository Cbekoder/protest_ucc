import requests

def send_verification_sms(phone, code):
    url = "https://notify.eskiz.uz/api/message/sms/send"
    api_key = "XSdi46QhZyFHYP5K41GLsAXcWmTDjP877GICvYiK"
    payload = {
        "mobile_phone": phone,
        "message": f"Tasdiqlash parolingiz: {code}",
        "from": "4546",
        # "callback_url": "http://your-callback-url.com"
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()
        if response.status_code == 200:
            print("SMS sent successfully.")
        else:
            print(f"Failed to send SMS: {response_data}")
    except requests.RequestException as e:
        print(f"Error sending SMS: {e}")

# Make sure to handle the case where the API might be down or the request fails
