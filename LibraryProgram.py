kütüphaneKayıt = {}
kitapKayıt = {}


def main():
    print("Kütüphane Programına Hoşgeldiniz  ")
    giriş = input("bana ne yapmak istediğini söyle!")
    print("""
        1. kayıt ol
        2. giriş yap
        3. admin mod
    
            """)
    if giriş == 1:
        kayıt()

    elif giriş == 2:
       if kullanıcıGirişi():
           print("hoşgeldiniz.")

       else:
           print("bu isim kayıtlı değil!")



    elif "adminMod" in giriş:
        şifre = "adsg4v3t34ty35"
        deneme = input("lütfen şifre giriniz: ")
        if deneme == şifre:
            print("teşekkürler")
            adminMode()
        else:
            print("yanlış şifre!")



def adminMod():
    print("admin mod'a hoşgeldiniz")
    adminInput = input("""yapmak istediğiniz sayıya basın:
                       1: kitap listesini göster
                       2: kullanıcı paneline gir
                       """)


def kitapListeGöster():
    print(kitapKayıt)

    print("""ne yapmak istiyorsunuz?:
            1. kütüphaneye kitap kayıt ettir
            2. kütüphaneden kitap kaydını sil
            """)
    fonkGirdi = int(input("sayı giriniz: "))
    if fonkGirdi == 1:
        kitapKayıtEt()
    elif fonkGirdi == 2:
        kitapKaydıSil()


def kitapKayıtEt():
    id = int(input("id giriniz: "))
    isim = input("isim giriniz: ")
    yayınYılı = int(input("yayın yılı giriniz: "))
    yazar = input("yazar giriniz: ")
    kitapKayıt[isim] = id, yayınYılı, yazar



def kitapKaydıSil():
    fonkGirdi = input("silmek istediğiniz kitabın adını giriniz: ")
    del kitapKayıt[fonkGirdi]










def kullanıcıGirişi():
    isimInput = input("isminizi giriniz: ")
    if isimInput in kütüphaneKayıt:
        return True
    else:
        return False

def kayitlarıGöster():
    global kütüphaneKayıt
    print("Kütüphaneye kayıtlı kişiler:")
    for isim, bilgiler in kütüphaneKayıt.items():
         print(f"İsim: {isim}, Yaş: {bilgiler['yas']}, E-posta: {bilgiler['eposta']}")


def kayıtGir():
    isim = input("isminizi giriniz: ")
    yaş =   int(input("yaşınızı giriniz: "))
    eposta = input("eposta giriniz: ")
    kayıt(isim, yas, eposta)

