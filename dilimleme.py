site1 = "www.webtekno.com"
site2 = "www.google.com"
site3 = "www.msi.com"
site4 = "www.kenanyaman.com"

print("Önce:", site1,site2,site3,site4, "\nsonra: ", sep="\n")

for isim in site1,site2,site3,site4:
    print("site: ", isim[4:-4])
