"""
1- veri isimli bir klasör oluşturun
2- zip dosyasını veri klasörüne çıkartın
csv dosyalarını okuma
csv dosyalarını gezme
3- zip dosyası içindeki csv dosyalarının tüm içeriğini tek bir csv dosyasında birleştirin
   (volume olmasın)
4- bu kayıtların tamamını sqlite veritabanına bir tablo oluşturarak yükleyin
5- kullanıcının belirlediği paritenin, aralığın , değerin grafiğini çizdirin
   veriler sqlite dan çekilecek
"""

import os.path
import zipfile

import pandas as pd
import sqlite3

if not os.path.exists("veri"):
    os.mkdir('veri')
    arsiv= zipfile.ZipFile('pariteler_cikti_1hour_2022_2022.zip')
    arsiv.extractall("veri/")


tum_dosyalar= os.listdir("veri")
pandas_csv_listesi=[]

for csv_dosya in tum_dosyalar:
    veri= pd.read_csv("veri/" + csv_dosya)
    del veri["volume"]
    pandas_csv_listesi.append(veri)


bag=sqlite3.connect()



