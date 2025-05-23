import fitz  # PyMuPDF
import requests
import json
import os

API_KEY = "API <----"

def pdf_to_text(pdf_yolu):
    print("📄 PDF'den metin çıkarılıyor...")
    doc = fitz.open(pdf_yolu)
    metin = ""
    for sayfa_num in range(len(doc)):
        sayfa = doc.load_page(sayfa_num)
        metin += sayfa.get_text()
    return metin

def openai_metni_isle(metin):
    print("🔗 Metin OpenAI GPT-3.5 Turbo'ya gönderiliyor...")

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Bu metni düzenli şekilde çıkar. Başlıkları koru, tabloları liste yap, okunaklı hale getir (NOT EKSİKSİZ YAZ HERŞEYİ):\n\n{metin}"}
        ],
        "max_tokens": 2000
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code != 200:
        print(f"❌ API Hatası: {response.status_code} - {response.text}")
        return "HATA"

    sonuc = response.json()
    cevap = sonuc["choices"][0]["message"]["content"]
    return cevap

def txt_kaydet(metin, dosya_adi="sonuc.txt"):
    with open(dosya_adi, "w", encoding="utf-8") as f:
        f.write(metin)
    print(f"✅ Metin '{dosya_adi}' dosyasına kaydedildi.")

# Kullanım
pdf_yolu = "transkript.pdf"

if os.path.exists(pdf_yolu):
    metin = pdf_to_text(pdf_yolu)
    sonuc = openai_metni_isle(metin)
    if sonuc != "HATA":
        txt_kaydet(sonuc)
else:
    print("❌ PDF dosyası bulunamadı.")
