import tkinter


pencere  =  tkinter.Tk()



pencere . geometri ( '500x400' )

lbl  =  Etiket ( pencere , text = "Parite" )
lbl . ızgara ( sütun = 0 , satır = 0 )

tarih_bas  =  StringVar ()
tarih_bit  =  StringVar ()

lbl22  =  Etiket ( pencere , text = "Başlangıç ​​Tarihi" )
lbl22 . ızgara ( sütun = 0 , satır = 1 )

cal = DateEntry ( pencere , seçim modu = 'gün' ,
              metin değişkeni = tarih_bas ,
              tarih_pattern = 'gg-aa-yyyy' )
kal . ızgara ( satır = 1 , sütun = 1 , padx = 15 )

lbl33  =  Etiket ( pencere , text = "Bitiş Tarihi" )
lbl33 . ızgara ( sütun = 0 , satır = 2 )

cal2 = DateEntry ( pencere , seçim modu = 'gün' ,
               metin değişkeni = tarih_bit ,
               tarih_pattern = 'gg-aa-yyyy' )
cal2 . ızgara ( satır = 2 , sütun = 1 , padx = 15 )

 kesin tiklandi ( ):
    parite  =  değişken _ al ()
    tarih_baslangic  =  tarih_bas . al ()
    tarih_bit  =  tarih_bit . al ()
    kazıyıcı  =  CmcScraper ( parite ,
                         tarih_baslangic ,
                         tarih_bitis )
    başlıklar , veri  =  kazıyıcı . get_data ()
    tarih_verisi  = []
    kapanis_degeri  = []
    hareketli_ortalama  = []
     i için numaralandırmada ( veri  ) veri :  _
        tarih_verisi . ekle ( veri [ 0 ])
        kapanis_degeri . ekle ( veri [ 4 ])
        eğer  ben  >  4 :
            ortalama  =  kapanis_degeri [ i ] +  kapanis_degeri [ i - 1 ]
            ortalama  +=  kapanmais_degeri [ i - 2 ] +  kapanmais_degeri [ i - 3 ]
            ortalama  +=  kapanis_degeri [ i - 4 ]
            hareketli_ortalama . ekle ( ortalama  /  5 )
    hareketli_ortalama . ekle ( 0 )
    hareketli_ortalama . ekle ( 0 )
    hareketli_ortalama . ekle ( 0 )
    hareketli_ortalama . ekle ( 0 )
    tarih_verisi . ters ()
    kapanis_degeri . ters ()
    hareketli_ortalama . ters ()
    pl . arsa ( tarih_verisi , kapanis_degeri )
    pl . arsa ( hareketli_ortalama )
    pl . göster ()
    geçmek

btn2  =  Düğme ( pencere , text = "Grafik Çiz" ,
              bg = "turuncu" , fg = "kırmızı" ,
              komut = tiklandi
              )

btn2 . ızgara ( sütun = 1 , satır = 3 )

değişken  =  StringVar ( pencere )
değişken _ set ( "BTC" ) # varsayılan değer


secenekler  = [ "BTC" , "ETH" , "ADA" ]
secenek_kutusu  =  OptionMenu ( pencere ,
                            değişken ,
                            * seçenekler )

secenek_kutusu . ızgara ( sütun = 1 , satır = 0 )



pencere . ana döngü ()