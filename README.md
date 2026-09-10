# Öğrenci Not Takip Sistemi

Python dili ile geliştirilmiş, Nesne Yönelimli Programlama (OOP) prensiplerine uygun, JSON tabanlı bir öğrenci ve not yönetim sistemidir.

## Özellikler

* **Öğrenci Ekleme:** Öğrenci numarası, ad, soyad, vize ve final notları ile yeni kayıt oluşturma.
* **Not Hesaplama:** Vizenin %40'ı ve finalin %60'ı alınarak ortalama ve harf notu (A, B, C, D, F) otomatik hesaplanır.
* **Veri Saklama (JSON):** Tüm veriler `ogrenciler.json` dosyasında kalıcı olarak saklanır.
* **Arama ve Filtreleme:** Numaraya veya soyada göre arama; harf notuna göre filtreleme imkanı.
* **Silme İşlemi:** Kayıtlı öğrencileri sistemden ve dosyadan silme.
* **Raporlama:** Sınıf ortalaması, geçen/kalan öğrenci sayıları özet raporu.

## Dosya Yapısı

* `ogrenci.py`: Öğrenci varlık sınıfı (Data Model) ve not hesaplama mantığı.
* `yonetici.py`: Veri yönetimi, JSON okuma/yazma ve CRUD işlemleri.
* `main.py`: Kullanıcı etkileşimli konsol menü arayüzü.

## Çalıştırma

Projeyi çalıştırmak için terminalde şu komutu yürütün:

```bash
python3 main.py