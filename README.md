# 🧠 TranscriptAI – OCR ve Yapay Zeka ile Transkript Düzenleyici

TranscriptAI, PDF formatındaki transkript belgelerini okuyarak, içerdiği metni OpenAI GPT modeli yardımıyla okunabilir, düzenli ve temiz bir şekilde çıktılayan Python tabanlı bir araçtır.

---

## 🚀 Özellikler

- 📄 PDF'den metin çıkarma (PyMuPDF)
- 🤖 Yapay zeka ile anlamlı ve biçimlendirilmiş metin üretme (OpenAI GPT-3.5 Turbo)
- 🗂️ Tabloları liste haline getirme, başlıkları koruma
- 📝 Düzenlenmiş metni `.txt` olarak kaydetme

---

## 🛠️ Kullanılan Kütüphaneler

Aşağıdaki Python kütüphaneleri gereklidir:

```bash
pip install PyMuPDF requests
PyMuPDF (fitz): PDF dosyalarından metin çıkarmak için

requests: OpenAI API'ye istek göndermek için

json, os: Python’un yerleşik kütüphaneleri (ayrıca yüklenmesi gerekmez)

🔑 OpenAI API Anahtarı
Bu proje, OpenAI API kullanmaktadır. API anahtarınızı kendiniz oluşturmalı ve aşağıdaki satırı kendi anahtarınızla değiştirerek kullanmalısınız:

python
Kopyala
Düzenle
API_KEY = "buraya-kendi-openai-api-anahtarınızı-yapıştırın"
⚠️ Güvenlik Uyarısı: API anahtarınızı GitHub gibi herkese açık yerlerde paylaşmayın. .env dosyası veya çevre değişkenleri ile gizli tutmanız önerilir.

⚙️ Kurulum ve Kullanım
Gereksinimleri yükleyin:

bash
Kopyala
Düzenle
pip install PyMuPDF requests
transkript.pdf adlı dosyayı proje klasörüne yerleştirin.

main.py içindeki API_KEY değişkenini kendi OpenAI anahtarınızla değiştirin.

Komutu çalıştırın:

bash
Kopyala
Düzenle
python main.py
Sonuçlar sonuc.txt dosyasına kaydedilir.

📦 Proje Yapısı
bash
Kopyala
Düzenle
TranscriptAI/
│
├── main.py              # Ana Python kodu
├── transkript.pdf       # Girdi PDF dosyası (kullanıcı ekler)
├── sonuc.txt            # Çıktı dosyası
└── README.md            # Proje açıklaması
📬 Katkı
Bu açık kaynak projeye katkı sağlayabilirsiniz. Hataları bildirerek ya da pull request göndererek destek olabilirsiniz.
