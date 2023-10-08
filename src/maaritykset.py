import pygame
import os
from enum import Enum
#from neljansuora import Neljansuora, Pelimuoto
from lauta import Lauta, Tulos

class Pelimuoto(Enum):
    
    YKSINPELI = 'Yksinpeli'
    HELPPO_YKSINPELI = 'Helppo yksinpeli'
    KAKSINPELI = 'Kaksinpeli'
    TEKOÄLY = 'Tekoäly peli'

class Maaritykset:

    #Kummallekin näkymälle yhteiset määritykset
    RUUDUN_KOKO = 150
    VALIKON_KOKO = 100
    IKKUNAN_LEVEYS = RUUDUN_KOKO * Lauta.SARAKKEIDEN_MAARA
    IKKUNAN_KORKEUS = RUUDUN_KOKO * Lauta.RIVIEN_MAARA + VALIKON_KOKO
    POHJAVARI = (255,250,240)
    VASTAVARI = (28,134,238)
    KELTAINEN = (204,204,0)
    PUNAINEN = (204,0,0)
    NAPPIEN_VARI = (153, 204, 255)
    NAPPIEN_REUNAN_VARI = (102, 178, 255)
    NAPPIEN_REUNAN_KOKO = 5
    OLETUS_FONTTI = 'freesansbold'
    NAPPIEN_TEKSTIN_VARI = (0, 51, 102)
    NAPPIEN_FONTIN_KOKO = 45
     
    #Alkuvalikon määritykset
    PELITAPOJEN_MAARA = 4
    LEVEYS_MARGINAALI = 10
    NAPPIEN_VALI = 10
    NAPIN_LEVEYS = (IKKUNAN_LEVEYS - LEVEYS_MARGINAALI * 2)/4 - NAPPIEN_VALI * (3/4)
    NAPIN_KORKEUS = int(NAPIN_LEVEYS / 3)
    OTSIKOIDEN_FONTIN_KOKO = 100
    OTSIKOIDEN_FONTIN_VARI = NAPPIEN_TEKSTIN_VARI
    
    #Pelin määritykset
    VIIVAN_LEVEYS = 5   
    

class Aloitusikkuna:

    PELAAJA_ALOITTAA = 'Pelaaja aloittaa'
    TEKOALY_ALOITTAA = 'Tekoäly aloittaa'

    def __init__(self, ikkuna):
        self.ikkuna = ikkuna
        self.pelitapanapit_y = 250
        self.aloitusvuoronapit_y = 600
        self.aloita_nappi_y = 800
        self.pelimuoto = Pelimuoto.YKSINPELI
        self.aloittaja = Aloitusikkuna.PELAAJA_ALOITTAA
        self.valmis = False
        self.yksinpeli_x = Maaritykset.LEVEYS_MARGINAALI
        self.helppo_yksinpeli_x = Maaritykset.LEVEYS_MARGINAALI + Maaritykset.NAPIN_LEVEYS + Maaritykset.NAPPIEN_VALI
        self.kaksinpeli_x = (Maaritykset.LEVEYS_MARGINAALI + Maaritykset.NAPIN_LEVEYS) * 2 + Maaritykset.NAPPIEN_VALI
        self.tekoalyn_peli_x = (Maaritykset.LEVEYS_MARGINAALI + Maaritykset.NAPIN_LEVEYS) * 3 + Maaritykset.NAPPIEN_VALI
        self.aloita_peli_x = Maaritykset.IKKUNAN_LEVEYS / 4 + Maaritykset.LEVEYS_MARGINAALI / 2
        self.aloita_peli_leveys = (Maaritykset.IKKUNAN_LEVEYS - Maaritykset.LEVEYS_MARGINAALI * 2) / 2 
        self.pelitapojen_fontti = pygame.font.SysFont(Maaritykset.OLETUS_FONTTI, Maaritykset.NAPPIEN_FONTIN_KOKO)
        self.otsikko_fontti = pygame.font.SysFont(Maaritykset.OLETUS_FONTTI, Maaritykset.OTSIKOIDEN_FONTIN_KOKO)
        
    def lue_pelitapa(self):
        self.piirra_aloitusikkuna()
        
        while not self.valmis:
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                    self.tarkista_nappien_painallus(tapahtuma.pos[0], tapahtuma.pos[1])
                    #self.valmis = True
            self.piirra_aloitusikkuna()
            pygame.display.update()

        return self.pelimuoto, self.aloittaja

    def tarkista_nappien_painallus(self, hiiri_x, hiiri_y):
        nappi_x = self.yksinpeli_x
        nappi_y = self.pelitapanapit_y 
        napin_leveys = Maaritykset.NAPIN_LEVEYS
        napin_korkeus = Maaritykset.NAPIN_KORKEUS
        pelimuoto = Pelimuoto.YKSINPELI

        #self.piirra_aloitusikkuna()
        
        #Yksinpeli
        self.tarkista_napin_painallus(pelimuoto, hiiri_x, hiiri_y, nappi_x, nappi_y, napin_leveys, napin_korkeus, Aloitusikkuna.PELAAJA_ALOITTAA)
        
        #Helppo yksinpeli
        nappi_x = self.helppo_yksinpeli_x
        pelimuoto = Pelimuoto.HELPPO_YKSINPELI
        self.tarkista_napin_painallus(pelimuoto, hiiri_x, hiiri_y, nappi_x, nappi_y, napin_leveys, napin_korkeus, Aloitusikkuna.PELAAJA_ALOITTAA)
        
        #Kaksinpeli
        nappi_x = self.kaksinpeli_x
        pelimuoto = Pelimuoto.KAKSINPELI
        self.tarkista_napin_painallus(pelimuoto, hiiri_x, hiiri_y, nappi_x, nappi_y, napin_leveys, napin_korkeus, None)
        
        #Tekoäly
        nappi_x = self.tekoalyn_peli_x
        pelimuoto = Pelimuoto.TEKOÄLY
        self.tarkista_napin_painallus(pelimuoto, hiiri_x, hiiri_y, nappi_x, nappi_y, napin_leveys, napin_korkeus, None)

        if self.pelimuoto == Pelimuoto.YKSINPELI or self.pelimuoto == Pelimuoto.HELPPO_YKSINPELI:
            #nappi_x = self.yksinpeli_x
            #pelimuoto = Pelimuoto.YKSINPELI
            #self.tarkista_napin_painallus(pelimuoto, hiiri_x, hiiri_y, nappi_x, nappi_y, napin_leveys, napin_korkeus)

            aloittaja = Aloitusikkuna.PELAAJA_ALOITTAA
            nappi_x = self.helppo_yksinpeli_x
            nappi_y = self.aloitusvuoronapit_y
            self.tarkista_napin_painallus(self.pelimuoto, hiiri_x, hiiri_y, nappi_x, nappi_y, napin_leveys, napin_korkeus, aloittaja)
            
            aloittaja = Aloitusikkuna.TEKOALY_ALOITTAA
            nappi_x = self.kaksinpeli_x
            self.tarkista_napin_painallus(self.pelimuoto, hiiri_x, hiiri_y, nappi_x, nappi_y, napin_leveys, napin_korkeus, aloittaja)

        nappi_x = self.aloita_peli_x
        nappi_y = self.aloita_nappi_y
        napin_leveys = self.aloita_peli_leveys
        if hiiri_x > nappi_x and hiiri_x < nappi_x + napin_leveys and hiiri_y > nappi_y and hiiri_y < nappi_y + napin_korkeus:
            self.valmis = True

        #print(self.pelimuoto)

    #def piirra_aloitusvuoronapit()
                    
    def tarkista_napin_painallus(self, pelimuoto, hiiri_x, hiiri_y, nappi_x, nappi_y, napin_leveys, napin_korkeus, aloittaja):
        if hiiri_x > nappi_x and hiiri_x < nappi_x + napin_leveys and hiiri_y > nappi_y and hiiri_y < nappi_y + napin_korkeus:
            
            self.pelimuoto = pelimuoto
            teksti = self.pelimuoto.value
            #input('toimii')
            self.aloittaja = aloittaja
            teksti = self.aloittaja
            
            self.piirra_nappi(nappi_x, nappi_y, napin_leveys, napin_korkeus, teksti, \
                              self.pelitapojen_fontti, Maaritykset.NAPPIEN_TEKSTIN_VARI, Maaritykset.POHJAVARI, \
                              Maaritykset.NAPPIEN_REUNAN_VARI, Maaritykset.NAPPIEN_REUNAN_KOKO)
      
    def piirra_aloitusikkuna(self):
            
        x = self.yksinpeli_x
        y = self.pelitapanapit_y 
        leveys = Maaritykset.NAPIN_LEVEYS
        korkeus = Maaritykset.NAPIN_KORKEUS
        fontti = self.pelitapojen_fontti
        fontin_vari = Maaritykset.NAPPIEN_TEKSTIN_VARI

        taustavari = Maaritykset.NAPPIEN_VARI
        reunavari = Maaritykset.NAPPIEN_REUNAN_VARI
        reunan_koko = Maaritykset.NAPPIEN_REUNAN_KOKO

        self.ikkuna.fill(Maaritykset.POHJAVARI)
        
        #Pelitapa teksti
        pelitapa = (Maaritykset.IKKUNAN_LEVEYS / 2, Maaritykset.VALIKON_KOKO)
        self.piirra_teksti(pelitapa, "Valitse pelitapa", self.otsikko_fontti, Maaritykset.OTSIKOIDEN_FONTIN_VARI)
        
        #Yksinpeli
        self.piirra_nappi(x, y, leveys, korkeus, Pelimuoto.YKSINPELI.value, fontti, fontin_vari, taustavari, reunavari, reunan_koko)
        
        #Helppo yksinpeli
        x = self.helppo_yksinpeli_x
        self.piirra_nappi(x, y, leveys, korkeus, Pelimuoto.HELPPO_YKSINPELI.value, fontti, fontin_vari, taustavari, reunavari, reunan_koko)
        
        #Kaksinpeli
        x = self.kaksinpeli_x
        self.piirra_nappi(x, y, leveys, korkeus, Pelimuoto.KAKSINPELI.value, fontti, fontin_vari, taustavari, reunavari, reunan_koko)
        
        #Tekoäly peli
        x = self.tekoalyn_peli_x
        self.piirra_nappi(x, y, leveys, korkeus, Pelimuoto.TEKOÄLY.value, fontti, fontin_vari, taustavari, reunavari, reunan_koko)
        #print(self.pelimuoto)

        if self.pelimuoto == Pelimuoto.YKSINPELI or self.pelimuoto == Pelimuoto.HELPPO_YKSINPELI:
            #Valise aloittaja teksti
            valitse_aloittaja = (Maaritykset.IKKUNAN_LEVEYS / 2, Maaritykset.IKKUNAN_KORKEUS / 2)
            self.piirra_teksti(valitse_aloittaja, "Valitse aloittaja", self.otsikko_fontti, Maaritykset.OTSIKOIDEN_FONTIN_VARI)
            x = self.helppo_yksinpeli_x
            y = self.aloitusvuoronapit_y
            self.piirra_nappi(x, y, leveys, korkeus, 'Pelaaja aloittaa', fontti, fontin_vari, taustavari, reunavari, reunan_koko)

            x = self.kaksinpeli_x
            self.piirra_nappi(x, y, leveys, korkeus, 'Tekoäly aloittaa', fontti, fontin_vari, taustavari, reunavari, reunan_koko)
        
        #Aloita peli
        x = self.aloita_peli_x
        y = self.aloita_nappi_y
        leveys = self.aloita_peli_leveys
        
        self.piirra_nappi(x, y, leveys, korkeus, 'Aloita peli', fontti, fontin_vari, taustavari, reunavari, reunan_koko)

        
    def piirra_teksti(self, koordinaatti, teksti, fontti, fontin_vari):
        teksti = fontti.render(teksti, 1, fontin_vari)
        rect = teksti.get_rect(center=koordinaatti)
        self.ikkuna.blit(teksti, rect)
        
    def piirra_nappi(self, x, y, leveys, korkeus, teksti, fontti, fontin_vari, taustavari, reunavari, reunan_koko):
    
        koordinaatti = (x,y,leveys,korkeus)
        if teksti == self.pelimuoto.value or teksti == self.aloittaja:
            taustavari = Maaritykset.POHJAVARI

        pygame.draw.rect(self.ikkuna, taustavari, pygame.Rect(koordinaatti))
        pygame.draw.rect(self.ikkuna, reunavari, pygame.Rect(koordinaatti), reunan_koko)
        keskikohta = (x + leveys / 2, y + korkeus / 2)
        self.piirra_teksti(keskikohta, teksti, fontti, fontin_vari)
