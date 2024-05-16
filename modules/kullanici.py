import ast
import time
from modules.dosya import DosyaIslemleri
from modules.kitaplik import Kitaplik
from datetime import datetime
import core.db.db as veritabani
from modules.tarih import Tarih
from modules.static import menu_baslik


class KullaniciIslemleri():
    def __init__(self, dosya):
        self.dosya = dosya
        self.DosyaIslemleri = DosyaIslemleri(dosya)
        self.Tarih = Tarih(self.dosya)
        self.kullanici_id = None
        self.Kitaplik = Kitaplik(self.dosya)

    def menu_ana_ekran(self):
        while True:
            menu_secenek = input("""\n####################### Kullanıcı Paneli #######################\n
1) Kitap listesini görüntüle.
2) Kitap ödünç al.
3) Ödünç alınan kitabı teslim et
4) Aldığım kitapların teslim durumunu görüntüle
5) Profil bilgilerini düzenle
6) Programı kapat  

Lütfen gitmek istediğiniz menüyü seçiniz: """)
            if int(menu_secenek) == 1:
                self.menu_kitap_liste()
            if int(menu_secenek) == 2:
                self.menu_odunc_al()
            elif int(menu_secenek) == 3:
                self.teslim_et()
            elif int(menu_secenek) == 4:
                self.menu_teslim_durumu()
            elif int(menu_secenek) == 5:
                print("burası yapılacaktır lütfen bekleyiniz.")
            elif int(menu_secenek) == 6:
                break
            else:
                print("Lütfen geçerli bir menü numarası giriniz.")

    def menu_kullanici_giris(self): # Kullanıcı giriş işlemi
        menu_baslik("Kullanıcı Giriş Yap")
        eposta = input("Lütfen e-posta adresinizi giriniz: ")
        sifre = input("Lütfen şifrenizi giriniz: ")
        return self.kullanici_kontrol(eposta, sifre)

    def kullanici_kayit(self): # Kullanıcı kayıt işlemi
        menu_baslik("Kullanıcı Kayıt Ol")
        isim = input("İsminizi giriniz: ")
        yas = int(input("Yaşınızı giriniz: "))
        eposta = input("E-postanızı giriniz: ")
        sifre = input("Şifrenizi giriniz: ")
        kullanici = {"id": str(int(time.time())), "isim": isim, "yas": yas, "eposta": eposta, "sifre": sifre}
        with open(self.dosya["kullanici"], 'a') as ekle:
            try:
                ekle.write(str(kullanici) + "\n")
                print("Başarıyla kayıt oldunuz! Kullanıcı paneline yönlendiriliyorsunuz...")
                # kullanici_paneli(list(map(int, [k for k in kullanici]))[0])
                self.menu_ana_ekran()
            except:
                print("Kullanıcı oluşturulamadı! Lütfen tekrar deneyiniz.")

    def kullanici_kontrol(self, eposta, sifre): # Kullanıcı kontrol işlemi
        with open(self.dosya["kullanici"], "r") as kullanicilar:
            for line in kullanicilar:
                kullanici_dict = dict(ast.literal_eval(line))
                if eposta == kullanici_dict["eposta"] and sifre == kullanici_dict["sifre"]:
                    self.kullanici_id = kullanici_dict["id"]

                    return kullanici_dict
        return False

    def kullanici_liste(self): # Kullanıcı listeleme işlemi
        with open(self.dosya["kullanici"], "r") as kullanicilar:
            for line in kullanicilar:
                kullanici_dict = dict(ast.literal_eval(line))
                print(
                    f"ID:{kullanici_dict['id']}, İsim: {kullanici_dict['isim']}, Yaş: {kullanici_dict['yas']}, E-posta: {kullanici_dict['eposta']}")

    def menu_kitap_liste(self): # Kitap listeleme işlemi
        menu_baslik("Kullanıcı Paneli: Kitap Listesi")
        if self.Kitaplik.kitap_liste():
            print("Kitaplar başarıyla listelendi.")
        else:
            print("Kütüphanemizde kitap bulunmamaktadır.")
        self.menu_ana_ekran()

    def menu_odunc_al(self): # Ödünç alma işlemi
        print("############################### Kullanıcı Paneli: Ödünç Al ###############################\n")
        aranacak_kitap = input("Ödünç alacağınız kitabın tam ismini giriniz: ").lower()
        kitap_bulundu = False

        # Kütüphanedeki kitapları oku
        with open(self.dosya["kutuphane"], 'r') as x:
            satirlar = x.readlines()

        # Kütüphanedeki kitapları yaz
        with open(self.dosya["kutuphane"], 'w') as x:
            for satir in satirlar:
                satir_dict = ast.literal_eval(satir)
                if aranacak_kitap == satir_dict["isim"].lower():
                    if satir_dict["odunc"] == 0:
                        satir_dict["odunc"] = self.kullanici_id
                        satir_dict["oduncAlmaTarihi"] = int(time.time())
                        kitap_bulundu = True
                        yeni_satir = str(satir_dict) + "\n"
                        x.write(yeni_satir)
                        print("Kitap başarıyla ödünç alındı.")
                    else:
                        print("Bu kitap daha önce ödünç alınmıştır.")
                else:
                    yeni_icerik = satir
                    x.write(yeni_icerik)

        if not kitap_bulundu:
            print("Aradığınız kitap kütüphanemizde bulunamadı. Lütfen tekrar deneyiniz.")

    def teslim_et(self): # Teslim etme işlemi
        menu_baslik("Kullanıcı Paneli: Teslim Et")
        aranacak_kitap = input("Ödünç alacağınız kitabın tam ismini giriniz: ").lower()
        kitap_bulundu = False

        # Kütüphanedeki kitapları oku
        with open(self.dosya['kutuphane'], 'r') as x:
            satirlar = x.readlines()

        # Kütüphanedeki kitapları yaz
        with open(self.dosya['kutuphane'], 'w') as x:
            for satir in satirlar:
                satir_dict = ast.literal_eval(satir)
                if aranacak_kitap == satir_dict["isim"].lower() and satir_dict["odunc"] == self.kullanici_id:
                    kitap_bulundu = True
                    satir_dict["odunc"] = 0
                    satir_dict["kalanSure"] = 0
                    yeni_satir = str(satir_dict) + "\n"
                    x.write(yeni_satir)
                    print("Kitap başarıyla teslim edildi.")
                else:
                    x.write(satir)
            if not satirlar:
                print("Teslim edilecek kitap bulunamadı.")
        if not kitap_bulundu:
            print("Aradığınız kitap kütüphanemizde bulunamadı. Lütfen tekrar deneyiniz.")

    def menu_teslim_durumu(self):
        menu_baslik("Kullanıcı Paneli: Teslim Durumu")

        # Kütüphanedeki kitapları oku
        with open(self.dosya["kutuphane"], 'r') as x:
            satirlar = x.readlines()

        # Kütüphanedeki kitapları yaz
        with open(self.dosya["kutuphane"], 'w') as x:
            for satir in satirlar:
                satir_dict = ast.literal_eval(satir)
                if satir_dict["odunc"] == self.kullanici_id:
                    cevap = self.Tarih.teslim_sure_kontrol(satir_dict["oduncAlmaTarihi"], self.dosya["varsayilanKalanGun"])
                    if not cevap[0]:
                        print(f"(*){satir_dict['isim']} adlı kitabın teslim süresi ({cevap[1]} gün) dolmuştur. Lütfen teslim ediniz.")
                        print(f"\tCeza bedeli: {-cevap[1]} TL\n")
                    else:
                        print("Bugün itibarıyla teslim etmeniz gereken kitap bulunmamaktadır.")
                x.write(satir)
            if not len(satirlar):
                print("Teslim edilecek kitap bulunamadı.")