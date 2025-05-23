🎓 TranscriptAI - OCR ve GPT ile Akıllı Transkript Düzenleyici
TranscriptAI, üniversite transkriptlerinizi ya da herhangi bir akademik PDF belgesini Python kullanarak okuyup, OpenAI GPT ile anlamlı, düzenli ve okunabilir metne dönüştüren hafif, akıllı ve etkili bir araçtır.
Transkriptler artık sadece bir belge değil; analiz edilebilir ve kullanılabilir bir yapıya kavuşuyor.

✨ Özellikler
📄 Yüksek doğruluklu PDF metin çıkarımı: PyMuPDF (fitz) ile OCR işlemi

🤖 Yapay zeka destekli metin biçimlendirme: OpenAI GPT-3.5 ile başlıkları koruyan, listeler oluşturan, tabloları metne dönüştüren düzenleme

💾 Otomatik çıktı kaydı: Düzenlenmiş metin sonuc.txt olarak kaydedilir

🔒 Kullanıcıya özel API anahtarı: Güvenli ve kişiselleştirilmiş kullanım imkanı

🚀 Kurulum & Kullanım
Depoyu klonlayın:

bash
Kopyala
Düzenle
git clone https://github.com/kullaniciadi/transcriptai.git
cd transcriptai
Gerekli paketleri yükleyin:


pip install PyMuPDF requests
OpenAI API anahtarınızı alın ve main.py dosyasındaki ilgili satırı şu şekilde güncelleyin:


API_KEY = "sk-..."  # ← kendi API anahtarınızı buraya yapıştırın
⚠️ API anahtarınızı GitHub veya başka herkese açık ortamlarda paylaşmayın!

transkript.pdf dosyanızı proje dizinine koyun.

Terminalden programı çalıştırın:


python main.py
Çıktı, proje dizininde sonuc.txt olarak otomatik kaydedilecektir.

📂 Proje Yapısı

transcriptai/
├── main.py            # Ana çalışma dosyası
├── sonuc.txt          # Oluşan çıktı dosyası
├── transkript.pdf     # İşlenecek PDF dosyası (kullanıcıdan)
└── README.md          # Proje dokümantasyonu (bu dosya)
📦 Kullanılan Teknolojiler
PyMuPDF (fitz) – PDF’den metin çıkarımı için

requests – API çağrıları için

OpenAI GPT-3.5 Turbo – Metni doğal ve düzenli biçimde yapılandırmak için

🤝 Katkıda Bulunma
Bu proje açık kaynaklıdır ve katkılarınızı bekler!
Yeni özellik önerileri, hata bildirimleri ya da doğrudan pull request’ler gönderebilirsiniz.

🧠 Neden TranscriptAI?
Çünkü bir belge sadece yazıdan ibaret olmamalı.
Bilgi düzenli olmalı. Anlam ön planda olmalı.
TranscriptAI, bunu sizin için yapar.

📫 İletişim & Bilgiler
Geliştirici: Senin GitHub profilin

Sürüm: 1.0

Lisans: MIT License

