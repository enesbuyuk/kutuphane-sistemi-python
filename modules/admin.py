import ast
import time
from core.db.db import veritabani
from modules.dosya import DosyaIslemleri
from modules.kullanici import KullaniciIslemleri


class AdminPaneli(KullaniciIslemleri):
    def __init__(self, dosya):
        self.dosya = dosya
        KullaniciIslemleri.__init__(self, dosya)

    def admin_menu_kitap_liste(self):
        print("############################### Admin Paneli: Kitap Listesi ###############################\n")
        with open(self.dosya["kutuphane"], "r") as kitaplar:
            for line in kitaplar:
                kitap_dict = dict(ast.literal_eval(line))
                odunc_mesaj = "Bu kitabı ödünç alabilirsiniz."
                if kitap_dict["odunc"]:
                    odunc_mesaj = "Bu kitap şu an başkası tarafından ödünç alınmıştır.\nTahmini kalan teslim süresi: " + \
                                  kitap_dict["kalanSure"] + " gün"
                print(f"""Kitap benzersiz ID: {kitap_dict["id"]}
Kitap adı: {kitap_dict["isim"]}
Kitap basım yılı: {kitap_dict["yil"]}
Kitap yazarı: {kitap_dict["yazar"]}
{odunc_mesaj}\n""")

    def admin_menu_kitap_ekle(self):
        print("############################### Admin Paneli: Kitap Ekle ###############################\n")
        adi = input("Lütfen kitabın adini giriniz: ")
        yil = input("Lütfen kitabın yayım yılını giriniz: ")
        yazar = input("Lütfen kitabın yazarını giriniz: ")
        kitap = {
            "id": str(int(time.time())),
            "isim": adi,
            "yil": int(yil),
            "yazar": yazar,
            "odunc": 0,
            "kalanSure": 0
        }
        if self.dosya_yaz(kitap):
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
    def admin_menu_ana_ekran(self):
        print("""############# Admin Paneline Hoş Geldiniz! #############
        1) Kütüphanedeki kitapları listele.
        2) Kütüphaneye kitap ekle.
        3) Kütüphaneden kitap çıkar.
        4) Kullanıcıları listele.
        0) Admin panelinden çıkış yap (Ana menüye döner).\n""")
        secim = input("LÜtfen yapmak istediğiniz menüyü seçiniz: ")
        print("\n")
        if secim == "1":
            if self.admin_menu_kitap_liste():
                print("Kitaplar başarıyla listelendi.")
                self.admin_menu_ana_ekran()
            else:
                print("Kitap listesi çekilirken bir hata oluştu.")
                self.admin_menu_kitap_liste()
        elif secim == "2":
            if self.admin_menu_kitap_ekle():
                print("Kitap başarıyla eklendi.")
                self.admin_menu_ana_ekran()
            else:
                print("Kitap eklenirken bir hata oluştu.")
                self.admin_menu_kitap_ekle()
        elif secim == "3":
            if self.admin_menu_kitap_cikar():
                print("Kitap başarıyla çıkarıldı.")
                self.admin_menu_ana_ekran()
            else:
                print("Kitap çıkartılırken bir hata oluştu.")
                self.admin_menu_kitap_cikar()
        elif secim == "4":
            self.kullanici_liste()
        elif secim == "0":
            return 0
        else:
            print(veritabani["hataliSecim"])
