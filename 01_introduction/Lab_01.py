#"""Diger programlama dilllerinde degisken tanimlarken atama oluyor mesela
#int x = 10
#Pythonda degisken tanimlarken herhangi bir tip belirtmiyoruz.
#x = 10
#Bir tip belirtmedigimiz icin degiskenimiz anlik olarak icerisineatilan degerin tipine burunmektedir.
#x = "muhammad ali"""
#region example
#first_name = "Muhammed"
#second_name = "Yakup"
#surname = "Dogan"
#print(first_name,second_name,surname)
# Burada print() built in fonksiyonu araciligi ile degisken uzerinde tutulan ifadeyi ekrana yazdirdik.
#first_name = 10
# Yukarida first_name degiskeni icerisine 10 degerini atadik gordugunuz gibi istedigimiz degeri degisken icerisine atayabiliyoruz.
#print(first_name)
# Kullanicidan alinan 2 adet sayi uzerinden temel 4 islem yapan uygulama
#print('Lutfen yapmak istediginiz islemi seciniz.\nDort islem uygulanabilir lutfen buna dikkat edin.')
#sayi1 = int(input('Lutfen ilk sayiyi giriniz:'))
#sayi2 = int(input('lutfen ikinci sayiyi giriniz:'))
#toplam = sayi1 + sayi2
#cikarma = sayi1 - sayi2
#carpma = sayi1 * sayi2
#bolme = sayi1 / sayi2
#print(f'sonuc: {toplam}')
#print(f'cikarma isleminin sonucu: {cikarma}')
#print("{} * {} = {}".format(sayi1,sayi2,carpma))
#print(f'{sayi1} / {sayi2} = {bolme}')
#endregion
# region example kare
"""Kullanicidan alinan kenar bilgisine gore bir karenin alanini ve cevresini hesaplayin"""
#kenar = int(input("kenari giriniz:"))
#karenin_cevresi = kenar * 4
#karenin_alani = kenar * kenar
#print(f'cevresi: {karenin_cevresi}')
#print(f'alan: {karenin_alani}')
# endregion
# region example dikdortgen
"""Kullanicidan alinan kisa ve uzun kenar bilgilerine gore bir dikdortgenin alanini ve cevresini hesaplayin"""
#kisa_kenar = int(input("Dikdortgenin kisa kenarini girin: "))
#uzun_kenar = int(input("Dikdortgenin uzun kenarini girin: "))
#dikdortgenin_alani = kisa_kenar * uzun_kenar
#dikdortgenin_cevresi = 2 * (kisa_kenar + uzun_kenar)
#print(f'dikdortgenin cevresi: {dikdortgenin_cevresi} , dikdortgenin alani: {dikdortgenin_alani}')
# endregion
#region example ucgen
"""ucgenin alanini hesaplayiniz"""
taban = float(input("taban degeri giriniz:"))
yukseklik = float(input("yukseklik degeri giriniz:"))
print(f'alan: {taban * yukseklik / 2}')
#endregion

