import calendar as cal
import datetime as dt
import time as t
import ast


def odunc_alanlarin_kalan_gunu():
    """
    bu fonksiyon kitap ödünç alanların kalan gününü döndürüyor.
    """
    yol = "C:/Users/aykut/PythonFiles/KütüphaneÖdevi/KütüphaneKitapları.txt"
    while True:

        kayıt_edilen_kitap = input("kayıt edeceğiniz kitabın adını giriniz") #enes bu fonksiyonu kayıt etme fonksiyonunun içine alacak

        def kitap_odunc_deger_degistir(dosya, kitap_ismi):
            degeri_degisecek_kitap_ismi = kitap_ismi #burası fonksiyondan gelecek, enes birleştirirse kodu o ekler
            durum = 15


            with open(dosya, 'r') as doysa:
                satirlar = doysa.readlines()
                for satir in satirlar:
                    if degeri_degisecek_kitap_ismi in satir:
                        degisecek_kitap_ismi = satir
                        degisecek_kitap_ismi_dict = ast.literal_eval(degisecek_kitap_ismi) #şu an çalışmıyor kodu entegre ederken yapacağız.
                        degisecek_kitap_ismi_dict['KalanSure'] = durum

            with open(dosya, 'w') as doysa:
                    satirlar = doysa.readlines()

            with open(dosya, 'w') as doysa:
                for i in satirlar:
                    if degisecek_kitap_ismi_dict['isim'] not in i:
                        doysa.write(i)

            def kitapKayıtEt():
                id = degisecek_kitap_ismi_dict['id']
                isim = degisecek_kitap_ismi_dict['isim']
                yayınYılı = degisecek_kitap_ismi_dict['yil']
                yazar = degisecek_kitap_ismi_dict['yazar']
                odunc_suresi = degisecek_kitap_ismi_dict['KalanSure']

                """
                burada Enes'in kodunda nasıl kitap ekleniyorsa ona göre tekrar yazacağız, amacımız KalanSure'yi güncellemek amacıyla
                txt dosyasını güncellemek.
                """

        kitap_odunc_deger_degistir(yol, kayıt_edilen_kitap)


        t.sleep(60*60*24)
        durum = -1
        if durum == 0:
            break

odunc_alanlarin_kalan_gunu()