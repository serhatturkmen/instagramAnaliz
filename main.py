import requests
from bs4 import BeautifulSoup as intvericek
URL = "https://www.instagram.com/{}"

def kullaniciBilgiAl(username):
    if(username == ""):
        print("Kullanıcı adını girmediniz.")
        exit(1)
    tam_url = URL.format(username)
    r = requests.get(tam_url)
    s = intvericek(r.text,"lxml")

    etiket = s.find("meta",attrs={"name":"description"})
    try:
        cekilen_veri = etiket.attrs['content']
        istenilen_veri = cekilen_veri.split("-")[0]
        istenilen_veri = istenilen_veri.replace("Followers","Takipçisi")
        istenilen_veri = istenilen_veri.replace("Following","Takip")
        istenilen_veri = istenilen_veri.replace("Posts","Gönderisi")
    except AttributeError as e:
        return 0
    
    if(istenilen_veri):
        return istenilen_veri
    else:
        return 0

kullaniciAdi = input("instagram kullanıcı adını giriniz: ")
veri = kullaniciBilgiAl(kullaniciAdi)
if(veri == 0):
    print("Girilen kullanıcı adını düzgün yazdığınızdan emin olunuz.")
else:
    print(kullaniciAdi,"adlı kullanıcının",veri,"bulunmaktadır.")
