# Integracion con What's App
# Aqui se manejan el envio de todos los msgs de wha

import requests
from django.conf import settings

def send_whatsapp_message(message):
    url = f"{settings.WHATSAPP_API_URL}{settings.WHATSAPP_PHONE_ID}/messages"
    phone_number = "524492580708"


    headers = {
        'Authorization': f"Bearer {settings.WHATSAPP_ACCESS_TOKEN}",
        'Content-type': 'application/json',
    }
    data ={
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "text",
        "text": {
            "body": message
        }
    }
    
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.json(), "status": response.status_code}