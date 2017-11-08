import random

def sayı_üret(başlangıç=0, bitiş=100, adet=6):
    sayılar = set()

    while len(sayılar) < adet:
        sayılar.add(random.randrange(başlangıç, bitiş))

    return sayılar

for i in range(8):
    print(sayı_üret())
