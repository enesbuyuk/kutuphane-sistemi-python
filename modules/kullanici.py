import ast
from modules.dosya import DosyaIslemleri

class KullaniciIslemleri(DosyaIslemleri):
    def __init__(self, dosya):
        super().__init__(dosya)

    def menu_kullanici_giris(self):
        print("############################### Giriş Yap ###############################\n")
        eposta = input("Lütfen e-posta adresinizi giriniz: ")
        sifre = input("Lütfen şifrenizi giriniz: ")
        return self.kullanici_kontrol(eposta, sifre)

    def kullanici_kontrol(self, eposta, sifre):
        with open(self.dosya, "r") as kullanicilar:
            for line in kullanicilar:
                kullanici_dict = dict(ast.literal_eval(line))
                if eposta == kullanici_dict["eposta"] and sifre == kullanici_dict["sifre"]:
                    return kullanici_dict
        return False

    def kullanici_liste(self):
        with open(self.dosya, "r") as kullanicilar:
            for line in kullanicilar:
                kullanici_dict = dict(ast.literal_eval(line))
                print(f"ID:{kullanici_dict['id']}, İsim: {kullanici_dict['isim']}, Yaş: {kullanici_dict['yas']}, E-posta: {kullanici_dict['eposta']}")