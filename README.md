# İSTANBUL ÜNİVERSİTESİ BİLGİSAYAR BİLİMLERİ KÜTÜPHANESİ

Bu Python programı, bir kütüphane sistemi için kullanıcı paneli ve admin paneli sağlar. Kullanıcılar kitap ödünç alabilir, teslim edebilir ve aldıkları kitapların durumunu kontrol edebilirler. Adminler ise kütüphaneye kitap ekleyebilir, çıkarabilir ve mevcut kitapları listeleyebilirler. Program, kullanıcı ve kitap bilgilerini dosyalarda saklar.

## Kurulum

1. Python 3'ün kurulu olduğundan emin olun.
2. Bu depoyu klonlayın: `git clone https://github.com/enesbuyuk/kutuphane-sistemi-python.git`
3. Proje dizinine gidin: `cd kutuphane-sistemi-python`
4. Gerekli paketleri yüklemek için şu komutu çalıştırın: `pip install -r requirements.txt`

## Kullanım

- Kullanıcı Paneli: Kullanıcılar kütüphaneden kitap ödünç alabilir, teslim edebilir ve ödünç aldıkları kitapların durumunu kontrol edebilirler.
- Yönetici Paneli: Yöneticiler kütüphaneye kitap ekleyebilir, çıkarabilir ve mevcut kitapları listeleyebilirler.

## Özellikler

- Kullanıcılar kütüphaneden kitap ödünç alabilir ve iade edebilir.
- Kullanıcılar ödünç aldıkları kitapların durumunu kontrol edebilirler.
- Yöneticiler kütüphaneye kitap ekleyebilir, çıkarabilir ve mevcut kitapları listeleyebilirler.
- Kitap teslim etme süresi 15 gündür. Teslim edilmeyen her gün için 1 TL ceza uygulanır.

## Dosya Yapısı

- `kullanici.txt`: Kullanıcı bilgilerini içeren dosya.
- `kutuphane.txt`: Kitap bilgilerini içeren dosya.
- `db.py`: Veritabanı bilgileri içeren dosya.

## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir pull request açın. Büyük değişiklikler yapmadan önce öneri olarak bir konu açmayı unutmayın.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.
