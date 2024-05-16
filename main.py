import ast
from core.db.db import veritabani
from modules.kutuphane import Kutuphane

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


def main():
    OBJ_kutuphane = Kutuphane(veritabani) # Kutuphane class'ından bir obje oluşturuldu.
    OBJ_kutuphane.ana_ekran() # Oluşturulan obje üzerinden ana ekran fonksiyonu çağrıldı.


if __name__ == "__main__":
    main() # main fonksiyonu çağrıldı.