class okul:
    def __init__(self,şube,öğretmen,bölüm,mevcut):
        self.şube=şube
        self.bölüm=bölüm
        self.öğretmen=öğretmen
        self.mevcut=mevcut


    def bilgileri_göster(self):
        print("-"*45)
        print("Sınıf Bilgileri")
        print("Şube:{}\nÖğretmen:{}\nBölüm:{}\nMevcut:{}".format(self.şube,self.öğretmen,self.bölüm,self.mevcut))
        print("-"*45)

    def öğretmen_adı(self):
        print("Öğretmen Adı:",self.bölüm)  


    def branş_değis(self):
        yeni_branş=input("Yeni branşınızı girin: ")
        print("***eski branş***",self.bölüm)
        self.bölüm=yeni_branş
        print("-"*45)
        print("Sınıf Bilgileri")
        print("Şube:{}\nÖğretmen:{}\nBölüm:{}\nMevcut:{}".format(self.şube,self.öğretmen,self.bölüm,self.mevcut))
        print("-"*45)

while True:
    sınıf_adı=input("Lütfen şube giriniz: ")
    öğretmen_bilgisi=input("Lütfen isminizi giriniz: ")
    bölüm_al=input("Lütfen branşınızı giriniz: ")
    mevcut=input("Mevcut giriniz: ")
    sınıf_olustur=input("Sınıf oluşturunuz: ")

    sınıf_olustur=okul(sınıf_adı,öğretmen_bilgisi,bölüm_al,mevcut)

    print("---Hoşgeldiniz---")
    seçim = input("Branş değiştirmek için 1 giriniz: ")

    if seçim == "1" :
        sınıf_olustur.branş_değis()
    else:
        print("İşlem bitti")  
        break  










