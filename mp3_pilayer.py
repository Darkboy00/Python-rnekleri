import webbrowser as web



print("""
***********************
Müzik Player

1) Müzik listesi
2) Yeni Müzik Eklemek
3) Müzik Silme
4) Müzik çal
5) Rastgele müzik çal

Programdan Çıkmak İçin q tuşuna basın

***********************
""")
mp3 = {}

while True:

    sec = input("Bir işlem seçin: ?")
    if sec == "q":
        print("Program Kapatıldı!")
        break
    elif sec == "1":
        for ad,link in mp3.items():
            print("{} <---> {}".format(ad, link))


    elif sec == "2":
        mp3ad = input("Eklemek istediğiniz müziği ismini girin: ")
        mp3link = input("Eklemek istediğiniz müziğin linkini girini: ")
        mp3[mp3ad] = mp3link
        print("Müzik Başarıyla eklendi")

    elif sec == "3":
        mp3_sil = input("Silmek istediğiniz müziğin adını giriniz: ")

        if mp3_sil not in mp3:
            print("Silmek istediğiniz müzik, bulunamadı. Lütfen kontrol edip tekrar deneyiniz")
        else:
            mp3.pop(mp3_sil)
            print("{}' Ögesi müzik listesinden silindi".format(mp3_sil))

    elif sec == "4":
        hangi = input("Çalmak istediğiniz müziğin adını yazın: ")
        for ad,link in mp3.items():
            print("Seçtiğini müzik açılıyor...",web.open(link))

    elif sec == "5":
        print("Programın Sonraki Güncellemesinde Bu Özellikte Eklenecektir.\n Şuan ki version: 1.4.6")
