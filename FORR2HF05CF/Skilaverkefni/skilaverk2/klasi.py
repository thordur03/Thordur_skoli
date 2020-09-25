class Verkalydsfelag:
    def __init__(self,nafn,felagsnumer,laun,kennitala):
        self.nafn = nafn
        self.felagsnumer = felagsnumer
        self.laun = laun
        self.kennitala = kennitala
    
    def skatt(self):
        return int(self.laun) * 0.36
    
    def utborgud_laun(self):
        return int(laun-skatt())
    def prenta_upplysingar_um_medlim(self):
        print(self.felagsnumer+"\t"+self.nafn+"\t\t"+self.laun+"\t\t"+self.kennitala)