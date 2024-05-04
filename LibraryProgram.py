kütüphaneKayıt = {}
kitapKayıt = {}


def adminMod():
    print("admin mod'a hoşgeldiniz")
    adminInput = input("""yapmak istediğiniz sayıya basın:
                       1: kitap listesini göster
                       2: kullanıcı paneline gir
                       """)

    if adminInput == "1":
        kitapListeGöster()

    elif adminInput == "2":
        print("Burayı Enes yazacak")


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
        kitapKaydıSil('KütüphaneKitapları.txt')


def kitapKayıtEt():
    id = input("id giriniz: ")
    isim = input("isim giriniz: ")
    yayınYılı = input("yayın yılı giriniz: ")
    yazar = input("yazar giriniz: ")
    kitapKayıt[isim] = id, yayınYılı, yazar

    def dosyayaYazdır(sözlük, dosya):
        with open(dosya, 'a') as doysa:
            for key, value in sözlük.items():
                doysa.write(f'{key}: {", ".join(value)}\n')

    dosyayaYazdır(kitapKayıt, 'KütüphaneKitapları.txt')


def kitapKaydıSil(dosya):
    fonkGirdi = input("silmek istediğiniz kitabın adını giriniz: ")

    with open(dosya, 'r') as doysa:
        satırlar = doysa.readlines()

    with open(dosya, 'w') as doysa:
        for satır in satırlar:
            if fonkGirdi not in satır:
                doysa.write(satır)

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


def main():
    print("Kütüphane Programına Hoşgeldiniz  ")
    print("""
        1. kayıt ol
        2. giriş yap
        3. admin mod
    
            """)
    giriş = int(input("bana ne yapmak istediğini söyle!"))

    if giriş == 1:
        kayıt()

    elif giriş == 2:
       if kullanıcıGirişi():
           print("hoşgeldiniz.")

       else:
           print("bu isim kayıtlı değil!")

    elif giriş == 3:
        şifre = "admineSor"
        deneme = input("lütfen şifre giriniz: ")
        if deneme == şifre:
            print("teşekkürler")
            adminMod()
        else:
            print("yanlış şifre!")

main()
