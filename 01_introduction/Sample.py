"""
gun_sayisi = int(input("Aracınız kaç gündür trafikte? : "))
if gun_sayisi == 1 or gun_sayisi <= 365:
    print("Aracınız 1. servis yılındadır.")
elif gun_sayisi >= 365 and gun_sayisi <= 365*2:
    print("Aracınız 2. servis yılındadır.")
elif gun_sayisi >=365*2 or gun_sayisi <= 365*3:
    print("Aracınız 3. servis yılındadır.")
else:
    print("Lütfen geçerli bir değer giriniz!")
"""
"""print("Manav reyonu, teknoloji reyonu ve kozmetik reyonumuz bulunmaktadir.")
urun = input("Lütfen almak istediğiniz ürün reyonunu seçiniz!: ")
manavreyonu = "domates, biber, patlican"
teknolojireyonu = "bilgisayar, telefon, tv"
kozmetikreyonu = "disfircasi, sampuan, sabun"
if (urun == domates or urun == biber or patlican):
    print("Manav reyonuna gitmelisiniz!")
elif (urun == bilgisayar or urun == telefon or urun == tv):
    print("Teknoloji reyonuna gitmelisiniz!")
elif (urun == disfircasi or urun == sampuan or urun == sabun):
    print("Kozmetik reyonuna gitmelisiniz!")
else:
    print("Girmis oldugunuz urun magazamizda veya reyonumuzda bulunmamaktadir!!")
"""
"""aracturu = input("arac turunu giriniz! : ")
hiz = int(input("mevcut hizinizi giriniz! : "))
if (aracturu == "otomobil" and hiz >= 60):
    print("cezalisin!")
elif (aracturu == "otomobil" and hiz < 60):
    print("cezali degilsin!")
elif (aracturu == "motosiklet" and hiz >= 90):
    print("cezalisin!")
elif (aracturu == "motosiklet" and hiz < 90):
    print("cezali degilsin!")
elif (aracturu == "kamyon" and hiz >= 40):
    print("cezalisin!")
elif (aracturu == "kamyon" and hiz < 40):
    print("cezali degilsin!")
else:
    print("Lutfen gecerli bir arac turu ve hiz degeri giriniz!!")
"""
"""username = input("username bilgisini giriniz!: ")
password = int(input("password giriniz!: "))
if (username == "beast" and password == 123):
    print("Basariyla giris yaptiniz!")
    kilo = int(input("Kilo bilginiz?: "))
    boy = int(input("Boy bilginiz?: "))
    vki = kilo/ boy ** 2
    if (0 <= vki <= 18.5):
        print("{} , {}".format("vki","zayif"))
    elif (18.6 <= vki <= 24.9):
        print("{} , {}".format("vki", "normal"))
    elif (25 < vki <=29.9):
        print("{} , {}".format("vki", "kilolu"))
    elif (30 < vki <= 34.9):
        print("{} , {}".format("vki", "fazla kilolu"))
    elif (35 < vki <= 39.9):
        print("{} , {}".format("vki", "obez"))
    else:
        print("{} , {}".format("vki", "ACIL DURUM DOKTORA GIT!! ya da girdigin degerleri kontrol et!"))
elif (username != "beast" and password == "123"):
    print("username bilginiz hatalidir lutfen tekrar deneyiniz!")
elif (username == "beast" and password != "123"):
    print(" password bilginiz hatalidir lutfen tekrar deneyiniz!")
else:
    print("Giris bilgileriniz hatalidir.")
"""
"""vize = int(input("vize notunuzu giriniz: "))
final = int(input("final notunuz giriniz: "))
odev = int(input("odev notunuzu giriniz: "))
ortalama = vize * 0.3 + final * 0.6 + odev * 0.1
if (0<= ortalama <=50):
    print("Kaldin dersten mal herif FF")
elif (51<=ortalama<=80):
    print("gectin CC")
elif (81<=ortalama<=100):
    print("aferin gectin AA")
else:
    print("gecerli bir deger giriniz!")
"""
"""satinalinankitapsayisi = int(input("satin aldiginiz kitap miktarini giriniz: "))
kitapfiyati = satinalinankitapsayisi * 5
if (satinalinankitapsayisi == 0):
    print("kitap okumani oneririm pis cahil")
elif (0<satinalinankitapsayisi<=20):
    print("{} * {} = {}".format(satinalinankitapsayisi,0.95,kitapfiyati, "TL"))
elif (21<satinalinankitapsayisi<=50):
    print("{} * {} = {}".format(kitapfiyati, 0.90,"TL"))
elif (51<satinalinankitapsayisi<=75):
    print("{} * {} = {}".format(kitapfiyati, 0.85,"TL"))
elif (76<satinalinankitapsayisi<=100):
    print("{} * {} = {}".format(kitapfiyati, 0.75,"TL"))
else:
    print("Girdiginiz degerde kitap satin alamazsiniz!!")
"""
"""sayac=0
while sayac<10:
    int(input("lutfen bir sayi giriniz:"))
    sayac = sayac + 1
"""
"""sayac = 0
toplam = 0
while sayac<=10:
    x = int(input("lutfen bir sayi giriniz: "))
    toplam = toplam + x
    sayac = sayac + 1
    break
    print("toplam")
"""
sayac = 1
ciftsayilar = 0
teksayilar = 0
while sayac <=100:
    if sayac mod2 == 0
    print(ciftsayilar = ciftsayilar + 1)

