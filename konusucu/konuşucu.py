#Markov zincirleriyle konuşan yazılım için arayüz...
#İlker Işık

from tkinter import *
from markov import *
from sys import exit as çık
from time import strftime
from glob import glob

BİLGİ=["Bilgi",("Markov Konuşucusu\n"+
                    "Markov zincirlerini kullanarak belli bir yazıyı temel "+
                    "alarak konuşabilen bir yazılım. Değişik metinlerden "+
                            "yararlanılabilir.\nYapım: İlker IŞIK\n2014")]
ASİ=["Akıllı Sözcük İşleme",("Bu basit özellik, yazılımın sözcükleri doğru\n"+
                             "biçimde yorumlamasını sağlar.\n"+
                             "Adımsıları çıkarmak, adılları düzeltmek\n"+
                             "gibi işlevleri vardır. Üstelik yazılımın\n"+
                             "yanıtlama hızında da neredeyse hiç fark yapmaz.\n"+
                             "\nBunu kapatmanızın tek nedeni gelişmiş bir \n"+
                             "kullanıcı olup yazılımı ayıklamak istemeniz olabilir.\n")]
GGS=["Gelişigüzel Seçim","""Bu özellik bir sözcüğe verilecek yanıtın nasıl
seçileceğını belirler. Kapalıysa, verilebilecek ilk
yanıt verilir; açıksa tüm verilebilecek yanıtlar
toplanıp gelişigüzel seçilen bir yanıt verilir.

Bu özellik, her ne kadar yazılımı daha eğlenceli
kılsa da hızı yaklaşık 25 kat düşürmektedir.
Buna karşın yazılım sözcük başına 1 saniyeden
az bekletmektedir."""]

KO=["Konuya odaklanma","""Bu açıkken, bilgisayar sizi yanıtladığında, bilgisayarın sözünü sürdürmesini istiyorsanız hiçbir şey yazmadan ileterek ("Enter" düğmesi) bilgisayarın sözünü sürdürmesini sağlayabilirsiniz."""]
class Uyg(Frame):
    def __init__(self,yazı,zS,abi=None):
        Frame.__init__(self,abi)
        self.grid()
        self.hazırla()
        self.arkadaşAdı="Bilgisayar"
        self.son=0
        self.geçmişGirdiler=[]
        self.geçmişGirdiU=10
        self.sonYanıt=""
        self.Markov=markov(zS)
        self.Markov.oku(yazı)
    def hazırla(self):
        self.master.title("Markov Konuşucusu")

        self.seçke=Menu(self)
        ayarlarS=Menu(self.seçke,tearoff=0)
        ayarlarS.add_command(label="Konuşmanın tümünü kopyala",
                             command=self.kopyala)
        ayarlarS.add_command(label="Konuşma geçmişini temizle",
                             command=self.temizle)
        ayarlarS.add_separator()
        self.asi=IntVar()
        self.asi.set(1)
        ayarlarS.add_checkbutton(label="Akıllı sözcük İşleme",variable=self.asi, \
                                 onvalue=1,offvalue=0)
        self.ggs=IntVar()
        self.ggs.set(1)
        ayarlarS.add_checkbutton(label="Gelişigüzel Seçim",variable=self.ggs, \
                                 onvalue=1,offvalue=0)
        self.ko=IntVar()
        self.ko.set(1)
        ayarlarS.add_checkbutton(label="Konuya odaklanma",variable=self.ko, \
                                 onvalue=1,offvalue=0)
        ayarlarS.add_separator()
        ayarlarS.add_command(label="Belge/Zincir seçimi",
                             command=self.ayarla)
        ayarlarS.add_command(label="Çıkış",command=self.master.destroy)
        self.seçke.add_cascade(label="Ayarlar",menu=ayarlarS)
        yardımS=Menu(self.seçke,tearoff=0)
        yardımS.add_command(label="Akıllı Sözcük İşleme",command=lambda: self.bilgi(ASİ))
        yardımS.add_command(label="Gelişigüzel Seçim",command=lambda: self.bilgi(GGS))
        yardımS.add_command(label="Konuya odaklanma",command=lambda: self.bilgi(KO))
        yardımS.add_separator()
        yardımS.add_command(label="Bilgi",command=lambda: self.bilgi(BİLGİ))
        self.seçke.add_cascade(label="Yardım",menu=yardımS)

        self.master.config(menu=self.seçke)
        
        self.yazı=Text(self.master,width=90,height=30)
        self.yazı.tag_config("kızıl",foreground="red")
        self.yazı.tag_config("yeşil",foreground="green")
        self.yazı.tag_config("mavi",foreground="blue")
        self.yazı.insert(INSERT,strftime("Konuşma başladı. Saat %H:%M, tarih %d.%m.%y \n")+"Kullanılan belge: "+belgeAdı+"\nZincir başına sözcük sayısı: "+str(ZincirS)+"\n\n","kızıl")
        self.yazı.config(state=DISABLED)
        
        self.yazı.grid(row=0,column=0,columnspan=4,sticky="EW")

        self.durumYazı=StringVar()
        Label(self.master,textvariable=self.durumYazı,bg="blue",fg="white",
              anchor="w").grid(column=0,row=1,columnspan=4,sticky="EW")
        self.durumYazı.set("Konuşmaya başlamak için iletinizi aşağıya yazınız. Konuşmaya bilgisayarın başlamasını isterseniz hiçbir şey yazmadan iletebilirsiniz.")
        
        self.girdi=Entry(self.master,width=90)
        self.girdi.grid(row=2,column=0,columnspan=3)
        self.girdi.bind("<Return>",self.gireBas)
        self.girdi.bind("<Up>",self.yukarı)
        self.girdi.bind("<Down>",self.aşağı)

        Button(self.master,text="İlet",command=self.iletim,relief=GROOVE,width=30).grid(row=2,column=3)
        Button(self.master,text="Benim yerime bilgisayar yanıtlasın",command=self.bilgisayarYanıtlasın,bg="green",fg="white",relief=GROOVE).grid(row=3,column=0)
        Button(self.master,text="Çıkış",command=self.master.destroy,bg="red",fg="white",relief=GROOVE).grid(row=3,column=3)
        self.grid_columnconfigure(0,weight=1)
        self.master.resizable(False,False)

        self.master.focus_force()
        self.girdi.focus_set()
        self.girdi.selection_range(0,END)
    def yukarı(self,e):
        ş=self.girdi.get()
        s=""
        try:
            s=self.geçmişGirdiler[self.geçmişGirdiler.index(ş)-1]
        except ValueError:
            try:
                s=self.geçmişGirdiler[-1]
                self.geçmişGirdiler.append(ş)
                if len(self.geçmişGirdiler)>self.geçmişGirdiU:
                    self.geçmişGirdiler=self.geçmişGirdiler[1:]
            except IndexError:
                return
        except IndexError:
            return #bu boş return komutları işlevden çıkarır
        self.girdi.delete(0,END)
        self.girdi.insert(END,s)
    def aşağı(self,e):
        ş=self.girdi.get()
        s=""
        try:
            s=self.geçmişGirdiler[self.geçmişGirdiler.index(ş)+1]
        except ValueError:
            return
        except IndexError:
            return
        self.girdi.delete(0,END)
        self.girdi.insert(END,s)
    def gireBas(self,e):
        self.iletim()
    def bilgisayarYanıtlasın(self):
        self.girdi.delete(0,END)
        self.girdi.insert(END,self.Markov.yanıtla(self.sonYanıt))
    def iletim(self):
        ileti=self.girdi.get()
        self.geçmişGirdiler.append(ileti)
        if len(self.geçmişGirdiler)>self.geçmişGirdiU:
            self.geçmişGirdiler=self.geçmişGirdiler[1:]
        self.Markov.akıllıSözcükİşleme=self.asi.get()
        self.Markov.gelişigüzelSeçim=self.ggs.get()
        self.Markov.odaklanma=self.ko.get()
        self.durumYazı.set(self.arkadaşAdı+" yazıyor...")
        if ileti:
            self.yazıEkleTakı("Sen: ","yeşil")
            self.yazıEkle(ileti+"\n")
        self.girdi.delete(0,END)
        self.master.update()
        yanıt=self.Markov.yanıtla(ileti)
        self.yazıEkleTakı(self.arkadaşAdı+": ","mavi")
        self.sonYanıt=yanıt
        self.yazıEkle(yanıt+"\n")
        self.durumYazı.set(strftime("Son alınan ileti saat %H:%M 'de, tarih %d.%m.%y"))
        self.girdi.focus_set()
    def yazıEkle(self,girdi):
        self.yazı.config(state=NORMAL)
        self.yazı.insert(END,girdi)
        self.yazı.see(END)
        self.yazı.config(state=DISABLED)
    def yazıEkleTakı(self,girdi,t):
        self.yazı.config(state=NORMAL)
        self.yazı.insert(END,girdi,t)
        self.yazı.see(END)
        self.yazı.config(state=DISABLED)
    def bilgi(self,b):
        messagebox.showinfo(b[0],b[1])
    def kopyala(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.yazı.get(1.0,END)+"\nMarkov Konuşucusu - İlker IŞIK - 2014")
    def temizle(self):
        self.yazı.config(state=NORMAL)
        self.yazı.delete(1.0,END)
        self.yazı.insert(END,strftime("Konuşma geçmişi temizlendi... Saat %H:%M, tarih %d.%m.%y \n")+"Kullanılan belge: "+belgeAdı+"\nZincir başına sözcük sayısı: "+str(ZincirS)+"\n\n","kızıl")
        self.yazı.config(state=DISABLED)
    def ayarla(self):
        self.master.destroy()
        başlangıç(False,Tk())
        
class başlangıç(Frame):
    def __init__(self,ilk=True,abi=None):
        Frame.__init__(self,abi)
        self.belgeler=[x[2:] for x in glob("./*.txt")]
        ilkBelge=""
        ilkZS=0
        if ".\\konuşucu.ayarlar" in glob("./*.ayarlar"):
            with open("konuşucu.ayarlar") as ayrB:
                ayar=ayrB.read().split("\n")
            ilkBelge=ayar[0]
            ilkZS=int(ayar[1])
            if ilk and ilkBelge in self.belgeler:
                self.master.destroy()
                UygBaşlat(ilkBelge,ilkZS)
                return
                
        
        self.grid()
        self.master.title("Markov Konuşucusu Ayarlar")
        Label(self.master,text="Kullanılacak belgeyi seçiniz:").grid(row=0,column=0)
        self.çs=Listbox(self.master,selectmode=SINGLE,width=30)
        if not self.belgeler:
            self.bilgi(["Sorun","Yazılımın bulunduğu konumda hiç .txt belgesi yok.\nYazılımın çalışması için .txt uzantılı bir belge gereklidir.\nYazılım kapatılacak."])
            self.master.destroy()
        for s,b in enumerate(self.belgeler):
            self.çs.insert(s,b)
            if b==ilkBelge:
                self.çs.selection_set(s)
        if not self.çs.curselection():
            self.çs.selection_set(0)
        self.çs.grid(row=1,column=0,columnspan=2)
        Label(self.master,text="Zincir başına düşen sözcük sayısı:").grid(column=0,row=2)
        self.zS=DoubleVar()
        self.zS.set(ilkZS if ilkZS else 2)
        Scale(self.master,variable=self.zS,orient=HORIZONTAL,from_=1,to=5).grid(row=3,column=0)
        Button(self.master,relief=GROOVE,text="Bu nedir?",command=lambda: self.bilgi(["Zincir başına düşen sözcük sayısı","Bu değer bir zincirde kaç tane sözcüğün bulunacağıdır.\nDaha düşük değerler gelişigüzelliği arttırırken\nyüksek değerler gelişigüzelliği düşürür."])).grid(row=3,column=1)
        Button(self.master,relief=GROOVE,text="Başlat",command=self.başlat).grid(row=4,column=0,columnspan=2)

        self.master.focus_force()
        self.çs.focus_set()
    def bilgi(self,b):
        messagebox.showinfo(b[0],b[1])
    def başlat(self):
        ad=(self.belgeler[self.çs.curselection()[0]])
        sy=int(self.zS.get())
        self.master.destroy()
        with open("konuşucu.ayarlar","w") as belge:
            belge.write(ad+"\n"+str(sy))
            
        UygBaşlat(ad,sy)
        
def UygBaşlat(bA,zS):
    global belgeAdı,ZincirS
    belgeAdı,ZincirS=bA,zS
    with open(bA) as belge:
        yazı=belge.read()
    yazı=yazı.replace("\n"," ")
    uyg=Uyg(yazı,zS,Tk())
    uyg.mainloop()
if __name__=="__main__":
    """with open(belgeAdı) as b:
        yazı=b.read()
    yazı=yazı.replace("\n"," ")
    u=Uyg()
    u.Markov=markov()
    u.Markov.oku(yazı)
    u.mainloop()"""
    başlangıç(True,Tk())

