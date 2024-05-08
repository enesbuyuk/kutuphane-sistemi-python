import time
import ast
from modules.admin import AdminPaneli
from modules.kullanici import KullaniciIslemleri
from core.db.db import veritabani

"""
###############################################################################
# KÜTÜPHANE OTOMASYON SİSTEMİ  
###############################################################################
#
# - Bu program, kütüphane işlemlerini gerçekleştirmek için kullanıcı ve admin paneli sunar.
# - Kullanıcılar, kütüphaneden kitap ödünç alabilir ve teslim edebilir.
# - Adminler, kütüphaneye kitap ekleyebilir, çıkarabilir ve kütüphanedeki kitapları listeleme yetkisine sahiptir.
# - Program, kullanıcı ve kitap bilgilerini dosyalarda saklar.
# 
###############################################################################
"""


def kitap_liste(dosya):
    with open(dosya, "r") as kitaplar:
        for line in kitaplar:
            kitap_dict = dict(ast.literal_eval(line))
            odunc_mesaj = "Bu kitabı ödünç alabilirsiniz."
            if kitap_dict["odunc"] == 0:
                odunc_mesaj = f"""Bu kitap şu an başkası tarafından ödünç alınmıştır.\nTahmini kalan teslim süresi: {kitap_dict["kalanSure"]} gün"""
                print(f"""Kitap benzersiz ID: {kitap_dict["id"]}
Kitap adı: {kitap_dict["isim"]}
Kitap basım yılı: {kitap_dict["yil"]}
Kitap yazarı: {kitap_dict["yazar"]}
{odunc_mesaj}\n""")


def kitap_detay(kitap_id, kitap_liste):
    for index, detay in kitap_liste.items():
        if kitap_id == index:
            odunc_mesaj = "Bu kitabı ödünç alabilirsiniz."
            if detay["odunc"] == 0:
                odunc_mesaj = """Bu kitap şu an başkası tarafından ödünç alınmıştır.\n
            	Tahmini kalan teslim süresi: {detay["kalanSure"]} gün"""
            print(f"""Kitap benzersiz ID: {detay["id"]}
            Kitap adı: {detay["isim"]}
       	    Kitap basım yılı: {detay["yil"]}
       	    Kitap yazarı: {detay["yazar"]}
       		{odunc_mesaj}
        	""")
            break


kütüphaneKayıt = {}

OBJ_admin_paneli = AdminPaneli(veritabani["kutuphane"],veritabani["kullanici"])
OBJ_kullanici = KullaniciIslemleri(veritabani["kullanici"])

def kayit_ol():
    isim = input("İsminizi giriniz: ")
    yas = int(input("Yaşınızı giriniz: "))
    eposta = input("E-postanızı giriniz: ")
    sifre = input("Şifrenizi giriniz: ")
    kullanici = {int(time.time()): {"isim": isim, "yas": yas, "eposta": eposta, "sifre": sifre}}
    with open(veritabani["kullanici"], 'a') as ekle:
        try:
            ekle.write(str(kullanici) + "\n")
            print("Başarıyla kayıt oldunuz! Kullanıcı paneline yönlendiriliyorsunuz...")
            kullanici_paneli(list(map(int, [k for k in kullanici]))[0])
        except:
            print("Kullanıcı oluşturulamadı! Lütfen tekrar deneyiniz.")


def odunc_al(kullanici_id):
    aranacak_kitap = input("Ödünç alacağınız kitabı aratın (tam ismini giriniz): ").lower()
    bulundu = 0
    for x in kitap_listesi.values():
        if bulundu == 1:
            break
        if x["isim"] == aranacak_kitap:
            bulundu = 1
            if x["odunc"] == 0:
                eh = input(f'Alacağınız kitap \"{x["isim"]}\" ise E değilse H tuşuna basınız: ')
                if eh == "E":
                    x["odunc"] = kullanici_id
                    print(f'{x["isim"]} isimli kitabı başarıyla ödünç aldınız.')
                else:
                    print(f'{x["isim"]}  isimli kitabı ödünç alamaktan vazgeçtiniz.')
            else:
                print(f"""Maalesef alacağınız kitap daha önce ödünç alınmıştır.
            	Ödünç alınan kişi tarafından teslim edildikten sonra ödünç alabilirsiniz.""")

    if bulundu == 0:
        print("Aradığınız kitap bulanamamaktadır!")


def teslim_et(kitap_id, kullanici_id):
    print("teslim edildi")


def kullanici_paneli(kullanici_id):
    while True:
        menu_secenek = input("""\n####################### Kullanıcı Paneli! #######################\n
        1) Kitap ödünç al.
        2) Ödünç alınan kitabı teslim et
        3) Profil bilgilerini düzenle
        4) Programı kapat  

		Lütfen gitmek istediğiniz menüyü seçiniz: 
		""")
        if int(menu_secenek) == 1:
            odunc_al(kullanici_id)
        elif int(menu_secenek) == 2:
            teslim_et(kullanici_id)
        elif int(menu_secenek) == 3:
            teslim_et(kullanici_id)
        elif int(menu_secenek) == 4:
            break
        else:
            print("Lütfen geçerli bir menü numarası giriniz.")


def admin_sifre_kontrol():
    while True:
        girilen = input("Lütfen şifre giriniz: ")
        if girilen == veritabani["adminSifre"]:
            print("Admin paneline başarıyla giriş yaptınız.\n")
            if OBJ_admin_paneli.admin_menu_ana_ekran() == 0:
                ana_ekran()
            break
        else:
            print("Yanlış şifre!\n")


def ana_ekran():
    print("""############# Kütüphane Programına Hoş Geldiniz! #############\n
    1. Kayıt Ol
    2. Giriş Yap
    3. Admin Paneli\n""")
    giriş = int(input("Gitmek istediğiniz seçeneği giriniz: "))

    if giriş == 1:
        kayit_ol()
    elif giriş == 2:
        if not OBJ_kullanici.menu_kullanici_giris():
            print("Yanlış kullanıcı adı veya şifre! Lütfen tekrar deneyiniz!")
            kullanici_paneli()
        else:
            OBJ_kullanici.menu_kullanici_giris()
    elif giriş == 3:
        admin_sifre_kontrol()


def main():
    ana_ekran()


if __name__ == "__main__":
    main()
