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
    OBJ_kutuphane = Kutuphane(veritabani)
    OBJ_kutuphane.ana_ekran()


if __name__ == "__main__":
    main()