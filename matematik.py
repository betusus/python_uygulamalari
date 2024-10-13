tel_rehberi=dict()

def tel_no_ekle(x):
    print("***NUMARA EKLEME EKRANINA HOŞGELDİNİZ***")
    numara_isim_al=input("Lütfen kayıt edilecek kişinin adını yazınız: ")
    numara_no_al=input("Lütfen telefon numarasını giriniz:")

    x=tel_rehberi.setdefault(numara_isim_al,numara_no_al)
    print(f"'{numara_isim_al}'adlı kişi telefon listesine eklendi...")
    input("Devam edilsin mi?")

def tel_rehber_göster(x):
    kişi_sayısı=len(x)
    print(f"Rehberinizdeki kayıtlı kişi.:{kişi_sayısı}")
    print("Rehbere hoşgeldiniz")

    for i,j in x.items():
        print(i,":",j)
    input("Devam edilsin mi?")

       


def no_sil(x):
    print("Kişi silme ekranına hoşgeldiniz...")
    silinecek_kişi=input("Silinecek kişiyi yazınız:")  
    x= tel_rehberi.pop(silinecek_kişi) 
    input("Devam edilsin mi?")     

while True:
    print("***HOŞGELDİNİZ***")
    print("***Seçim yapınız***")
    seçim_yap=int(input("1-Ekle\n2-Sil\n3-Rehberi Gör\n"))
    if seçim_yap==1:
        tel_no_ekle(tel_rehberi)
    elif seçim_yap==2:
        no_sil(tel_rehberi)
    elif seçim_yap==3:
        tel_rehber_göster(tel_rehberi)
    else:
        print("Lütfen uygun tuşlara basınız")           

