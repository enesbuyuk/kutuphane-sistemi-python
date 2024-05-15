from datetime import datetime


class Tarih:
    def __init__(self, veritabani):
        self.veritabani = veritabani

    def teslim_sure_kontrol(self, odunc_alma_tarihi, kalan_gun):
        fark = datetime.now() - datetime.fromtimestamp(odunc_alma_tarihi)
        if kalan_gun >= fark.days :
            return [True, fark.days + self.veritabani["varsayilanKalanGun"]]
        else:
            return [False, -fark.days + self.veritabani["varsayilanKalanGun"]]
