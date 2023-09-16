from enum import Enum

class Tulos(Enum):
    """Luokka joka kertoo pelin nykytilanteen"""

    MENEILLAAN = 1
    TASAPELI = 2
    EKA_VOITTI = 3
    TOKA_VOITTI = 4
    
class Lauta():

    SARAKKEIDEN_MAARA = 7 
    RIVIEN_MAARA = 6
    KELTAINEN = 'K'
    PUNAINEN = 'P'
    TYHJA = '-'
    KELTAISEN_VUORO = 1
    PUNAISEN_VUORO = 2 

    def __init__(self):
        self.tulos = Tulos.MENEILLAAN
        self.ruudukko = [['-' for i in range(Lauta.SARAKKEIDEN_MAARA)] for j in range(Lauta.RIVIEN_MAARA)]
        self.kenen_vuoro = Lauta.KELTAISEN_VUORO
        
    def lisaa_keltainen(self, sarake):
        #print("Lisätään keltainen")
        vapaa_rivi = self.vapaa_rivi_sarakkeessa(sarake)
        print(f'Vapaa rivi {vapaa_rivi}')
        if vapaa_rivi != -1:
            self.ruudukko[vapaa_rivi][sarake] = Lauta.KELTAINEN
            self.kenen_vuoro = Lauta.PUNAISEN_VUORO
            
    def lisaa_punainen(self, sarake):
        #print("Lisätään punainen")
        vapaa_rivi = self.vapaa_rivi_sarakkeessa(sarake)
        print(f'Vapaa rivi {vapaa_rivi}')
        if vapaa_rivi != -1:
            self.ruudukko[vapaa_rivi][sarake] = Lauta.PUNAINEN
            self.kenen_vuoro = Lauta.KELTAISEN_VUORO
        
    def vapaa_rivi_sarakkeessa(self, sarake):
        print(f'{sarake} = sarake')
        vapaa_rivi_indeksi = -1
        for rivi in range(Lauta.RIVIEN_MAARA - 1, -1, -1):
            #print(self.ruudukko[rivi][sarake])
            print(f'Rivi={rivi}')
            if self.ruudukko[rivi][sarake] == Lauta.TYHJA:
                vapaa_rivi_indeksi = rivi
                return vapaa_rivi_indeksi
        
        return vapaa_rivi_indeksi
        
    def tulosta_lauta(self):
        for i in range(len(self.ruudukko)):
            for j in range(len(self.ruudukko[i])):
                print(self.ruudukko[i][j], end=' ')
            print()
