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



def main():
    OBJ_kutuphane = Kutuphane(veritabani)
    OBJ_kutuphane.ana_ekran()


if __name__ == "__main__":
    main()
