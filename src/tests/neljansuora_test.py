import unittest
from unittest.mock import patch
#from testi import Neljansuora  #Heittää pygame import virhettä. Täytyy korjata
#from neljansuora import Neljansuora  #Heittää pygame import virhettä. Täytyy korjata
from lauta import Lauta, Tulos
'''

class TestNeljansuora(unittest.TestCase):
    
    #def setUp(self):
    #    self.neljansuora = Neljansuora()
    def test_konstruktori_toimii(self):
        self.assertEqual(1, 1) 
'''        
class TestLauta(unittest.TestCase):

    def setUp(self):
        self.lauta = Lauta()
        
    def test_konstruktori_toimii(self):
        self.assertEqual(self.lauta.tulos, Tulos.MENEILLAAN)
        self.assertEqual(self.lauta.ruudukko, [['-' for i in range(Lauta.SARAKKEIDEN_MAARA)] for j in range(Lauta.RIVIEN_MAARA)])
        self.assertEqual(self.lauta.kenen_vuoro, Lauta.KELTAISEN_VUORO)
        
    def test_lisaa_keltainen_toimii(self):
        self.lauta.lisaa_keltainen(1)
        self.assertEqual(self.lauta.ruudukko[5][1], 'K')
        self.lauta.lisaa_keltainen(1)
        self.assertEqual(self.lauta.ruudukko[4][1], 'K')
        self.lauta.lisaa_keltainen(1)
        self.lauta.lisaa_keltainen(1)
        self.lauta.lisaa_keltainen(1)
        self.lauta.lisaa_keltainen(1)
        self.assertEqual(self.lauta.ruudukko[0][1], 'K')
        self.lauta.lisaa_keltainen(1)
        self.assertEqual(self.lauta.ruudukko[0][1], 'K')
        
    def test_lisaa_punainen_toimii(self):
        self.lauta.lisaa_punainen(2)
        self.assertEqual(self.lauta.ruudukko[5][2], 'P')
        self.lauta.lisaa_punainen(2)
        self.assertEqual(self.lauta.ruudukko[4][2], 'P')
        self.lauta.lisaa_punainen(2)
        self.lauta.lisaa_punainen(2)
        self.lauta.lisaa_punainen(2)
        self.lauta.lisaa_punainen(2)
        self.assertEqual(self.lauta.ruudukko[0][2], 'P')
        self.lauta.lisaa_punainen(2)
        self.assertEqual(self.lauta.ruudukko[0][2], 'P')
