import pygame
import os
import math
import copy
from lauta import Lauta, Tulos

class Neljansuora:

    RUUDUN_KOKO = 150
    VALIKON_KOKO = 100
    IKKUNAN_LEVEYS = RUUDUN_KOKO * Lauta.SARAKKEIDEN_MAARA
    IKKUNAN_KORKEUS = RUUDUN_KOKO * Lauta.RIVIEN_MAARA + VALIKON_KOKO
    POHJAVARI = (255,250,240)
    VASTAVARI = (28,134,238)
    VIIVAN_LEVEYS = 5
    NAPPIEN_MAARA = 3
        
    def __init__(self):
        self.lauta = Lauta()
        self.KELTAINEN_NAPPI = pygame.transform.scale(pygame.image.load\
        ("src/kuvat/keltainen.jpeg"), (Neljansuora.RUUDUN_KOKO, Neljansuora.RUUDUN_KOKO))
        self.PUNAINEN_NAPPI = pygame.transform.scale(pygame.image.load\
        ("src/kuvat/punainen.jpeg"), (Neljansuora.RUUDUN_KOKO, Neljansuora.RUUDUN_KOKO))
        
        self.ikkuna = pygame.display.set_mode((Neljansuora.IKKUNAN_LEVEYS, Neljansuora.IKKUNAN_KORKEUS))
        self.ikkuna.fill(Neljansuora.POHJAVARI)
        self.on_kaynnissa = True


    def aloita_peli(self):
        '''Alustaa pygamen ja aloittaa pelin. Pyörii loputtomassa for loopissa kunnes painetaan raksia
        tai hiiren vasemmalla lautaa.
        '''
        
        pygame.init()
        
        
        while self.on_kaynnissa:

            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    self.on_kaynnissa = False
                elif tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                    self.tarkista_nappulan_painallus(tapahtuma.pos[0], tapahtuma.pos[1])
                    self.aseta_merkki(tapahtuma.pos[0], tapahtuma.pos[1])       
            self.piirra_ikkuna()
        pygame.quit()
        
    def piirra_ikkuna(self):
        self.piirra_taulukko()
        self.piirra_napit()
        self.piirra_tekstit()
        pygame.display.update()
        
    def piirra_tekstit(self):
        minun_fontti = 'arial'
        fontin_koko = 45
        fontin_vari = (0, 0, 0)
        fontti = pygame.font.SysFont(minun_fontti, fontin_koko)
        status = (Neljansuora.IKKUNAN_LEVEYS / 2, Neljansuora.VALIKON_KOKO / 2)
        sulje = (Neljansuora.IKKUNAN_LEVEYS * (((Neljansuora.NAPPIEN_MAARA * 2)-1)/(Neljansuora.NAPPIEN_MAARA * 2)), Neljansuora.VALIKON_KOKO / 2)
        aloita_alusta = (Neljansuora.IKKUNAN_LEVEYS / (Neljansuora.NAPPIEN_MAARA * 2), Neljansuora.VALIKON_KOKO / 2)
        
        
        #Status teksti
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        if tilanne == Tulos.MENEILLAAN:
            if self.lauta.kenen_vuoro(self.lauta.ruudukko) == Lauta.KELTAINEN:
                vuoro = "Keltaisen vuoro"
            else:
                vuoro = "Punaisen vuoro"
        elif tilanne == Tulos.TASAPELI:
            vuoro = "Tasapeli"
        elif tilanne == Tulos.KELTAINEN_VOITTI:
            vuoro = "Keltainen voitti"
        elif tilanne == Tulos.PUNAINEN_VOITTI:
            vuoro = "Punainen voitti"

        status_teksti = fontti.render(vuoro, 1, fontin_vari)
        status_rect = status_teksti.get_rect(center=status)
        self.ikkuna.blit(status_teksti, status_rect)
        
        
        #Sulje teksti
        sulje_teksti = fontti.render("Sulje peli", 1, fontin_vari)
        sulje_rect = sulje_teksti.get_rect(center=sulje)
        self.ikkuna.blit(sulje_teksti, sulje_rect)
        
        
        #Aloita alusta teskti
        aloita_alusta_teksti = fontti.render("Aloita alusta", 1, fontin_vari)
        aloita_alusta_rect = aloita_alusta_teksti.get_rect(center=aloita_alusta)
        self.ikkuna.blit(aloita_alusta_teksti, aloita_alusta_rect)
    
    def piirra_taulukko(self):
        '''Piirtää taulukon neljansuora pelille pygamen ikkunaan
        '''

        for x in range(0, Neljansuora.IKKUNAN_LEVEYS, Neljansuora.RUUDUN_KOKO):
            for y in range(Neljansuora.VALIKON_KOKO, Neljansuora.IKKUNAN_KORKEUS, Neljansuora.RUUDUN_KOKO):
                ruutu = pygame.Rect(x, y, Neljansuora.IKKUNAN_LEVEYS, Neljansuora.IKKUNAN_KORKEUS)
                pygame.draw.rect(self.ikkuna, Neljansuora.VASTAVARI, ruutu, Neljansuora.VIIVAN_LEVEYS)
        
    def piirra_napit(self):
        nappien_vari = Neljansuora.VASTAVARI
        nappien_reunan_vari = (61, 89, 171)
        nappien_reunan_koko = 10
        
        #Ensimmäinen nappi
        pygame.draw.rect(self.ikkuna, nappien_vari, (0, 0, Neljansuora.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA,\
                                                     Neljansuora.VALIKON_KOKO))
        pygame.draw.rect(self.ikkuna, nappien_reunan_vari, \
                         pygame.Rect((0, 0, Neljansuora.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA,\
                                      Neljansuora.VALIKON_KOKO - nappien_reunan_koko / 2)), nappien_reunan_koko)
        
        #Status
        pygame.draw.rect(self.ikkuna, nappien_vari, (Neljansuora.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA,\
                                                     0, Neljansuora.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA,\
                                                     Neljansuora.VALIKON_KOKO))
        pygame.draw.rect(self.ikkuna, nappien_reunan_vari, \
                         pygame.Rect((Neljansuora.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA,\
                                      0, Neljansuora.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA,\
                                      Neljansuora.VALIKON_KOKO - nappien_reunan_koko / 2)), nappien_reunan_koko)
        
        #Kolmas nappi
        pygame.draw.rect(self.ikkuna, nappien_vari, (Neljansuora.IKKUNAN_LEVEYS - Neljansuora.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA,\
                                                     0, Neljansuora.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA, Neljansuora.VALIKON_KOKO))
        pygame.draw.rect(self.ikkuna, nappien_reunan_vari, \
                         pygame.Rect((Neljansuora.IKKUNAN_LEVEYS - Neljansuora.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA,\
                                      0, Neljansuora.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA, \
                                      Neljansuora.VALIKON_KOKO - nappien_reunan_koko / 2)), nappien_reunan_koko)
                                      
    def tarkista_nappulan_painallus(self, hiiri_x, hiiri_y):
        if hiiri_x >= Neljansuora.IKKUNAN_LEVEYS - Neljansuora.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA\
        and hiiri_y <= Neljansuora.VALIKON_KOKO:
            self.on_kaynnissa = False
            
        elif hiiri_x < Neljansuora.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA\
        and hiiri_y <= Neljansuora.VALIKON_KOKO:
            self.lauta = Lauta()
            self.ikkuna.fill(Neljansuora.POHJAVARI)
                
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
        if vuoro == Lauta.KELTAINEN and hiiri_y > 100:
            self.lauta.lisaa_nappula(sarake, self.lauta.ruudukko)
        elif vuoro == Lauta.PUNAINEN and hiiri_y > 100:
            self.lauta.lisaa_paras_siirto()
      
        self.piirra_tilanne()
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        
    def piirra_tilanne(self):
        '''Piirtää tilanteen pygamen ikkunaan Lauta luokan ruudukosta
        '''

        self.piirra_taulukko()
        
        for x_ruutu in range(0, self.lauta.SARAKKEIDEN_MAARA):
            for y_ruutu in range(0, self.lauta.RIVIEN_MAARA):
                x_koordinaatti = Neljansuora.RUUDUN_KOKO * x_ruutu
                y_koordinaatti = Neljansuora.RUUDUN_KOKO * y_ruutu
                if self.lauta.ruudukko[y_ruutu][x_ruutu] == 'K':
                    self.ikkuna.blit(self.KELTAINEN_NAPPI, (x_koordinaatti, y_koordinaatti + Neljansuora.VALIKON_KOKO))
                elif self.lauta.ruudukko[y_ruutu][x_ruutu] == 'P':
                    self.ikkuna.blit(self.PUNAINEN_NAPPI, (x_koordinaatti, y_koordinaatti + Neljansuora.VALIKON_KOKO))
