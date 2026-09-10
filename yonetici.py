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

    def ogrenci_sil(self, ogrenci_no):
        """Numarasına göre öğrenciyi sistemden siler."""
        for o in self.ogrenciler:
            if o.ogrenci_no == str(ogrenci_no):
                self.ogrenciler.remove(o)
                self.veri_kaydet()
                return True, "Öğrenci başarıyla silindi."
        return False, "Öğrenci bulunamadı."

    def ogrenci_ara(self, arama_metni):
        """Soyada veya numaraya göre arama yapar."""
        metin = str(arama_metni).strip().upper()
        sonuclar = [
            o for o in self.ogrenciler 
            if metin in o.soyad or metin in o.ogrenci_no
        ]
        return sonuclar

    def harf_notuna_gore_filtrele(self, harf_notu):
        """Belirtilen harf notuna sahip öğrencileri filtreler."""
        harf = str(harf_notu).strip().upper()
        return [o for o in self.ogrenciler if o.harf_notu == harf]

    def genel_rapor(self):
        """Sistemdeki genel durumu raporlar (Özet ekranı)."""
        toplam = len(self.ogrenciler)
        if toplam == 0:
            return {"toplam": 0, "gecen": 0, "kalan": 0, "ort": 0.0}

        gecenler = sum(1 for o in self.ogrenciler if o.durum_bilgisi() == "Geçti")
        kalanlar = toplam - gecenler
        genel_ortalama = round(sum(o.ortalama for o in self.ogrenciler) / toplam, 2)

        return {
            "toplam": toplam,
            "gecen": gecenler,
            "kalan": kalanlar,
            "ort": genel_ortalama
        }