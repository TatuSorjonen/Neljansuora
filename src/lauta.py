from enum import Enum
import random
import math
import copy

class Tulos(Enum):
    """Luokka joka kertoo pelin nykytilanteen
    """

    MENEILLAAN = 1
    KELTAINEN_VOITTI = 2
    TASAPELI = 3
    PUNAINEN_VOITTI = 4
    MAKSIMIPISTEET = 1000

class Lauta:
    '''Lauta pitää yllä laudan tapahtumia
    '''

    SYVYYYS = 5
    SARAKKEIDEN_MAARA = 7
    RIVIEN_MAARA = 6
    KELTAINEN = 'K'
    PUNAINEN = 'P'
    TYHJA = '-'

    def __init__(self):
        self.ruudukko = [['-' for i in range(Lauta.SARAKKEIDEN_MAARA)] \
                              for j in range(Lauta.RIVIEN_MAARA)]

    def kenen_vuoro(self, taulukko):
        '''Tarkistaa kumman pelaajan vuoro on seuraavaksi käymällä läpi taulukon 
           ja tarkastamalla kumpia nappuloita on enemmän
        
        Parametrit:
            taulukko: Taulukko josta molempien pelaajien nappuloiden määrä tarkastetaan
            
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
    
    def vapaa_rivi_sarakkeessa(self, sarake, taulukko):
        '''Tarkistaa annetun sarakkeen avulla seuraavan vapaan rivin

        Parametrit:
            sarake: Mistä sarakkeesta tarkistetaan vapaa rivi
            taulukko: Taulukko mistä tarkistetaan
        Palauttaa:
            Vapaan rivin annetun sarakkeen avulla
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
            taulukko: Kyseinen taulukko josta katsotaan pelin tilanne

        Palauttaa:
            Pelin tilanteen
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
            rivi: Rivikoordinaatti
            sarake: Sarakkeen koordinaatti
            taulukko: Taulukko josta katsotaan löytyykö voittajaa

        Palauttaa:
            Pelin tilanteen
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
            taulukko: Kyseinen tulukko, josta tasapeli tarkistetaan

        Palauttaa:
            Pelin tilanteen
        '''

        tilanne = Tulos.MENEILLAAN
        if not any('-' in x for x in taulukko):
            tilanne = Tulos.TASAPELI
        return tilanne
        
    def lisaa_nappula(self, sarake, taulukko):
        '''Lisaa nappulan ruudukkoon
        
        Parametrit:
            sarake: Mihin sarakkeeseen nappula laitetaan
            taulukko: Taulukko mihin nappula laitetaan
        '''

        vuoro = self.kenen_vuoro(taulukko)
        vapaa_rivi = self.vapaa_rivi_sarakkeessa(sarake, taulukko)
        if vapaa_rivi != -1:
            taulukko[vapaa_rivi][sarake] = vuoro
        return vapaa_rivi

    def lisaa_satunnainen(self, vari):
        '''Lisää satunnaisen pelinappulan laudalle
        
        Parametrit:
            vari: Kummalle värille satunnainen pelinappula asetetaan

        Palauttaa:
            Vapaan rivin ja sarakkeen
        '''

        vapaa_rivi = -1
        sarake = 0
        tilanne = self.tarkista_tilanne(self.ruudukko)
        while vapaa_rivi == -1 and tilanne != Tulos.TASAPELI:
            sarake = random.randint(0, 6)
            vapaa_rivi = self.vapaa_rivi_sarakkeessa(sarake, self.ruudukko)
            if vapaa_rivi != -1:
                self.ruudukko[vapaa_rivi][sarake] = vari
        return vapaa_rivi, sarake

    def lisaa_paras_siirto(self, syvyys):
        '''Käy läpi kaikki mahdolliset siirrot ja kutsuu minimax algoritmia

        Parametrit:
            syvyys: miltä syvyydeltä katsotaan

        Palauttaa:
            parhaan sarakkeen, parhaan rivin ja parhaan tuloksen
        '''
        paras_tulos = -math.inf
        paras_sarake = -1
        paras_rivi = -1

        for sarake in range(0, Lauta.SARAKKEIDEN_MAARA):

            #Jokainen testattava siirto tehdään uudelle laudan kopiolle
            taulukko = copy.deepcopy(self.ruudukko)

            etaisyys_keskelta = abs(sarake - 3)

            rivi = self.vapaa_rivi_sarakkeessa(sarake, taulukko)
            if rivi != -1:
                self.lisaa_nappula(sarake, taulukko)
                minimax_tulos = self.minimax(syvyys, False, taulukko, -math.inf, math.inf)
                if minimax_tulos > paras_tulos or \
                  (minimax_tulos == paras_tulos and etaisyys_keskelta < paras_etaisyys):
                    paras_tulos = minimax_tulos
                    paras_sarake = sarake
                    paras_rivi = rivi
                    paras_etaisyys = etaisyys_keskelta

        self.lisaa_nappula(paras_sarake, self.ruudukko)
        return paras_sarake, paras_rivi, paras_tulos

    def minimax(self, syvyys, onko_max, taulukko, alpha, beta):
        '''Käy läpi eri vaihtoehtoja ja palauttaa parhaan vaihtoehdon
        
        Parametrit:
            syvyys: Kuinka monen siirron takaa haetaan vaihtoehtoja
            onko_max: Halutaanko tarkastaa paras vaihtoehto tekoälylle
                      vai huonoin vaihtoehto pelaajalle
            taulukko: Taulukko josta katsotaan vaihtoehdot
        
        Palauttaa:
            Parhaan aseman pisteet
        '''

        tulos = self.tarkista_tilanne(taulukko)

        if tulos != Tulos.MENEILLAAN or syvyys == 0:

            # Jos vastustaja voittaa, palauttaa huonon tuloksen
            if onko_max and (tulos == Tulos.KELTAINEN_VOITTI or tulos == Tulos.PUNAINEN_VOITTI):
                return 0 - Tulos.MAKSIMIPISTEET.value - syvyys
            
            # Jos itse voittaa palauttaa hyvän tuloksen
            elif tulos == Tulos.KELTAINEN_VOITTI or tulos == Tulos.PUNAINEN_VOITTI:
                return Tulos.MAKSIMIPISTEET.value + syvyys
            
            # Jos löytyy tasapeli palauttaa 0
            elif tulos == Tulos.TASAPELI:
                return 0
            
            # Muulloin arvioi parhaan aseman käyttäen arvioi_asema funktiota
            else:
                return self.arvioi_asema(taulukko)

        if onko_max:
            paras_tulos = -math.inf
            for sarake in range(0, Lauta.SARAKKEIDEN_MAARA):
                

                #Jokainen testattava siirto tehdään uudelle laudan kopiolle
                kopio_taulukko = copy.deepcopy(taulukko)

                rivi = self.vapaa_rivi_sarakkeessa(sarake, taulukko)
                if rivi != -1:
                    self.lisaa_nappula(sarake, kopio_taulukko)
                    minimax_tulos = self.minimax(syvyys - 1, False, kopio_taulukko, alpha, beta)
                    paras_tulos = max(minimax_tulos, paras_tulos)
                    alpha = max(alpha, paras_tulos)
                    if beta <= alpha:
                        break
            return paras_tulos
        else:
            paras_tulos = math.inf
            for sarake in range(0, Lauta.SARAKKEIDEN_MAARA):

                #Jokainen testattava siirto tehdään uudelle laudan kopiolle
                kopio_taulukko = copy.deepcopy(taulukko)

                rivi = self.vapaa_rivi_sarakkeessa(sarake, taulukko)
                if rivi != -1:
                    self.lisaa_nappula(sarake, kopio_taulukko)
                    minimax_tulos = self.minimax(syvyys - 1, True, kopio_taulukko, alpha, beta)
                    paras_tulos = min(minimax_tulos, paras_tulos)
                    beta = min(beta, paras_tulos)
                    if beta <= alpha:
                        break
            return paras_tulos

    def arvioi_asema(self, taulukko):
        '''Arvioi parhaimman aseman, jos ei ole löytynyt suoraa voittoa kummallekaan.

        Parametrit:
            taulukko: Taulukko mistä arvioidaan

        Palauttaa:
            Parhaat pisteet
        '''
        nappuloiden_maara = 0
        pisteet = {Lauta.KELTAINEN: 0, Lauta.PUNAINEN: 0}
        for rivi in range(0, Lauta.RIVIEN_MAARA):
            for sarake in range(0, Lauta.SARAKKEIDEN_MAARA):
                if taulukko[rivi][sarake] != Lauta.TYHJA:
                    nappuloiden_maara += 1
                else:
                    continue
                pisteet = self.pisteyta_voittomahdollisuudet(taulukko, rivi, sarake, pisteet)

        pisteet_keltainen = int(pisteet[Lauta.KELTAINEN])
        pisteet_punainen = int(pisteet[Lauta.PUNAINEN])

        vuoro = self.kenen_vuoro(taulukko)
        if (vuoro == Lauta.KELTAINEN and Lauta.SYVYYYS % 2 != 0) or \
           (vuoro == Lauta.PUNAINEN and Lauta.SYVYYYS % 2 == 0):
            pyoristys = (pisteet_keltainen - pisteet_punainen) / nappuloiden_maara
            return int(10 * round(float(pyoristys) / 10))
        else:
            pyoristys = (pisteet_punainen - pisteet_keltainen) / nappuloiden_maara
            return int(10 * round(float(pyoristys) / 10))

    def pisteyta_voittomahdollisuudet(self, taulukko, rivi, sarake, pisteet):
        '''Pisteyttää voittomahdollisuudet

        Parametrit:
            taulukko: Taulukko josta pisteytetään
            rivi: Rivi josta pisteytetään
            sarake: Sarake josta pisteytetään
            pisteet: Pisteet joihin lisätään

        Palauttaa:
            Pisteet lisäämisten jälkeen
        '''

        vari = taulukko[rivi][sarake]
        pisteet_kolmesta = int(Tulos.MAKSIMIPISTEET.value/7)
        pisteet_kahdesta = int(Tulos.MAKSIMIPISTEET.value/30)
        pisteet_yhdesta = int(Tulos.MAKSIMIPISTEET.value/75)

        #Neljän suoran mahdollisuudet ruudusta suoraan ylöspäin
        if rivi-4 >= 0:
            if taulukko[rivi][sarake] == taulukko[rivi-1][sarake] == \
                taulukko[rivi-2][sarake] and taulukko[rivi-3][sarake] == Lauta.TYHJA:
                pisteet[vari] += pisteet_kolmesta
            elif taulukko[rivi][sarake] == taulukko[rivi-1][sarake] and \
                  taulukko[rivi-2][sarake] == taulukko[rivi-3][sarake] == Lauta.TYHJA:
                pisteet[vari] += pisteet_kahdesta
            elif taulukko[rivi-1][sarake] == taulukko[rivi-2][sarake] == \
                  taulukko[rivi-3][sarake] == Lauta.TYHJA:
                pisteet[vari] += pisteet_yhdesta

        #Neljän suoran mahdollisuudet ruudusta suoraan vasemmalle
        if sarake-3 >= 0:
            if taulukko[rivi][sarake] == taulukko[rivi][sarake-1] == \
                taulukko[rivi][sarake-2] and taulukko[rivi][sarake-3] == Lauta.TYHJA:
                pisteet[vari] += pisteet_kolmesta
            elif taulukko[rivi][sarake] == taulukko[rivi][sarake-1] and \
                  taulukko[rivi][sarake-2] == taulukko[rivi][sarake-3] == Lauta.TYHJA:
                pisteet[vari] += pisteet_kahdesta
            elif taulukko[rivi][sarake-1] == taulukko[rivi][sarake-2] == \
                  taulukko[rivi][sarake-3] == Lauta.TYHJA:
                pisteet[vari] += pisteet_yhdesta

        #Neljän suoran mahdollisuudet ruudusta suoraan oikealle
        if sarake+3 < Lauta.SARAKKEIDEN_MAARA:
            if taulukko[rivi][sarake] == taulukko[rivi][sarake+1] == \
                taulukko[rivi][sarake+2] and taulukko[rivi][sarake+3] == Lauta.TYHJA:
                pisteet[vari] += pisteet_kolmesta
            elif taulukko[rivi][sarake] == taulukko[rivi][sarake+1] and \
                  taulukko[rivi][sarake+2] == taulukko[rivi][sarake+3] == Lauta.TYHJA:
                pisteet[vari] += pisteet_kahdesta
            elif taulukko[rivi][sarake+1] == taulukko[rivi][sarake+2] == \
                  taulukko[rivi][sarake+3] == Lauta.TYHJA:
                pisteet[vari] += pisteet_yhdesta

        #Neljän suoran mahdollisuudet ruudusta vinosti oikealle ylös
        if sarake+3 < Lauta.SARAKKEIDEN_MAARA and rivi-3 >= 0:
            if taulukko[rivi][sarake] == taulukko[rivi-1][sarake+1] == \
                taulukko[rivi-2][sarake+2] and taulukko[rivi-3][sarake+3] == Lauta.TYHJA:
                pisteet[vari] += pisteet_kolmesta
            elif taulukko[rivi][sarake] == taulukko[rivi-1][sarake+1] and \
                  taulukko[rivi-2][sarake+2] == taulukko[rivi-3][sarake+3] == Lauta.TYHJA:
                pisteet[vari] += pisteet_kahdesta
            elif taulukko[rivi-1][sarake+1] == taulukko[rivi-2][sarake+2] == \
                  taulukko[rivi-3][sarake+3] == Lauta.TYHJA:
                pisteet[vari] += pisteet_yhdesta

        #Neljän suoran mahdollisuudet ruudusta vinosti vasemmalle ylös
        if sarake-3 >= 0 and rivi-3 >= 0:
            if taulukko[rivi][sarake] == taulukko[rivi-1][sarake-1] == \
                taulukko[rivi-2][sarake-2] and taulukko[rivi-3][sarake-3] == Lauta.TYHJA:
                pisteet[vari] += pisteet_kolmesta
            elif taulukko[rivi][sarake] == taulukko[rivi-1][sarake-1] and \
                  taulukko[rivi-2][sarake-2] == taulukko[rivi-3][sarake-3] == Lauta.TYHJA:
                pisteet[vari] += pisteet_kahdesta
            elif taulukko[rivi-1][sarake-1] == taulukko[rivi-2][sarake-2] == \
                  taulukko[rivi-3][sarake-3] == Lauta.TYHJA:
                pisteet[vari] += pisteet_yhdesta

        return pisteet
