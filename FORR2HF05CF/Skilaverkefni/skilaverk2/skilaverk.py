import csv
import time
import sys
from klasi import Verkalydsfelag
    
def opnaSkra(): # fall sem opnar skránna les með delimiternum , gerir object með upplýsingum starfsmanns og setur allt í lista
    with open("verkalydsfelag.csv","r",newline="",encoding="utf-8") as f: 
        reader = csv.reader(f,delimiter=",")
        listi = []
        starfsmannalisti = []
        for x in reader:
            listi.append(x)
        for x in listi:
            starfsmannalisti.append(Verkalydsfelag(x[0],x[1],x[2],x[3]))
    return starfsmannalisti
def skifSkra(starfsmannalisti): # skrifar allar nýju upplýinganar um starfsmennina í csv skránna
    with open("verkalydsfelag.csv","w",newline="",encoding="utf-8") as f:
        skrifari = csv.writer(f,delimiter=",")
        for x in starfsmannalisti:
            skrifari.writerow([x.nafn,x.felagsnumer,x.laun,x.kennitala])
            
def nyrMedlimur(nafn,felagsnumer,laun,kennitala): # fall sem tekur inn upplýsingar um meðlim og setur það í listann
    starfsmannalisti.append(Verkalydsfelag(nafn,felagsnumer,laun,kennitala))

def eydaMedlimi(felagsnumereyda): # fall sem tekur inn félagsnumer á starfsmanni og eyðir honum úr listanum
    for x in starfsmannalisti:
        if x.felagsnumer == felagsnumereyda:
            print(x.nafn," hefurverið eitt")
            starfsmannalisti.remove(x)
            

def breytaMedlim(felagsnumerbr,nafn,felagsnumer,laun,kennitala): # fall sem tekur inn felagsnúmer starfsmanns og svo nýjar upplýsingar um hann og breytir svo starfsmanni og set í lista
    for x in starfsmannalisti:
        if x.felagsnumer == felagsnumerbr:
            x.nafn = nafn
            x.felagsnumer = felagsnumer
            x.laun = laun
            x.kennitala = kennitala
def prentaVerkalydsfelag(): # preti upplýsingar um alla starfsmenn í verkalýðsfélaginu
    for x in starfsmannalisti:
        x.prenta_upplysingar_um_medlim()
def nafnoglaun(): # prenti út nafn starfsmanna og laun þeirra
    for x in starfsmannalisti:
        print("Nafn: ",x.nafn," Laun: ",x.laun)    
def heildarskattar(): # prenti út heildar skatt allrastarfsmanna
    skattur = 0
    for x in starfsmannalisti:
        skattur = skattur + int(x.skatt())
    return str(skattur)+" kr"
def arseydsla(): # reikna út hvað félagið eyðir á ári í laun
    heildarlaun = 0
    for x in starfsmannalisti:
        heildarlaun = heildarlaun + (int(x.laun))*12
    return heildarlaun
   


on = True
while on == True:
    print("(1) Opna Skrá")
    print("(2) Skrifa Skrá")
    print("(3) Nýr Meðlimur")
    print("(4) Eyða Meðlimi")
    print("(5) Breyta meðlimi")
    print("(6) Prenta Verkalydsfélag")
    print("(7) Nafn og Laun")
    print("(8) heildarskattur")
    print("(9) Heildarlaun")
    print("(0) Loka")
    val=int(input("hvað viltu gera? "))
    if val==1:
        try:
            starfsmannalisti = opnaSkra()
            print("Skrá hefur verið opnuð")
        except:
            print("einhvað fór rangt skrá opnaðist ekki")
    elif val==2:
        try:
            skifSkra(starfsmannalisti)
        except:
            print("einhvað fór rangt skráinn hefur ekki vistast")
            print(sys.exc_info()[0])
    elif val==3:
        nafn = input("sláðu inn nafn: ")
        felagsnumer = input("sláðu inn felagsnúmer: ")
        laun = input("sláðu inn laun: ")
        kennitala = input("sláðu inn kennitölu: ")
        nyrMedlimur(nafn,felagsnumer,laun,kennitala)
        print(nafn," hefur verið bætt við")
    elif val==4:
        eyda = input("Sláðu inn félagsnúmer á starfsmanni sem á að eyða: ")
        eydaMedlimi(eyda)
    elif val==5:
        felagsnumerbr = input("Sláðu inn félagsnúmer á starfsmanni sem á að breyta: ")
        nafn = input("sláðu inn nafn: ")
        felagsnumer = input("sláðu inn felagsnúmer: ")
        laun = input("sláðu inn laun: ")
        kennitala = input("sláðu inn kennitölu: ")
        breytaMedlim(felagsnumerbr,nafn,felagsnumer,laun,kennitala)
    elif val==6:
        prentaVerkalydsfelag()
    elif val==7:
        nafnoglaun()
    elif val==8:
        print("Heildarskattur allra starfsmanna er: ",heildarskattar())
    elif val==9:
        print("fyrirtækið notar",arseydsla(),"í laun á ári")
    elif val==0:
        lokaval = input("ertu viss um að þú viljir hætta ja eða nei: ")
        lokaval = lokaval.lower()
        if lokaval == "ja":
            on=False
    





