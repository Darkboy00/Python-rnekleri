while True:
    ilk = input("Bir sayı gir (Programdan çıkmak için q tuşuna bas): ")
    
    if ilk == "q":
        print("Program kapatıldı!")
        break
        
    iki = input("İkinci bir sayı girin: ")
    üç = input("İki sayı ile yapılacak olan işlemi girin, (toplama, çıkarma, çarpma ve bölme): ")
    izinli_karakterler = ("+","-","*","/")
    try:
        sayı1 = int(ilk)
        sayı2 = int(iki)
        
        for i in izinli_karakterler:
            if üç == i:
                print("İşleniyor...")
                
        if üç == "+":
            print(sayı1, "+", sayı2, "=", sayı1 + sayı2)
        elif üç == "-":
            print(sayı1, "-", sayı2, "=", sayı1 - sayı2)
        elif üç == "*":
            print(sayı1, "*", sayı2, "=", sayı1 * sayı2)
        elif üç == "/":
            print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
        else:
            break
    except (ValueError, ZeroDivisionError) as hata:
        print("Bir hata oluştu!")
        print("orijinal hata mesajı: ", hata) 
