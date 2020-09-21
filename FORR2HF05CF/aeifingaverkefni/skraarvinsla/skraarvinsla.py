on = True

veldi = 2
texti_veldi = ""
texti_veldi = texti_veldi+str(1)+","
for x in range(21):
    for p in range(x):
        veldi = veldi*2
    texti_veldi = texti_veldi+str(veldi)+","
    veldi = 2
with open("veldi.txt","w",encoding= "utf-8") as f:
    f.write(texti_veldi)

while on:
    print("(1) Gera listann")
    print("(2) prenta listann")
    print("(3) skrár með tölum sem enda á 6")
    print("(4) báðar skrár")
    print("(5) dictionary1")
    print("(0) Til að loka")
    valmynd_val = int(input("Veldu: "))
    if valmynd_val == 1:
        with open("veldi.txt","r",encoding= "utf-8") as f:
            veldi_texti = f.read()
        lista_addari = ""
        velda_listi = []
        for x in veldi_texti:
            if x !=",":
                lista_addari = lista_addari + str(x)
            elif x == ",":
                velda_listi.append(int(lista_addari))
                lista_addari = ""
    elif valmynd_val == 2:
        tal = 0
        for x in velda_listi:
            tal = tal+1
            print(x,end=" ")
            if tal%10==0:
                print("")
    elif valmynd_val == 3:
        sex_listi = []
        tal = 0
        for x in velda_listi:
            tala = str(x)
            if tala[-1] == "6":
                sex_listi.append(x)
                velda_listi.pop(tal)
            tal = tal+1
        print(sex_listi)
        sex_texti = ""
        for x in sex_listi:
            sex_texti=sex_texti+str(x)+","
        with open("6listi.txt","w",encoding="utf-8") as f:
            f.write(sex_texti)
    elif valmynd_val == 4:
        with open("veldi.txt","r",encoding= "utf-8") as f:
            veldi_texti = f.read()
        lista_addari = ""
        velda_listi = []
        for x in veldi_texti:
            if x !=",":
                lista_addari = lista_addari + str(x)
            elif x == ",":
                velda_listi.append(int(lista_addari))
                lista_addari = ""
        print("velda listi",velda_listi)
        with open("6listi.txt","r",encoding= "utf-8") as f:
            sex_texti = f.read()
        lista_addari = ""
        sex_listi = []
        for x in sex_texti:
            if x !=",":
                lista_addari = lista_addari + str(x)
            elif x == ",":
                sex_listi.append(int(lista_addari))
                lista_addari = ""
        print("sex tölur",sex_listi)
    elif valmynd_val == 5:
        for x in sex_texti:
            if x !=",":
                lista_addari = lista_addari + str(x)
            elif x == ",":
                sex_listi.append(int(lista_addari))
                lista_addari = ""
            dictionary = {}
            tal = 0
        for x in sex_listi:
            tal = tal +1
            dictionary[str(tal)] = x
        print(dictionary)
    elif valmynd_val == 0:
        on = False
