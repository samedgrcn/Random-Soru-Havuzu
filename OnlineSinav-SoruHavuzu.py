# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:41:07 2021

@author: burci
"""

while True:
    import random
    puan = 0
    sorular = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sorulan_sorular = []

    soru1_cevaplar = ["a", "b", "c", "d", "e"]
    soru2_cevaplar = ["a", "b", "c", "d", "e"]
    soru3_cevaplar = ["a", "b", "c", "d", "e"]
    soru4_cevaplar = ["a", "b", "c", "d", "e"]
    soru5_cevaplar = ["a", "b", "c", "d", "e"]
    soru6_cevaplar = ["a", "b", "c", "d", "e"]
    soru7_cevaplar = ["a", "b", "c", "d", "e"]
    soru8_cevaplar = ["a", "b", "c", "d", "e"]
    soru9_cevaplar = ["a", "b", "c", "d", "e"]
    soru10_cevaplar = ["a", "b", "c", "d", "e"]

    soru_numarası = ["1.Soru", "2.Soru", "3.Soru", "4.Soru", "5.Soru",
                     "6.Soru", "7.Soru", "8.Soru", "9.Soru", "10.Soru"]

    soru_sayacı = 0
    yazılan_cevaplar = []
    dogru_cevaplar = []
    yanlıs_cevaplar = []

    a = "a"
    b = "b"
    c = "c"
    d = "d"
    e = "e"

    # Sorular

    soru1 = """Aşağıda verilen kutunun içerisindeki gibi kelimelerin
    bir alt satıra geçmesini sağlayan kod nedir?
    
    a)\b     b)\c    c)?c    d)\n    e)/n    \n"""
    
    soru2 = """liste.append() komutunun görevi aşağıdakilerden hangiisidir?
    
    a)Listede kaç eleman olduğunu,karakter sayısını verir.
    b)Liste oluşturmayı sağlar.
    c)Listeden eleman silmeyi sağlar.
    d)Listeye yeni eleman eklemeyi sağlar.
    d)Listeyi yazdırır.    \n"""
    
    soru3 = """Hangisi tüm harfleri büyük yapar?
    
    a)toUpperCase()
    b9upper()
    c)uppercase()
    d)upperCade()
    e)len()  \n"""
    
    soru4 = """x=input("Lütfen bir değeri giriniz:")
    print(12/x)
    Yukarıdaki kodlar çalıştırıldığında, klavyeden girilirse ekran çıktısı ne olur?
    
    a)Klavyeden girilen değer sayıya integer dönüştürülmediği için hata oluşur.
    b)12/0          c)Sayı sıfıra bölünmez hatası verir     d)print sıfıra bölünmez hatası verir      d)0    \n"""
    
    soru5 = """Aşağıda verilen kod parçası çalıştırıldığında;
    KullaniciAdi=input(“Kullanıcı Adınızı Giriniz”)
    Sifre=input(“Parolanızı Giriniz”)
    if KullaniciAdi==”Hitit” and parola==”1234″
    print(“Giriş başarılı”)
    else:
    print(“Hatalı kullanıcı adı veya parola”)
    Kullanıcı adı olarak “Hitit” parola olarak “12345” yazıldığında hangi ekran çıktısı elde edilir?
    
    a)Giriş başarılı     b)Giriş başarısız       c)Böyle bir kullanıcı tanımlı değil
    d)Hatalı kullanıcı adı veya parola          e)kullanıcı adı hatalı    \n"""
    
    soru6 = """Hangi seçenekteki komut, \n ile çıktıyı birden fazla satıra yazdırmaz?  
    
    a)print('Fazıl','Hüsnü','Dağlarca',sep='\n')
    b)print('Ahmet\nHamdi\nTanpınar')
    c)print('Nazım'+'\n'+'Hikmet'+'\n'+'Ran')
    d)print('Bedri\n','Rahmi\n','Eyüboğlu',end='\n')
    e)print('Orhan\\nVeli\\nKanık')  \n"""
    
    soru7 = """Değişken isimlendirme ile ilgili verilen bilgilerden hangisi yanlıştır?
    
    a?Boşluk kullanılmaz.
    b)as,not,if gibi özel komutlar kullanılmaz
    c)+-*/&# gibi özel karakterler kullanılmaz
    d)Değişken adına rakamLa başlanmaz
    e)Altçizgi(_)karakteri kullanılmaz   \n"""
    
    soru8 = """Aşağıdaki önermelerden hangisi "True"(Doğru) değeri döndürür?
    
    a)45<30
    b)x=5 y=2 x+y==3
    c)37==25
    d)58>34
    e)y1=90 y1>95    \n"""
    
    soru9 = """if 5<9:
        print("X")
    elif 8>5:
        print("Y")
    else:
        print("Z")
    Kodlar çalıştırıldığında ekran çıktısı ne olur?
    (Şıklardaki birden fazla harfler, alt alta satırlar halinde yazdırılmıştır)
    
    a)X Z     b)X Y Z     c)Y     d)Z      e)X     \n"""
    
    soru10 = """kur=3.7
    miktar=int(input("TL'ye çevrilecek Dolar miktarını giriniz:"))
    hesapla=miktar*kur
    print(miktar,"Doların TL cinsinden değeri=", hesapla, "TL'dir.")
    Verilen program çalıştırıldığında, klavyeden 100 değeri girilirse;ekrana hangi çıktıyı verir?
    
    a)3.7TLnin dolar cinsinde değeri=370.0 Dolardır.
    b)100TL nin dolar cinsinden değeri=27.02' dolardır.
    c)100Doların TL cinsinden değeri=370.0TL'dir
    d)input komutunda yazım hatasıolduğu için hata verir
    e)print komutunda yazım hatası olduğu için hata verir.     \n"""

    # Cevaplar

    soru1_cevap = "d"
    soru2_cevap = "d"
    soru3_cevap = "b"
    soru4_cevap = "a"
    soru5_cevap = "a"
    soru6_cevap = "e"
    soru7_cevap = "e"
    soru8_cevap = "d"
    soru9_cevap = "e"
    soru10_cevap = "c"

    print("""
******************** PYTHON İLE PROGRAMLAMAYA GİRİŞ DERSİ GÜZ DÖNEMİ SINAVI ********************
    """)

    basla = input("Teste başlamak istiyor musunuz? e/h ")
    if basla == "e" or basla == "E":
        for i in range(10):
            print(soru_numarası[soru_sayacı])
            soru_sayacı += 1
            soru = random.choice(sorular)
            if soru not in sorulan_sorular:
                sorulan_sorular.append(soru)
            else:
                while True:
                    soru = random.choice(sorular)
                    if soru not in sorulan_sorular:
                        sorulan_sorular.append(soru)
                        break
                    else:
                        continue

            if soru == 1:
                yazılan_cevaplar.clear()
                for j in range(5):
                    cevap = random.choice(soru1_cevaplar)
                    if cevap not in yazılan_cevaplar:
                        yazılan_cevaplar.append(cevap)
                    else:
                        while True:
                            cevap = random.choice(soru1_cevaplar)
                            if cevap not in yazılan_cevaplar:
                                yazılan_cevaplar.append(cevap)
                                break
                            else:
                                continue
                a = yazılan_cevaplar[0]
                b = yazılan_cevaplar[1]
                c = yazılan_cevaplar[2]
                d = yazılan_cevaplar[3]
                e = yazılan_cevaplar[4]
                
                print(soru1)
                print("a)" + a, " b)" + b, " c)" + c, " d)" + d, " e)" + e)
                print("\nİşaretlemek istediğiniz şıkkı klavyeden tuşlayın.")
                while True:
                    cevap = input("Cevap: \n")
                    if cevap == "a":
                        if a == soru1_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "b":
                        if b == soru1_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "c":
                        if c == soru1_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "d":
                        if d == soru1_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "e":
                        if e == soru1_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    else:
                        print("Lütfen geçerli bir şıkkı seçin.")
                        continue
                    
            elif soru == 2:
                yazılan_cevaplar.clear()
                for j in range(5):
                    cevap = random.choice(soru2_cevaplar)
                    if cevap not in yazılan_cevaplar:
                        yazılan_cevaplar.append(cevap)
                    else:
                        while True:
                            cevap = random.choice(soru2_cevaplar)
                            if cevap not in yazılan_cevaplar:
                                yazılan_cevaplar.append(cevap)
                                break
                            else:
                                continue
                a = yazılan_cevaplar[0]
                b = yazılan_cevaplar[1]
                c = yazılan_cevaplar[2]
                d = yazılan_cevaplar[3]
                e = yazılan_cevaplar[4]
                
                print(soru2)
                print("a)" + a, " b)" + b, " c)" + c, " d)" + d, " e)" + e)
                print("\nİşaretlemek istediğiniz şıkkı klavyeden tuşlayın.")
                while True:
                    cevap = input("Cevap: \n")
                    if cevap == "a":
                        if a == soru2_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "b":
                        if b == soru2_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "c":
                        if c == soru2_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "d":
                        if d == soru2_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "e":
                        if e == soru2_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    else:
                        print("Lütfen geçerli bir şıkkı seçin.")
                        continue
                    
            elif soru == 3:
                yazılan_cevaplar.clear()
                for j in range(5):
                    cevap = random.choice(soru3_cevaplar)
                    if cevap not in yazılan_cevaplar:
                        yazılan_cevaplar.append(cevap)
                    else:
                        while True:
                            cevap = random.choice(soru3_cevaplar)
                            if cevap not in yazılan_cevaplar:
                                yazılan_cevaplar.append(cevap)
                                break
                            else:
                                continue

                a = yazılan_cevaplar[0]
                b = yazılan_cevaplar[1]
                c = yazılan_cevaplar[2]
                d = yazılan_cevaplar[3]
                e = yazılan_cevaplar[4]

                print(soru3)
                print("a)" + a, " b)" + b, " c)" + c, " d)" + d, " e)" + e)

                print("\nİşaretlemek istediğiniz şıkkı klavyeden tuşlayın.")

                while True:

                    cevap = input("Cevap: \n")

                    if cevap == "a":
                        if a == soru3_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "b":
                        if b == soru3_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "c":
                        if c == soru3_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "d":
                        if d == soru3_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "e":
                        if e == soru3_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    else:
                        print("Lütfen geçerli bir şıkkı seçin.")
                        continue

            elif soru == 4:
                yazılan_cevaplar.clear()
                for j in range(5):
                    cevap = random.choice(soru4_cevaplar)
                    if cevap not in yazılan_cevaplar:
                        yazılan_cevaplar.append(cevap)
                    else:
                        while True:
                            cevap = random.choice(soru4_cevaplar)
                            if cevap not in yazılan_cevaplar:
                                yazılan_cevaplar.append(cevap)
                                break
                            else:
                                continue

                a = yazılan_cevaplar[0]
                b = yazılan_cevaplar[1]
                c = yazılan_cevaplar[2]
                d = yazılan_cevaplar[3]
                e = yazılan_cevaplar[4]

                print(soru4)
                print("a)" + a, " b)" + b, " c)" + c, " d)" + d, " e)" + e)

                print("\nİşaretlemek istediğiniz şıkkı klavyeden tuşlayın.")

                while True:

                    cevap = input("Cevap: \n")

                    if cevap == "a":
                        if a == soru4_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "b":
                        if b == soru4_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "c":
                        if c == soru4_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "d":
                        if d == soru4_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "e":
                        if e == soru4_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    else:
                        print("Lütfen geçerli bir şıkkı seçin.")
                        continue

            elif soru == 5:
                yazılan_cevaplar.clear()
                for j in range(5):
                    cevap = random.choice(soru5_cevaplar)
                    if cevap not in yazılan_cevaplar:
                        yazılan_cevaplar.append(cevap)
                    else:
                        while True:
                            cevap = random.choice(soru5_cevaplar)
                            if cevap not in yazılan_cevaplar:
                                yazılan_cevaplar.append(cevap)
                                break
                            else:
                                continue

                a = yazılan_cevaplar[0]
                b = yazılan_cevaplar[1]
                c = yazılan_cevaplar[2]
                d = yazılan_cevaplar[3]
                e = yazılan_cevaplar[4]

                print(soru5)
                print("a)" + a, " b)" + b, " c)" + c, " d)" + d, " e)" + e)

                print("\nİşaretlemek istediğiniz şıkkı klavyeden tuşlayın.")

                while True:

                    cevap = input("Cevap: \n")

                    if cevap == "a":
                        if a == soru5_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "b":
                        if b == soru5_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "c":
                        if c == soru5_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "d":
                        if d == soru5_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "e":
                        if e == soru5_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    else:
                        print("Lütfen geçerli bir şıkkı seçin.")
                        continue

            elif soru == 6:
                yazılan_cevaplar.clear()
                for j in range(5):
                    cevap = random.choice(soru6_cevaplar)
                    if cevap not in yazılan_cevaplar:
                        yazılan_cevaplar.append(cevap)
                    else:
                        while True:
                            cevap = random.choice(soru6_cevaplar)
                            if cevap not in yazılan_cevaplar:
                                yazılan_cevaplar.append(cevap)
                                break
                            else:
                                continue

                a = yazılan_cevaplar[0]
                b = yazılan_cevaplar[1]
                c = yazılan_cevaplar[2]
                d = yazılan_cevaplar[3]
                e = yazılan_cevaplar[4]

                print(soru6)
                print("a)" + a, " b)" + b, " c)" + c, " d)" + d, " e)" + e)

                print("\nİşaretlemek istediğiniz şıkkı klavyeden tuşlayın.")

                while True:

                    cevap = input("Cevap: \n")

                    if cevap == "a":
                        if a == soru6_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "b":
                        if b == soru6_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "c":
                        if c == soru6_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "d":
                        if d == soru6_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "e":
                        if e == soru6_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    else:
                        print("Lütfen geçerli bir şıkkı seçin.")
                        continue

            elif soru == 7:
                yazılan_cevaplar.clear()
                for j in range(5):
                    cevap = random.choice(soru7_cevaplar)
                    if cevap not in yazılan_cevaplar:
                        yazılan_cevaplar.append(cevap)
                    else:
                        while True:
                            cevap = random.choice(soru7_cevaplar)
                            if cevap not in yazılan_cevaplar:
                                yazılan_cevaplar.append(cevap)
                                break
                            else:
                                continue

                a = yazılan_cevaplar[0]
                b = yazılan_cevaplar[1]
                c = yazılan_cevaplar[2]
                d = yazılan_cevaplar[3]
                e = yazılan_cevaplar[4]

                print(soru7)
                print("a)" + a, " b)" + b, " c)" + c, " d)" + d, " e)" + e)

                print("\nİşaretlemek istediğiniz şıkkı klavyeden tuşlayın.")

                while True:

                    cevap = input("Cevap: \n")

                    if cevap == "a":
                        if a == soru7_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "b":
                        if b == soru7_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "c":
                        if c == soru7_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "d":
                        if d == soru7_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "e":
                        if e == soru7_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    else:
                        print("Lütfen geçerli bir şıkkı seçin.")
                        continue

            elif soru == 8:
                yazılan_cevaplar.clear()
                for j in range(5):
                    cevap = random.choice(soru8_cevaplar)
                    if cevap not in yazılan_cevaplar:
                        yazılan_cevaplar.append(cevap)
                    else:
                        while True:
                            cevap = random.choice(soru8_cevaplar)
                            if cevap not in yazılan_cevaplar:
                                yazılan_cevaplar.append(cevap)
                                break
                            else:
                                continue

                a = yazılan_cevaplar[0]
                b = yazılan_cevaplar[1]
                c = yazılan_cevaplar[2]
                d = yazılan_cevaplar[3]
                e = yazılan_cevaplar[4]

                print(soru8)
                print("a)" + a, " b)" + b, " c)" + c, " d)" + d, " e)" + e)

                print("\nİşaretlemek istediğiniz şıkkı klavyeden tuşlayın.")

                while True:

                    cevap = input("Cevap: \n")

                    if cevap == "a":
                        if a == soru8_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "b":
                        if b == soru8_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "c":
                        if c == soru8_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "d":
                        if d == soru8_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "e":
                        if e == soru8_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    else:
                        print("Lütfen geçerli bir şıkkı seçin.")
                        continue

            elif soru == 9:
                yazılan_cevaplar.clear()
                for j in range(5):
                    cevap = random.choice(soru9_cevaplar)
                    if cevap not in yazılan_cevaplar:
                        yazılan_cevaplar.append(cevap)
                    else:
                        while True:
                            cevap = random.choice(soru9_cevaplar)
                            if cevap not in yazılan_cevaplar:
                                yazılan_cevaplar.append(cevap)
                                break
                            else:
                                continue

                a = yazılan_cevaplar[0]
                b = yazılan_cevaplar[1]
                c =yazılan_cevaplar[2]
                d = yazılan_cevaplar[3]
                e = yazılan_cevaplar[4]

                print(soru9)
                print("a)" + a, " b)" + b, " c)" + c, " d)" + d, " e)" + e)

                print("\nİşaretlemek istediğiniz şıkkı klavyeden tuşlayın.")

                while True:

                    cevap = input("Cevap: \n")

                    if cevap == "a":
                        if a == soru9_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "b":
                        if b == soru9_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "c":
                        if c == soru9_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "d":
                        if d == soru9_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "e":
                        if e == soru9_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    else:
                        print("Lütfen geçerli bir şıkkı seçin.")
                        continue

            elif soru == 10:
                yazılan_cevaplar.clear()
                for j in range(5):
                    cevap = random.choice(soru10_cevaplar)
                    if cevap not in yazılan_cevaplar:
                        yazılan_cevaplar.append(cevap)
                    else:
                        while True:
                            cevap = random.choice(soru10_cevaplar)
                            if cevap not in yazılan_cevaplar:
                                yazılan_cevaplar.append(cevap)
                                break
                            else:
                                continue

                a = yazılan_cevaplar[0]
                b = yazılan_cevaplar[1]
                c = yazılan_cevaplar[2]
                d = yazılan_cevaplar[3]
                e = yazılan_cevaplar[4]

                print(soru10)
                print("a)" + a, " b)" + b, " c)" + c, " d)" + d, " e)" + e)

                print("\nİşaretlemek istediğiniz şıkkı klavyeden tuşlayın.")

                while True:

                    cevap = input("Cevap: \n")

                    if cevap == "a":
                        if a == soru10_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "b":
                        if b == soru10_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "c":
                        if c == soru10_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "d":
                        if d == soru10_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    elif cevap == "e":
                        if e == soru10_cevap:
                            puan += 10
                            dogru_cevaplar.append(soru)
                            break
                        else:
                            yanlıs_cevaplar.append(soru)
                            break
                    else:
                        print("Lütfen geçerli bir şıkkı seçin.")
                        continue

        print("\nToplam 10 sorudan oluşan testimizde;")

        if len(dogru_cevaplar) == 10:
            print("Tebrikler bütün soruları doğru cevapladınız")
        else:
            print("{} soruyu doğru, {} soruyu yanlış cevapladınız.".format(len(dogru_cevaplar), len(yanlıs_cevaplar)))

        print("\nToplam puanınız: " + str(puan))


    elif basla == "h" or basla == "H":
        break
    else:
        print("Lütfen geçerli bir seçenek girin.")
