#-*- coding: utf-8 -*-

# Release: İlker IŞIK
# Date: 30.06.2014
# Mail: iiilker99@gmail.com



import TrDenetle as tr
import time as öy
from random import choice as seç
from random import uniform as rastKesir
from random import random as rastgele
def yumuşakYaz(yazı,hız=35,diziAtla=True):
    bekleme=1/hız
    for d in yazı:
        if d in ",.:;":
            bekleYaz(d,bekleme*10)
        else:
            bekleYaz(d,bekleme)
    if diziAtla: print()

ÖLÜM=[
    "Ölümden kaçmak için attığımız her adım, bizi ölüme götürürmüş, anladım. -Demokritos",
    "Ölüm korkusu, ölümden daha korkunçtur. -Friedrich Nietzsche",
    "Ölümün iyi yanı, bir daha ölümün olmamasıdır. -Friedrich Nietzsche",
    "Yüreğin her atışı, kendi ölümünün ayak sesidir. -Beyazid-i Bistami",
    "Ölümü kendine sevdir, nasıl olsa gelecek. -Hz.Ebubekir",
    "Herkes kimsenin sağ kalmayacağını bilir de, kendi ölümüne inanmak istemez. -Namık Kemal",
    "Ölüm son uyku değil, son uynaıştır. -Walter Scott",
    "Ölüm olmasaydı, yaşam tüm güzelliğini yitirirdi. -Vasilyeviç Gogol",
    "Kimi amaçlar o kadar değerlidirler ki o yolda yenilmek bile başarı sayılır. -Ahmet Haşim",
    "Düşen değil, kalkmayı beceremeyen yenilir."
    ]
KAZANI=[
    "Yapabileceğimiz her şeyi yapsaydık, buna kendimiz bile şaşırırdık. -Thomas Edison",
    "Düşünmek, söylemek kolay; ancak yaşamak, özellikle başarı ile sonuçlandırmak çok zordur. -Ziya Gökalp",
    "Güçlükler başarının değerini artıran süslerdir. -Mollaire"
    ,"Hiçbir başarıya çiçekli yollardan gidilmez. -Fontaine",
    "Hak ederek kazanılan az şey, hak etmeyerek kazanılan az şeyden daha iyidir. -Hz.Muhammed",
    "Ben başarıya asansörle çıkmış hiç kimse görmedim, kesinlikle merdivenlerden çıkmak zorundasınız."
    ]
def bekleYaz(yazı,bekleme,diziAtla=False):
    if not diziAtla: print(yazı,end="")
    else: print(yazı)
    öy.sleep(bekleme)

#İLERDE BİR YIĞIN BETİK
class Oyun:
    def __init__(self):
        self.kazanılanSavaşlar=0
        self.oyuncuGüç=2
        self.oyuncuCan=10
        self.oyuncuCanEnÇok=10
        self.oyuncuKoruma=1.0
        self.oyuncuSavunmaÇarpanı=1.0
        self.oyuncuSaldırıÇarpanı=1.0
        self.oyuncuTabanAğırlık=1.0
        self.ağırlık=0
        self.gelindi=[]
        self.B_AYRAÇ="-"
        self.SAVAŞ_ENDÜŞÜK=0.80
        self.SAVAŞ_ENYÜKSEK=1.20
        self.konum=0
        self.ölü=False
        self.bölümler={}
        self.blm={}
        self.çanta=[]
        self.sözler={"al":self.al, "tut":self.al, "kaldır":self.al, "taşı":self.al,
                     "bırak":self.bırak, "fırlat":self.bırak,
                     "bak": self.incele, "incele":self.incele, "açıkla":self.incele,
                     "oku":self.incele, "gör":self.incele,
                     "çanta":self.çantaAçıkla, "envanter":self.çantaAçıkla,
                     "öl":self.öl, "geber":self.öl,
                     "kuzey":self.kuzey, "k":self.kuzey,
                     "güney":self.güney, "g":self.güney,
                     "doğu":self.doğu, "d":self.doğu,
                     "batı":self.batı, "b":self.batı,
                     "kuzeybatı":self.kuzeybatı, "kb":self.kuzeybatı,
                     "güneybatı":self.güneybatı, "gb":self.güneybatı,
                     "kuzeydoğu":self.kuzeydoğu, "kd":self.kuzeydoğu,
                     "güneydoğu":self.güneydoğu, "gd":self.güneydoğu,
                     "yukarı":self.yukarı, "y":self.yukarı,
                     "aşağı":self.aşağı , "a": self.aşağı,
                     "içeri":self.içeri, "içine":self.içeri, "gir":self.içeri,
                     "dışarı":self.dışarı, "dışına":self.dışarı, "çık":self.dışarı,
                     "git":self.git, "yürü":self.git,
                     "konuş":self.konuş, "söyleş":self.konuş,
                     "saldır":self.saldır, "dal":self.saldır, "savaş":self.saldır, "öldür":self.saldır,
                     "bekle":self.dinlen, "dinlen":self.dinlen, "dur":self.dinlen,
                     "kullan":self.kullan,
                     "baguvix":self.hile,
                     "at":self.bırak #bunu en sona bıraktım.
                     #böylece at diye bir hayvan eklersen onla karışmasın
                     }
        
        self.nesne = {}
        self.nsn = {}
        
        self.yön = {"kuzey":0, "k":0, "güney":1, "g":1,
       "batı":2, "b":2, "doğu":3 , "d":3,
       "kuzeydoğu":4, "kd":4, "güneydoğu":5, "gd":5,
       "kuzeybatı":6, "kb":6, "güneybatı":7, "gb":7,
       "yukarı":8, "y":8, "aşağı":9, "a":9,
       "iç":10, "içine":10, "içeri":10, "giriş":10,
       "dış":11, "dışına":11, "dışarı":11, "çıkış":11
       }

    def oynaNesneEkle(self,ad,nesne):
        if not self.nesne=={}:
            kimlik=max(list(self.nesne.keys()))+1
        else:
            kimlik=0
        self.nesne[kimlik]=nesne
        self.nsn[ad]=kimlik
        self.nesne[kimlik].oyun=self
        self.nesne[kimlik].kimlik=kimlik
        return kimlik

    def bölümeNesneEkle(self,ns,blm):
        self.bölümler[blm].nesneler.append(ns)

    def oynaBölümEkle(self,ad,bölm):
        if self.bölümler=={}:
            kimlik=0
        else:
            kimlik=max(list(self.bölümler.keys()))+1
        self.bölümler[kimlik]=bölm
        self.blm[ad]=kimlik
        self.bölümler[kimlik].oyun=self
        self.bölümler[kimlik].kimlik=kimlik
        return kimlik

    def ağırlıkHesapla(self):
        ağr=0
        for sayı in self.çanta:
            ağr+=self.nesne[sayı].ağırlık
        self.ağırlık=ağr
        return ağr+self.oyuncuTabanAğırlık
    def bırak(self,girdi):
        if not girdi:
            print("Bırakılacak nesne söylenmedi.")
        else:
            for g in girdi:
                bilinmiyor=True
                for sayı in self.nesne:
                    if g in tr.çizelgeTümEklerle(self.nesne[sayı].tümAdlar):
                        if sayı in self.çanta:
                            self.çanta.remove(sayı)
                            self.bölümler[self.konum].nesneler.append(sayı)
                            self.nesne[sayı].oyuncuBıraktı()
                            print(self.nesne[sayı].ad, " bırakıldı")
                            self.bekle()
                        else:
                            print(self.nesne[sayı].ad, " çantada yok.")
                        bilinmiyor=False
                if bilinmiyor:
                    print(g," ne demek bilinmiyor.")

    def kullan(self,girdi):
        if not girdi:
            print("Kullanılacak nesne söylenmedi.")
        else:
            for g in girdi:
                bilinmiyor=True
                for sayı in self.nesne:
                    if g in tr.çizelgeTümEklerle(self.nesne[sayı].tümAdlar):
                        if sayı in self.çanta:
                            self.nesne[sayı].kullan()
                            self.bekle()
                        else:
                            print(self.nesne[sayı].ad, " çantada yok.")
                        bilinmiyor=False
                if bilinmiyor:
                    print(g," ne demek bilinmiyor.")
    def nesneAl(self,x):
        if not x in self.bölümler[self.konum].nesneler:
            print("Burada öyle bir şey yok.")
        else:
            if not self.nesne[x].al:
                print("Onu alamazsın.")
            else:
                self.bölümler[self.konum].nesneler.remove(x)
                self.çanta.append(x)
                self.nesne[x].oyuncuAldı()
                print(self.nesne[x].ad," alındı.")
    def incele(self,girdi):
        if not girdi:
            self.bölümAçıkla(self.konum)
        else:
            for g in girdi:
                bilinmiyor=True
                for sayı in self.nesne:
                    if g in tr.çizelgeTümEklerle(self.nesne[sayı].tümAdlar):
                        if sayı in self.çanta or sayı in self.bölümler[self.konum].nesneler:
                            print(self.nesneİncele(sayı))
                            self.bekle()
                        else:
                            print(g, " ortalıkta yok.")
                        bilinmiyor=False
                if bilinmiyor:
                    print(g," ne demek bilinmiyor.")
    def nesneKonuş(self,s,söz):
        açk=self.nesne[s].konuşma
        if isinstance(açk, str):
            print(söz+" diyor:")
            return açk
        else:
            return "O konuşacağa benzemiyor..."
    def konuş(self,girdi):
        if not girdi:
            print("Kiminle konuşulacağı söylenmedi.")
        else:
            for g in girdi:
                bilinmiyor=True
                for sayı in self.nesne:
                    if g in tr.çizelgeTümEklerle(self.nesne[sayı].tümAdlar):
                        söz=self.nesne[sayı].ad
                        if sayı in self.çanta or sayı in self.bölümler[self.konum].nesneler:
                            print(self.nesneKonuş(sayı,söz))
                            self.bekle()
                        else:
                            print(g, " ortalıkta yok.")
                        bilinmiyor=False
                if bilinmiyor:
                    print(g," ne demek bilinmiyor.")
    def al(self,girdi):
        if not girdi:
            print("Alınacak nesne söylenmedi.")
        else:
            for g in girdi:
                if g in tr.tümOlasıEkleriyle("tümü") or g in tr.tümOlasıEkleriyle("hepsi"):
                    birazVar=False
                    for i in self.bölümler[self.konum].nesneler:
                        if self.nesne[i].al:
                            birazVar=True
                            self.nesneAl(i)
                    if not birazVar:
                        print("Alacak bir şey yok...")
                else:
                    bilinmiyor=True
                    for sayı in self.nesne:
                        if g in tr.çizelgeTümEklerle(self.nesne[sayı].tümAdlar):
                            self.nesneAl(sayı)
                            bilinmiyor=False
                    if bilinmiyor:
                        print(g," ne demek bilinmiyor.")
    def saldırı(self,x):
        if not x in self.bölümler[self.konum].nesneler:
            print("Burada öyle bir şey yok.")
        else:
            #yağının gücü, savunma çarpanı 
            yGüç=self.nesne[x].güç*self.nesne[x].savunmaÇarpanı
            #saldırılacak araç
            oGüç=self.oyuncuGüç*self.oyuncuSaldırıÇarpanı
            anlaşılmadı=True
            while anlaşılmadı:
                print("Neyle saldıracaksın?")
                print("el")
                for s in self.çanta:
                    if self.nesne[s].vuraç==True:
                        print(self.nesne[s].tümAdlar[0])
                grd=tr.küçült(input(">")).split(" ")[0]
                kuşamGüç=0
                if grd in tr.tümOlasıEkleriyle("el"):
                    kuşamGüç=0
                    break
                else:
                    for s in self.çanta:
                        if grd in tr.çizelgeTümEklerle(self.nesne[s].tümAdlar):
                            kuşamGüç+=(self.nesne[s].güç)*self.nesne[s].saldırıÇarpanı
                            print(self.nesne[s].ad," kuşandın.")
                            anlaşılmadı=False
                            break
                if anlaşılmadı:
                    print("Girdi anlaşılmadı, yeniden dene.")
            
            print("Saldırı")
            print(self.B_AYRAÇ*7)
            print("{0:15} {1:5}+{2:5}".format("Senin gücün",round(oGüç,2),round(kuşamGüç,2)))
            print("{0:15} {1:5}".format("Yağının gücü",round(yGüç,2)))
            print(self.B_AYRAÇ*7)
            print("{0:15} {1:5}".format("Senin canın",round(self.oyuncuCan,2)))
            print("{0:15} {1:5}".format("Yağının canı",round(self.nesne[x].can,2)))
            print(self.B_AYRAÇ*7)
            #oyuncunun güçüne vuraç gücü
            while 1:
                yGüç=(self.nesne[x].güç*self.nesne[x].savunmaÇarpanı)*(self.nesne[x].can/self.nesne[x].canEnÇok)
                #güçleri yeniler
                oGüç=(self.oyuncuGüç*self.oyuncuSaldırıÇarpanı)*(self.oyuncuCan/self.oyuncuCanEnÇok)
                oGüç+=kuşamGüç
                
                yumuşakYaz("Sıra sende. ")
                oyuncuZarar=(1/self.nesne[x].koruma)*(oGüç*rastKesir(self.SAVAŞ_ENDÜŞÜK,self.SAVAŞ_ENYÜKSEK))
                yumuşakYaz("Verilen zarar: "+str(round(oyuncuZarar,2)))
                self.nesne[x].can-=oyuncuZarar
                if self.nesne[x].can<=0:
                    yumuşakYaz("Kazandın!")
                    self.kazanılanSavaşlar+=1
                    self.bölümler[self.konum].nesneler.remove(x)
                    self.nesne[x].yokOldu()
                    break
                else:
                    yumuşakYaz("Yağının canı: "+str(round(self.nesne[x].can,2)))
                    yumuşakYaz("Sıra yağıda. ")
                    yağıZarar=(1/self.oyuncuKoruma)*(yGüç*rastKesir(self.SAVAŞ_ENDÜŞÜK,self.SAVAŞ_ENYÜKSEK))
                    yumuşakYaz("Verdiği zarar: "+str(round(yağıZarar,2)))
                    self.oyuncuCan-=yağıZarar
                    if self.oyuncuCan<=0:
                        self.öl(["ÖLÜM!"])
                        break
                    else:
                        yumuşakYaz("Kalan canın: "+str(round(self.oyuncuCan,2)))
                        print(self.B_AYRAÇ*7)
                    
    def savunma(self,x):
        if not x in self.bölümler[self.konum].nesneler:
            print("SORUN: BURADA ÖYLE BİR ŞEY YOK")
        else:
            print("Sana ",self.nesne[x].ad," saldırıyor!")
            #yağının gücü, aldırı çarpanı 
            yGüç=self.nesne[x].güç*self.nesne[x].saldırıÇarpanı
            #saldırılacak araç
            oGüç=self.oyuncuGüç*self.oyuncuSavunmaÇarpanı
            anlaşılmadı=True
            while anlaşılmadı:
                print("Neyle savunacaksın?")
                print("el")
                for s in self.çanta:
                    if self.nesne[s].vuraç==True:
                        print(self.nesne[s].tümAdlar[0])
                grd=tr.küçült(input(">")).split(" ")[0]
                kuşamGüç=0
                if grd in tr.tümOlasıEkleriyle("el"):
                    kuşamGüç=0
                    break
                else:
                    for s in self.çanta:
                        if grd in tr.çizelgeTümEklerle(self.nesne[s].tümAdlar):
                            kuşamGüç+=(self.nesne[s].güç)*self.nesne[s].savunmaÇarpanı
                            print(self.nesne[s].ad," kuşandın.")
                            anlaşılmadı=False
                            break
                if anlaşılmadı:
                    print("Girdi anlaşılmadı, yeniden dene.")
            print("Savunma")
            print(self.B_AYRAÇ*7)
            print("{0:15} {1:5}+{2:5}".format("Senin gücün",round(oGüç,2),round(kuşamGüç,2)))
            print("{0:15} {1:5}".format("Yağının gücü",round(yGüç,2)))
            print(self.B_AYRAÇ*7)
            print("{0:15} {1:5}".format("Senin canın",round(self.oyuncuCan,2)))
            print("{0:15} {1:5}".format("Yağının canı",round(self.nesne[x].can,2)))
            print(self.B_AYRAÇ*7)
            #oyuncunun güçüne vuraç gücü
            oGüç+=kuşamGüç
            while 1:
                yGüç=(self.nesne[x].güç*self.nesne[x].saldırıÇarpanı)*(self.nesne[x].can/self.nesne[x].canEnÇok)
                #güçleri yeniler
                oGüç=(self.oyuncuGüç*self.oyuncuSavunmaÇarpanı)*(self.oyuncuCan/self.oyuncuCanEnÇok)
                oGüç+=kuşamGüç
                
                yumuşakYaz("Sıra yağıda. ")
                yağıZarar=(1/self.oyuncuKoruma)*(yGüç*rastKesir(self.SAVAŞ_ENDÜŞÜK,self.SAVAŞ_ENYÜKSEK))
                yumuşakYaz("Verdiği zarar: "+str(round(yağıZarar,2)))
                self.oyuncuCan-=yağıZarar
                if self.oyuncuCan<=0:
                    self.öl(["ÖLÜM!"])
                    break
                else:
                    yumuşakYaz("Kalan canın: "+str(round(self.oyuncuCan,2)))
                    yumuşakYaz("Sıra sende. ")
                    oyuncuZarar=(1/self.nesne[x].koruma)*(oGüç*rastKesir(self.SAVAŞ_ENDÜŞÜK,self.SAVAŞ_ENYÜKSEK))
                    yumuşakYaz("Verilen zarar: "+str(round(oyuncuZarar,2)))
                    self.nesne[x].can-=oyuncuZarar
                    if self.nesne[x].can<=0:
                        yumuşakYaz("Kazandın!")
                        self.kazanılanSavaşlar+=1
                        self.nesne[x].yokOldu()
                        self.bölümler[self.konum].nesneler.remove(x)
                        break
                    else:
                        yumuşakYaz("Yağının canı: "+str(round(self.nesne[x].can,2)))
                        print(self.B_AYRAÇ*7)       
    def saldır(self,girdi):
        if not girdi:
            print("Saldırılacak nesne söylenmedi.")
        else:
            for g in girdi:
                    bilinmiyor=True
                    for sayı in self.nesne:
                        if g in tr.çizelgeTümEklerle(self.nesne[sayı].tümAdlar):
                            bilinmiyor=False
                            if self.nesne[sayı].saldırılabilir:
                                self.saldırı(sayı)
                            else:
                                print("Ona saldıramazsın.")
                    if bilinmiyor:
                        print(g," ne demek bilinmiyor.")

    def çantaAçıkla(self,girdi):
        print("{0:20} {1:3}/{2:3}".format("Canın:",round(self.oyuncuCan,2),round(self.oyuncuCanEnÇok,2)))
        print("{0:20} {1:3}".format("Gücün:",round(self.oyuncuGüç,2)))
        if self.oyuncuKoruma>1:
            print("%"+str((self.oyuncuKoruma-1)*100)+" daha ÇOK koruma")
        if self.çanta:
            print("Çantanda şunlar var:")
            for n in self.çanta:
                print(self.nesne[n].ad)
        else:
            print("Çantan bomboş.")
    def nesneİncele(self,s):
        açk=self.nesne[s].açk
        if isinstance(açk, str):
            return açk
        else:
            return "Onun önemli bir özelliği görünmüyor."
    def nesneAçıkla(self,s):
        self.nesne[s].oyuncuBaktı()
        açk=self.nesne[s].uzunAd
        if isinstance(açk,str):
            return açk+" "
        else:
            return ""
    def bölümAçıkla(self,b):
        if not b in self.gelindi:
            self.gelindi.append(b)
        print(self.bölümler[self.konum].başlık)
        print(self.B_AYRAÇ*len(self.bölümler[self.konum].başlık))
        yumuşakYaz(self.bölümler[self.konum].açk,80)
        for N in self.bölümler[self.konum].nesneler:
            yumuşakYaz(self.nesneAçıkla(N),80,False)
        print()
    def bekle(self):
        for sayı in self.bölümler[self.konum].nesneler:
            self.nesne[sayı].oyuncuBekledi()
        for sayı in self.çanta:
            self.nesne[sayı].oyuncuBekledi()
    def dinlen(self,girdi):
        ilk=self.oyuncuCan
        self.oyuncuCan+=1
        if self.oyuncuCan>self.oyuncuCanEnÇok:
            self.oyuncuCan=self.oyuncuCanEnÇok
        print("Burada biraz dinlendin. ",self.oyuncuCan-ilk," kadar canın yenilendi.")
        self.bekle()
    def gitSayı(self,yn):
        yenb=self.bölümler[self.konum].çizin[yn]
        if yenb == -1:
            print("O yöne gidemezsin.")
        else:
            if not self.bölümler[yenb].gidilemez:
                self.bölümler[self.konum].oyuncuGitti()
                self.konum=yenb
                self.bölümler[self.konum].oyuncuGeldi()
                self.bölümAçıkla(yenb)
                ağr=round(self.ağırlıkHesapla())
                for gereksiz in range(ağr):
                    self.bekle()
            else:
                print("Oraya gidemezsin: ", self.bölümler[yenb].gidilmemeNedeni)

    def kuzey(self,girdi):
        self.gitSayı(0)
    def güney(self,girdi):
        self.gitSayı(1)
    def batı(self,girdi):
        self.gitSayı(2)
    def doğu(self,girdi):
        self.gitSayı(3)
    def kuzeydoğu(self,girdi):
        self.gitSayı(4)
    def güneydoğu(self,girdi):
        self.gitSayı(5)
    def kuzeybatı(self,girdi):
        self.gitSayı(6)
    def güneybatı(self,girdi):
        self.gitSayı(7)
    def yukarı(self,girdi):
        self.gitSayı(8)
    def aşağı(self,girdi):
        self.gitSayı(9)
    def içeri(self,girdi):
        self.gitSayı(10)
    def dışarı(self,girdi):
        self.gitSayı(11)
    def git(self,girdi):
        if not girdi:
            print("Yön belirlemelisin.")
        else:
            bilinmiyor=True
            for g in girdi:
                for y in self.yön:
                    if g in tr.tümOlasıEkleriyle(y):
                        self.gitSayı(self.yön[y])
                        bilinmiyor=False
            if bilinmiyor:
                print("Gitmek istenen yer anlaşılmadı.")
    def oyunÖzeti(self):
        print(self.B_AYRAÇ*50)
        print(self.B_AYRAÇ*19,"OYUN ÖZETİ",self.B_AYRAÇ*19)
        print(self.B_AYRAÇ*50)
        print("{0:29} {1:20d}".format("Uğranılan yer",len(self.gelindi)))
        print("{0:29} {1:20d}".format("Toplam yer",len(self.bölümler)))
        print("{0:29} {1:20f}".format("Uğranılan yer oranı",round((len(self.gelindi)/len(self.bölümler)),2)))
        print("{0:29} {1:20d}".format("Kazanılan savaşlar",self.kazanılanSavaşlar))
        
    def öl(self,girdi):
        yumuşakYaz("Öldün...",17)
        yumuşakYaz("\""+ seç(ÖLÜM)+ "\"",35)
        self.oyunÖzeti()
        print("{0:29} {1:20}".format("Ölüm yeri",self.bölümler[self.konum].başlık))
        self.ölü=True

    def kazan(self):
        yumuşakYaz("Kazandın!",17)
        yumuşakYaz("\""+ seç(KAZANI)+ "\"",35)
        self.oyunÖzeti()
        self.ölü=True

    def hile(self,girdi):
        yumuşakYaz("Kazandın!",17)
        yumuşakYaz("Hak ederek kazanılan az şey, hak etmeyerek kazanılan az şeyden daha iyidir. -Hz.Muhammed")
        print("\n(Evet, hile yaptığını biliyorum. Ne sandın?)")
        self.ölü=True
    def girdiyiÇalıştır(self,x):
        if x:
            bilinmiyor=True
            girdi=x.split(" ")
            for sözcük in x.split(" "):
                if sözcük in self.sözler:
                    işlev=self.sözler[sözcük]
                    girdi.remove(sözcük)
                    işlev(girdi)
                    bilinmiyor=False
            if bilinmiyor:
                print("Komut anlaşılmadı.")
        else:
            print("Girdi yok.")
    def oyunuÇalıştır(self):
        self.bölümAçıkla(self.konum)
        self.bekle()
        while not self.ölü:
            self.girdiyiÇalıştır(tr.küçült(input(">")))
            

class Nesne:
    def __init__(self):
        #nesnenin alınabilirliği
        self.al=True
        #diğer
        self.vuraç=False
        self.saldırılabilir=True
        
        #altta yazı değerleri
        self.ad=None
        self.tümAdlar=[]
        self.uzunAd=None
        self.açk=None
        self.konuşma=None

        #altta sayı değerleri
        self.güç=0
        self.can=1
        self.canEnÇok=1
        self.koruma=1.0
        self.saldırıÇarpanı=1.0
        self.savunmaÇarpanı=1.0
        self.ağırlık=0.1

        self.saldırganlık=0.0
        self.oyun=None
        self.kimlik=None

    def kullan(self):
        print("Bu nesne kullanılmıyor.")
    def oyuncuBekledi(self):
        "Oyunuc beklediğinde çalıştırılacak betik"
        if self.saldırganlık==1.0:
            self.oyun.savunma(self.kimlik)
        elif self.saldırganlık==0.0:
            pass
        elif self.saldırganlık>=rastgele():
            self.oyun.savunma(self.kimlik)
    def oyuncuAldı(self):
        "Oyuncu bu nesneyi aldığında çalıştırılacak betik"

    def oyuncuBıraktı(self):
        "Oyuncu bu nesneyi bıraktığında çalıştırılacak betik"

    def oyuncuBaktı(self):
        "Oyuncu bu nesneye baktığında çalıştırılacak betik"

    def yokOldu(self):
        "Saldırıda/savunmada yok olursa çalıştırılacak betik"

    
class Bölüm:
    def __init__(self):
        self.başlık="BÖLÜM-BAŞLIĞI"
        self.açk="BÖLÜM-AÇIKLAMASI"
        self.gidilemez=False
        self.gidilmemeNedeni="GİDİLMEME-NEDENİ"
        self.çizin=[
#  k,  g,  b,  d,  kd,  gd,  kb,  gb,  y,  a,  iç, dış
[ -1, -1, -1, -1,  -1,  -1,  -1,  -1, -1, -1,  -1,  -1]
            ]

        self.nesneler=[]
        self.oyun=None
        self.kimlik=None

    def oyuncuGeldi(self):
        "Oyuncu geldiğinde çalıştırılacak betik"
    def oyuncuGitti(self):
        "Oyuncu gittiğinde çalıştırılacak betik"
