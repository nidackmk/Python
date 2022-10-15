a=4
d=7
c=20
b=0

if a>c:
    print("a c den büyüktür")

if d<0: print("d 0 dan küçüktür")

if d>0: print("d büyük 0"); print("d 0 dan büyük"); d=5


#python'da else if yerine elif yazılır
if a>5:
    print("a 5 ten büyük")
elif a==5:
    print("a=5")
else:
    print("a 5 ten küçük")



#short if örneği
print("a ile b farklı") if a!=b else print("a ile b aynı") 


#and ve or örnekleri
if a<10 or c<10:
    print("a ya da c 10 da küçük")

if a==5 and c==5:
    print("a ve c 5 e eşit")


# is ifadesi
# ÖDEV: is gerçekte nerde kullanılır???
if a is 4:
    print("a 4 e eşit")

if a is not 4:
    print("a 4 e eşit değil")


# iç içe koşullu ifade
if a<5:
    if c>10:
        print("merhaba dünya")

#pass ifadesi
#hiçbir şey yapma burayı geç demek
if a<10:
    pass


#while
while a<15:
    print(a)
    a+=1
    if a==10:
        continue
    if a ==12:
        break

else:
    print("a artık 15 ya da daha büyük")    


#for döngüsü
#3. paremetre kaçar kaçar ilerleyeceğini belirtir
for i in range(0,10,2):
    print(i)

for i in range(20,10,-2):
    print(i)


#listeler
liste=["a",True,1.3,4,["aaaa","bbbbb","cccc"]]

for i in liste:
    print(i)

for i in liste[4]:
    print(i)

for i in range(0,3):
    print(i)
else:
    print("for bitti")


#iki paremetreli for döngüsü
#sep metodu virgülle ayrılan yerlerde boşluk olmaması içindir
for i, eleman in enumerate(liste):
    print(i+1,". eleman: ",eleman,sep="")



#fonksiyonlar
#fonksiyonlar def ile başlar
def yazdir():
    print("yazıyorum")

yazdir()    


def topla(a,b):
    return a+b

print(topla(3,5))


#iki değer döndüren fonksiyon
#tupple olarak döndürür sonucu
def topla_carp(a,b):
    return a+b,a*b

#atama işlemi de yapılabilir
toplam, carpım=topla_carp(3,5)
print(topla_carp(3,4))


#TUPPLE NE DEMEK?????

#birden çok paremetre
def topla_nevarsa(*a):
    toplam = 0
    for deger in a:
        toplam += deger
    return toplam

print(topla_nevarsa(2,3,6,5,4,7))



#başka paremetrelere değer gönderme
def topla(*toplanacak,fazladan=0):
    toplam = 0
    for deger in toplanacak:
        toplam += deger +fazladan
    return toplam

print(topla(3,6,5,4,fazladan=5))



#dictionary
def birim_islem(**birim):
    print("tipi:",type(birim))
    print("ad : ", birim["ad"])
    print("soyad : ", birim["soyad"])
    print("yıl : ", birim["yıl"])

birim_islem(ad="nida", yıl=2019, soyad="çakmak")    




#lambda : doğrudan bir foksiyon bir değişkene atanmış oluyor
lambda_fonksiyonu=lambda a: a+10

print(lambda_fonksiyonu(5))



#çok paremetreli lambda
topla_cok_paremetre=lambda a,b: a+b

print(topla_cok_paremetre(4,6))


#NOT: fonksiyonlarda da pass ifadesi kullanılır


#lambda ile iç içe fonksiyon
#SINAV SORUSUUUUU
def benim_fonksiyonum(n):
    return lambda a:a*n

katini_al=benim_fonksiyonum(2)
print(katini_al(5))

katini_al=benim_fonksiyonum(5)
print(katini_al(5))



