"""
1. soru: kendisine gönderilen sayılardan sadece palindrom olanları toplayan
diğerlerini de bu toplamdan çıkaran ve geri döndüren python fonksiyonunu yazınız

palindrom: baştan da sondan da aynı olan sayılar
"""

def palindrom_fonksiyonu(*paremetre):
    toplam = 0
    for sayi in paremetre:
        if str(sayi)== str(sayi)[::-1]:
            toplam += sayi
        else:
            toplam -= sayi
    return toplam




 palindrom_fonksiyonu(111,20,656,41)
