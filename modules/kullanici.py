import ast
import time
from modules.dosya import DosyaIslemleri
import core.db.db as veritabani


class KullaniciIslemleri(DosyaIslemleri):
    def __init__(self, dosya):
        super().__init__(dosya["kutuphane"])
        self.dosya = dosya
        self.kullanici_id = None

    def menu_ana_ekran(self):
        while True:
            menu_secenek = input("""\n####################### Kullanıcı Paneli! #######################\n
                1) Kitap ödünç al.
                2) Ödünç alınan kitabı teslim et
                3) Profil bilgilerini düzenle
                4) Programı kapat  

        		Lütfen gitmek istediğiniz menüyü seçiniz: 
        		""")
            if int(menu_secenek) == 1:
                self.menu_odunc_al()
            elif int(menu_secenek) == 2:
                teslim_et(kullanici_id)
            elif int(menu_secenek) == 3:
                teslim_et(kullanici_id)
            elif int(menu_secenek) == 4:
                break
            else:
                print("Lütfen geçerli bir menü numarası giriniz.")
    def menu_kullanici_giris(self):
        print("############################### Kullanıcı Giriş Yap ###############################\n")
        eposta = input("Lütfen e-posta adresinizi giriniz: ")
        sifre = input("Lütfen şifrenizi giriniz: ")
        return self.kullanici_kontrol(eposta, sifre)

    def kullanici_kayit(self):
        print("############################### Kullanıcı Kayıt Ol ###############################\n")
        isim = input("İsminizi giriniz: ")
        yas = int(input("Yaşınızı giriniz: "))
        eposta = input("E-postanızı giriniz: ")
        sifre = input("Şifrenizi giriniz: ")
        kullanici = {"id": str(int(time.time())), "isim": isim, "yas": yas, "eposta": eposta, "sifre": sifre}
        with open(self.dosya["kullanici"], 'a') as ekle:
            try:
                ekle.write(str(kullanici) + "\n")
                print("Başarıyla kayıt oldunuz! Kullanıcı paneline yönlendiriliyorsunuz...")
                kullanici_paneli(list(map(int, [k for k in kullanici]))[0])
            except:
                print("Kullanıcı oluşturulamadı! Lütfen tekrar deneyiniz.")

    def kullanici_kontrol(self, eposta, sifre):
        with open(self.dosya["kullanici"], "r") as kullanicilar:
            for line in kullanicilar:
                kullanici_dict = dict(ast.literal_eval(line))
                if eposta == kullanici_dict["eposta"] and sifre == kullanici_dict["sifre"]:
                    self.kullanici_id = kullanici_dict["id"]
                    return kullanici_dict
        return False

    def kullanici_liste(self):
        with open(self.dosya["kullanici"], "r") as kullanicilar:
            for line in kullanicilar:
                kullanici_dict = dict(ast.literal_eval(line))
                print(
                    f"ID:{kullanici_dict['id']}, İsim: {kullanici_dict['isim']}, Yaş: {kullanici_dict['yas']}, E-posta: {kullanici_dict['eposta']}")

    def menu_odunc_al(self):
        print("############################### Kullanıcı Paneli: Ödünç Al ###############################\n")
        aranacak_kitap = input("Ödünç alacağınız kitabın tam ismini giriniz: ").lower()
        kitap_bulundu = False

        with open(self.dosya["kutuphane"], 'r') as file:
            lines = file.readlines()

        with open(self.dosya["kutuphane"], 'w') as file:
            for satir in lines:
                satir_dict = ast.literal_eval(satir)
                if aranacak_kitap == satir_dict["isim"].lower():
                    if satir_dict["odunc"] == 0:
                        satir_dict["odunc"] = self.kullanici_id
                        satir_dict["kalanSure"] = 15
                        kitap_bulundu = True
                        yeni_satir = str(satir_dict) + "\n"
                        file.write(yeni_satir)
                        print("Kitap başarıyla ödünç alındı.")
                    else:
                        print("Bu kitap daha önce ödünç alınmıştır.")
                else:
                    yeni_icerik = satir
                    file.write(yeni_icerik)

        if not kitap_bulundu:
            print("Aradığınız kitap kütüphanemizde bulunamadı. Lütfen tekrar deneyiniz.")
