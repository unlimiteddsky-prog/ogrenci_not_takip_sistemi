# ogrenci.py

class Ogrenci:
    """Öğrenci bilgilerini ve not hesaplama mantığını tutan varlık sınıfı."""
    
    def __init__(self, ogr_no, ad, soyad, vize=0.0, final=0.0):
        self.ogr_no = str(ogr_no)
        self.ad = str(ad).strip().title()
        self.soyad = str(soyad).strip().upper()
        self.vize = float(vize)
        self.final = float(final)
        self.ortalama = self.ortalama_hesapla()
        self.harf_notu = self.harf_notu_hesapla()

    def ortalama_hesapla(self):
        """Vizenin %40'ı ve Finalin %60'ını alarak ortalamayı hesaplar."""
        return round((self.vize * 0.40) + (self.final * 0.60), 2)

    def harf_notu_hesapla(self):
        """Hesaplanan ortalamaya göre harf notunu belirler."""
        ort = self.ortalama
        if 90 <= ort <= 100:
            return "A"
        elif 80 <= ort < 90:
            return "B"
        elif 70 <= ort < 80:
            return "C"
        elif 60 <= ort < 70:
            return "D"
        else:
            return "F"

    def durum_bilgisi(self):
        """Harf notuna göre geçti/kaldı durumunu döner."""
        return "Kaldı" if self.harf_notu == "F" else "Geçti"

    def to_dict(self):
        """Sınıf verisini JSON dosyasına kaydetmek üzere sözlüğe dönüştürür."""
        return {
            "ogr_no": self.ogr_no,
            "ad": self.ad,
            "soyad": self.soyad,
            "vize": self.vize,
            "final": self.final,
            "ortalama": self.ortalama,
            "harf_notu": self.harf_notu
        }

    @classmethod
    def from_dict(cls, data):
        """Sözlük verisinden Ogrenci nesnesi oluşturur."""
        ogrenci = cls(
            ogr_no=data["ogr_no"],
            ad=data["ad"],
            soyad=data["soyad"],
            vize=data["vize"],
            final=data["final"]
        )
        return ogrenci

    def __str__(self):
        return f"[{self.ogr_no}] {self.ad} {self.soyad} | Vize: {self.vize} | Final: {self.final} | Ort: {self.ortalama} | Harf: {self.harf_notu} ({self.durum_bilgisi()})"