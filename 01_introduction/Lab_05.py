# List
# Uygulama icerisinde anlik olarak bizim icin deger tutan bir yapidir. Birden fazla tipte farkli tipte deger tutabilr.
# Listeler RAM uzerinde tutuldugu icin uygulama calistigi surece uzerine yeni eklenen degerleri saklarlar.
# Yani uygulama kapatildiginda ilk haline doner.
# Ornegin futbol takimi listemiz olsun
# futbol_takimlari = [Besiktas, Galatasaray, Adana Demirspor]
#Uygulama calistirildiginda bu liste tam olarak yukaridaki yapida RAM'in hesap alanina cikartilir.
#Uygulama runtime'da yani calisiyor.Asagidaki kod calistigini varsayalim.
# futbol_takimlari.append("Trabzonspor")
#Artik listemiz 4 elemanli. Lakin uygulama shutdown edildiginde ilk yaratildigi hale geri donecektir.Listeler cunku RAM'de saklanir.
#top_boxers = ["Muhammad Ali","Mike Tyson","Lenox Lewis","Evander Holyfiled","Rocky Marciano"]
# top_boxers.append("George Forman")
# print(top_boxers)

#insert() fonksiyonu listenin herhangi bir index degerine eleman ekleme islemini yerine getirir.
# aldigi ilk parametre index degerini , ikinci parametre ise value temsil eder.
# top_boxers.insert(3,"Floyd Maywheater")
# print(top_boxers)

#remove() => listeden silinmesini istedigimiz item'in degerini kendisine vererek silme islemini gerceklestiriyoruz
# top_boxers.remove("Mike Tyson")
# print(top_boxers)

#clear() => fonksiyonu listenin alayini siler.
#top_boxers.clear()

#pop() =
#top_boxers.pop(4)

#extend => iki farkli listeyi birlestirmeye yarar.
#current_boxers = ["Tyson Fury","Deantony Wilder","Antony Jasua"]
#top_boxers.extend(current_boxers)

# movies = ["Fight Club","Matrix","Interstellar","Inception"]
# for movie in movies:
#     print(movie)
#
# for i in range(0,len(movies)):
#     print(movies[i])

# 2 farkli liste icerisine random olarak 10 adet sayi ile dolduralim.
# sayilar 0-100 arasinda uretilsin.
# ilk adimda doldurulan bu iki listenin karsilikli gelen index degerleri toplanarak 3. bir listeye eklensin.
#Soruyu index mantigiyla cozelim.
# import random
# lst1 = []
# lst2 = []
# lst3 = []
# for i in range(10):
#     lst1.insert(i, random.randint(0,101))
#     lst2.insert(i, random.randint(0, 101))
#     lst3.insert(i, lst1[i] + lst2[i])
#     print("{} + {} = {}".format(lst1,lst2,lst3))
# print(lst3)

#kullanicidan alinan soz obeginde ki sesli harfleri bir listeye dolduralim.
#sesli harfler tekrar etmesin.
#bosluklari sayin
#soz obeginde ki rakamlari bir listeye doldurun. Rakam listesi olusturmadan hazir bir fonksiyonla cozun.
# word = input("Please type something:")
# sesli_harfler = ["a","e","ı","i","o","ö","u","ü"]
# yakalanan_sesli_harf = []
# yakalanan_sayilar = []
# bosluk_sayisi = 0
# for character in word:
#     if character in sesli_harfler:
#         if character not in yakalanan_sesli_harf:
#             yakalanan_sesli_harf.append(character)
#     elif character == " ":
#         bosluk_sayisi += 1
#     elif character.isdigit():
#         yakalanan_sayilar.append(character)
# print(yakalanan_sesli_harf)
# print(yakalanan_sayilar)
# print("Yakalanan bosluk sayisi: {}".format(bosluk_sayisi))

# import string
# kullanici_adi = input("Kullanici adinizi giriniz:")
# sifre = input("Sifre giriniz:")
# if len(sifre)>=16:
#     for i in sifre:
#         if i.isdigit():
#             print("Sifrenize rakam ekleyiniz!")
#             break
#         elif i not in string.punctuation:
#             print("Sifrenize noktalama isareti ekleyiniz!")
#             break
#         elif i.islower():
#             print("Sifrenize kucuk harf ekleyiniz!")
#             break
#         elif i.isupper():
#             print("Sifrenize buyuk harf ekleyiniz!")
#             break
# else:
#     print("Sifrenizin minimum 16 karakter olmasi gereklidir!")

#list comprehension
#rakamlari bir listeye ekleme
#sayilar
#for i in range(10):
#   sayilar.append(i)
#print(sayilar)
#print([i for  i in range(10)])

#rakamlarin karesini listeye dolduralim.
#print([i*i for i in range(10)])

#0-100 arasinda 3 tam bolunen sayilarin karesini listeye dolduralim
#print([i*i for i in range(100) if i % 3 == 0])
