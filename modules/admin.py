import time
import ast
from core.db.db import veritabani
from modules.dosya import DosyaIslemleri
from modules.kullanici import KullaniciIslemleri
from modules.kitaplik import Kitaplik
from modules.static import menu_baslik
from datetime import datetime


class AdminPaneli(KullaniciIslemleri):
    def __init__(self, dosya):
        self.dosya = dosya
        KullaniciIslemleri.__init__(self, dosya)
        self.DosyaIslemleri = DosyaIslemleri(self.dosya)
        self.Kitaplik = Kitaplik(self.dosya)

    def admin_menu_kitap_liste(self):
        menu_baslik("Admin Paneli: Kitap Listesi")
        if self.Kitaplik.kitap_liste():
            print("Kitaplar başarıyla listelendi.")
        else:
            print("Kütüphanemizde kitap bulunmamaktadır.")
        self.admin_menu_ana_ekran()

    def admin_menu_kitap_ekle(self):
        menu_baslik("Admin Paneli: Kitap Ekle")
        adi = input("Lütfen kitabın adini giriniz: ")
        yil = input("Lütfen kitabın yayım yılını giriniz: ")
        yazar = input("Lütfen kitabın yazarını giriniz: ")
        kullanilacak_unix_time = int(time.time())
        kitap = {
            "id": str(int(time.time())),
            "isim": adi,
            "yil": int(yil),
            "yazar": yazar,
            "odunc": 0,
            "oduncAlmaTarihi": kullanilacak_unix_time
        }
        if self.DosyaIslemleri.dosya_yaz(self.dosya["kutuphane"], kitap):
            return True
        else:
            return False

    def admin_menu_kitap_cikar(self):
        print("############################### Admin Paneli: Kitap Çıkar ###############################\n")
        cikarilacak = input(
            "Kütüphaneden kaldırmak istediğiniz kitabın tam adını giriniz (büyük/küçük harf önemsiz): ").lower()
        bulundu = False
        yeni_icerik = []
        with open(self.dosya["kutuphane"], 'r') as file:
            lines = file.readlines()
        with open(self.dosya["kutuphane"], 'w') as file:
            for satir in lines:
                satir_dict = ast.literal_eval(satir)
                if cikarilacak != satir_dict["isim"].lower():
                    yeni_icerik.append(satir)
                else:
                    bulundu = True

            if bulundu:
                file.writelines(yeni_icerik)
                return True
            else:
                return False

    def admin_menu_kullanici_liste(self):
        print("############################### Admin Paneli: Kullanıcı Listesi ###############################")
        self.kullanici_liste()

    def admin_menu_ana_ekran(self):
        while True:
            print("""\n\n\n############################### Admin Paneli: Ana Ekran ###############################
            1) Kütüphanedeki kitapları listele.
            2) Kütüphaneye kitap ekle.
            3) Kütüphaneden kitap çıkar.
            4) Kullanıcıları listele.
            0) Admin panelinden çıkış yap (Ana menüye döner).\n""")
            secim = input("LÜtfen yapmak istediğiniz menüyü seçiniz: ")
            print("\n")
            if secim == "1":
                self.admin_menu_kitap_liste()
            elif secim == "2":
                if self.admin_menu_kitap_ekle():
                    print("Kitap başarıyla eklendi.")
                    self.admin_menu_ana_ekran()
                else:
                    print("Kitap eklenirken bir hata oluştu.")
                    self.admin_menu_ana_ekran()
            elif secim == "3":
                if self.admin_menu_kitap_cikar():
                    print("Kitap başarıyla çıkarıldı.")
                    self.admin_menu_ana_ekran()
                else:
                    print("Kitap çıkartılırken bir hata oluştu.")
                    self.admin_menu_kitap_cikar()
            elif secim == "4":
                self.admin_menu_kullanici_liste()
            elif secim == "0":
                print("degistir")
            else:
                print(veritabani["hataliSecim"])
