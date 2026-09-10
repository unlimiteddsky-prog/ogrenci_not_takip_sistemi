# yonetici.py

import json # JSON dosyalarıyla çalışmamızı sağlar.
import os # İşletim sistemiyle ilgili işlemleri yapmamızı sağlar.
from ogrenci import ogrenci # ogrenci.py dosyasından ogrenci isimli sınıfı/fonksiyonu içe aktarır.


class Yonetici:
    """Öğrenci verilerini yöneten ve dosya işlemlerini gerçekleştiren sınıf."""

    def __init__(self, dosya_adi="ogrenciler.json"):
        self.dosya_adi = dosya_adi
        self.ogrenciler = []
        self.veri_yukle()

    def veri_yukle(self):
        """JSON dosyasındaki verileri okur ve ogrenci nesnelerine dönüştürür."""
        if not os.path.exists(self.dosya_adi):
            self.ogrenciler = []
            return

        try:
            with open(self.dosya_adi, "r", encoding="utf-8") as dosya:
                veri_listesi = json.load(dosya)
                self.ogrenciler = [ogrenci.from_dict(d) for d in veri_listesi]
        except (json.JSONDecodeError, FileNotFoundError):
            self.ogrenciler = []

    def veri_kaydet(self):
        """Mevcut öğrenci listesini JSON dosyasına kaydeder."""
        try:
            veri_listesi = [o.to_dict() for o in self.ogrenciler]
            with open(self.dosya_adi, "w", encoding="utf-8") as dosya:
                json.dump(veri_listesi, dosya, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            print(f"Dosya kaydetme hatası: {e}")
            return False

    def ogrenci_ekle(self, yeni_ogrenci):
        """Yeni bir öğrenci ekler (Aynı öğrenci numarası varsa eklemez)."""
        for o in self.ogrenciler:
            if o.ogrenci_no == yeni_ogrenci.ogrenci_no:
                return False, "Bu öğrenci numarası zaten mevcut!"

        self.ogrenciler.append(yeni_ogrenci)
        self.veri_kaydet()
        return True, "Öğrenci başarıyla eklendi."