import pygame
import os
import math
import copy
from enum import Enum
from lauta import Lauta, Tulos
from maaritykset import Pelimuoto, Maaritykset, Aloitusikkuna

class Neljansuora:

    NAPPIEN_MAARA = 3
        
    def __init__(self):
        self.on_kaynnissa = False
        self.pelimuoto = Pelimuoto.YKSINPELI
        self.aloittaja = Aloitusikkuna.PELAAJA_ALOITTAA

        self.ikkuna = pygame.display.set_mode((Maaritykset.IKKUNAN_LEVEYS, Maaritykset.IKKUNAN_KORKEUS), pygame.NOFRAME)
        self.ikkuna.fill(Maaritykset.POHJAVARI)
        pygame.init()

        self.lauta = Lauta()

    def alusta_peli(self, pelimuoto, aloittaja):
        self.on_kaynnissa = True
        self.pelimuoto = pelimuoto
        self.aloittaja = aloittaja
        self.ikkuna.fill(Maaritykset.POHJAVARI)
        self.lauta = Lauta()

    def lue_maaritykset(self):
        #print('toimii')
        aloitusikkuna = Aloitusikkuna(self.ikkuna)
        pelimuoto, aloittaja = aloitusikkuna.lue_pelitapa()
        #print(f'Pelimuoto on: {pelimuoto}, Aloittaja on: {aloittaja}')
        self.alusta_peli(pelimuoto, aloittaja)
        self.aloita_peli()
        
    def piirra_nappi(self, x, y, leveys, korkeus, teksti, fontti, fontin_vari, taustavari, reunavari, reunan_koko):
    
        koordinaatti = (x,y,leveys,korkeus)

        pygame.draw.rect(self.ikkuna, taustavari, pygame.Rect(koordinaatti))
        pygame.draw.rect(self.ikkuna, reunavari, pygame.Rect(koordinaatti), reunan_koko)
        keskikohta = (x + leveys / 2, y + korkeus / 2)
        
        self.piirra_teksti(keskikohta, teksti, fontti, fontin_vari)
        
    def piirra_teksti(self, koordinaatti, teksti, fontti, fontin_vari):
        teksti = fontti.render(teksti, 1, fontin_vari)
        rect = teksti.get_rect(center=koordinaatti)
        self.ikkuna.blit(teksti, rect)

    def aloita_peli(self):
        '''Alustaa pygamen ja aloittaa pelin. Pyörii loputtomassa for loopissa kunnes painetaan raksia
        tai hiiren vasemmalla lautaa.
        '''

        self.piirra_ikkuna()
        #print(self.pelimuoto) #Debug
        
        while self.on_kaynnissa:

            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    self.on_kaynnissa = False
                elif tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                    self.tarkista_hiiren_painallus(tapahtuma.pos[0], tapahtuma.pos[1])
                    
        pygame.quit()
        
    def piirra_ikkuna(self):
        self.ikkuna.fill(Maaritykset.POHJAVARI)
        self.piirra_taulukko()
        self.piirra_pelin_napit_ja_tekstit()
        self.piirra_tilanne()
        pygame.display.update()
        
    def piirra_pelin_napit_ja_tekstit(self):
        minun_fontti = 'freesansbold'
        fontin_koko = 45
        status_fontin_vari = Maaritykset.KELTAINEN
        nappuloiden_fontin_vari = Maaritykset.NAPPIEN_TEKSTIN_VARI
        fontti = pygame.font.SysFont(minun_fontti, fontin_koko)

        #Aloita alusta
        aloita_alusta_x = 0
        aloita_alusta_y = 0
        aloita_alusta_napin_leveys = Maaritykset.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA
        aloita_alusta_napin_korkeus = Maaritykset.VALIKON_KOKO
        self.piirra_nappi(aloita_alusta_x, aloita_alusta_y, aloita_alusta_napin_leveys, aloita_alusta_napin_korkeus, 'Aloita alusta', fontti, nappuloiden_fontin_vari, Maaritykset.NAPPIEN_VARI, Maaritykset.NAPPIEN_REUNAN_VARI, Maaritykset.NAPPIEN_REUNAN_KOKO)
        
        #Sulje
        sulje_x = Maaritykset.IKKUNAN_LEVEYS - Maaritykset.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA
        sulje_y = 0
        sulje_napin_leveys = Maaritykset.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA
        sulje_napin_korkeus = Maaritykset.VALIKON_KOKO
        self.piirra_nappi(sulje_x, sulje_y, sulje_napin_leveys, sulje_napin_korkeus, 'Sulje peli', fontti, nappuloiden_fontin_vari, Maaritykset.NAPPIEN_VARI, Maaritykset.NAPPIEN_REUNAN_VARI, Maaritykset.NAPPIEN_REUNAN_KOKO)
        
        #Status
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        taustan_vari = (220,220,220)
        if tilanne == Tulos.MENEILLAAN:
            if self.lauta.kenen_vuoro(self.lauta.ruudukko) == Lauta.KELTAINEN:
                vuoro = "Keltaisen vuoro"
                status_fontin_vari = Maaritykset.KELTAINEN
            else:
                vuoro = "Punaisen vuoro"
                status_fontin_vari = Maaritykset.PUNAINEN
        elif tilanne == Tulos.TASAPELI:
            vuoro = "Tasapeli"
            status_fontin_vari = (255,255,255)
        elif tilanne == Tulos.KELTAINEN_VOITTI:
            vuoro = "Keltainen voitti"
            status_fontin_vari = Maaritykset.KELTAINEN
        elif tilanne == Tulos.PUNAINEN_VOITTI:
            vuoro = "Punainen voitti"
            status_fontin_vari = Maaritykset.PUNAINEN
            
        #Statuksen tausta
        taustan_vari = Maaritykset.VASTAVARI
        pygame.draw.rect(self.ikkuna, taustan_vari, (Maaritykset.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA,\
                                                     0, Maaritykset.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA,\
                                                     Maaritykset.VALIKON_KOKO))
                                                     
        status = (Maaritykset.IKKUNAN_LEVEYS / 2, Maaritykset.VALIKON_KOKO / 2)
        self.piirra_teksti(status, vuoro, fontti, status_fontin_vari)
    
    def piirra_taulukko(self):
        '''Piirtää taulukon neljansuora pelille pygamen ikkunaan
        '''

        for x in range(0, Maaritykset.IKKUNAN_LEVEYS, Maaritykset.RUUDUN_KOKO):
            for y in range(Maaritykset.VALIKON_KOKO, Maaritykset.IKKUNAN_KORKEUS, Maaritykset.RUUDUN_KOKO):
                ruutu = pygame.Rect(x, y, Maaritykset.IKKUNAN_LEVEYS, Maaritykset.IKKUNAN_KORKEUS)
                pygame.draw.rect(self.ikkuna, Maaritykset.VASTAVARI, ruutu, Maaritykset.VIIVAN_LEVEYS)
                                      
    def tarkista_hiiren_painallus(self, hiiri_x, hiiri_y):
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        if tilanne == Tulos.MENEILLAAN and hiiri_y > Maaritykset.VALIKON_KOKO:
            self.aseta_merkki(hiiri_x, hiiri_y) 
        elif hiiri_x >= Maaritykset.IKKUNAN_LEVEYS - Maaritykset.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA\
        and hiiri_y <= Maaritykset.VALIKON_KOKO:
            self.on_kaynnissa = False
            
        elif hiiri_x < Maaritykset.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA\
        and hiiri_y <= Maaritykset.VALIKON_KOKO:
            self.on_kaynnissa = False
            self.lue_maaritykset()
            
                
    def aseta_merkki(self, hiiri_x, hiiri_y):
        '''Asettaa merkin oikeaan kohtaan laudalle käyttämällä Lauta luokan metodeita lisaa_nappula tai 
        lisaa_paras_siirto riippuen kumman pelaajan vuoro on
        
        Parametrit:
            hiiri_x: X koordinaattii johon painettiin
            hiiri_y: Y koordinaatti johon painettiin
        '''
        
        #pygame.mixer.music.load('Pudotus.mp3')
        sarake = math.floor(hiiri_x / Maaritykset.RUUDUN_KOKO)
        rivi = math.floor(hiiri_y / Maaritykset.RUUDUN_KOKO)

        vuoro = self.lauta.kenen_vuoro(self.lauta.ruudukko) 
        if vuoro == Lauta.KELTAINEN and hiiri_y > 100:
            rivi = self.lauta.lisaa_nappula(sarake, self.lauta.ruudukko)
            self.animoi_pudotus(sarake, rivi, vuoro)
            self.piirra_ikkuna()
            pygame.display.update()
            #pygame.mixer.music.play(1)
            vuoro = self.lauta.kenen_vuoro(self.lauta.ruudukko)
            sarake, rivi = self.lauta.lisaa_paras_siirto() #Jos halutaan pelaavan heti
            self.animoi_pudotus(sarake, rivi, vuoro)
            #pygame.mixer.music.play(1)
            self.piirra_ikkuna()
        elif vuoro == Lauta.PUNAINEN and hiiri_y > 100:
            self.lauta.lisaa_paras_siirto()

        #self.piirra_tilanne()
        #tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        
    def animoi_pudotus(self, sarake, rivi, vuoro):
        pygame.mixer.music.load('Pudotus.mp3')
        nappulan_vari = Maaritykset.KELTAINEN
        if vuoro == self.lauta.PUNAINEN:
            nappulan_vari = Maaritykset.PUNAINEN
        x = Maaritykset.RUUDUN_KOKO * sarake + int(Maaritykset.RUUDUN_KOKO / 2)
        y = Maaritykset.VALIKON_KOKO + int(Maaritykset.RUUDUN_KOKO / 2)
        y_loppu = Maaritykset.RUUDUN_KOKO * rivi + int(Maaritykset.RUUDUN_KOKO / 2) + Maaritykset.VALIKON_KOKO
        
        for i in range(y, y_loppu):
            self.piirra_taulukko()
            pygame.draw.circle(self.ikkuna, nappulan_vari, (x, i), int(Maaritykset.RUUDUN_KOKO / 2))
            pygame.display.update()
            pygame.draw.circle(self.ikkuna, Maaritykset.POHJAVARI, (x, i), int(Maaritykset.RUUDUN_KOKO / 2))
        pygame.mixer.music.play(1)
    
    def piirra_tilanne(self):
        '''Piirtää tilanteen pygamen ikkunaan Lauta luokan ruudukosta
        '''

        self.piirra_taulukko()
        
        for x_ruutu in range(0, self.lauta.SARAKKEIDEN_MAARA):
            for y_ruutu in range(0, self.lauta.RIVIEN_MAARA):
                x_koordinaatti = Maaritykset.RUUDUN_KOKO * x_ruutu + int(Maaritykset.RUUDUN_KOKO / 2)
                y_koordinaatti = Maaritykset.RUUDUN_KOKO * y_ruutu + int(Maaritykset.RUUDUN_KOKO / 2) + Maaritykset.VALIKON_KOKO
                if self.lauta.ruudukko[y_ruutu][x_ruutu] == 'K':
                    pygame.draw.circle(self.ikkuna, Maaritykset.KELTAINEN, (x_koordinaatti, y_koordinaatti), int(Maaritykset.RUUDUN_KOKO / 2 - Maaritykset.VIIVAN_LEVEYS))
                elif self.lauta.ruudukko[y_ruutu][x_ruutu] == 'P':
                    pygame.draw.circle(self.ikkuna, Maaritykset.PUNAINEN, (x_koordinaatti, y_koordinaatti), int(Maaritykset.RUUDUN_KOKO / 2 - Maaritykset.VIIVAN_LEVEYS))
