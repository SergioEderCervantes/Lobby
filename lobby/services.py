# Integracion con What's App
# Aqui se manejan el envio de todos los msgs de wha

import requests
from django.conf import settings


def notify(message: str) -> None:
    url = "https://ntfy.sh/LobbyRestaurantBar"
    
    requests.post(url=url, data=message,
                  headers={
                      "Title": "Lobby Web Aplication"
                  })
    
    
    
if __name__ == "__main__":
    notify("Hola, primera Prueba ")
    
