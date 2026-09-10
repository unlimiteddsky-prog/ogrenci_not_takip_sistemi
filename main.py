# main.py

from ogrenci import ogrenci
from yonetici import Yonetici


def sayi_al(mesaj):
    """Girdi sayıya çevrilemezse hata yakalayan yardımcı fonksiyon."""
    while True:
        try:
            deger = float(input(mesaj))
            if 0 <= deger <= 100:
                return deger
            print("Hata: Not 0 ile 100 arasında olmalıdır!")
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı giriniz!")


def ogrenci_ekle_menusu(yonetici):
    print("\n--- YENİ ÖĞRENCİ EKLE ---")
    ogr_no = input("Öğrenci Numarası: ").strip()
    if not ogr_no:
        print("Hata: Öğrenci numarası boş bırakılamaz!")
        return

    ad = input("Adı: ").strip()
    soyad = input("Soyadı: ").strip()

    if not ad or not soyad:
        print("Hata: Ad ve soyad boş bırakılamaz!")
        return

    vize = sayi_al("Vize Notu (0-100): ")
    final = sayi_al("Final Notu (0-100): ")

    yeni_ogr = ogrenci(ogr_no, ad, soyad, vize, final)
    basari, mesaj = yonetici.ogrenci_ekle(yeni_ogr)
    print(f"\nSonuç: {mesaj}")


def ogrenci_listele(ogrenciler):
    if not ogrenciler:
        print("\nKayıtlı öğrenci bulunamadı.")
        return

    print("\n" + "=" * 70)
    print(f"{'No':<10} {'Ad':<15} {'Soyad':<15} {'Vize':<7} {'Final':<7} {'Ort':<7} {'Harf':<5}")
    print("=" * 70)
    for o in ogrenciler:
        print(f"{o.ogrenci_no:<10} {o.ad:<15} {o.soyad:<15} {o.vize:<7.1f} {o.final:<7.1f} {o.ortalama:<7.2f} {o.harf_notu:<5}")
    print("=" * 70)


def ogrenci_ara_menusu(yonetici):
    print("\n--- ÖĞRENCİ ARA ---")
    kriter = input("Aranacak Öğrenci No veya Soyad: ").strip()
    sonuclar = yonetici.ogrenci_ara(kriter)
    ogrenci_listele(sonuclar)


def harf_notu_filtreleme_menusu(yonetici):
    print("\n--- HARF NOTUNA GÖRE FİLTRELE ---")
    harf = input("Filtrelenecek Harf Notu (A/B/C/D/F): ").strip().upper()
    sonuclar = yonetici.harf_notuna_gore_filtrele(harf)
    ogrenci_listele(sonuclar)


def ogrenci_sil_menusu(yonetici):
    print("\n--- ÖĞRENCİ SİL ---")
    ogr_no = input("Silinecek Öğrenci Numarası: ").strip()
    basari, mesaj = yonetici.ogrenci_sil(ogr_no)
    print(f"\nSonuç: {mesaj}")


def rapor_ekrani(yonetici):
    rapor = yonetici.genel_rapor()
    print("\n--- SİSTEM ÖZET RAPORU ---")
    print(f"Toplam Öğrenci Sayısı : {rapor['toplam']}")
    print(f"Geçen Öğrenci Sayısı  : {rapor['gecen']}")
    print(f"Kalan Öğrenci Sayısı  : {rapor['kalan']}")
    print(f"Sınıf Ortalaması      : {rapor['ort']}")


def ana_menu():
    yonetici = Yonetici()

    while True:
        print("\n" + "=" * 40)
        print("    ÖĞRENCİ NOT TAKİP SİSTEMİ")
        print("=" * 40)
        print("1. Öğrenci Ekle")
        print("2. Tüm Öğrencileri Listele")
        print("3. Öğrenci Ara (No veya Soyada Göre)")
        print("4. Harf Notuna Göre Filtrele")
        print("5. Öğrenci Sil")
        print("6. Özet Raporu Görüntüle")
        print("0. Çıkış")
        print("=" * 40)

        secim = input("Seçiminiz (0-6): ").strip()

        if secim == "1":
            ogrenci_ekle_menusu(yonetici)
        elif secim == "2":
            ogrenci_listele(yonetici.ogrenciler)
        elif secim == "3":
            ogrenci_ara_menusu(yonetici)
        elif secim == "4":
            harf_notu_filtreleme_menusu(yonetici)
        elif secim == "5":
            ogrenci_sil_menusu(yonetici)
        elif secim == "6":
            rapor_ekrani(yonetici)
        elif secim == "0":
            print("\nProgramdan çıkılıyor. İyi günler!")
            break
        else:
            print("\nGeçersiz seçim! Lütfen 0 ile 6 arasında bir değer giriniz.")


if __name__ == "__main__":
    ana_menu()