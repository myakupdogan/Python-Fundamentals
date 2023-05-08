#Karar mekanizmasi (if-elif-else)
#region example 1
#sayi1 = int(input("sayi girin:"))
#sayi2 = int(input("sayi girin:"))
#if sayi1 > sayi2:
#    print(f'{sayi1} buyuktur.')
#else:
#    print(f'{sayi2} buyuktur.')
#endregion
#region example 2
#Kullanicidan alinan sayi cift mi tek mi?
#x = int(input("Sayi giriniz: "))
#if x % 2== 0:
#    print(f'{x} cift sayidir.')
#else:
#    print(f'{x} tek sayidir.')
#endregion
#region example 3
#kullanicidan alinan sayi pozitif mi negatif mi notr mu?
#number = int(input("please type into a number:"))
#if number > 0:
#    print(f'{number} the number is positive')
#elif number < 0:
#    print(f'{number} the number is negative')
#elif number == 0:
#    print(f'{number} the number is notr')
#else:
#    print(f'{number} take it easy my friend')
#end region
#region example 4
# kullanicidan mevsim bilgisi alalim alinan mevsim bilgisine gore aylari ekrana yazdiralim
#mevsim = input("Lutfen bir mevsim giriniz: ").lower() #burada kullanilan lower() python icerisinde built in olan
# bu fonksiyon ile kullanicidan alinan inputu kucuk harfe donusturduk
#mesaj = " "
#if mevsim == "kis":
#    mesaj = "Aralik - Ocak - Subat"
#elif mevsim == "ilkbahar":
#    mesaj = "Mart - Nisan - Mayis"
#elif mevsim == "yaz":
#    mesaj = "Haziran - Temmuz - Agustos"
#elif mevsim == "sonbahar":
#    mesaj = "Eylul - Ekim - Kasim"
#else:
#    mesaj = "Boyle bir mevsim yok!"
#print(mesaj)
#endregion
#region example 5
# #Kullanıcıdan aracının trafikte olduğu gün sayısını alıyoruz. Şayet
# #Şayet 365 günün altında ise 1. servis yılında 365 ve 365*2 aralığında ise 2. servis aralığında 365*2 ve 365*3
# # ise 3. servis aralığında değilse aracını artık değiştir fosil olmuş.
# Gun_sayisi=int(input("Aracınız kaç gündür trafikte: "))
#
# if Gun_sayisi <= 365:
#     print("Aracınız 1. servis yılındadır.")
# elif Gun_sayisi > 365 and Gun_sayisi <= 365*2:
#     print("Aracınız 2. servis yılındadır.")
# elif Gun_sayisi > 365*2 and Gun_sayisi >= 365*3:
#     print("Aracınız 3. servis yılındadır.")
# else:
#     print("Lütfen geçerli bir değer giriniz!")
#endregion
#region example 6
#kullanicidan alinan arac turu ve hiz bilgisine gore aracin cezali olup olmadigini belirten uygulamayi yazin
# aracturu = input("arac turunu giriniz! : ")
# hiz = int(input("mevcut hizinizi giriniz! : "))
# if (aracturu == "otomobil" and hiz >= 60):
#     print("cezalisin!")
# elif (aracturu == "otomobil" and hiz < 60):
#     print("cezali degilsin!")
# elif (aracturu == "motosiklet" and hiz >= 90):
#     print("cezalisin!")
# elif (aracturu == "motosiklet" and hiz < 90):
#     print("cezali degilsin!")
# elif (aracturu == "kamyon" and hiz >= 40):
#     print("cezalisin!")
# elif (aracturu == "kamyon" and hiz < 40):
#     print("cezali degilsin!")
# else:
#     print("Lutfen gecerli bir arac turu ve hiz degeri giriniz!!")
#endregion
#region example 7
#lineer bir dogrunun reel koklerini hesaplayalim.
# import math yazip math.sqrt() seklinde de yazabiliriz.
# from math import sqrt
# a = int(input("Birinci katsayi: "))
# b= int(input("Birinci katsayi: "))
# c= int(input("Birinci katsayi: "))
# diskriminant = b ** 2 - 4 * a * c
# #uyari: pythonda aritmetiksel islemler icn moduller var. Bu modulun adi "math". Karekok icin sqrt()fonksiyonundan faydalanacagiz.
# if diskriminant > 0:
#     x1 = -b - sqrt(diskriminant) / 2 * a
#     x2 = -b - sqrt(diskriminant) / 2 * a
#     print(f'2 reel kok bulunmaktadir.\n birinci reel kok ==> {x1}\n ikinci reel kok ==> {x2}')
# elif diskriminant == 0:
#     x1 = -b - sqrt(diskriminant) / 2 * a
# elif diskriminant < 0:  #else durumu icin sart kosmayip bu satirada else diyebilirdik!
#     print("reel kok bulunmamaktadir.")
#endregion
#region example 8
#kullanicidan alinan 3 tane sayiyi buyukluk olarak karsilastiralim
# a = int(input("Sayi giriniz: "))
# b = int(input("Sayi giriniz: "))
# c = int(input("Sayi giriniz: "))
# if a > b and a > c:
#     print(f"{a} diger sayilardan buyuktur..")
# elif b > a and b > c:
#     print("{} diger sayilardan buyuktur.".format(b))
# elif c > a and c > b:
#     print("{} diger sayilardan buyuktur.".format(c))
# else:
#     print("Sayilardan bazilari birbirinden buyuk olabilir.")
#endregion
#region example 9
# vize = int(input("vize notunuzu giriniz: "))
# final = int(input("final notunuz giriniz: "))
# odev = int(input("odev notunuzu giriniz: "))
# ortalama = vize * 0.3 + final * 0.6 + odev * 0.1
# if (0<= ortalama <=50):
#     print("Kaldin dersten mal herif FF")
# elif (51<=ortalama<=80):
#     print("gectin CC")
# elif (81<=ortalama<=100):
#     print("aferin gectin AA")
# else:
#     print("gecerli bir deger giriniz!")
#endregion
#region example 10
# name = input("Tam Adiniz: ") #muhammed yakup dogan
# pwd = input("Sifre: ")
# #kullanicinin ismi birden fazla kelime icerebilir. bu yuzden bize gelen string ifade icerisinde bulunan bosluk karakterinden
# #ifademizi asagida split ediyoruz yani parcaliyoruz. split() fonksiyonu bizden asagidaki kullaniminda bir parametre istedi
# #bizde burada bosluk karakterini kullandik. split() isini bitirdikten sonra bize bir liste dondu. bu elde ettigimiz listeyi de'name_list'
# #isimli degiskene atadik.
# name_list = name.split(" ")
# #artik name_list lsitesinin index degerlerinde bulunan ifadelere istedigim gibi erisebilirim. asagida sifirinci indexte tutulan degeri printledik
# #print(name_list [0])
# if name_list[0].lower() == "yakup" and pwd == "12":
#     kg = float(input("kilo: "))
#     hg = float(input("Boy: "))
#     bmi = kg/(hg/100)**2
#     if 0 <= bmi <=18.5:
#         print(f'{name},{bmi} kilo degerlendirmen zayif..')
#     elif 18.6 <= bmi <= 24.9:
#         print("{} , {} kilo degerlendirmen normal..".format(name,bmi))
#     elif 25 <= bmi <= 29.9:
#         print("{} , {} kilo degerlendirmen kilolu..".format(name,bmi))
#     elif 30 <= bmi <= 35:
#         print("{} , {} kilo degerlendirmen fazla kilolu..".format(name,bmi))
#     elif 36 <= bmi <= 39.9:
#         print("{} , {} kilo degerlendirmen obez..".format(name,bmi))
#     else:
#         print("bilgilerinizi kontrol ediniz!")
# else:
#     print("Kullanici bilgileriniz hatali..")

# 2. cozum

# username = input("username bilgisini giriniz!: ")
# password = int(input("password giriniz!: "))
# if (username == "beast" and password == 123):
#     print("Basariyla giris yaptiniz!")
#     kilo = int(input("Kilo bilginiz?: "))
#     boy = int(input("Boy bilginiz?: "))
#     vki = kilo / (boy*boy)
#     if (0 <= vki <= 18.5):
#         print("{} , {}".format("vki","zayif"))
#     elif (18.6 <= vki <= 24.9):
#         print("{} , {}".format("vki", "normal"))
#     elif (25 < vki <=29.9):
#         print("{} , {}".format("vki", "kilolu"))
#     elif (30 < vki <= 34.9):
#         print("{} , {}".format("vki", "fazla kilolu"))
#     elif (35 < vki <= 39.9):
#         print("{} , {}".format("vki", "obez"))
#     else:
#         print("{} , {}".format("vki", "ACIL DURUM DOKTORA GIT!! ya da girdigin degerleri kontrol et!"))
# elif (username != "beast" and password == "123"):
#     print("username bilginiz hatalidir lutfen tekrar deneyiniz!")
# elif (username == "beast" and password != "123"):
#     print(" password bilginiz hatalidir lutfen tekrar deneyiniz!")
# else:
#     print("Giris bilgileriniz hatalidir.")
#endregion
#region example 11
# product = input("urun giriniz: ")
# if product == "muz" or product =="ananas" or product == "elma"
#     print("Sebze reyonu")
# elif product == "tv" or product =="pc" or product == "telefon"
#     print("Teknoloji reyonu")
# else:
#     print("Aradiginiz urun bulunmamaktadir!")
#endregion
#region example 12
# kitap_sayisi = int(input("Kitap sayisi: "))
# if 0<=kitap_sayisi<=20:
#     print(f'alinan kitap sayisi {kitap_sayisi}\ntoplam odenecek tutar{kitap_sayisi * 5 * 0.95}')
# elif 21<=kitap_sayisi<=50:
#     print(f'alinan kitap sayisi {kitap_sayisi}\ntoplam odenecek tutar{kitap_sayisi * 5 * 0.90}')
# elif 51<=kitap_sayisi<75:
#     print(f'alinan kitap sayisi {kitap_sayisi}\ntoplam odenecek tutar{kitap_sayisi * 5 * 0.85}')
# elif 76<=kitap_sayisi<=100:
#     print(f'alinan kitap sayisi {kitap_sayisi}\ntoplam odenecek tutar{kitap_sayisi * 5 * 0.75}')
# else:
#     print("kitap sayisini dogru giriniz>>")
#
# #benim cozumum
#
# satinalinankitapsayisi = int(input("satin aldiginiz kitap miktarini giriniz: "))
# kitapfiyati = satinalinankitapsayisi * 5
# if (satinalinankitapsayisi == 0):
#     print("Kitap okumani oneririm pis cahil - ILBER ORTAYLI")
# elif (0<satinalinankitapsayisi<=20):
#     print("{} * {} = {} TL".format(kitapfiyati,0.95,kitapfiyati * 0.95))
# elif (21<satinalinankitapsayisi<=50):
#     print("{} * {} = {} TL ".format(kitapfiyati,0.90,kitapfiyati * 0.90))
# elif (51<satinalinankitapsayisi<=75):
#     print("{} * {} = {} TL".format(kitapfiyati,0.85,kitapfiyati * 0.85))
# elif (76<satinalinankitapsayisi<=100):
#     print("{} * {} = {} TL".format(kitapfiyati,0.75,kitapfiyati * 0.75))
# else:
#     print("Hele bir elindeki kitaplari oku sonra satin alirsin yegenim :)")
#endregion
#region command slash yoruma aliyor satirlari
#region example 13
# #kullanicidan tam adini alalim ve isim.soyisim@bilgeadam.com mail adresini olusturalim ekrana basalim.
# Tam_ad = input("Tam adinizi giriniz: ").lower()
# name_list = Tam_ad.split(" ")
# print("{}.{}@bilgeadam.com.".format(name_list[0],name_list[-1]))
#endregion
