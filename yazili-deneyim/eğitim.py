#-*- coding: utf-8 -*-

# Release: İlker IŞIK
# Date: 30.06.2014
# Mail: iiilker99@gmail.com

#EĞİTİM BÖLÜMÜ
from ana import *

oyun=Oyun()
oyun.oyuncuGüç=1

b1=Bölüm()
b1.başlık="Eğitim: Yönler"
b1.açk="Oyuna hoşgeldin! Bu bir yazı tabanlı oyundur. Oyuncu, oyunu yazılı komutlar vererek oynanır. Altta \">\" ile başlayan yere Türkçe komutlar gireceksin. Şimdi, 2. bölüme geçmek için doğuya gitmen gerekiyor. "+'Bunun için "doğuya git" ya da "doğu" ya da kısaca "d" yaz.'
#             k,  g,  b,  d,  kd,  gd,  kb,  gb,  y,  a,  iç, dış
b1.çizin=[ -1, -1, -1,  1,  -1,  -1,  -1,  -1, -1, -1,  -1,  -1]
b2=Bölüm()
b2.başlık="Eğitim: Çanta"
b2.açk="Güzel. Buraya gelmeyi başardın. Şimdi diğer konumuz: Çanta, nesneler. Bu oyunda çevrendeki nesnelerden kimilerini alabilirsin. Aldığın nesneler sana kimi üstünlükler, yetkiler sağlayabilir ya da onları silah olarak kullanabilirsin. Çantanda neler olduğunu görmek ve adamının özelliklerine bakmak için \"çanta\" yaz. Eğitimini sürdürmek için kuzeye gitmelisin."
b2.çizin=[ 2, -1, -1, -1,  -1,  -1,  -1,  -1, -1, -1,  -1,  -1]


class Savaş(Bölüm):
    def __init__(self):
        super().__init__()
        self.başlık="Eğitim: Dövüş"
        self.açk="Oyunda tehlikeler de yok değil. Yaşayabilmek için savaşman gerekecek."+"Oyunda dövüşler şöyle: Senin de, düşmanının da bir gücü vardır. Ayrıca ikinizden birinin "+"saldırıda ya da savunmada kazandığı ek gücü olabilir. Her iki tarafın da canları azaldıkça "+"verecekleri zarar da azalır. Aynı zamanda bir silah kullanarak gücünü arttırabilirsin."
        #             k,  g,  b,  d,  kd,  gd,  kb,  gb,  y,  a,  iç, dış
        self.çizin=[ -1,  -1, -1, -1,   -1,  -1,  -1,  -1, -1, -1,  -1,   -1]
        self.gidilemez=True
        self.gidilmemeNedeni="Kapı kilitli. "
    def oyuncuGeldi(self):
        try: oyun.çanta.remove(oyun.nsn["açkı"])
        except: pass

b4=Bölüm()
b4.başlık="Eğitim: Dinlen"
b4.açk= "Kurta olan dövüşten sonra artık güvenli bir yerdesin. Ancak dövüşte canın azaldı. "+'Öğrendiğin gibi, çantandan canını görebilirsin. Şimdi "dinlen" yazarak biraz dinlen. Böylelikle canının bir bölümü yenilenir.'+" Ardından kuzeye git."
b4.çizin=[ 4, -1, -1, -1,  -1,  -1,  -1,  -1, -1, -1,  -1,  -1]
class Son(Bölüm):
    def __init__(self):
        super().__init__()
        self.başlık="Eğitim bitti"
        self.açk="Eğitimini bitirdin."
    def oyuncuGeldi(self):
        self.oyun.kazan()
        
oyun.oynaBölümEkle("yönler",b1) #0
oyun.oynaBölümEkle("çanta",b2) #1
oyun.oynaBölümEkle("dövüş",Savaş()) #2
oyun.oynaBölümEkle("dinlen",b4) #3
oyun.oynaBölümEkle("son",Son())

class Açkı(Nesne):
    def __init__(self):
        super().__init__()
        self.saldırılabilir=False
        #altta yazı değerleri
        self.ad="Bir anahtar"
        self.tümAdlar=["açkı","açak","anahtar"]
        self.uzunAd="Yerde bir anahtar görünüyor. Onu \"anahtarı al\" yazarak alabilirsin. Anahtarı incelemek için \"anahtarı incele\" yazabilirsin."
        self.açk="Sanırım bu anahtar bir yere ait. Alsam iyi olacak"
        self.konuşma=None
        
    def oyuncuAldı(self):
        oyun.bölümler[2].gidilemez=False
    def oyuncuBıraktı(self):
        oyun.bölümler[2].gidilemez=True

class Bıçak(Nesne):
    def __init__(self):
        super().__init__()
        self.vuraç=True
        self.güç=2
        self.saldırıÇarpanı=1.5
        self.ad="Bıçak"
        self.tümAdlar=["bıçak"]
        self.uzunAd="Burada silah olarak kullanabileceğin bir bıçak var. Alsan iyi olur."
class Kurt(Nesne):
    def __init__(self):
        super().__init__()
        self.al=False
        self.ad="Kurt"
        self.tümAdlar=["kurt"]
        self.uzunAd="Burada bir kurt var. Eğitimi sürdürmek için bu kurtu öldürmelisin. \"kurta saldır\" yazarak kurta saldırabilirsin."
        self.can=5
        self.canEnÇok=5
        self.güç=2
        self.saldırıÇarpanı=1.5
    def yokOldu(self):
        self.oyun.konum=3
        self.oyun.gelindi.append(3)
        self.oyun.incele([])
        
oyun.bölümeNesneEkle(oyun.oynaNesneEkle("açkı",Açkı()),1)
oyun.bölümeNesneEkle(oyun.oynaNesneEkle("bıçak",Bıçak()),2)
oyun.bölümeNesneEkle(oyun.oynaNesneEkle("kurt",Kurt()),2)

oyun.oyunuÇalıştır()
