isim = input("İsminiz: ")
        
if len(isim) <= 5:
    print(isim[:5])
else:
    print(isim.capitalize()[:5] + "...")
 
