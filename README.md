# 🎓 TranscriptAI - OCR ve GPT ile Akıllı Transkript Düzenleyici

TranscriptAI, üniversite transkriptlerinizi ya da herhangi bir akademik PDF belgesini Python kullanarak okuyup, OpenAI GPT ile düzenli ve okunabilir metne çeviren hafif, akıllı ve etkili bir araçtır. Transkriptler artık sadece bir belge değil, anlamlı ve analiz edilebilir bir yapıya kavuşuyor.

---

## ✨ Özellikler

- 📄 PDF’den metin çıkarımı – PyMuPDF (fitz) ile yüksek doğrulukta OCR işlemi  
- 🤖 Yapay Zeka destekli biçimlendirme – OpenAI GPT-3.5 ile başlıkları koruyan, listeler oluşturan, tabloyu metne döken düzenleme  
- 💾 Otomatik kayıt – Çıktılar `sonuc.txt` olarak diske kaydedilir  
- 🔒 Kullanıcıya özel API anahtarı – Güvenli ve kişiselleştirilmiş kullanım

---

## 🚀 Yüklemen Gereken Kütüphaneler



```bash
import fitz  # yani --> PyMuPDF "pip install PyMuPDF" <--
import requests
import json
import os


OpenAI GPT’yi kullanabilmek için OpenAI API Key oluşturun ve .py dosyasında şu satırı güncelleyin:


API_KEY = "sk-..."  # ← kendi API anahtarınızı buraya yapıştırın
⚠️ API anahtarınızı GitHub'da veya herkese açık ortamlarda asla paylaşmayın.

transkript.pdf adlı dosyanızı proje dizinine koyun. Terminalden aşağıdaki komutu çalıştırın:



🤝 Katkı Sağla
Bu proje açık kaynaklıdır ve katkıya açıktır. Yeni özellik önerileri, hata bildirimleri ya da doğrudan pull request’ler gönderebilirsiniz.

🧠 Neden TranscriptAI?
Çünkü bir belge sadece yazıdan ibaret olmamalı. Bilgi düzenli olmalı. Anlam ön planda olmalı.
TranscriptAI, bunu sizin için yapar.

📫 Geliştirici: [Besat Çıngar]
📅 Sürüm: 1.0
🔗 Lisans: MIT
