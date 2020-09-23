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
    def prenta_upplysingar_um_medlim(self)
        print("Nafn: ",self.nafn)
        print("Félagsnúmer: ",self.felagsnumer)
        print("Laun: ",self.laun)
        print("Kennitala: ",self.kennitala)