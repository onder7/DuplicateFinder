# DuplicateFinder
Yinelenen Dosya Bulucu
https://drive.google.com/file/d/1HdHpmFnlvy0Py_PamRe1BsT8u5AOBux6/view?usp=drive_link
# Yinelenen Dosya Bulucu (Duplicate File Finder)
![image](https://github.com/user-attachments/assets/d5c43a78-9cb1-4fc5-a93c-9537a3426eae)

Yinelenen Dosya Bulucu, bilgisayarınızdaki çift kopya dosyaları bulmanızı sağlayan Python tabanlı bir GUI uygulamasıdır.

## Özellikler

- 🔍 Klasör ve alt klasörlerde yinelenen dosyaları bulma
- 🔒 Çoklu hash algoritması desteği (MD5, SHA-256, SHA-1)
- 📊 Detaylı dosya karşılaştırma ve boyut analizi
- ⚡ Çoklu iş parçacığı desteği ile hızlı tarama
- 🛑 Taramayı durdurma ve devam ettirme özelliği
- 🧹 Sonuçları temizleme
- 📈 İlerleme durumu gösterimi
- 💾 Disk alanı kullanım analizi

## Kurulum

### Gereksinimler

- Python 3.8 veya üzeri
- PyQt5

```bash
# Gerekli kütüphaneleri yükleyin
pip install PyQt5

# Repository'yi klonlayın
git clone https://github.com/onder7/duplicate-file-finder.git

# Proje dizinine gidin
cd duplicate-file-finder

# Uygulamayı çalıştırın
python script_gui.py
```

## Kullanım

1. Uygulamayı başlatın
2. "Klasör Seç" düğmesine tıklayarak veya Ctrl+O kısayolunu kullanarak taranacak klasörü seçin
3. İsterseniz hash algoritmasını değiştirin (varsayılan: MD5)
4. "Taramayı Başlat" düğmesine tıklayın
5. Tarama tamamlandığında yinelenen dosyaların listesini ve detaylı analizi görüntüleyin

### Klavye Kısayolları

- `Ctrl+O`: Klasör seç
- `Ctrl+Q`: Uygulamayı kapat

## Teknik Detaylar

- GUI Framework: PyQt5
- Desteklenen hash algoritmaları: MD5, SHA-256, SHA-1
- Çoklu iş parçacığı desteği ile ana arayüz donmaz
- Büyük dosyalar için chunk-based okuma
- Tarama iptali için güvenli durdurma mekanizması

## Katkıda Bulunma

1. Bu repository'yi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'feat: Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Bir Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## İletişim

Mustafa Önder Aköz

[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin&labelColor=blue)](https://www.linkedin.com/in/mustafa-önder-aköz-23174592)
[![GitHub](https://img.shields.io/badge/GitHub-black?style=flat&logo=github&labelColor=black)](https://github.com/onder7)
[![Medium](https://img.shields.io/badge/Medium-black?style=flat&logo=medium&labelColor=black)](https://medium.com/@onder7)
[![Website](https://img.shields.io/badge/Website-blue?style=flat&logo=google-chrome&labelColor=blue)](https://ondernet.net)

## Teşekkürler

Bu projeyi kullandığınız için teşekkür ederiz. Geri bildirimleriniz ve katkılarınız her zaman değerlidir.

---
© 2024 Mustafa Önder Aköz - Tüm hakları saklıdır.
