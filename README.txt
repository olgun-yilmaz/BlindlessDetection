Diyabetik Retinopati Tespit Sistemi

Bu proje, diyabetik retinopati hastalığının tespiti için geliştirilmiş bir yapay zeka tabanlı görüntü işleme uygulamasıdır. Diyabetik retinopati, diyabet hastalarında görülen ve körlüğe kadar gidebilen ciddi bir göz hastalığıdır. Bu uygulama, göz fundus görüntülerini analiz ederek hastalığın erken teşhisine yardımcı olmayı amaçlamaktadır.

Kullanılan Teknolojiler:
- Python 3.9
- PyQt5 (Kullanıcı Arayüzü)
- TensorFlow/Keras (Yapay Zeka Modeli)
- OpenCV (Görüntü İşleme)
- NumPy (Sayısal İşlemler)
- Pandas (Veri İşleme)

Proje Yapısı:
/src
  /ai - Yapay zeka modeli ve eğitim kodları
    - train_model.ipynb: Model eğitim ve değerlendirme kodları
    - augmentation.ipynb: Veri artırma ve ön işleme kodları
    - load_model.py: Eğitilmiş modelin yüklenmesi ve kullanımı
  /ui - Kullanıcı arayüzü bileşenleri
    - get_started_screen.py: Başlangıç ekranı
    - main_screen.py: Ana uygulama ekranı
    - detection_screen.py: Tespit sonuçları ekranı
  /module - Yardımcı modüller
/icons - Uygulama ikonları
/output - Çıktı dosyaları ve tespit sonuçları

Özellikler:
- Görüntü yükleme ve ön işleme
  * Fundus görüntülerinin yüklenmesi
  * Görüntü kalitesi kontrolü
  * Otomatik görüntü düzeltme
- Diyabetik retinopati tespiti
  * Derin öğrenme tabanlı sınıflandırma
  * Hastalık evresinin belirlenmesi
  * Güven skoru hesaplama
- Sonuçların görselleştirilmesi
  * Tespit edilen lezyonların işaretlenmesi
  * Detaylı rapor oluşturma
  * Sonuçların kaydedilmesi
- Kullanıcı dostu arayüz
  * Kolay kullanım
  * Görsel geri bildirim
  * Yardım ve kılavuz

Kurulum:
1. Python 3.9'i yükleyin
   - Windows: https://www.python.org/downloads/release/python-3913/
   - Linux: sudo apt-get install python3.9
   - macOS: brew install python@3.9

2. Gerekli kütüphaneleri yükleyin:
   pip install -r requirements.txt

3. Uygulamayı başlatın:
   python run.py

Kullanım:
1. Uygulamayı başlatın
2. "Görüntü Yükle" butonuna tıklayın
3. Fundus görüntüsünü seçin
4. Tespit işlemini başlatın
5. Sonuçları inceleyin ve raporu kaydedin

Not: Model eğitimi için gerekli veri seti ve eğitim parametreleri src/ai/train_model.ipynb dosyasında bulunmaktadır. Model eğitimi için yeterli GPU donanımı ve veri seti gereklidir.

Katkıda Bulunma:
- Projeye katkıda bulunmak için pull request gönderebilirsiniz
- Hata bildirimleri için issue açabilirsiniz
- Yeni özellik önerileri için discussion başlatabilirsiniz

Lisans:
Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için LICENSE dosyasına bakınız. Diyabetik Retinopati Tespit Sistemi

Bu proje, diyabetik retinopati hastalığının tespiti için geliştirilmiş bir yapay zeka tabanlı görüntü işleme uygulamasıdır. Diyabetik retinopati, diyabet hastalarında görülen ve körlüğe kadar gidebilen ciddi bir göz hastalığıdır. Bu uygulama, göz fundus görüntülerini analiz ederek hastalığın erken teşhisine yardımcı olmayı amaçlamaktadır.

Kullanılan Teknolojiler:
- Python 3.9
- PyQt5 (Kullanıcı Arayüzü)
- TensorFlow/Keras (Yapay Zeka Modeli)
- OpenCV (Görüntü İşleme)
- NumPy (Sayısal İşlemler)
- Pandas (Veri İşleme)

Proje Yapısı:
/src
  /ai - Yapay zeka modeli ve eğitim kodları
    - train_model.ipynb: Model eğitim ve değerlendirme kodları
    - augmentation.ipynb: Veri artırma ve ön işleme kodları
    - load_model.py: Eğitilmiş modelin yüklenmesi ve kullanımı
  /ui - Kullanıcı arayüzü bileşenleri
    - get_started_screen.py: Başlangıç ekranı
    - main_screen.py: Ana uygulama ekranı
    - detection_screen.py: Tespit sonuçları ekranı
  /module - Yardımcı modüller
/icons - Uygulama ikonları
/output - Çıktı dosyaları ve tespit sonuçları

Özellikler:
- Görüntü yükleme ve ön işleme
  * Fundus görüntülerinin yüklenmesi
  * Görüntü kalitesi kontrolü
  * Otomatik görüntü düzeltme
- Diyabetik retinopati tespiti
  * Derin öğrenme tabanlı sınıflandırma
  * Hastalık evresinin belirlenmesi
  * Güven skoru hesaplama
- Sonuçların görselleştirilmesi
  * Tespit edilen lezyonların işaretlenmesi
  * Detaylı rapor oluşturma
  * Sonuçların kaydedilmesi
- Kullanıcı dostu arayüz
  * Kolay kullanım
  * Görsel geri bildirim
  * Yardım ve kılavuz

Kurulum:
1. Python 3.9'i yükleyin
   - Windows: https://www.python.org/downloads/release/python-3913/
   - Linux: sudo apt-get install python3.9
   - macOS: brew install python@3.9

2. Gerekli kütüphaneleri yükleyin:
   pip install -r requirements.txt

3. Uygulamayı başlatın:
   python run.py

Kullanım:
1. Uygulamayı başlatın
2. "Görüntü Yükle" butonuna tıklayın
3. Fundus görüntüsünü seçin
4. Tespit işlemini başlatın
5. Sonuçları inceleyin ve raporu kaydedin

Not: Model eğitimi için gerekli veri seti ve eğitim parametreleri src/ai/train_model.ipynb dosyasında bulunmaktadır. Model eğitimi için yeterli GPU donanımı ve veri seti gereklidir.

Katkıda Bulunma:
- Projeye katkıda bulunmak için pull request gönderebilirsiniz
- Hata bildirimleri için issue açabilirsiniz
- Yeni özellik önerileri için discussion başlatabilirsiniz

Lisans:
Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için LICENSE dosyasına bakınız. 