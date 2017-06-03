#markov.py
#İlker Işık


from random import choice as seç
from time import time as öğ
belgeAdı="BELGE_ADINI_GİRİN.txt"
HARF="ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZXQ"
KHARF="abcçdefgğhıijklmnoöprsştuüvyzxq"
def temelleştir(yazı):
    çıktı=""
    for i in yazı:
        if i in HARF:
            çıktı+=KHARF[HARF.find(i)]
        elif i == " " or i in KHARF or i in "1234567890":
            çıktı+=i

    return çıktı

class markov:
    def __init__(self,say=1):
        self.zincir={}
        self.TümceBitişi=".!?"
        self.zB=say
        self.akıllıSözcükİşleme=True
        self.gelişigüzelSeçim=True
        self.odaklanma=True
        self.ilerlenecek=None
        self.adıllar={"ben":"sen","benim":"senin","sen":"ben","senin":"benim",
                      "sizin":"bizim","bizim":"sizin","sizler":"bizler",
                      "bizler":"sizler","benle":"senle","senle":"benle",
                      "sizle":"bizle","bizle":"sizle",
                      "siz":"biz","biz":"siz"}
        self.ikinciller=["hocam","efendim","arkadaşım","ve","ya",
                         "mı","mi","mu","mü","da","ne","hangi",
                         "ki","evet","hayır"] #bu sözcüklere diğer sözcüklerden sonra bakılır
    def oku(self,girdi):
        çizelge=[a for a in girdi.split() if a]
        for s,a in enumerate(çizelge):
            try:
                açkıZincir=(a,)
                for sayı in range(1,self.zB):
                    ek=çizelge[s+sayı]
                    if ek:
                        açkıZincir+=(ek,)
            except IndexError:
                break
            if not açkıZincir in self.zincir:
                self.zincir[açkıZincir]=[]
            try:
                ekleme=çizelge[s+self.zB]
            except IndexError:
                break
            if ekleme:
                self.zincir[açkıZincir].append(ekleme)
                ekleme=""
    def yaz(self,tS=1):
        if (not self.odaklanma) or (not self.ilerlenecek):
            başlama=[a for a in self.zincir.keys() if a[0][0].isupper()]
            açkı=seç(başlama)
        if self.odaklanma and self.ilerlenecek:
            açkı=self.ilerlenecek
        süreç=0
        çıktı=[]
        for a in açkı:
            if not (self.odaklanma and self.ilerlenecek):
                çıktı.append(a)
        while süreç<tS:
            try:
                ekleme=seç(self.zincir[açkı])
            except KeyError:
                break
            except IndexError:
                break
            çıktı.append(ekleme)
            açkı=açkı[1:]+(ekleme,)
            if ekleme[-1] in self.TümceBitişi:
                süreç+=1
                if süreç>=tS:
                    break
        """try:
            ekleme=seç(self.zincir[açkı])
        except:
            self.ilerlenecek=None
            return " ".join(çıktı)
        self.ilerlenecek=açkı[1:]+(ekleme,)"""
        self.ilerlenecek=açkı
        return " ".join(çıktı)
    def sonraki(self,girdi):
        olasıAçkılar=[]
        for açkı in self.zincir:
            for a in açkı:
                if temelleştir(a)==temelleştir(girdi):
                    if not self.gelişigüzelSeçim:
                        return self.sonrakiAçkı(açkı)
                    olasıAçkılar.append(açkı)
        if olasıAçkılar:
            return self.sonrakiAçkı(seç(olasıAçkılar))
        else:
            return ""
    def sonrakiAçkı(self,açkı):
        çıktı=[]
        for a in açkı:
            çıktı.append(a)
        while True:
            try:
                ekleme=seç(self.zincir[açkı])
            except KeyError:
                break
            except IndexError:
                break
            çıktı.append(ekleme)
            açkı=açkı[1:]+(ekleme,)
            if ekleme[-1] in self.TümceBitişi:
                break
        self.ilerlenecek=açkı
        return " ".join(çıktı)
    def konuş(self):
        "güncellendi"
        konuş=""
        print("Konuşmadan ayrılmak için CTRL+C basın.")
        while True:
            konuş=input(">").lower()
            yanıt=self.yanıtla(konuş)
            print(yanıt)
    def yanıtla(self,girdi):
        if girdi:
            g=temelleştir(girdi).split()
            ig=[ö for ö in g if (not ö in self.ikinciller and (len(ö)>=2 or ö=="o"))]
            if ig and self.akıllıSözcükİşleme:
                k=seç(ig)
            else:
                if g:
                    k=seç(g)
                else:
                    return self.yaz()
            if self.akıllıSözcükİşleme:
                if k in self.adıllar:
                    k=self.adıllar[k]
            çıktı= self.sonraki(k)
            while not çıktı:
                g.remove(k)
                try:
                    ig.remove(k)
                except ValueError:
                    pass
                if ig:
                    k=seç(ig)
                    çıktı=self.sonraki(k)
                else:
                    if g:
                        k=seç(g)
                        çıktı=self.sonraki(k)
                    else:
                        return self.yaz()
            return çıktı
        else:
            return self.yaz()

if __name__=="__main__":
    with open(belgeAdı) as b:
        yazı=b.read()
    yazı=yazı.replace("\n"," ")
    Markov=markov()
    Markov.oku(yazı)
    Markov.konuş() 
