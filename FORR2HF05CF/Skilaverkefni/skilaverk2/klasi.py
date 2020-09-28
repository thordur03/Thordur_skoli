class Verkalydsfelag: # object sem er starfsmaður hjá verkalýðsfélaginu og er með eginleikanna nafn, félagsnúmer, laun og kennitölu 
    def __init__(self,nafn,felagsnumer,laun,kennitala):
        self.nafn = nafn
        self.felagsnumer = felagsnumer
        self.laun = laun
        self.kennitala = kennitala
    
    def skatt(self): # fall sem reikanr skatt starfsmann
        return int(self.laun) * 0.36
    
    def utborgud_laun(self): # fall sem reiknar laun eftir skatt
        return int(laun-skatt())
    def prenta_upplysingar_um_medlim(self): # fall sem prentir út allar uppkýsingar um meðlim
        print(self.felagsnumer+"\t"+self.nafn+"\t\t"+self.laun+"\t\t"+self.kennitala)