from bs4 import BeautifulSoup
import requests

url = input("Linkleri bulmak istediğiniz web sayfasının adresini giriniz: ")
r = requests.get("http://" +url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))