def Fjoldi_Orda(strengur):
    tal = 1
    for x in strengur:
        if x == " ":
            tal = tal + 1
    tal = str(tal)
    return "Fjöldi orða:" + tal 

def Fyrstu5(strengur):
    
    billaust = ""
    for x in strengur:
        if x == " ":
            pass
        else: 
            billaust=billaust+x
    strengur = billaust

    
    if len(strengur)>4:
        fimmstafir = "" 
        for x in range(5):
            fimmstafir = fimmstafir+strengur[x]
        return "fyrstu fimm stafinir eru: " + fimmstafir
    else:
        return "orðið er undir 5 stöfum"

def seinustu4(strengur):
    fjorstafir = "" 
    billaust = ""
    for x in strengur:
        if x == " ":
            pass
        else: 
            billaust=billaust+x
    strengur = billaust
    if len(strengur)>3:
        for x in range(-4,0):
            fjorstafir = fjorstafir+strengur[x]
        return "seinustu fjóru stafinir eru: " + fjorstafir
    else:
        return "orðið er undir 4 stöfum"

def midjustafur(strengur):
    billaust = ""
    for x in strengur:
        if x == " ":
            pass
        else: 
            billaust=billaust+x
    strengur = billaust
    if len(strengur)%2==0:
        return "það er enginn stafur í miðjunni"
    else:
        return "miðjustafurinn er: "+str(strengur[int(len(strengur)/2)])
    
def Sfinnari(strengur):
    sStrentgur = ""
    for x in strengur:
        if x == "s" or x == "S":
            sStrentgur = sStrentgur + x
        elif x == " ":
            sStrentgur = sStrentgur + " "
        else:
            sStrentgur = sStrentgur + "#"
    return "öll s í strengnum: "+sStrentgur
    
string = input("sláðu inn streng: ")


print(Fjoldi_Orda(string))
print(Fyrstu5(string))
print(seinustu4(string))
print(midjustafur(string))
print(Sfinnari(string))






