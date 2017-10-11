while True:
    ilk = input("Bir sayı gir (Programdan çıkmak için q tuşuna bas): ")

    if ilk == "q":
        print("Program kapatıldı!")
        break

    iki = input("İkinci bir sayı girin: ")
    üç = input("İki sayı ile yapılacak olan işlemi girin, (+  -  *  / ): ")
    izinli_karakterler = ("+","-","*","/")
    sonuç = []
    try:
        sayı1 = int(ilk)
        sayı2 = int(iki)

        for i in izinli_karakterler:
            if üç == i:
                print("İşleniyor...")

        if üç == "+":
            so = (sayı1, "+", sayı2, "=", sayı1 + sayı2)
            sonuç += so
            print(sonuç[0], "+", sonuç[2], "=", sonuç[4])
        elif üç == "-":
            so = (sayı1, "-", sayı2, "=", sayı1 - sayı2)
            sonuç += so
            print(sonuç[0], "-", sonuç[2], "=", sonuç[4])
        elif üç == "*":
            so = (sayı1, "*", sayı2, "=", sayı1 * sayı2)
            sonuç += so
            print(sonuç[0], "*", sonuç[2], "=", sonuç[4])
        elif üç == "/":
            so = (sayı1, "/", sayı2, "=", sayı1 / sayı2)
            sonuç += so
            print(sonuç[0], "/", sonuç[2], "=", sonuç[4])
        else:
            break


        with open("log.txt","a+") as log:
            veri = log.read()
            for i in sonuç:
                log.write("{}\n".format(i)+veri)


    except (ValueError, ZeroDivisionError) as hata:
        print("Bir hata oluştu!")
        print("orijinal hata mesajı: ", hata)
