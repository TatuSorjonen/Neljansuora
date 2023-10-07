import pygame
import os
import math
import copy
from enum import Enum
from lauta import Lauta, Tulos

class Pelimuoto(Enum):
    
    YKSINPELI = 1
    HELPPO_YKSINPELI = 2
    KAKSINPELI = 3
    TEKOÄLY = 4

class Neljansuora:

    RUUDUN_KOKO = 150
    VALIKON_KOKO = 100
    IKKUNAN_LEVEYS = RUUDUN_KOKO * Lauta.SARAKKEIDEN_MAARA
    IKKUNAN_KORKEUS = RUUDUN_KOKO * Lauta.RIVIEN_MAARA + VALIKON_KOKO
    POHJAVARI = (255,250,240)
    VASTAVARI = (28,134,238)
    KELTAINEN = (204,204,0)
    PUNAINEN = (204,0,0)
    VIIVAN_LEVEYS = 5
    NAPPIEN_MAARA = 3
    PELITAPOJEN_MAARA = 4
    NAPPIEN_VARI = (153, 204, 255)
    NAPPIEN_REUNAN_VARI = (102, 178, 255)
    NAPPIEN_REUNAN_KOKO = 5
    OLETUS_FONTTI = 'freesansbold'
    PAINIKE_TEKSTIN_VARI = (0, 51, 102)
        
    def __init__(self):
        self.lauta = Lauta()
        
        self.ikkuna = pygame.display.set_mode((Neljansuora.IKKUNAN_LEVEYS, Neljansuora.IKKUNAN_KORKEUS), pygame.NOFRAME)
        self.ikkuna.fill(Neljansuora.POHJAVARI)
        self.on_kaynnissa = True
        self.pelimuoto = Pelimuoto.YKSINPELI
        self.pelaaja_aloittaa = True


    def aloitusikkuna(self):
        pygame.init()
        self.aloitusikkunan_napit()
        
        while self.on_kaynnissa:
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    self.on_kaynnissa = False
                elif tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                    self.on_kaynnissa = False
                    
        self.on_kaynnissa = True
        self.ikkuna.fill(Neljansuora.POHJAVARI)
        self.aloita_peli()
        
    def aloitusikkunan_napit(self):
        tasojen_fontin_koko = 45
        otsikoiden_fontin_koko = 100
        otsikoiden_fontin_vari = Neljansuora.PAINIKE_TEKSTIN_VARI
        nappuloiden_fontin_vari = Neljansuora.PAINIKE_TEKSTIN_VARI
        leveys_marginaali = 10
        nappien_vali = 10
        napin_leveys = (Neljansuora.IKKUNAN_LEVEYS - leveys_marginaali * 2)/4 - nappien_vali * (3/4)
        napin_korkeus = int(napin_leveys / 3)
        pelitapanapit_y = 250
        
        pelitapojen_fontti = pygame.font.SysFont(Neljansuora.OLETUS_FONTTI, tasojen_fontin_koko)
        otsikko_fontti = pygame.font.SysFont(Neljansuora.OLETUS_FONTTI, otsikoiden_fontin_koko)
        
        #Pelitapa teksti
        pelitapa = (Neljansuora.IKKUNAN_LEVEYS / 2, Neljansuora.VALIKON_KOKO)
        self.piirra_teksti(pelitapa, "Valitse pelitapa", otsikko_fontti, otsikoiden_fontin_vari)
        
        #Yksinpeli
        kaksinpeli_x = leveys_marginaali
        self.piirra_nappi(kaksinpeli_x, pelitapanapit_y, napin_leveys, napin_korkeus, 'Yksinpeli', pelitapojen_fontti, nappuloiden_fontin_vari, Neljansuora.NAPPIEN_VARI, Neljansuora.NAPPIEN_REUNAN_VARI, Neljansuora.NAPPIEN_REUNAN_KOKO)
        
        #Helppo yksinpeli
        kaksinpeli_x = leveys_marginaali + napin_leveys + nappien_vali
        self.piirra_nappi(kaksinpeli_x, pelitapanapit_y, napin_leveys, napin_korkeus, 'Helppo yksinpeli', pelitapojen_fontti, nappuloiden_fontin_vari, Neljansuora.NAPPIEN_VARI, Neljansuora.NAPPIEN_REUNAN_VARI, Neljansuora.NAPPIEN_REUNAN_KOKO)
        
        #Kaksinpeli
        kaksinpeli_x = (leveys_marginaali + napin_leveys) * 2 + nappien_vali
        self.piirra_nappi(kaksinpeli_x, pelitapanapit_y, napin_leveys, napin_korkeus, 'Kaksinpeli', pelitapojen_fontti, nappuloiden_fontin_vari, Neljansuora.NAPPIEN_VARI, Neljansuora.NAPPIEN_REUNAN_VARI, Neljansuora.NAPPIEN_REUNAN_KOKO)
        
        #Tekoälyn peli
        kaksinpeli_x = (leveys_marginaali + napin_leveys) * 3 + nappien_vali
        self.piirra_nappi(kaksinpeli_x, pelitapanapit_y, napin_leveys, napin_korkeus, 'Tekoälyn peli', pelitapojen_fontti, nappuloiden_fontin_vari, Neljansuora.NAPPIEN_VARI, Neljansuora.NAPPIEN_REUNAN_VARI, Neljansuora.NAPPIEN_REUNAN_KOKO)

        #Valise aloittaja teskti
        valitse_aloittaja = (Neljansuora.IKKUNAN_LEVEYS / 2, Neljansuora.IKKUNAN_KORKEUS / 2)
        self.piirra_teksti(valitse_aloittaja, "Valitse aloittaja", otsikko_fontti, otsikoiden_fontin_vari)
        
        aloitusvuoronapit_y = 600
        
        #Pelaaja aloittaa
        pelaaja_aloittaa_x = leveys_marginaali + napin_leveys + nappien_vali
        self.piirra_nappi(pelaaja_aloittaa_x, aloitusvuoronapit_y, napin_leveys, napin_korkeus, 'Pelaaja aloittaa', pelitapojen_fontti, nappuloiden_fontin_vari, Neljansuora.NAPPIEN_VARI, Neljansuora.NAPPIEN_REUNAN_VARI, Neljansuora.NAPPIEN_REUNAN_KOKO)
        
        #Tekoäly aloittaa
        tekoäly_aloittaa_x = (leveys_marginaali + napin_leveys) * 2 + nappien_vali
        self.piirra_nappi(tekoäly_aloittaa_x, aloitusvuoronapit_y, napin_leveys, napin_korkeus, 'Tekoäly aloittaa', pelitapojen_fontti, nappuloiden_fontin_vari, Neljansuora.NAPPIEN_VARI, Neljansuora.NAPPIEN_REUNAN_VARI, Neljansuora.NAPPIEN_REUNAN_KOKO)
        
        aloita_peli_napit_y = 800
        aloita_peli_napin_leveys = (Neljansuora.IKKUNAN_LEVEYS - leveys_marginaali * 2) / 2 
        
        #Aloita peli
        aloita_peli_x = Neljansuora.IKKUNAN_LEVEYS / 4 + leveys_marginaali / 2
        self.piirra_nappi(aloita_peli_x, aloita_peli_napit_y, aloita_peli_napin_leveys, napin_korkeus, 'Aloita peli', pelitapojen_fontti, nappuloiden_fontin_vari, Neljansuora.NAPPIEN_VARI, Neljansuora.NAPPIEN_REUNAN_VARI, Neljansuora.NAPPIEN_REUNAN_KOKO)
        
        pygame.display.update()
        
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
        
        while self.on_kaynnissa:

            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    self.on_kaynnissa = False
                elif tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                    self.tarkista_hiiren_painallus(tapahtuma.pos[0], tapahtuma.pos[1])
                    
        pygame.quit()
        
    def piirra_ikkuna(self):
        self.ikkuna.fill(Neljansuora.POHJAVARI)
        self.piirra_taulukko()
        self.piirra_pelin_napit_ja_tekstit()
        self.piirra_tilanne()
        pygame.display.update()
        
    def piirra_pelin_napit_ja_tekstit(self):
        minun_fontti = 'freesansbold'
        fontin_koko = 45
        status_fontin_vari = Neljansuora.KELTAINEN
        nappuloiden_fontin_vari = Neljansuora.PAINIKE_TEKSTIN_VARI
        fontti = pygame.font.SysFont(minun_fontti, fontin_koko)
        
        
        nappien_vari = (153, 204, 255)
        nappien_reunan_vari = (102, 178, 255)
        nappien_reunan_koko = 5
        
        #Aloita alusta
        aloita_alusta_x = 0
        aloita_alusta_y = 0
        aloita_alusta_napin_leveys = Neljansuora.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA
        aloita_alusta_napin_korkeus = Neljansuora.VALIKON_KOKO
        self.piirra_nappi(aloita_alusta_x, aloita_alusta_y, aloita_alusta_napin_leveys, aloita_alusta_napin_korkeus, 'Aloita alusta', fontti, nappuloiden_fontin_vari, Neljansuora.NAPPIEN_VARI, Neljansuora.NAPPIEN_REUNAN_VARI, Neljansuora.NAPPIEN_REUNAN_KOKO)
        
        #Sulje
        sulje_x = Neljansuora.IKKUNAN_LEVEYS - Neljansuora.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA
        sulje_y = 0
        sulje_napin_leveys = Neljansuora.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA
        sulje_napin_korkeus = Neljansuora.VALIKON_KOKO
        self.piirra_nappi(sulje_x, sulje_y, sulje_napin_leveys, sulje_napin_korkeus, 'Sulje peli', fontti, nappuloiden_fontin_vari, Neljansuora.NAPPIEN_VARI, Neljansuora.NAPPIEN_REUNAN_VARI, Neljansuora.NAPPIEN_REUNAN_KOKO)
        
        #Status
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        taustan_vari = (220,220,220)
        if tilanne == Tulos.MENEILLAAN:
            if self.lauta.kenen_vuoro(self.lauta.ruudukko) == Lauta.KELTAINEN:
                vuoro = "Keltaisen vuoro"
                status_fontin_vari = Neljansuora.KELTAINEN
            else:
                vuoro = "Punaisen vuoro"
                status_fontin_vari = Neljansuora.PUNAINEN
        elif tilanne == Tulos.TASAPELI:
            vuoro = "Tasapeli"
            status_fontin_vari = (255,255,255)
        elif tilanne == Tulos.KELTAINEN_VOITTI:
            vuoro = "Keltainen voitti"
            status_fontin_vari = Neljansuora.KELTAINEN
        elif tilanne == Tulos.PUNAINEN_VOITTI:
            vuoro = "Punainen voitti"
            status_fontin_vari = Neljansuora.PUNAINEN
            
        #Statuksen tausta
        taustan_vari = Neljansuora.VASTAVARI
        pygame.draw.rect(self.ikkuna, taustan_vari, (Neljansuora.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA,\
                                                     0, Neljansuora.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA,\
                                                     Neljansuora.VALIKON_KOKO))
                                                     
        status = (Neljansuora.IKKUNAN_LEVEYS / 2, Neljansuora.VALIKON_KOKO / 2)
        self.piirra_teksti(status, vuoro, fontti, status_fontin_vari)
    
    def piirra_taulukko(self):
        '''Piirtää taulukon neljansuora pelille pygamen ikkunaan
        '''

        for x in range(0, Neljansuora.IKKUNAN_LEVEYS, Neljansuora.RUUDUN_KOKO):
            for y in range(Neljansuora.VALIKON_KOKO, Neljansuora.IKKUNAN_KORKEUS, Neljansuora.RUUDUN_KOKO):
                ruutu = pygame.Rect(x, y, Neljansuora.IKKUNAN_LEVEYS, Neljansuora.IKKUNAN_KORKEUS)
                pygame.draw.rect(self.ikkuna, Neljansuora.VASTAVARI, ruutu, Neljansuora.VIIVAN_LEVEYS)
                                      
    def tarkista_hiiren_painallus(self, hiiri_x, hiiri_y):
        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        if tilanne == Tulos.MENEILLAAN and hiiri_y > Neljansuora.VALIKON_KOKO:
            self.aseta_merkki(hiiri_x, hiiri_y) 
        elif hiiri_x >= Neljansuora.IKKUNAN_LEVEYS - Neljansuora.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA\
        and hiiri_y <= Neljansuora.VALIKON_KOKO:
            self.on_kaynnissa = False
            
        elif hiiri_x < Neljansuora.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA\
        and hiiri_y <= Neljansuora.VALIKON_KOKO:
            self.lauta = Lauta()
            self.ikkuna.fill(Neljansuora.POHJAVARI)
            self.aloitusikkuna()
                
    def aseta_merkki(self, hiiri_x, hiiri_y):
        '''Asettaa merkin oikeaan kohtaan laudalle käyttämällä Lauta luokan metodeita lisaa_nappula tai 
        lisaa_paras_siirto riippuen kumman pelaajan vuoro on
        
        Parametrit:
            hiiri_x: X koordinaattii johon painettiin
            hiiri_y: Y koordinaatti johon painettiin
        '''
        
        pygame.mixer.music.load('Pudotus.mp3')
        sarake = math.floor(hiiri_x / Neljansuora.RUUDUN_KOKO)
        rivi = math.floor(hiiri_y / Neljansuora.RUUDUN_KOKO)

        vuoro = self.lauta.kenen_vuoro(self.lauta.ruudukko) 
        if vuoro == Lauta.KELTAINEN and hiiri_y > 100:
            rivi = self.lauta.lisaa_nappula(sarake, self.lauta.ruudukko)
            self.animoi_pudotus(sarake, rivi, vuoro)
            self.piirra_ikkuna()
            pygame.display.update()
            pygame.mixer.music.play(1)
            vuoro = self.lauta.kenen_vuoro(self.lauta.ruudukko)
            sarake, rivi = self.lauta.lisaa_paras_siirto() #Jos halutaan pelaavan heti
            self.animoi_pudotus(sarake, rivi, vuoro)
            pygame.mixer.music.play(1)
            self.piirra_ikkuna()
        elif vuoro == Lauta.PUNAINEN and hiiri_y > 100:
            self.lauta.lisaa_paras_siirto()

        #self.piirra_tilanne()
        #tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        
    def animoi_pudotus(self, sarake, rivi, vuoro):
        nappulan_vari = Neljansuora.KELTAINEN
        if vuoro == self.lauta.PUNAINEN:
            nappulan_vari = Neljansuora.PUNAINEN
        x = Neljansuora.RUUDUN_KOKO * sarake + int(Neljansuora.RUUDUN_KOKO / 2)
        y = Neljansuora.VALIKON_KOKO + int(Neljansuora.RUUDUN_KOKO / 2)
        y_loppu = Neljansuora.RUUDUN_KOKO * rivi + int(Neljansuora.RUUDUN_KOKO / 2) + Neljansuora.VALIKON_KOKO
        
        for i in range(y, y_loppu):
            self.piirra_taulukko()
            pygame.draw.circle(self.ikkuna, nappulan_vari, (x, i), int(Neljansuora.RUUDUN_KOKO / 2))
            pygame.display.update()
            pygame.draw.circle(self.ikkuna, Neljansuora.POHJAVARI, (x, i), int(Neljansuora.RUUDUN_KOKO / 2))
    
    def piirra_tilanne(self):
        '''Piirtää tilanteen pygamen ikkunaan Lauta luokan ruudukosta
        '''

        self.piirra_taulukko()
        
        for x_ruutu in range(0, self.lauta.SARAKKEIDEN_MAARA):
            for y_ruutu in range(0, self.lauta.RIVIEN_MAARA):
                x_koordinaatti = Neljansuora.RUUDUN_KOKO * x_ruutu + int(Neljansuora.RUUDUN_KOKO / 2)
                y_koordinaatti = Neljansuora.RUUDUN_KOKO * y_ruutu + int(Neljansuora.RUUDUN_KOKO / 2) + Neljansuora.VALIKON_KOKO
                if self.lauta.ruudukko[y_ruutu][x_ruutu] == 'K':
                    pygame.draw.circle(self.ikkuna, Neljansuora.KELTAINEN, (x_koordinaatti, y_koordinaatti), int(Neljansuora.RUUDUN_KOKO / 2 - Neljansuora.VIIVAN_LEVEYS))
                elif self.lauta.ruudukko[y_ruutu][x_ruutu] == 'P':
                    pygame.draw.circle(self.ikkuna, Neljansuora.PUNAINEN, (x_koordinaatti, y_koordinaatti), int(Neljansuora.RUUDUN_KOKO / 2 - Neljansuora.VIIVAN_LEVEYS))
