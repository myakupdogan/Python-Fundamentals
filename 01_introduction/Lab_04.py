#"""FOR LOOP"""
#"in", "not in" ve range() fonsiyonu.
# "in" operatoru bir liste icerisinde aranan ifade geciyorsa true gecmiyorsa false doner. string ifadelerde in kullanabiliriz.
#"not in" operatoru ise "in" operatorunun tam tersi mantikta calisir.
# name = "muhammad ali"
# print("b" in name)
# print("m" in name)
# print("M" in name)


# print("b" not in name)
# print("m" not in name)
# print("M" not in name)


# range() fonksiyonu for loop ile sik kullanilan bir fonksiyondur.
# range(100) fonksiyonu icerisine 100 dedigimizde 0-99 arasi tam sayi listesi doner.

# for i in range(10):  #n-1 mantiginda calisir!!
#     print(i, end=" ") #end yazinca yan yana bastiriyoruz range i normalde alt alta basilir!

# for i in range(5,10):
#     print(i)

# range() 3 arguman verirsek 1. arguman baslangic 2. arguman bitis, 3. arguman ise adim miktarini temsil eder.
# for i in range(1,21,2):
#     print(i)

#region example 1
# 1-100 arasindaki cift ve tek sayilarin toplami
# ciftlerintoplami = 0
# teklerintoplami = 0
# for i in range(1,101):  #while loop oldugu gibi adi miktarini biz arttirmiyoruz aksini soylemdeigimiz surece 1 olarak yani defaultbir kabul edip calisir.
#     if i % 2 == 0:
#         ciftlerintoplami += i
#     else:
#         teklerintoplami += i
# print("ciftlerin toplami: {} , teklerin toplami: {}".format(ciftlerintoplami,teklerintoplami))
#endregion
#region example 2
#kullanicidan baslangic bitis ve adim miktarlari alalim. 
# bu sartlara bagli kalarak her bir adimdaki sayinin karesini alarak ekrana yazdiralim.
# Cikti 1. adimda ki sonuc:2
# baslangic = int(input("Baslangic:"))
# bitis = int(input("Bitis:"))
# adim = int(input("Adim:"))
# counter = 1
# for i in range(baslangic, bitis, adim):
#     print("{}. adimda ==> {} ".format(counter, i**2))
#     counter += 1
#endregion
#region example 3
#Kullanicidan alinan sayi asal mi degil mi?
# sayi1 = int(input("Bir sayi giriniz: "))
# if sayi1 <= 0:
#     print("Sifir ve negatif sayilar asal degildir.")
# else:
#     is_prime = True
#     if sayi1 == 1:
#         is_prime = False
#
#     for i in range(2,sayi1):
#         if sayi1 % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print("{} sayisi asal sayidir.".format(sayi1))
#     else:
#         print("{} sayisi asal sayi degildir.".format(sayi1))
#endregion
#region example 4
#0-1000 arasindaki sayilari 10 ar 10 ar toplayalim. her bir adimda ki toplami kullaniciya gosterelim.
# toplam = 0
# counter = 1
# for i in range(0, 1001, 10):
#     toplam += i
#     print("{}.adimda ==> {} ".format(counter, i))
#     counter += 1

#endregion
#region example 5
# carpim tablosu
# for i in range(0,11):
#     for j in range(0,11):
#         print("{} * {} = {}".format(i,j,i*j))
#     print("~~~~~~~~~~~")
#endregion
#region example 6
#"*" sembollerini kullanarak kare sembolu yapiniz.
# edge = int(input("kenar uzunlugunu giriniz:"))
# for i in range(0,edge):
#     for j in range(0,edge):
#         print("*", end=" ")
#     print(" ")
#endregion
#region example 7
#dik ucgen yap
# taban = int(input("kenar uzunlugu girin:"))
# for i in range(0,taban):
#     for j in range(0,taban):
#         if j <= i:
#             print("*",end="")
#     print("")
# #endregion
#region example 8
# ici bos bir listeye rakamlari ekleyelim.
# sayilar = []
# for i in range(0,10):
#     sayilar.append(i)
# print(sayilar)
#endregion
#region example 9
# bos bir listenin icerisini 0-100 arasinda olacak sekilde rastgele 10 sayi ile doldurun
# import random
# list = []
# for i in range(10):
#     sayilar = random.randint(0, 100)
#     list.append(sayilar)
# print(list)
#endregion
#region example 10
#0-100 arasinda olacak sekilde rastgele 10 adet sayi uretin, bu sayilardan 3 tam bolunenlerin karesi bir listeye doldurun.
# import random
# list = []
# for i in range(10):
#     sayilar = random.randint(0,100)
#     if sayilar % 3 == 0:
#         print(sayilar)
#         list.append(sayilar**2)
# print(list)
#endregion
#region example 11
# kullanicidan bir soz obegi aliyoruz.
# or: merhaba ben muhammed yakup dogan
# yukaridaki soz obeginde ki her bir harfi bir listeye ekleyelim.

# word = input("please type something:")
# list = []
# print(len(word))
# yol 1
# soz obegi icerisinde adim adim dolasarak

# for i in range(0,len(word)):
#     if word[i] != " ":
#         list.append(word[i])
# print(list)
# yol 2
# soz obeginde ki her bir harfi donguye iterate ederek yapin.

# for character in word:
#     if character != " ":
#         list.append(character)
# print(list)
#endregion