import time

num_arac=0

zaman =time.localtime()

class arac1():
    def __init__(self,otomobil,zaman,bakiye):
        self.sinif=otomobil
        self.zaman=zaman
        self.bakiye=bakiye
        
class arac2():
    def __init__(self,minibus,zaman,bakiye):
        self.sinif=minibus
        self.zaman=zaman
        self.bakiye=bakiye

class arac3():
    def __init__(self,otobus,zaman,bakiye):
        self.sinif=otobus
        self.zaman=zaman
        self.bakiye=bakiye
      
class gise():
    def __init__(self,arac1,arac2,arac3):
        self.arac1=arac1
        self.arac2=arac2
        self.arac3=arac3
    def bakiye_durum(self,ucret):
        self.bakiye-=ucret

if bakiye<0:
    print("bakiye yetersiz gecis yok")
if bakiye>0:
    print("bakiye yeterli gecis olabilir")
    
    
    
if aracGecen == otomobil:
    toplam =0
otobUcret = bakiye-ucret
for i in aracGecen:
    toplam +=1
    return toplam

elif aracGecen == minibus:
    toplam =0
minUcret = bakiye-ucret
for i in aracGecen:
    toplam +=1
    return toplam

else aracGecen == otobus:
   toplam =0
otoUcret = bakiye-ucret
for i in aracGecen:
    toplam +=1
    return toplam
        
        
@classmethod     
class araclar():
    def gecen_arac_sayisi(self,aracGecen):
        self.sinif+=aracGecen
    def bilgiler(self,HGSno,isim,soyad,sinif,zaman,bakiye):
        self.HGSno=HGSno
        self.isim=isim
        self.soyad=soyad
        self.sinif=sinif
        self.zaman=zaman
        self.bakiye=bakiye
        araclar.num_arac +=1
    print(bilgiler.__dict__)
    def bilgileri_goster(self):
        print("HGSno",self.HGSno,"isim",self.isim,"soyad",
              self.soyad,"sinif",self.sinif,"zaman",self.zaman,"bakiye",self.bakiye)
 
print(zaman)
        
class yonetim():
    def __init__(self):
        pass
  
    def rapor():
      topBakiye="((otomobil*otobUcret)+(minibus*minUcret)+(otobus*otoUcret))"
        return topBakiye
        print(topBakiye)
    


