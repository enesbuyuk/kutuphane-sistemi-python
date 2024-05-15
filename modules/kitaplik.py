import ast
from modules.tarih import Tarih
from datetime import datetime
class Kitaplik:
    def __init__(self, veritabani):
        self.veritabani = veritabani
        self.Tarih = Tarih(self.veritabani)

    def kitap_liste(self):
        with open(self.veritabani["kutuphane"], "r") as x:
            kitaplar = x.readlines()
            for line in kitaplar:
                kitap_dict = dict(ast.literal_eval(line))
                odunc_mesaj = "Bu kitabı ödünç alabilirsiniz."
                if kitap_dict["odunc"]:
                    odunc_mesaj = "Bu kitap şu an başkası tarafından ödünç alınmıştır.\nTahmini kalan teslim süresi: " + \
                                  str(self.Tarih.teslim_sure_kontrol(kitap_dict["oduncAlmaTarihi"], self.veritabani["varsayilanKalanGun"])[1]) + " gün"
                print(f"""Kitap benzersiz ID: {kitap_dict["id"]}
        Kitap adı: {kitap_dict["isim"]}
        Kitap basım yılı: {kitap_dict["yil"]}
        Kitap yazarı: {kitap_dict["yazar"]}
        {odunc_mesaj}\n""")
            if not len(kitaplar):
                return False
            else:
                return True
