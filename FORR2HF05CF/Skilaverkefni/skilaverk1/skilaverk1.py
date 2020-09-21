def lesaLyklabok(): # Klassi sem les lyklar.txt og setur það í dictionary
    lyklabok = {}
    with open("lyklar.txt","r") as f:
        for line in f:
            (key,val) = line.split(";")
            lyklabok[key] = val.replace("\n","")
        return lyklabok


on = True

while on:
    print("(1) Póstnúmer dictionary")
    print("(2) Áfangar")
    print("(3) Lyklar.txt")
    print("(4) stafavíxl")
    print("(0) Til að loka")
    valmynd_val = int(input("Veldu: "))
    if valmynd_val == 1:
        # dictonary með postnumerum
        postnumer = {"Miðborg":101,"Hagartorg":102,"Háleitshverfi":103,"Laugardalur":104,"Hlíðar":105,"Vesturbær":107,"Bústaðarvegur":108,"Breiðholt":109,"Árbær":110,"Grafarvogur":112}
        on1 = True
        while on1:
            print("(1) Finna póstnúmer")
            print("(2) Bæta stað")
            print("(3) Eyða úr dictionary")
            print("(4) Breyta Pósnúmeri")
            print("(0) Til að fara til baka")
            postnmr_val = int(input("Veldu: "))
            if postnmr_val == 1: # spyr notenda um stað og fer í gegnum dict til að sjá hvað póstnúmerið er
                stadur_notenda = input("veldu stað: ")
                try:
                    print(postnumer[stadur_notenda])
                except:
                    print("þessi staður er ekki í dictionary")
            elif postnmr_val == 2: # bið notenda um stað og psotnumer til að bæti í dictionary
                stadur = input("Sláðu inn stað: ")
                postnmr_key = int(input("sláðu inn póstnúmer: "))    
                print("skrifaðu rétt póstnúmer")
                postnumer[stadur] = postnmr_key
                print(postnumer)
            elif postnmr_val == 3: # bið notenda um stað til að eyða
                stadur_eyda = input("Veldu stað til að eyða: ")
                postnumer.pop(stadur_eyda)
                print(postnumer)
            elif postnmr_val == 4: # bið notenda um stað og nytt postnumer til að breyta
                
                print("Sláðu inn stað til að breyta póstnúmri")
                stadur = input("Staður: ")
                print("hvað vitu að póstnúmerið sé?")
                if stadur in postnumer:
                    postnmr_key = int(input("Póstnúmer: "))
                    postnumer[stadur] = postnmr_key
                    print(postnumer)
                else:
                    print("þessi staður er ekki til")

            elif postnmr_val == 0:
                on1 = False
        
    elif valmynd_val == 2:
        # bið notenda um fjolda í áföngunnum og nöfn fyrir nemandanna
        print("Hvað eru margir í Forritunarhópnum?")
        fjoldi_Forr = int(input("Fjöldi: "))
        forritunar_listi = []
        for x in range(fjoldi_Forr):
            forritunar_listi.append(input("sláðu inn nafn: "))
        
        print("Hvað eru margir í Vesm hópnum?")
        fjoldi_Vesm = int(input("Fjöldi: "))
        vesm_listi = []
        for x in range(fjoldi_Vesm):
            vesm_listi.append(input("sláðu inn nafn: "))
        
        
        # sorta listanna
        forritunar_listi = sorted(forritunar_listi)
        vesm_listi = sorted(vesm_listi)
        
        # prenti listanna
        print("Forritunar Listinn: ")
        for x in forritunar_listi:
            print(x)
        print("vesm Listinn: ")
        for x in vesm_listi:
            print(x)

        #skrifa út þá sem eru í báðum hópunnnum
        for x in forritunar_listi:
            if x in vesm_listi:
                print(x)
        print(vesm_listi)
        print(forritunar_listi)
        # skrifa hver hópurinn er stærri
        if len(vesm_listi)<len(forritunar_listi):
            print("Forritunar hóðurinn er stærri")
        elif len(vesm_listi)>len(forritunar_listi):
            print("Vesm hópurinn er stærri")
        elif len(vesm_listi)==len(forritunar_listi):
            print("Hópanir eru jafnstórir")
        # færi tvo öftustu nemendur í Forritun yfir í vesm
        for x in range(2):
            seinasta_tala = forritunar_listi[-1]
            vesm_listi.append(seinasta_tala)
            forritunar_listi.pop(-1)
        print(vesm_listi)
        print(forritunar_listi) 
    elif valmynd_val == 3:
        
        lyklabok = lesaLyklabok() # fæ dictionary úr klassanum
        nafn = input("sláðu inn nafn: ") # bið notenda um naf og lykilorð
        lykilord = input("sláðu inn lykilorð: ")
        for x in lyklabok: # ef lykilorðið og notendanafið er rett skrifas6t ut þú ert meðlimur en ef annaðhvort er rétt
            # þá skirfast út annaðhvort er vitlaust en ef allt er vitlaust skrifast þú ert ekki meðlimur 
            if nafn == x and nafn == lyklabok[x]:
                print("þú ert meðlimur")
            elif nafn == x and lykilord != lyklabok[x] or nafn != x and lykilord == lyklabok[x]:
                print("Það er eitthvað rangt annað hvort nafn eða lykilorð")
            else:
                print("þú ert ekki meðlimur")
    elif valmynd_val == 4: 
        strengur = input("Sláðu inn streng: ") # bið notenda um streng
        vixlstrengur = ""
        lokastrengur = ""
        vixl = ""
        teljari = 0
        lokteljari = 0
        if len(strengur)%2 == 0: # ef lengd textans er slétt þarrf ég ekki að hugsa um seinasta stafinn
            for x in strengur:
                teljari = teljari + 1 # nota teljara
                
                if teljari == 1 or teljari == 2: # ef teljarinn er einn eða tveir bæti ég staf í víxlstreng
                    vixlstrengur = vixlstrengur + x
                if teljari == 2:  # ef teljari er tveir víxla ég stafina og set í lokastreng og núlla teljarann
                    vixl = vixl + vixlstrengur[1]
                    vixl = vixl + vixlstrengur[0]  
                    lokastrengur = lokastrengur + vixl
                    vixlstrengur = ""
                    vixl = ""
                    teljari = 0
        else: # ef lengdinn er oddatala þá geri ég eginlega eins nema að ég nota nýjan teljara 
            # ef það er komið að seinustu tölunni þá bæti ég henni neint í lokastrenginn
            for x in strengur:
                
                teljari = teljari + 1
                lokteljari = lokteljari +1
                
                if teljari == 1 or teljari == 2:
                    vixlstrengur = vixlstrengur + x
                    
                if teljari == 2 or lokteljari==len(strengur): 
                   
                    if lokteljari != len(strengur):
                        
                        vixl = vixl + vixlstrengur[1]
                        vixl = vixl + vixlstrengur[0]  
                        lokastrengur = lokastrengur + vixl
                        vixlstrengur = ""
                        vixl = ""
                        teljari = 0
                    else:
                        
                        lokastrengur= lokastrengur+strengur[-1]
        print(lokastrengur)
    elif valmynd_val == 0:
        on = False