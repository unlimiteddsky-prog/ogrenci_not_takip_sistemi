# ogrenci.py

class ogrenci:
    """Öğrenci bilgilerini ve not hesaplama mantığını tutan varlık sınıfı."""
    
    def __init__(self, ogrenci_no, ad, soyad, vize=0.0, final=0.0):
        self.ogrenci_no = str(ogrenci_no)
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
        ortalama = self.ortalama
        if 90 <= ortalama <= 100:
            return "A"
        elif 80 <= ortalama < 90:
            return "B"
        elif 70 <= ortalama < 80:
            return "C"
        elif 60 <= ortalama < 70:
            return "D"
        else:
            return "F"

    def durum_bilgisi(self):
        """Harf notuna göre geçti/kaldı durumunu döner."""
        return "Kaldı" if self.harf_notu == "F" else "Geçti"

    def to_dict(self):
        """Sınıf verisini JSON dosyasına kaydetmek üzere sözlüğe dönüştürür."""
        return {
            "ogrenci_no": self.ogrenci_no,
            "ad": self.ad,
            "soyad": self.soyad,
            "vize": self.vize,
            "final": self.final,
            "ortalama": self.ortalama,
            "harf_notu": self.harf_notu
        }

    @classmethod
    def from_dict(cls, data):
        """Sözlük verisinden ogrenci nesnesi oluşturur."""
        ogrenci_nesnesi = cls(
            ogrenci_no=data["ogrenci_no"],
            ad=data["ad"],
            soyad=data["soyad"],
            vize=data["vize"],
            final=data["final"]
        )
        return ogrenci_nesnesi

    def __str__(self):
        return f"[{self.ogrenci_no}] {self.ad} {self.soyad} | Vize: {self.vize} | Final: {self.final} | Ort: {self.ortalama} | Harf: {self.harf_notu} ({self.durum_bilgisi()})"
    
   