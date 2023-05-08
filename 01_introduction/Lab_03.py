"""WHILE LOOP"""
#region example 1
#0-100 arasinda ki sayilari ekrana yazdiralim.
# sayac = 0
# while sayac <=100:
#     print(sayac)
#     sayac += 1
#endregion
#region example 2
#1-101 arasindaki cift ve tek sayilarin miktarini ekrana yazdiralim.
# sayac = 1
# ciftsayilar = 0
# teksayilar = 0
# while sayac<101:
#     sayac += 1
#     if sayac % 2 == 0:
#         ciftsayilar += 1
#     else:
#         teksayilar += 1
# print("1-101 arasinda {} tane cift sayi, {} tane tek sayi bulunmaktadir.".format(ciftsayilar,teksayilar))
#benim cozumum
# sayac = 1
# while sayac<=100:
#     sayac+=1
#     if sayac % 2 ==0:
#         print("{} ciftsayi.".format(sayac))
#     else:
#         print("{} teksayi.".format(sayac))
#endregion
#region example 3
#1-1000 arasindaki cift ve tek sayilarin toplamini ekrana yazdiralim.
# sayac = 1
# ciftsayilarin_toplami = 0
# teksayilarin_toplami = 0
# while sayac<=1000:
#     if sayac % 2 == 0:
#         ciftsayilarin_toplami += sayac
#     else:
#         teksayilarin_toplami += sayac
#     sayac += 1
# print("1-1000 arasinda ki cift sayilarin toplami: {}\ntek sayilarin toplami: {}".format(ciftsayilarin_toplami,teksayilarin_toplami))
#endregion#
#region example 4
# kulllanicidan bir islem turu alalim ('+','-',vb) ve 2 adet sayi uzerinden kullanicinin istedigi islemi gerceklestirelim.
# kullanici klavyeden e harfi gonderirse uygulamayi durduralim. kullanici isterse sonsuza kadar islem yapsin.
# """Basit hesaplama islemi yapmak uzere sistemimize hos geldiniz!
# toplama islemi icin 1
# cikarma islemi icin 2
# carpma islemi icin 3
# bolme islemi icin 4
# cikmak icin e
# keyifli calismalar dileriz"""
#
# while True:
#     işlem = input("İşlem numarasını giriniz:")
#     a = int(input("Birinci sayı:"))
#     b = int(input("İkinci sayı:"))
#     if (işlem == "1"):
#         print("{} ile {} nin toplamı {}'dir.".format(a, b, a+b))
#     elif (işlem == "2"):
#         print("{} ile {} nin farkı {}'dir.".format(a, b, a-b))
#     elif (işlem == "3"):
#         print("{} ile {} nin çarpımı {}'dir.".format(a, b, a*b))
#     elif (işlem == "4"):
#         print("{} ile {} nin bölümü {}'dir.".format(a, b, a/b))
#     elif (işlem == "e"):
#         break
#     else:
#         print("Geçersiz İşlem! Lütfen Geçerli Bir İşlem Giriniz.")
#Hocanin cozumu
# process_type_list = ["+","-","*","/","e"]
# while True:
#     process = input("Islem turu giriniz: ")
#     if process in process_type_list:
#         #in operatoru ile bir liste icerisinde item varsa true yoksa false doner.
#         if process == "e":
#             print("uygulama kapatiliyor..")
#             break
#         else:
#             sayi1 = int(input("Birinci sayiyi giriniz: "))
#             sayi2 = int(input("Ikinci sayiyi giriniz: "))
#             if process == "+":
#                 print(" Sonuc {} ' dir.".format(sayi1+sayi2))
#             elif process == "-":
#                 print(" Sonuc {} ' dir.".format(sayi1-sayi2))
#             elif process == "*":
#                 print(" Sonuc {} ' dir.".format(sayi1*sayi2))
#             elif process == "/":
#                 print(" Sonuc {} ' dir.".format(sayi1/sayi2))
#     else:
#         print("{} islemi icin lutfen gecerli bir islem turu seciniz!".format(process))
#endregion
#region example 5
#kullanicidan yil bilgisi alacaginiz bu yil bilgisi 1943 ile gunumuz yili arasinda ise buldunuz degilse aradiginiz yil bulunmamaktadir diyen uygulama
# while True:
#     year_information = int(input("Please enter the year: "))
#     if 1943 < year_information <=2023:
#         print("Buldunuz.")
#         break
#     else:
#         print("Aradiginiz yil bulunmamaktadir.")
#hocanin cozumu
# from datetime import datetime
# started_date = 1943
# search_date= int(input("aradiginiz yili giriniz: "))
# while started_date <= datetime.now().year:
#     if started_date == search_date:
#         print("Bulundu.. Aradiginiz yil {}".format(started_date))
#         break
#     else:
#         print("Aradiginiz {} yili bulunmamaktadir.".format(started_date))
#     started_date += 1
# hocanin diger cozumu
# from datetime import datetime
# started_date = 1943
# search_date= int(input("aradiginiz yili giriniz: "))
# is_exist = False
# while started_date <= datetime.now().year:
#     if started_date == search_date:
#         print("Bulundu.. Aradiginiz yil {}".format(started_date))
#         is_exist = True
#         break
#     started_date += 1
# if not is_exist:
#     print("Aradiginiz tarih bulunmamaktadir.")

#endregion
#region example 6
#tek sayilarin toplamini bulun continue kullanarak.0-101 arasinda
# i = 0
# sum = 0
# while i<= 101:
#     i +=1
#     if i % 2 == 0:
#         continue
#     sum += i
# print(sum)
#eksi olma durumu cep telefonunda var
#endregion