import pymysql
import pymysql.cursors



print("""

1) Km ekle
2) Tüm Km'leri göster
3) Km sil

0) Çıkış
    """)




while True:
    try:
        conn = pymysql.connect(host = '',
                           unix_socket = '/var/run/mysqld/mysqld.sock',
                           user = '',
                           passwd = '',
                           db = '',
                           charset='utf8')
        cursor = conn.cursor()
    except:
        print("Veritabanı Bağlantısında Hata")
        cursor.close()
        conn.close()
        giris = input("Yapmak istediğiniz işlemi seçiniz: ")
        giris = int(giris)





    giris = input("Yapmak istediğiniz işlemi seçiniz: ")
    giris = int(giris)

    if giris == 1:
        try:
            ekle = input("Aralarına boşluk bırakarak sırasıyla, arabanın ismini ve KM'sini yazın: ")
            p = ekle.split()
            sorguu = "INSERT INTO araba (isim, km) VALUES ('{isim}', '{km}')".format(isim = p[0], km = p[1])
            cursor.execute(sorguu)
            print("Başarıyla eklendi")
        except:
            print("Bilgiler Eklenemedi")

        cursor.close()
        conn.close()



    elif giris == 2:
        sorgu = "SELECT * FROM araba"
        cursor.execute(sorgu)
        hepsi = cursor.fetchall()
        for i in hepsi:
            print(i[0],"<-->",i[1],i[2],i[3])

        cursor.close()
        conn.close()


    elif giris == 3:
        baglanti = pymysql.connect(host = '185.154.131.61', unix_socket = '/var/run/mysqld/mysqld.sock', user = 'anahtary_kenan', passwd = 'Five-Seven54', db = 'anahtary_python', charset='utf8')
        cursors = baglanti.cursor()
        sorgu = "SELECT * FROM araba"
        cursors.execute(sorgu)
        hepsi = cursors.fetchall()
        for i in hepsi:
            print(i[0],"<-->",i[1],i[2],i[3])

        sil = int(input("Silmek istediğiniz Km'nin İD sini giriniz: "))




