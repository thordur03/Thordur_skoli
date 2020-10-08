# Þórður Ingi Sigurjónsson
# 5.10.2020
import random # importa random library


class Verkefni_2: # Klassin Verkefni 2
    def __init__(self,nafn): # tek inn færibreytuna Nnafn
        self.nafn = nafn
    
    def __str__(self): # skrifa hvað klassinn gerir og hvað notendi heitir
        return "Þetta er klassinn verkefni_2 og hann getur fundið aðrahverja tölu fundið tölur með 5 og skrifað stjörnur og þú heitir "+self.nafn
    
    def onnurhver(listi): # fall sem velur aðrahverja tölu í lista
        teljari = 0 # geri teljara og lista
        listi_ananrhver = []
        for x in listi: # fer í gegnum listann
            teljari += 1 # plúsa teljarann
            if teljari%2 == 0: # ef teljari er ekki oddatala bætir hún í listann
                listi_Ananrhver.append(x) # appenda tölunni í nýja listann
        return listi_ananrhver # returna nýja listanum

    def finnatolu(listi): # fall sem finnur töluna 5 í intiger í lista
        fimm_Listi = [] # geri lista fyrir tölunar með fimm
        for x in listi: # fer í gegnum listann
            if "5" in str(x): # Breyti x í string og nota in til að sjá hvort 5 sé í tölunni 
                fimm_Listi.append(int(x)) # ef talan er með fimm bæti ég henni í listann
        return fimm_Listi # returna nýja listanum

    def stjornur(listi): # geri fall fyrir stjörnur
        for x in listi: # fer í gengum listann
            stjornu_strengur = "" # geri tóman streng
            for y in range(x): # bæti við hve mörgum stjörnum stakið í listanum segir
                stjornu_strengur +="*"
            print(stjornu_strengur) # prenti stjörnunar




def kasta_pening(): # geri fall sem notar randint til að velja milli 1 eða tveir og skila út annaðhvort True eða False
    kast = random.randint(1,2)
    if kast == 1:
        return True
    if kast == 2:
        return False


on = True # geri breytu fyrir valmynd
while on == True: # aðal Valmynd
    print("(1) Kasta pening") 
    print("(2) Prenta upplýsingar Klasa")
    print("(3) Önnur hver tala")
    print("(4) Finna tölur með 5")
    print("(5) stjörnur")
    print("(0) Hætta við")
    try: # nota try til að biðja notenda um tölu milli 0 og 5
        val=int(input("hvað viltu gera? ")) # ef það er ekki 0 til 5 setur það val í -1 svo forritið crashi ekki og segir notenda hvað hann gerði vitlaust
        if val != 1 and val != 2 and val != 3  and val != 4 and val != 5 and val != 0:
            raise ValueError
    except: # ef notendi gerir ekki tölu milli 1 og 4 
        val = -1
        print("þú verður að slá inn tölu milli 0-5")
    if val==1:
        kasta = True # set kasta á true fyrir valmyndina
        lodna = 0 # geri færibreytu til að telja hversu oft lodna og skjaldamerki
        skjald = 0
        while kasta == True: #valmynd til að kasta pening
            print("(1) kasta pening")
            print("(0) hætta")
            try: 
                val=int(input("hvað viltu gera? ")) # tek inn tölu milli 1 og 0
                if val != 1 and val != 0: # ef talan er ekki 1 eða 0 þá rasar það errori
                    raise ValueError
            except: # ef það er ekki 1 eða 0 setur það val í -1 svo forritið crashi ekki og segir notenda hvað hann gerði vitlaust
                print("þú verður að slá inn tölu milli 0-1")
                val = -1
            if val==1: 
                kast = kasta_pening() # kastar peningnum
                if kast == True: # ef fallið skilar True þá er það Skjaldamerki en ef Fasle er það Lodna og telur hve oft hvað kemur
                    print("Skjaldamerki")
                    skjald += 1
                elif kast == False:
                    lodna += 1
                    print("Loðna")
            elif val==0:
                if lodna > 0 or skjald > 0: # að lokum sýnir það hve oft hvað kom
                    print("hve oft hver hlið kom upp")
                    print("loðna: ",lodna)
                    print("skjaldamerki: ",skjald)
                kasta = False
    elif val==2:
        try:
            nafn = input("Sláðu inn nafn: ") # bið um nafn og set það í klasann og prenti __str__ fallið í klasanum
            klasi = Verkefni_2(nafn)
            print(klasi.__str__())
        except:
            print("Einhvað fór úrskeiðis reindu aftur") # ef einhver villa kemur upp crashar forritið ekkis
    elif val==3:
        listi = [1,2,3,4,5,6,7] # geri lista
        print(Verkefni_2.onnurhver(listi)) # nota fallið onnurhver
        
    elif val==4:
        listi = [1,2,3,517,45,40,5,150] # geri lista
        print(Verkefni_2.finnatolu(listi)) # nota fallið finnatolu
    elif val ==5:
        listi = [2,4,6,8000,6,4,2] # geri lista
        Verkefni_2.stjornur(listi) # nota fallið  stjorunr
    elif val==0:
        lokaval = input("ertu viss um að þú viljir hætta ja eða nei: ")
        lokaval = lokaval.lower()
        if lokaval == "ja":
            on=False