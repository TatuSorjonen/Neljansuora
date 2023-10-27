import unittest
from lauta import Lauta, Tulos
       
class TestLauta(unittest.TestCase):

    def setUp(self):
        self.lauta = Lauta()
        
    def test_konstruktori_toimii(self):
        '''Testaa konstruktorin toimivuuden
        '''

        self.assertEqual(self.lauta.ruudukko, [['-', '-', '-', '-', '-', '-', '-'], \
                                               ['-', '-', '-', '-', '-', '-', '-'], \
                                               ['-', '-', '-', '-', '-', '-', '-'], \
                                               ['-', '-', '-', '-', '-', '-', '-'], \
                                               ['-', '-', '-', '-', '-', '-', '-'], \
                                               ['-', '-', '-', '-', '-', '-', '-']])

    def test_lisaa_nappula_toimii(self):
        '''Nappulan laittaminen oikeaan kohtaan toimii testi
        '''

        self.lauta.lisaa_nappula(1, self.lauta.ruudukko)
        self.assertEqual(self.lauta.ruudukko[5][1], self.lauta.KELTAINEN)
        self.lauta.lisaa_nappula(1, self.lauta.ruudukko)
        self.assertEqual(self.lauta.ruudukko[4][1], 'P')
        self.lauta.lisaa_nappula(1, self.lauta.ruudukko)
        self.lauta.lisaa_nappula(1, self.lauta.ruudukko)
        self.lauta.lisaa_nappula(1, self.lauta.ruudukko)
        self.lauta.lisaa_nappula(1, self.lauta.ruudukko)
        self.assertEqual(self.lauta.ruudukko[0][1], 'P')
        self.lauta.lisaa_nappula(1, self.lauta.ruudukko)
        self.assertEqual(self.lauta.ruudukko[0][1], 'P')

    def test_vuoron_vaihto_toimii(self):
        '''Vuoron vaihto toimii jokaisen siirron jälkeen
        '''

        vuoro = self.lauta.kenen_vuoro(self.lauta.ruudukko)
        self.assertEqual(vuoro, self.lauta.KELTAINEN)

        self.lauta.lisaa_nappula(1, self.lauta.ruudukko)
        vuoro = self.lauta.kenen_vuoro(self.lauta.ruudukko)
        self.assertEqual(vuoro, self.lauta.PUNAINEN)

        self.lauta.lisaa_nappula(1, self.lauta.ruudukko)
        vuoro = self.lauta.kenen_vuoro(self.lauta.ruudukko)
        self.assertEqual(vuoro, self.lauta.KELTAINEN)
        
    def test_vapaa_rivi_sarakkeessa_toimii(self):
        '''Tarkistaa, että oikea rivi löytyy tietyssä sarakkeessa
        '''

        vapaa = self.lauta.vapaa_rivi_sarakkeessa(1, self.lauta.ruudukko)
        self.assertEqual(vapaa, 5)
        self.lauta.lisaa_nappula(1, self.lauta.ruudukko)

        vapaa = self.lauta.vapaa_rivi_sarakkeessa(1, self.lauta.ruudukko)
        self.assertEqual(vapaa, 4)
        
    def test_voiton_tarkastus_toimii_keltaisella(self):
        '''Tarkistaa löytyykö voitto keltaiselle
        '''

        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        self.lauta.lisaa_nappula(0, self.lauta.ruudukko)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        self.lauta.lisaa_nappula(1, self.lauta.ruudukko)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        self.lauta.lisaa_nappula(0, self.lauta.ruudukko)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        self.lauta.lisaa_nappula(1, self.lauta.ruudukko)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        self.lauta.lisaa_nappula(0, self.lauta.ruudukko)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        self.lauta.lisaa_nappula(1, self.lauta.ruudukko)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        self.lauta.lisaa_nappula(0, self.lauta.ruudukko)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.KELTAINEN_VOITTI)
 
    def test_voiton_tarkastus_toimii_punaisella(self):
        '''Tarkistaa löytyykö voitto punaiselle
        '''

        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        self.lauta.lisaa_nappula(0, self.lauta.ruudukko)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        self.lauta.lisaa_nappula(1, self.lauta.ruudukko)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        self.lauta.lisaa_nappula(0, self.lauta.ruudukko)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        self.lauta.lisaa_nappula(1, self.lauta.ruudukko)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        self.lauta.lisaa_nappula(0, self.lauta.ruudukko)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        self.lauta.lisaa_nappula(1, self.lauta.ruudukko)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        self.lauta.lisaa_nappula(4, self.lauta.ruudukko)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        self.lauta.lisaa_nappula(1, self.lauta.ruudukko)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.PUNAINEN_VOITTI)
        
    def test_tarkista_tasapeli_toimii(self):
        '''Testaa löytyykö tasapeli
        '''

        self.lauta.ruudukko = [['K', 'K', 'P', 'P', 'P', '-', 'P'], \
                               ['P', 'P', 'K', 'K', 'K', 'P', 'K'], \
                               ['K', 'K', 'P', 'P', 'P', 'K', 'P'], \
                               ['P', 'P', 'K', 'K', 'K', 'P', 'K'], \
                               ['P', 'K', 'P', 'P', 'K', 'P', 'P'], \
                               ['K', 'K', 'P', 'K', 'P', 'K', 'K']]
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        self.lauta.lisaa_nappula(5, self.lauta.ruudukko)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.TASAPELI)

    def test_sarake_taynna_lisaaminen_ei_onnistu(self):
        '''Testaa täyteen sarakkeeseen lisäämisen epäonnistumisen
        '''

        self.lauta.ruudukko = [['-', '-', '-', 'P', '-', '-', '-'], \
                               ['-', '-', '-', 'K', '-', '-', '-'], \
                               ['-', '-', '-', 'P', '-', '-', '-'], \
                               ['-', '-', '-', 'K', '-', '-', '-'], \
                               ['-', '-', '-', 'P', '-', '-', '-'], \
                               ['-', '-', '-', 'K', '-', '-', '-']]
        rivi = self.lauta.lisaa_nappula(3, self.lauta.ruudukko)
        self.assertEqual(rivi, -1)

    def test_lisaa_satunnainen_toimii(self):
        '''Testaa satunnaisen lisäämisen toimivuuden
        '''

        oikea_sarake = False
        self.lauta.ruudukko = [['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', '-', '-', '-', '-', '-']]
        rivi, sarake = self.lauta.lisaa_satunnainen('K')
        self.assertEqual(rivi, 5)
        if sarake == 0 or sarake == 1 or sarake == 2 or \
           sarake == 3 or sarake == 4 or sarake == 5 or sarake == 6:
            oikea_sarake = True
        self.assertEqual(oikea_sarake, True)

        #Testataan myös täydellä laudalla, että tämä lisääminen ei onnistu
        self.lauta.ruudukko = [['K', 'K', 'P', 'P', 'P', 'K', 'P'], \
                               ['P', 'P', 'K', 'K', 'K', 'P', 'K'], \
                               ['K', 'K', 'P', 'P', 'P', 'K', 'P'], \
                               ['P', 'P', 'K', 'K', 'K', 'P', 'K'], \
                               ['P', 'K', 'P', 'P', 'K', 'P', 'P'], \
                               ['K', 'K', 'P', 'K', 'P', 'K', 'K']]
        rivi, sarake = self.lauta.lisaa_satunnainen('K')
        self.assertEqual(rivi, -1)

    def test_minimax_toiminnalisuus(self):
        '''Minimaxin toiminnalisuuden testaaminen eri vaihtoehdoilla
        '''

        #Löytyykö voitto suoraan
        syvyys = 1
        self.lauta.ruudukko = [['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', 'P', 'K', '-', '-', '-'], \
                               ['-', '-', 'P', 'K', '-', '-', '-'], \
                               ['-', '-', 'P', 'K', '-', '-', '-']]
        minimax_tulos = self.lauta.lisaa_paras_siirto(syvyys)[2]
        self.assertEqual(minimax_tulos, Tulos.MAKSIMIPISTEET.value + syvyys)

        #Löytyykö voitto kahden päästä
        syvyys = 3
        self.lauta.ruudukko = [['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', 'P', 'P', '-', '-', '-'], \
                               ['-', '-', 'K', 'K', '-', '-', '-']]
        minimax_tulos = self.lauta.lisaa_paras_siirto(syvyys)[2]
        self.assertEqual(minimax_tulos, Tulos.MAKSIMIPISTEET.value + syvyys - 2)

        #Toinen testi löytyykö voitto kahden päästä
        syvyys = 4
        self.lauta.ruudukko = [['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', '-', 'P', '-', '-', '-'], \
                               ['-', '-', '-', 'P', '-', '-', '-'], \
                               ['K', '-', '-', 'K', '-', '-', '-'], \
                               ['P', '-', 'K', 'K', '-', '-', '-'], \
                               ['P', 'P', 'P', 'K', 'K', 'K', 'P']]
        minimax_tulos = self.lauta.lisaa_paras_siirto(syvyys)[2]
        self.assertEqual(minimax_tulos, Tulos.MAKSIMIPISTEET.value + syvyys - 2)

    def test_tarkista_voitto_seitseman_siirron_paasta(self):
        '''Testissä käytetty manuaalista toisen pelaajan parasta siirtoa. 
        Olisi muuten kestänyt testi turhan kauan.
        '''

        syvyys = 7
        self.lauta.ruudukko = [['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', 'K', 'P', '-', '-', '-'], \
                               ['P', '-', 'P', 'K', 'K', '-', '-'], \
                               ['P', 'K', 'P', 'K', 'K', 'K', '-'], \
                               ['P', 'P', 'K', 'K', 'P', 'P', '-']]

        # Siirto 1
        minimax_tulos = self.lauta.lisaa_paras_siirto(syvyys)[2]
        self.assertEqual(minimax_tulos, Tulos.MAKSIMIPISTEET.value + syvyys - 6)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        # Siirto 2
        self.lauta.lisaa_nappula(1, self.lauta.ruudukko)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        # Siirto 3
        minimax_tulos = self.lauta.lisaa_paras_siirto(syvyys)[2]
        self.assertEqual(minimax_tulos, Tulos.MAKSIMIPISTEET.value + syvyys - 4)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        #Siirto 4
        self.lauta.lisaa_nappula(5, self.lauta.ruudukko)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        #Siirto 5
        minimax_tulos = self.lauta.lisaa_paras_siirto(syvyys)[2]
        self.assertEqual(minimax_tulos, Tulos.MAKSIMIPISTEET.value + syvyys - 2)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        #Siirto 6
        self.lauta.lisaa_nappula(6, self.lauta.ruudukko)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.MENEILLAAN)

        #Siirto 7
        minimax_tulos = self.lauta.lisaa_paras_siirto(syvyys)[2]
        self.assertEqual(minimax_tulos, Tulos.MAKSIMIPISTEET.value + syvyys - 0)
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        self.assertEqual(tilanne, Tulos.KELTAINEN_VOITTI)

    def test_minimax_loytaa_tasapelin_toimii(self):
        '''Testaa löytääkö minimax varman tasapelin
        '''

        syvyys = 4
        self.lauta.ruudukko = [['P', 'P', 'K', 'P', 'P', '-', '-'], \
                               ['K', 'K', 'P', 'K', 'K', 'K', '-'], \
                               ['P', 'P', 'K', 'K', 'P', 'P', '-'], \
                               ['K', 'K', 'P', 'P', 'K', 'K', '-'], \
                               ['P', 'P', 'K', 'K', 'P', 'K', 'P'], \
                               ['K', 'P', 'K', 'P', 'K', 'K', 'P']]
        minimax_tulos = self.lauta.lisaa_paras_siirto(syvyys)[2]
        self.assertEqual(minimax_tulos, 0)

    def test_minimax_osaa_estaa_voiton(self):
        '''Testaa löytääkö minimax vastustajan voiton ja estää tämän
        '''
        
        #Osaa estää yhden päässä olevan voiton
        syvyys = 1
        self.lauta.ruudukko = [['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', '-', 'K', '-', '-', '-'], \
                               ['-', '-', 'P', 'K', '-', '-', '-'], \
                               ['-', '-', 'P', 'K', '-', '-', '-']]
        paras_sarake = self.lauta.lisaa_paras_siirto(syvyys)[0]
        self.assertEqual(paras_sarake, 3)

        #Osaa estää kehden päässä olevan voiton
        syvyys = 3
        self.lauta.ruudukko = [['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', '-', '-', '-', '-', '-'], \
                               ['-', '-', '-', 'P', '-', '-', '-'], \
                               ['-', '-', 'K', 'K', '-', '-', '-']]
        paras_sarake = self.lauta.lisaa_paras_siirto(syvyys)[0]
        onko_paras = False
        if paras_sarake == 1 or paras_sarake == 4:
            onko_paras = True
        self.assertEqual(onko_paras, True)
