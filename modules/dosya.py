from core.db.db import veritabani


class DosyaIslemleri:
    def __init__(self, dosya):
        self.dosya = dosya

    def dosya_oku(self):
        with open(self.dosya, "r") as doysa:
            return doysa.readlines()

    def dosya_yaz(self, yazilacak, veri):
        with open(yazilacak, 'a') as x:
            x.write(f"""{str(veri)}\n""")
        return True
