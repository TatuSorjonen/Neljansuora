from enum import Enum
import random
import math
import copy

class Tulos(Enum):
    """Luokka joka kertoo pelin nykytilanteen"""

    MENEILLAAN = 1
    KELTAINEN_VOITTI = 2
    TASAPELI = 3
    PUNAINEN_VOITTI = 4
    
class Lauta():

    SARAKKEIDEN_MAARA = 7 
    RIVIEN_MAARA = 6
    KELTAINEN = 'K'
    PUNAINEN = 'P'
    TYHJA = '-'

    def __init__(self):
        self.ruudukko = [['-' for i in range(Lauta.SARAKKEIDEN_MAARA)] for j in range(Lauta.RIVIEN_MAARA)]
        self.laskuri = 0 #Debug
        
    def lisaa_nappula(self, sarake, taulukko):
        '''Lisaa nappulan ruudukkoon
        
        Parametrit:
            sarake: mihin sarakkeeseen nappula laitetaan
            taulukko: taulukko mihin nappula laitetaan
        '''

        vuoro = self.kenen_vuoro(taulukko)
        vapaa_rivi = self.vapaa_rivi_sarakkeessa(sarake, taulukko)
        if vapaa_rivi != -1:
            taulukko[vapaa_rivi][sarake] = vuoro
        
    def kenen_vuoro(self, taulukko):
        '''Tarkistaa kumman pelaajan vuoro on seuraavaksi käymällä läpi taulukon ja tarkastamalla kumpia
        nappuloita on enemmän
        
        Parametrit:
            taulukko: taulukko mistä molempien pelaajien nappuloiden määrä tarkastetaan
            
        Palauttaa:
            Kumman pelaajan vuoro on seuraavaksi
        '''

        keltaisten_maara = 0
        punaisten_maara = 0
        
        vuoro = None

        for rivi in range(0, Lauta.RIVIEN_MAARA):
            for sarake in range(0, Lauta.SARAKKEIDEN_MAARA):
                if taulukko[rivi][sarake] == Lauta.KELTAINEN:
                    keltaisten_maara = keltaisten_maara + 1
                if taulukko[rivi][sarake] == Lauta.PUNAINEN:
                    punaisten_maara = punaisten_maara + 1
        
        if keltaisten_maara == punaisten_maara:
            vuoro = Lauta.KELTAINEN
        elif punaisten_maara == keltaisten_maara - 1:
            vuoro = Lauta.PUNAINEN
              
        return vuoro

    def lisaa_paras_siirto(self):
        '''Käy läpi kaikki mahdolliset siirrot ja kutsuu minimax algoritmia
        '''

        paras_tulos = -math.inf
        paras_sarake = -1
        paras_etaisyys = 3
        vari = Lauta.KELTAINEN
        
        for sarake in range(0, Lauta.SARAKKEIDEN_MAARA):

            #Jokainen testattava siirto tehdään uudelle laudan kopiolle
            taulukko = copy.deepcopy(self.ruudukko)

            rivi = self.vapaa_rivi_sarakkeessa(sarake, taulukko)
            if rivi != -1: 
                self.lisaa_nappula(sarake, taulukko)
                minimax_tulos = self.minimax(5, False, taulukko, -math.inf, math.inf)
                if minimax_tulos == 0:
                    minimax_tulos = self.tarkista_paras_asema(rivi, sarake, vari)
                    etaisyys = math.dist([rivi, sarake], [2,3])
                    if etaisyys < paras_etaisyys:
                        paras_etaisyys = etaisyys
                        minimax_tulos += 1
                        #print(f'Etäisyys on {etaisyys}') #Debug
                #print(f'SARAKE: {sarake}: MINIMAX TULOS: {minimax_tulos}') #Debug
                if minimax_tulos > paras_tulos:
                    paras_tulos = minimax_tulos
                    paras_sarake = sarake

        #print(f'Käytiin läpi {self.laskuri} asemaa!') #Debug
        self.laskuri = 0
        self.lisaa_nappula(paras_sarake, self.ruudukko)
        
    def minimax(self, syvyys, onko_max, taulukko, alpha, beta):
        '''Käy läpi eri vaihtoehtoja ja palauttaa parhaan vaihtoehdon
        
        Parametrit:
            syvyys: kuinka monen siirron takaa haetaan vaihtoehtoja
            onko_max: halutaanko tarkastaa paras vaihtoehto tekoälylle vai huonoin vaihtoehto pelaajalle
            taulukko: taulukko mistä katsotaan vaihtoehdot
        
        Palauttaa:
            -1 jos löytyy keltaiselle voitto
            1 jos löytyy punaiselle voitto
            0 jos ei löydy kummallekaan voittoa
        '''

        self.laskuri = self.laskuri + 1
        tulos = self.tarkista_tilanne(taulukko)
        if tulos != Tulos.MENEILLAAN or syvyys == 0:
            if tulos == Tulos.KELTAINEN_VOITTI:
                return -100 - syvyys
            elif tulos == Tulos.PUNAINEN_VOITTI:
                return 100 + syvyys
            else:
                return 0
        #else:
        #    return self.paras_asema(taulukko)       

        if onko_max:
            paras_tulos = -math.inf
            for sarake in range(0, Lauta.SARAKKEIDEN_MAARA):

                #Jokainen testattava siirto tehdään uudelle laudan kopiolle
                kopio_taulukko = copy.deepcopy(taulukko)

                rivi = self.vapaa_rivi_sarakkeessa(sarake, kopio_taulukko)
                self.lisaa_nappula(sarake, kopio_taulukko)
                minimax_tulos = self.minimax(syvyys - 1, False, kopio_taulukko, alpha, beta) 
                paras_tulos = max(paras_tulos, minimax_tulos)
                alpha = max(alpha, paras_tulos)
                if beta <= alpha:
                    break
            return paras_tulos
        else:
            paras_tulos = math.inf
            for sarake in range(0, Lauta.SARAKKEIDEN_MAARA):
            
                #Jokainen testattava siirto tehdään uudelle laudan kopiolle
                kopio_taulukko = copy.deepcopy(taulukko)

                rivi = self.vapaa_rivi_sarakkeessa(sarake, kopio_taulukko)
                self.lisaa_nappula(sarake, kopio_taulukko)
                minimax_tulos = self.minimax(syvyys - 1, True, kopio_taulukko, alpha, beta)
                paras_tulos = min(minimax_tulos, paras_tulos)
                beta = min(beta, paras_tulos)
                if beta <= alpha:
                    break
            return paras_tulos
    
    def tarkista_paras_asema(self, rivi, sarake, vari):
        toinen_vari = Lauta.PUNAINEN
        if vari == Lauta.PUNAINEN:
            toinen_vari = Lauta.KELTAINEN
        paras_tulos = 0
        #print(f'Rivi on {rivi} ja Sarake on {sarake}') #Debug
        for x in range(0, Lauta.RIVIEN_MAARA):
            for y in range(0, Lauta.SARAKKEIDEN_MAARA):
                if y + 1 < Lauta.SARAKKEIDEN_MAARA:
                    if self.ruudukko[x][y] == vari and self.ruudukko[x][y+1] == vari and (y+2 == sarake or y-1 == sarake):
                        paras_tulos += 1
                    if self.ruudukko[x][y] == toinen_vari and self.ruudukko[x][y+1] == vari and (y+2 == sarake or y-1 == sarake):
                        paras_tulos += 1

                if x + 1 < Lauta.RIVIEN_MAARA:
                    if self.ruudukko[x][y] == vari and self.ruudukko[x+1][y] == vari and (x+2 == rivi or x-1 == rivi):
                        paras_tulos += 1
                    if self.ruudukko[x][y] == toinen_vari and self.ruudukko[x+1][y] == toinen_vari and (x+2 == rivi or x-1 == rivi):
                        paras_tulos += 1

                if x + 1 < Lauta.RIVIEN_MAARA and y + 1 < Lauta.SARAKKEIDEN_MAARA:
                    if self.ruudukko[x][y] == vari and self.ruudukko[x+1][y+1] == vari and ((x+2 == rivi and y+2 == sarake) or (x-1 == rivi and y-1 == sarake)):
                        paras_tulos += 1
                    if self.ruudukko[x][y] == toinen_vari and self.ruudukko[x+1][y+1] == toinen_vari and ((x+2 == rivi and y+2 == sarake) or (x-1 == rivi and y-1 == sarake)):
                        paras_tulos += 1

                if x - 1 >= 0 and y + 1 < Lauta.SARAKKEIDEN_MAARA:
                    if self.ruudukko[x][y] == vari and self.ruudukko[x-1][y+1] == vari and ((x-2 == rivi and y+2 == sarake) or (x+1 == rivi and y-1 == sarake)):
                        paras_tulos += 1
                    if self.ruudukko[x][y] == toinen_vari and self.ruudukko[x-1][y+1] == toinen_vari and ((x-2 == rivi and y+2 == sarake) or (x+1 == rivi and y-1 == sarake)):
                        paras_tulos += 1
                        
        return paras_tulos
        
    def vapaa_rivi_sarakkeessa(self, sarake, taulukko):
        '''Tarkistaa annetun sarakkeen avulla seuraavan vapaan rivin
        
        Parametrit:
            sarake: mistä sarakkeesta tarkistetaan vapaa rivi
            taulukko: taulukko mistä tarkistetaan
        Palauttaa:
            vapaan rivin annetun sarakkeen avulla
        '''

        vapaa_rivi_indeksi = -1
        for rivi in range(Lauta.RIVIEN_MAARA - 1, -1, -1):
            if taulukko[rivi][sarake] == Lauta.TYHJA:
                vapaa_rivi_indeksi = rivi
                break        
        return vapaa_rivi_indeksi
        
    def tarkista_tilanne(self, taulukko):
        '''Tarkastaa tarkista_voittaja metodin avulla mikä tilanne pelissä on. Onko voittajaa,
        onko tasapeli vai onko peli edelleen meneillään
        
        Parametrit:
            taulukko: kyseinen taulukko mistä katsotaan pelin tilanne
            
        Palauttaa:
            pelin tilanteen
        '''

        tilanne = Tulos.MENEILLAAN        
        for rivi in range(0, Lauta.RIVIEN_MAARA):
            for sarake in range(0, Lauta.SARAKKEIDEN_MAARA):
                if taulukko[rivi][sarake] == '-':
                    continue
                tilanne = self.tarkista_voittaja(rivi, sarake, taulukko)                
                if tilanne != Tulos.MENEILLAAN:
                    return tilanne        
        if tilanne == Tulos.MENEILLAAN:
            tilanne = self.tarkista_tasapeli(taulukko)
        return tilanne

       
    def tarkista_voittaja(self, rivi, sarake, taulukko):
        '''Tarkistaa onko pelissä jo voittaja
        
        Parametrit:
            rivi: rivikoordinaatti
            sarake: sarakkeen koordinaatti
            taulukko: taulukko josta katsotaan löytyykö voittajaa
            
        Palauttaa:
            pelin tilanteen
        '''

        voittaja = None
        tilanne = Tulos.MENEILLAAN
        
        if sarake + 3 < Lauta.SARAKKEIDEN_MAARA:
            if taulukko[rivi][sarake] == taulukko[rivi][sarake+1]\
               == taulukko[rivi][sarake+2] == taulukko[rivi][sarake+3]:
                voittaja = taulukko[rivi][sarake]

        if rivi + 3 < Lauta.RIVIEN_MAARA:
            if taulukko[rivi][sarake] == taulukko[rivi+1][sarake]\
               == taulukko[rivi+2][sarake] == taulukko[rivi+3][sarake]:
                voittaja = taulukko[rivi][sarake]

        if rivi + 3 < Lauta.RIVIEN_MAARA and sarake + 3 < Lauta.SARAKKEIDEN_MAARA:
            if taulukko[rivi][sarake] == taulukko[rivi+1][sarake+1]\
               == taulukko[rivi+2][sarake+2] == taulukko[rivi+3][sarake+3]:
                voittaja = taulukko[rivi][sarake]

        if rivi - 3 >= 0 and sarake + 3 < Lauta.SARAKKEIDEN_MAARA:
            if taulukko[rivi][sarake] == taulukko[rivi-1][sarake+1]\
               == taulukko[rivi-2][sarake+2] == taulukko[rivi-3][sarake+3]:
                voittaja = taulukko[rivi][sarake]
        
        if voittaja == Lauta.KELTAINEN:
            tilanne = Tulos.KELTAINEN_VOITTI
        elif voittaja == Lauta.PUNAINEN:
            tilanne = Tulos.PUNAINEN_VOITTI
        return tilanne
        
    def tarkista_tasapeli(self, taulukko):
        '''Tarkastaa onko peli päättynyt tasapeliin katsomalla onko laudalla enään tyhjiä merkkejä
        
        Parametrit:
            taulukko: kyseinen tulukko, josta tasapeli tarkistetaan
            
        Palauttaa:
            pelin tilanteen
        '''

        tilanne = Tulos.MENEILLAAN
        if not any('-' in x for x in taulukko):
            tilanne = Tulos.TASAPELI
        return tilanne
        
    def nollaa_taulu(self):
        self.ruudukko = [['-' for i in range(Lauta.SARAKKEIDEN_MAARA)] for j in range(Lauta.RIVIEN_MAARA)]
    
    #Debug
    def tulosta_lauta(self, taulukko):
        print()
        for i in range(len(taulukko)):
            for j in range(len(taulukko[i])):
                print(taulukko[i][j], end=' ')
            print()
        print()
        
    #Ei käytössä tällä hetkellä. En saanu rekursion kanssa toimimaan     
    def peru_siirto(self, rivi, sarake, taulukko):
        '''Peruu siirron
        
        Parametrit:
            rivi: miltä riviltä nappula poistetaan
            sarake: miltä sarakkeelta nappula poistetaan
            taulukko: taulukko josta nappula poistetaan
        '''

        taulukko[rivi][sarake] = Lauta.TYHJA
        
    '''
    Käytän ehkä myöhemmin lisaa_random_punainen funktiota
    
    def lisaa_random_punainen(self):
        sarake = random.randint(0, 6)
        #print("Lisätään punainen")
        vapaa_rivi = self.vapaa_rivi_sarakkeessa(sarake)
        #print(f'Vapaa rivi {vapaa_rivi}')
        if vapaa_rivi != -1:
            self.ruudukko[vapaa_rivi][sarake] = Lauta.PUNAINEN
    '''
    
    '''
    Käytän ehkä myöhemmin lisaa_punainen funktiota

    def lisaa_punainen(self, sarake):
        #print("Lisätään punainen")
        vapaa_rivi = self.vapaa_rivi_sarakkeessa(sarake)
        print(f'Vapaa rivi {vapaa_rivi}')
        if vapaa_rivi != -1:
            self.ruudukko[vapaa_rivi][sarake] = Lauta.PUNAINEN
            self.kenen_vuoro = Lauta.KELTAISEN_VUORO
        self.tarkista_tilanne()
    '''
