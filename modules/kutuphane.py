from abc import ABC, abstractmethod

from core.db.db import veritabani
from modules.admin import AdminPaneli
from modules.kullanici import KullaniciIslemleri
from modules.static import menu_baslik


class KutuphaneAbstract(ABC):
    def __init__(self, veritabani_input):
        self.veritabani = veritabani_input
        self.AdminPaneli = AdminPaneli(self.veritabani)

    @abstractmethod
    def ana_ekran(self):
        pass


class Kutuphane(KutuphaneAbstract):
    def __init__(self, veritabani_input):
        super().__init__(veritabani_input)
        self.veritabani = veritabani_input
        self.AdminPaneli = AdminPaneli(self.veritabani)
        self.KullaniciIslemleri = KullaniciIslemleri(self.veritabani)

    def ana_ekran(self):
        menu_baslik("KÜTÜPHANEYE HOŞ GELDİNİZ!")
        print("""
        1. Kayıt Ol
        2. Giriş Yap
        3. Admin Paneli\n""")
        giriş = int(input("Gitmek istediğiniz seçeneği giriniz: "))

        if giriş == 1:
            self.KullaniciIslemleri.kullanici_kayit()
        elif giriş == 2:
            if self.KullaniciIslemleri.menu_kullanici_giris():
                self.KullaniciIslemleri.menu_ana_ekran()
            else:
                print("Yanlış kullanıcı adı veya şifre! Lütfen tekrar deneyiniz!")
                self.KullaniciIslemleri.menu_kullanici_giris()
        elif giriş == 3:
            girilen = input("Lütfen şifre giriniz: ")
            if girilen == veritabani["adminSifre"]:
                print("Admin paneline başarıyla giriş yaptınız.\n")
                if self.AdminPaneli.admin_menu_ana_ekran() == 0:
                    self.ana_ekran()
            else:
                print("Yanlış şifre girdiniz, lütfen tekrar deneyiniz!\n")
                self.ana_ekran()
