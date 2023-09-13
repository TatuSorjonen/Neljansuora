from enum import Enum

class Tulos(Enum):

    MENEILLAAN = 1
    TASAPELI = 2
    EKA_VOITTI = 3
    TOKA_VOITTI = 4
    
class Lauta():

    def __init__(self):
        self.SARAKKEIDEN_MAARA = 7 
        self.RIVIEN_MAARA = 6
        self.KELTAINEN = 'K'
        self.PUNAINEN = 'P'
        self.TYHJA = '-'
        self.KELTAISEN_VUORO = 1
        self.PUNAISEN_VUORO = 2 
        self.tulos = Tulos.MENEILLAAN
        self.lauta = [['-' for i in range(self.SARAKKEIDEN_MAARA)] for j in range(self.RIVIEN_MAARA)]
        self.kenen_vuoro = self.KELTAISEN_VUORO
        
    def lisaa_keltainen(self, y, x):
        if not self.onko_varattu(y, x):
            self.lauta[y][x] = self.KELTAINEN
            self.kenen_vuoro = self.PUNAISEN_VUORO
            
    def lisaa_sininen(self, y, x):
        if not self.onko_varattu(y, x):
            self.lauta[y][x] = self.PUNAINEN
            self.kenen_vuoro = self.KELTAISEN_VUORO
        
    def onko_varattu(self, y, x):
        return self.lauta[y][x] != self.TYHJA
