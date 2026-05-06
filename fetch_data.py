import os
import json
import requests
from datetime import datetime

# GitHub Secrets üzerinden gelen kimlik bilgilerini al
API_KEY = os.environ.get("INTERVALS_API_KEY")
ATHLETE_ID = os.environ.get("INTERVALS_ATHLETE_ID")

if not API_KEY or not ATHLETE_ID:
    print("Hata: Kimlik bilgileri bulunamadı!")
    exit(1)

# API İstek Başlıkları ve Kimlik Doğrulama
# Intervals.icu'da kullanıcı adı olarak 'API_KEY' kelimesi kullanılır, şifre ise senin gizli anahtarındır.
auth = ("API_KEY", API_KEY)
headers = {"Accept": "application/json"}

# Çekilecek verinin adresi (Örnek olarak fitness/wellness endpointi)
url = f"https://intervals.icu/api/v1/athlete/{ATHLETE_ID}/fitness"

print("Intervals.icu ile iletişim kuruluyor...")
response = requests.get(url, auth=auth, headers=headers)

if response.status_code == 200:
    data = response.json()
    
    # Klasör yoksa oluştur
    os.makedirs("training-data", exist_ok=True)
    
    # Veriyi latest.json olarak kaydet
    file_path = "training-data/latest.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print("Harika! Veriler başarıyla çekildi ve 'latest.json' dosyasına kaydedildi.")
else:
    print(f"Bir hata oluştu. Kod: {response.status_code}")
    print(response.text)
