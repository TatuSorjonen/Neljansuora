import pygame
import os
import math
from lauta import Lauta, Tulos
    

class Neljansuora:

    RUUDUN_KOKO = 150
    IKKUNAN_LEVEYS = RUUDUN_KOKO * Lauta.SARAKKEIDEN_MAARA
    IKKUNAN_KORKEUS = RUUDUN_KOKO * Lauta.RIVIEN_MAARA
    POHJAVARI = (255,250,240)
    VASTAVARI = (28,134,238)
    VIIVAN_LEVEYS = 5
        
    def __init__(self):
        pygame.init()
        self.lauta = Lauta()
        self.KELTAINEN_NAPPI = pygame.transform.scale(pygame.image.load\
        ("src/kuvat/keltainen.jpeg"), (Neljansuora.RUUDUN_KOKO, Neljansuora.RUUDUN_KOKO))
        self.PUNAINEN_NAPPI = pygame.transform.scale(pygame.image.load\
        ("src/kuvat/punainen.jpeg"), (Neljansuora.RUUDUN_KOKO, Neljansuora.RUUDUN_KOKO))
        
        self.ikkuna = pygame.display.set_mode((Neljansuora.IKKUNAN_LEVEYS, Neljansuora.IKKUNAN_KORKEUS))
        self.ikkuna.fill(Neljansuora.POHJAVARI)

        
#rivi = 6
#sarake = 7
#lauta = [[0] * sarake for _ in range(ROWS)]
#pygame.display.flip()

    def aloita_peli(self):
        
        while True:

            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    pygame.quit()
                elif tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                    self.aseta_merkki(tapahtuma.pos[0], tapahtuma.pos[1])
    
            self.piirra_taulukko()
            pygame.display.update()
        
    
    def piirra_taulukko(self):
        for x in range(0, Neljansuora.IKKUNAN_LEVEYS, Neljansuora.RUUDUN_KOKO):
            for y in range(0, Neljansuora.IKKUNAN_KORKEUS, Neljansuora.RUUDUN_KOKO):
                ruutu = pygame.Rect(x, y, Neljansuora.IKKUNAN_LEVEYS, Neljansuora.IKKUNAN_KORKEUS)
                pygame.draw.rect(self.ikkuna, Neljansuora.VASTAVARI, ruutu, Neljansuora.VIIVAN_LEVEYS)
                
    def aseta_merkki(self, hiiri_x, hiiri_y):
        sarake = math.floor(hiiri_x / Neljansuora.RUUDUN_KOKO)
        #rivi = math.floor(hiiri_y / Neljansuora.RUUDUN_KOKO)
        
        #debug
        print(f"sarake:{sarake}")
        print(f"Kenenvuoro:{self.lauta.kenen_vuoro}") 
        
        if self.lauta.kenen_vuoro == Lauta.KELTAISEN_VUORO:
            self.lauta.tulosta_lauta()
            self.lauta.lisaa_keltainen(sarake)
        elif self.lauta.kenen_vuoro == Lauta.PUNAISEN_VUORO:
            self.lauta.tulosta_lauta() #debug muuta
            self.lauta.lisaa_punainen(sarake)
        self.piirra_tilanne()
        
    def piirra_tilanne(self):
        self.piirra_taulukko()
        
        for x_ruutu in range(0, self.lauta.SARAKKEIDEN_MAARA):
            for y_ruutu in range(0, self.lauta.RIVIEN_MAARA):
                x_koordinaatti = Neljansuora.RUUDUN_KOKO * x_ruutu
                y_koordinaatti = Neljansuora.RUUDUN_KOKO * y_ruutu
                if self.lauta.ruudukko[y_ruutu][x_ruutu] == 'K':
                    self.ikkuna.blit(self.KELTAINEN_NAPPI, (x_koordinaatti, y_koordinaatti))
                elif self.lauta.ruudukko[y_ruutu][x_ruutu] == 'P':
                    self.ikkuna.blit(self.PUNAINEN_NAPPI, (x_koordinaatti, y_koordinaatti))
