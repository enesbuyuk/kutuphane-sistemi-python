# -*- coding: utf-8 -*-

import ast
from datetime import datetime
from kutuphane_sistemi_python.core.db.db import veritabani

def kalan_sureyi_guncelle(dosya, guncellenecek_kitap):

    with open(dosya, "r") as f:
        kutuphane_str = f.readlines()

    kutuphane = [ast.literal_eval(kitap) for kitap in kutuphane_str]

    for kitap in kutuphane:
        if kitap['id'] == guncellenecek_kitap:
            kitap['kalanSure'] -= 1
            print("Kalan süre güncellendi:", kitap['kalanSure'])
            break
        else:
            print("Belirtilen id ile eşleşen bir kayıt bulunamadı.")

    with open(veritabani['kutuphane'], "w") as file:
        for kitap in kutuphane:
            file.write(str(kitap) + "\n")

guncellenecek_kitap = input("güncellemek istediğiniz kitabın id'sini giriniz: ")
kalan_sureyi_guncelle(veritabani['kutuphane'], guncellenecek_kitap)

def gun_farki_hesapla(odunc_alma_tarihi):# odunc_alma_tarihi değişkenini sistemde enes her kitap için oluşturacak
    ilk_tarih = datetime(2024, 4, 28)
    mevcut_tarih = datetime.now()#ENES odunc_alma_tarihi DEĞİŞKENİNİ BU METOD İLE OLUŞTURMALISIN

    tarih_farki = mevcut_tarih - ilk_tarih
    print(tarih_farki)

    gun_farki = tarih_farki.days
    print("İki tarih arasındaki gün farkı:", gun_farki)

    return gun_farki


def guncelleme_kosulu(gun_farki):
    ceza_sayisi = 0
    if gun_farki_hesapla(odunc_alma_tarihi) >= 1:# odunc_alma_tarihi değişkenini sistemde enes oluşturacak
        guncellenecek_kitap = input("güncellemek istediğiniz kitabın id'sini giriniz: ")
        kalan_sureyi_guncelle(veritabani['kutuphane'], guncellenecek_kitap)

    if gun_farki > 15:
        ceza_sayisi += gun_farki - 15
        """
        BU KÜTÜPHANEDE CEZALI OLUNAN HERGÜN İÇİN 1 TL CEZA ÖDENMEKTEDİR.
        """

    return ceza_sayisi

def cezayi_kullanıcıya_ata(kullanıcı_id):
    with open(veritabani['kullanici'], "r") as d:
        with open(dosya, "r") as d:
            kutuphane_str = d.readlines()

        gecici_kullanici = [ast.literal_eval(kitap) for kitap in kutuphane_str]

    for kullanici in gecici_kullanici:
        if kullanici['id'] == kullanıcı_id:
            kullanici['ceza_durumu'] = guncelleme_kosulu()#burada her kullanıcı için ceza durumu oluşturulacak
            break
        else:
            print("Belirtilen id ile eşleşen bir kullanıcı bulunamadı.")

    with open(veritabani['kullanici'], "w") as d:
        for kullanici in gecici_kullanici:
            d.write(str(kitap) + "\n")

def cezalilari_göster():
    with open(veritabani['kullanici'], "r") as d:
        cezalilar = d.read()
        print(cezalilar)