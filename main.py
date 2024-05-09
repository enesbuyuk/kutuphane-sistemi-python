import time
import ast
from modules.admin import AdminPaneli
from modules.dosya import DosyaIslemleri
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
            if kitap_dict["odunc"]:
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

OBJ_admin_paneli = AdminPaneli(veritabani)
OBJ_kullanici = KullaniciIslemleri(veritabani)


def teslim_et(kitap_id, kullanici_id):
    print("teslim edildi")





def ana_ekran():
    print("""############# Kütüphane Programına Hoş Geldiniz! #############\n
    1. Kayıt Ol
    2. Giriş Yap
    3. Admin Paneli\n""")
    giriş = int(input("Gitmek istediğiniz seçeneği giriniz: "))

    if giriş == 1:
        OBJ_kullanici.kullanici_kayit()
    elif giriş == 2:
        if not OBJ_kullanici.menu_kullanici_giris():
            print("Yanlış kullanıcı adı veya şifre! Lütfen tekrar deneyiniz!")
            OBJ_kullanici.menu_ana_ekran()
        else:
            OBJ_kullanici.menu_kullanici_giris()
    elif giriş == 3:
        girilen = input("Lütfen şifre giriniz: ")
        if girilen == veritabani["adminSifre"]:
            print("Admin paneline başarıyla giriş yaptınız.\n")
            if OBJ_admin_paneli.admin_menu_ana_ekran() == 0:
                ana_ekran()
        else:
            print("Yanlış şifre girdiniz, lütfen tekrar deneyiniz!\n")
            ana_ekran()


def main():
    ana_ekran()


if __name__ == "__main__":
    main()
