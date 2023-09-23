from enum import Enum
import random
import math
import copy

class Tulos(Enum):
    """Luokka joka kertoo pelin nykytilanteen"""

    MENEILLAAN = 1
    TASAPELI = 2
    KELTAINEN_VOITTI = 3
    PUNAINEN_VOITTI = 4
    
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
        #self.viimeisin_siirto = [-1,-1, Lauta.TYHJA]
        
    def lisaa_nappula(self, sarake, vari):
        #print("Lisätään keltainen")
        vapaa_rivi = self.vapaa_rivi_sarakkeessa(sarake)
        #self.tulosta_lauta()
        uusi_vari = None
        #print(f'Vapaa rivi {vapaa_rivi}')
        if vapaa_rivi != -1:
            self.ruudukko[vapaa_rivi][sarake] = vari
            uusi_vari = self.vaihda_vuoro(vari)
        return uusi_vari    
                
    def vaihda_vuoro(self, vari):
        uusi_vari = None
        if vari == Lauta.PUNAINEN:
            self.kenen_vuoro = Lauta.KELTAISEN_VUORO
            uusi_vari = Lauta.KELTAINEN
        else:
            self.kenen_vuoro = Lauta.PUNAISEN_VUORO
            uusi_vari = Lauta.PUNAINEN
        return uusi_vari
            
    def peru_siirto(self, rivi, sarake):
        #print(f'Peru siirto {rivi}, {sarake}')
        if self.ruudukko[rivi][sarake] == Lauta.KELTAINEN:
            self.vaihda_vuoro(Lauta.KELTAINEN)
        elif self.ruudukko[rivi][sarake] == Lauta.PUNAINEN:
            self.vaihda_vuoro(Lauta.PUNAINEN)
        else:
            print('EI VOI PERUA TYHJÄÄÄÄÄÄÄÄ!!!!!!!!!!!')
        self.ruudukko[rivi][sarake] = Lauta.TYHJA
        self.tulos = Tulos.MENEILLAAN
    
    #Debug  
    def lisaa_random_punainen(self):
        sarake = random.randint(0, 6)
        #print("Lisätään punainen")
        vapaa_rivi = self.vapaa_rivi_sarakkeessa(sarake)
        #print(f'Vapaa rivi {vapaa_rivi}')
        if vapaa_rivi != -1:
            self.ruudukko[vapaa_rivi][sarake] = Lauta.PUNAINEN
            self.kenen_vuoro = Lauta.KELTAISEN_VUORO
    
    def lisaa_paras_siirto(self, vari):
        paras_tulos = -math.inf
        paras_sarake = 0
        #ruudukko_kopio = copy.deepcopy(self.ruudukko)
        for sarake in range(0, Lauta.SARAKKEIDEN_MAARA):
            rivi = self.vapaa_rivi_sarakkeessa(sarake)
            if rivi != -1: 
                #print(f'Mahdollinen siirto on [{rivi},{sarake}]')
                uusi_vari = self.lisaa_nappula(sarake, vari)
                minimax_tulos = self.minimax(1, False, uusi_vari)
                #print(f'Perutaan {vari} siirtoa sarakkeesta {sarake} ja riviltä {rivi}')
                self.peru_siirto(rivi, sarake)
                if minimax_tulos > paras_tulos:
                    paras_tulos = minimax_tulos
                    paras_sarake = sarake
                #print(f'Paras tulos: {paras_tulos}, paras_sarake: {paras_sarake}')
        self.lisaa_nappula(paras_sarake, vari)
        
    def minimax(self, syvyys, onko_max, vari):
        self.tarkista_tilanne()
        if self.tulos != Tulos.MENEILLAAN or syvyys == 0: # Syvyys on debugia varten koska muuten heittää rekursive erroria
            #print('Rekursio päättyi')
            if self.tulos == Tulos.KELTAINEN_VOITTI:
                #self.tulosta_lauta()
                #nb = input('')
                
                return -1
            elif self.tulos == Tulos.PUNAINEN_VOITTI:
                return 1
            elif self.tulos == Tulos.TASAPELI or self.tulos == Tulos.MENEILLAAN:
                return 0
                
        

        if onko_max:
            paras_tulos = -math.inf
            #print(type(paras_tulos))
            for sarake in range(0, Lauta.SARAKKEIDEN_MAARA):
                rivi = self.vapaa_rivi_sarakkeessa(sarake)
                if rivi == 5 and sarake == 3:
                    self.tulosta_lauta()
                uusi_vari = self.lisaa_nappula(sarake, vari)
                minimax_tulos = self.minimax(syvyys - 1, False, uusi_vari)
                self.peru_siirto(rivi, sarake)
                #print(type(tulos))
                if minimax_tulos > paras_tulos:
                    paras_tulos = minimax_tulos
            return paras_tulos
        else:
            paras_tulos = math.inf
            for sarake in range(0, Lauta.SARAKKEIDEN_MAARA):
                rivi = self.vapaa_rivi_sarakkeessa(sarake)
                uusi_vari = self.lisaa_nappula(sarake, vari)
                minimax_tulos = self.minimax(syvyys - 1, True, uusi_vari)
                self.peru_siirto(rivi, sarake)
                if minimax_tulos < paras_tulos:
                    paras_tulos = minimax_tulos
            return paras_tulos
        
        
    '''
    def lisaa_paras_punainen(self):
        paras_tulos = -math.inf
        for rivi in range(Lauta.RIVIEN_MAARA - 1, -1, -1):
            for sarake in range(Lauta.SARAKKEIDEN_MAARA - 1, -1, -1):
                if self.mahdollinen_siirto(rivi, sarake):
                    print(f'Mahdollinen siirto on [{rivi},{sarake}]')
                    #self.ruudukko[rivi][sarake] = Lauta.PUNAINEN
                    tulos = self.minimax(self.ruudukko)
                    #self.ruudukko[rivi][sarake] == '-'
                    if tulos > paras_tulos:
                        paras_tulos = tulos
                        siirto = [rivi, sarake]
        print(siirto)
        self.ruudukko[siirto[0]][siirto[1]] = Lauta.PUNAINEN
        self.kenen_vuoro = Lauta.KELTAISEN_VUORO
        
        #Debug
        #self.lisaa_random_punainen()
   
    def mahdollinen_siirto(self, rivi, sarake):
        onko_mahdollinen = False
        if (rivi == Lauta.RIVIEN_MAARA - 1 and self.ruudukko[rivi][sarake] == Lauta.TYHJA):
            onko_mahdollinen = True
        elif rivi != Lauta.RIVIEN_MAARA - 1 and (self.ruudukko[rivi][sarake] == Lauta.TYHJA or self.ruudukko[rivi][sarake] == Lauta.TYHJA) and (self.ruudukko[rivi+1][sarake] == Lauta.PUNAINEN or self.ruudukko[rivi+1][sarake] == Lauta.KELTAINEN):
            onko_mahdollinen = True
        return onko_mahdollinen               
         
    def lisaa_punainen(self, sarake):
        #print("Lisätään punainen")
        vapaa_rivi = self.vapaa_rivi_sarakkeessa(sarake)
        print(f'Vapaa rivi {vapaa_rivi}')
        if vapaa_rivi != -1:
            self.ruudukko[vapaa_rivi][sarake] = Lauta.PUNAINEN
            self.kenen_vuoro = Lauta.KELTAISEN_VUORO
        self.tarkista_tilanne()
    '''        
    def vapaa_rivi_sarakkeessa(self, sarake):
        #print(f'{sarake} = sarake')
        vapaa_rivi_indeksi = -1
        for rivi in range(Lauta.RIVIEN_MAARA - 1, -1, -1):
            #print(self.ruudukko[rivi][sarake])
            #print(f'Rivi={rivi}')
            if self.ruudukko[rivi][sarake] == Lauta.TYHJA:
                vapaa_rivi_indeksi = rivi
                return vapaa_rivi_indeksi
        
        return vapaa_rivi_indeksi
        
    def tarkista_tilanne(self):

        for rivi in range(0, Lauta.RIVIEN_MAARA):
            for sarake in range(0, Lauta.SARAKKEIDEN_MAARA):

                if self.ruudukko[rivi][sarake] == '-':
                    continue
                self.tarkista_voittaja(rivi, sarake)

        self.tarkista_tasapeli()
        #print(f'Tulos on = {self.tulos}')

       
    def tarkista_voittaja(self, rivi, sarake):

        if sarake + 3 < Lauta.SARAKKEIDEN_MAARA:
            if self.ruudukko[rivi][sarake] == self.ruudukko[rivi][sarake+1]\
               == self.ruudukko[rivi][sarake+2] == self.ruudukko[rivi][sarake+3]:
                self.aseta_voittaja(self.ruudukko[rivi][sarake])

        if rivi + 3 < Lauta.RIVIEN_MAARA:
            if self.ruudukko[rivi][sarake] == self.ruudukko[rivi+1][sarake]\
               == self.ruudukko[rivi+2][sarake] == self.ruudukko[rivi+3][sarake]:
                self.aseta_voittaja(self.ruudukko[rivi][sarake])

        if rivi + 3 < Lauta.RIVIEN_MAARA and sarake + 3 < Lauta.SARAKKEIDEN_MAARA:
            if self.ruudukko[rivi][sarake] == self.ruudukko[rivi+1][sarake+1]\
               == self.ruudukko[rivi+2][sarake+2] == self.ruudukko[rivi+3][sarake+3]:
                self.aseta_voittaja(self.ruudukko[rivi][sarake])

        if rivi - 3 >= 0 and sarake + 3 < Lauta.SARAKKEIDEN_MAARA:
            if self.ruudukko[rivi][sarake] == self.ruudukko[rivi-1][sarake+1]\
               == self.ruudukko[rivi-2][sarake+2] == self.ruudukko[rivi-3][sarake+3]:
                self.aseta_voittaja(self.ruudukko[rivi][sarake])
        
    def aseta_voittaja(self, voittaja):
        if voittaja == Lauta.KELTAINEN:
            self.tulos = Tulos.KELTAINEN_VOITTI
        else:
            self.tulos = Tulos.PUNAINEN_VOITTI
        
    def tarkista_tasapeli(self):
        if not any('-' in x for x in self.ruudukko) and self.tulos == Tulos.MENEILLAAN:
            self.tulos = Tulos.TASAPELI
    
    #Debug
    def tulosta_lauta(self):
        print()
        for i in range(len(self.ruudukko)):
            for j in range(len(self.ruudukko[i])):
                print(self.ruudukko[i][j], end=' ')
            print()
        print()
