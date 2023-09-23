import pygame
import os
import math
import copy
from lauta import Lauta, Tulos
#from lautaa import Lauta, Tulos
    

class Neljansuora:

    RUUDUN_KOKO = 150
    IKKUNAN_LEVEYS = RUUDUN_KOKO * Lauta.SARAKKEIDEN_MAARA
    IKKUNAN_KORKEUS = RUUDUN_KOKO * Lauta.RIVIEN_MAARA
    POHJAVARI = (255,250,240)
    VASTAVARI = (28,134,238)
    VIIVAN_LEVEYS = 5
        
    def __init__(self):
        self.lauta = Lauta()
        self.KELTAINEN_NAPPI = pygame.transform.scale(pygame.image.load\
        ("src/kuvat/keltainen.jpeg"), (Neljansuora.RUUDUN_KOKO, Neljansuora.RUUDUN_KOKO))
        self.PUNAINEN_NAPPI = pygame.transform.scale(pygame.image.load\
        ("src/kuvat/punainen.jpeg"), (Neljansuora.RUUDUN_KOKO, Neljansuora.RUUDUN_KOKO))
        
        self.ikkuna = pygame.display.set_mode((Neljansuora.IKKUNAN_LEVEYS, Neljansuora.IKKUNAN_KORKEUS))
        self.ikkuna.fill(Neljansuora.POHJAVARI)


    def aloita_peli(self):
        '''Alustaa pygamen ja aloittaa pelin. Pyörii loputtomassa for loopissa kunnes painetaan raksia
        tai hiiren vasemmalla lautaa.
        '''
        
        pygame.init()
        
        
        while True:

            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    pygame.quit()
                elif tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                    self.aseta_merkki(tapahtuma.pos[0], tapahtuma.pos[1])
    
            self.piirra_taulukko()
            pygame.display.update()
        
    
    def piirra_taulukko(self):
        '''Piirtää taulukon neljansuora pelille pygamen ikkunaan
        '''

        for x in range(0, Neljansuora.IKKUNAN_LEVEYS, Neljansuora.RUUDUN_KOKO):
            for y in range(0, Neljansuora.IKKUNAN_KORKEUS, Neljansuora.RUUDUN_KOKO):
                ruutu = pygame.Rect(x, y, Neljansuora.IKKUNAN_LEVEYS, Neljansuora.IKKUNAN_KORKEUS)
                pygame.draw.rect(self.ikkuna, Neljansuora.VASTAVARI, ruutu, Neljansuora.VIIVAN_LEVEYS)
                
    def aseta_merkki(self, hiiri_x, hiiri_y):
        '''Asettaa merkin oikeaan kohtaan laudalle käyttämällä Lauta luokan metodeita lisaa_nappula tai 
        lisaa_paras_siirto riippuen kumman pelaajan vuoro on
        
        Parametrit:
            hiiri_x: X koordinaattii johon painettiin
            hiiri_y: Y koordinaatti johon painettiin
        '''
 
        sarake = math.floor(hiiri_x / Neljansuora.RUUDUN_KOKO)
        #rivi = math.floor(hiiri_y / Neljansuora.RUUDUN_KOKO)

        vuoro = self.lauta.kenen_vuoro(self.lauta.ruudukko) 
        
        if vuoro == Lauta.KELTAINEN:
            self.lauta.lisaa_nappula(sarake, self.lauta.ruudukko)
        elif vuoro == Lauta.PUNAINEN:
            self.lauta.lisaa_paras_siirto()
      
        self.piirra_tilanne()
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        
        if tilanne != Tulos.MENEILLAAN:
            self.lauta.tulosta_lauta(self.lauta.ruudukko)
            input(f'TULOS: {tilanne}')
        
    def piirra_tilanne(self):
        '''Piirtää tilanteen pygamen ikkunaan Lauta luokan ruudukosta
        '''

        self.piirra_taulukko()
        
        for x_ruutu in range(0, self.lauta.SARAKKEIDEN_MAARA):
            for y_ruutu in range(0, self.lauta.RIVIEN_MAARA):
                x_koordinaatti = Neljansuora.RUUDUN_KOKO * x_ruutu
                y_koordinaatti = Neljansuora.RUUDUN_KOKO * y_ruutu
                if self.lauta.ruudukko[y_ruutu][x_ruutu] == 'K':
                    self.ikkuna.blit(self.KELTAINEN_NAPPI, (x_koordinaatti, y_koordinaatti))
                elif self.lauta.ruudukko[y_ruutu][x_ruutu] == 'P':
                    self.ikkuna.blit(self.PUNAINEN_NAPPI, (x_koordinaatti, y_koordinaatti))
