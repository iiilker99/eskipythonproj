#-*- coding: utf-8 -*-

# Release: İlker IŞIK
# Date: 30.06.2014
# Mail: iiilker99@gmail.com


HARF="ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZXQ"
KHARF="abcçdefgğhıijklmnoöprsştuüvyz"
ÜNLÜLER={"tümü":"aeıioöuü", "kalın":"aıou", "ince":"eiöü", "dar":"ıiuü",
         "geniş":"aeoö", "düz":"aeıi", "yuvarlak": "oöuü"}
HARFVB=HARF+"abcçdefgğhıijklmnoöprsştuüvyz"+" \n\t"
HARFVBN=HARF+"abcçdefgğhıijklmnoöprsştuüvyzxq"+"0123456789 \n\t"

def tümOlasıEkleriyle(sözcük):
    eklerle=[sözcük]
    for ek in ÜNLÜLER["tümü"]:
        eklerle.append(sözcük+ek)
    #ünsüz yumuşaması
    if sözcük[-1]=="p":
        eklerle=eklerle+(tümOlasıEkleriyle(sözcük[0:-1]+"b"))
    elif sözcük[-1]=="ç":
        eklerle=eklerle+(tümOlasıEkleriyle(sözcük[0:-1]+"c"))
    elif sözcük[-1]=="t":
        eklerle=eklerle+(tümOlasıEkleriyle(sözcük[0:-1]+"d"))
    elif sözcük[-1]=="k":
        eklerle=eklerle+(tümOlasıEkleriyle(sözcük[0:-1]+"g"))
        eklerle=eklerle+(tümOlasıEkleriyle(sözcük[0:-1]+"ğ"))
    #kaynaştırma
    elif sözcük[-1] in ÜNLÜLER["tümü"]:
        eklerle=eklerle+(tümOlasıEkleriyle(sözcük+"y"))
        eklerle=eklerle+(tümOlasıEkleriyle(sözcük+"n"))
    eklerle.append(sözcük+"la")
    eklerle.append(sözcük+"le")
    return eklerle
def çizelgeTümEklerle(çz):
    çıktı=[]
    for sözcük in çz:
        çıktı=çıktı+tümOlasıEkleriyle(sözcük)
    return çıktı
def küçült(yazı):
    çıktı=""
    for i in yazı:
        if i in HARF:
            çıktı+=KHARF[HARF.find(i)]
        else:
            çıktı+=i

    return çıktı

def büyüt(yazı):
    çıktı=""
    for i in yazı:
        if i in KHARF:
            çıktı+=HARF[KHARF.find(i)]
        else:
            çıktı+=i

    return çıktı

            
        
