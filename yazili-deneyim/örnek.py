#-*- coding: utf-8 -*-

# Release: İlker IŞIK
# Date: 30.06.2014
# Mail: iiilker99@gmail.com


#İLK ÖRNEK
from ana import *
print("AMACIN:")
print("Köye ulaşmak")
oyun=Oyun()
blm1=Bölüm()
blm1.başlık="Bataklık"
blm1.açk="""Pis bir bataklığın yanındasın. Kuzeyde bir eski ev var. Güneye doğru bir çıkış, ardından köy yer alıyor.""",
"Geri kalan her yer bataklık."
#             k,  g,  b,  d,  kd,  gd,  kb,  gb,  y,  a,  iç, dış
blm1.çizin=[  1,  3, -1, -1,  -1,  -1,  -1,  -1, -1, -1,  -1,  -1]
oyun.oynaBölümEkle("bataklık",blm1)#0
class Ev(Bölüm):
    def __init__(self):
        super().__init__()
        self.başlık="Terk edilmiş ev"
        self.açk="""Kapıyı açkıyla açtın. Evin içine girdin. Burası terk edilmişe benziyor. Çıkış güneyde. Kuzeydoğuda bir oda daha var"""
        #             k,  g,  b,  d,  kd,  gd,  kb,  gb,  y,  a,  iç, dış
        self.çizin=[ -1,  0, -1, -1,   2,  -1,  -1,  -1, -1, -1,  -1,   0]
        self.gidilemez=True
        self.gidilmemeNedeni="Kapı kilitli. "
    def oyuncuGeldi(self):
        try: oyun.çanta.remove(oyun.nsn["açkı"])
        except: pass
        self.açk="""Terk edilmiş evdesin.. Çıkış güneyde. Kuzeydoğuda bir oda daha var"""
        self.gidilemez=False

oyun.oynaBölümEkle("ev",Ev())#1

blm2=Bölüm()
blm2.başlık="Boş oda"
blm2.açk="Bu odada da kimse yok. Yanlızca derin bir sessizlik... Çıkış güneybatıda."
#             k,  g,  b,  d,  kd,  gd,  kb,  gb,  y,  a,  iç, dış
blm2.çizin=[ -1, -1, -1, -1,  -1,  -1,  -1,  1, -1, -1,  -1,  1]
oyun.oynaBölümEkle("oda",blm2)#2

blm2=Bölüm()
blm2.başlık="Bataklığın çıkışı"
blm2.açk="Burada bataklık bitmeye başlıyor. Güneyde de bir köy yer alıyor. Geri kalan her yer bataklık."
#             k,  g,  b,  d,  kd,  gd,  kb,  gb,  y,  a,  iç, dış
blm2.çizin=[  0,  4, -1, -1,  -1,  -1,  -1,  1, -1, -1,  -1,  1]
oyun.oynaBölümEkle("bataklık-çıkışı",blm2)

class Köy(Bölüm):
    def __init__(self):
        super().__init__()
        self.başlık="Köy"
        self.açk="""Köye geliyorsun. İnsanlar seni sevinçle karışılıyor!"""
        #             k,  g,  b,  d,  kd,  gd,  kb,  gb,  y,  a,  iç, dış
        self.çizin=[ -1,  -1, -1, -1, -1,  -1,  -1,  -1, -1, -1,  -1,  -1]
    def oyuncuGeldi(self):
        self.oyun.kazan()

oyun.oynaBölümEkle("köy",Köy())
"""
# -1 yok demektir
#  k,  g,  b,  d,  kd,  gd,  kb,  gb,  y,  a,  iç, dış
[  1, -1, -1, -1,  -1,  -1,  -1,  -1, -1, -1,  -1,  -1],#0
[ -1,  0, -1, -1,  -1,  -1,  -1,  -1, -1, -1,  -1,   0]#1
"""
class Açkı(Nesne):
    def __init__(self):
        super().__init__()
        #nesnenin alınabilirliği
        #self.al=True
        self.karşıt=False
        self.saldırılabilir=False
        #altta yazı değerleri
        self.ad="Bir açkı"
        self.tümAdlar=["açkı","açak","anahtar"]
        self.uzunAd="Burada bir açkı var."
        self.açk="Bu açkı bir evin, sanırım."
        self.konuşma=None
        
    def oyuncuAldı(self):
        oyun.bölümler[1].gidilemez=False
    def oyuncuBıraktı(self):
        oyun.bölümler[1].gidilemez=True
    
class Kurt(Nesne):
    def __init__(self):
        super().__init__()
        self.al=False
        self.ad="Kurt"
        self.tümAdlar=["kurt"]
        self.uzunAd="Bir kurt görünüyor..."
        self.konuşma="Biliyor musun, bende ne var?"
        self.can=10
        self.canEnÇok=10 #ÇOK ÖNEMLİ!
        self.güç=2
        self.saldırıÇarpanı=1.5
        self.saldırganlık=1.0
class Bıçak(Nesne):
    def __init__(self):
        super().__init__()
        self.vuraç=True
        self.güç=1
        self.ad="Paslı bıçak"
        self.tümAdlar=["bıçak"]
        self.uzunAd="Paslı bir bıçak görüyorum."
        self.açk="Bıçak, paslı, kirli, eski yine de keskin."

class Yelek(Nesne):
    def __init__(self):
        super().__init__()
        
        #altta yazı değerleri
        self.ad="Yelek"
        self.tümAdlar=["yelek","giysi","giyecek"]
        self.uzunAd="Burada bir yelek var."
        self.açk="Bu yelek sağlam görünüyor."
        self.konuşma=None
        
    def oyuncuAldı(self):
        oyun.oyuncuKoruma+=1
    def oyuncuBıraktı(self):
        oyun.oyuncuKoruma-=1
        
oyun.bölümeNesneEkle(oyun.oynaNesneEkle("açkı",Açkı()),0)
oyun.bölümeNesneEkle(oyun.oynaNesneEkle("kurt",Kurt()),3)
oyun.bölümeNesneEkle(oyun.oynaNesneEkle("bıçak",Bıçak()),1)
oyun.bölümeNesneEkle(oyun.oynaNesneEkle("yelek",Yelek()),2)

oyun.oyunuÇalıştır()
