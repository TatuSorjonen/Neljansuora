'''Tiedosto, jossa on luokat Peimuoto, Maaritykset, sekä Aloitusikkuna
'''

import math
from enum import Enum
import pygame
from lauta import Lauta

class Pelimuoto(Enum):
    '''Luokka, jossa hallitaan eri pelimuotoja
    '''

    YKSINPELI = 'Yksinpeli'
    HELPPO_YKSINPELI = 'Helppo yksinpeli'
    KAKSINPELI = 'Kaksinpeli'
    TEKOALY = 'Tekoäly peli'

class Maaritykset:
    '''Luokka, jossa pidetään eri pelin määrityksiä yllä
    '''

    #Kummallekin näkymälle yhteiset määritykset
    RUUDUN_KOKO = 150
    VIIVAN_LEVEYS = int(RUUDUN_KOKO / 30)
    VALIKON_KOKO = math.ceil (2 * RUUDUN_KOKO / 3)
    IKKUNAN_LEVEYS = RUUDUN_KOKO * Lauta.SARAKKEIDEN_MAARA
    IKKUNAN_KORKEUS = RUUDUN_KOKO * Lauta.RIVIEN_MAARA + \
                      VALIKON_KOKO + math.ceil(VIIVAN_LEVEYS / 2)
    POHJAVARI = (255,250,240)
    VASTAVARI = (28,134,238)
    KELTAINEN = (204,204,0)
    PUNAINEN = (204,0,0)
    NAPPIEN_VARI = (153, 204, 255)
    NAPPIEN_REUNAN_VARI = (102, 178, 255)
    NAPPIEN_REUNAN_KOKO = math.ceil(RUUDUN_KOKO/30)
    OLETUS_FONTTI = 'freesansbold'
    NAPPIEN_TEKSTIN_VARI = (0, 51, 102)
    NAPPIEN_FONTIN_KOKO = int(RUUDUN_KOKO / 3) - 5

    #Alkuvalikon määritykset
    PELITAPOJEN_MAARA = 4
    LEVEYS_MARGINAALI = int(RUUDUN_KOKO / 15)
    NAPPIEN_VALI = LEVEYS_MARGINAALI
    NAPIN_LEVEYS = (IKKUNAN_LEVEYS - LEVEYS_MARGINAALI * 2)/4 - NAPPIEN_VALI * (3/4)
    NAPIN_KORKEUS = int(NAPIN_LEVEYS / 3)
    OTSIKOIDEN_FONTIN_KOKO = math.ceil(2 * RUUDUN_KOKO / 3)
    OTSIKOIDEN_FONTIN_VARI = NAPPIEN_TEKSTIN_VARI

class Aloitusikkuna:
    '''Luokka, joka hoitaa aloitusikkunan toiminnallisuudet
    '''

    PELAAJA_ALOITTAA = 'Pelaaja aloittaa'
    TEKOALY_ALOITTAA = 'Tekoäly aloittaa'

    def __init__(self, ikkuna):
        self.ikkuna = ikkuna
        self.pelitapanapit_y = Maaritykset.RUUDUN_KOKO + math.ceil(Maaritykset.RUUDUN_KOKO / 3)
        self.aloitusvuoronapit_y = Maaritykset.RUUDUN_KOKO * 4
        self.aloita_nappi_y = Maaritykset.RUUDUN_KOKO * 5
        self.pelimuoto = Pelimuoto.YKSINPELI
        self.aloittaja = Aloitusikkuna.PELAAJA_ALOITTAA
        self.valmis = False
        self.yksinpeli_x = Maaritykset.LEVEYS_MARGINAALI
        self.helppo_yksinpeli_x = Maaritykset.LEVEYS_MARGINAALI \
                                + Maaritykset.NAPIN_LEVEYS + Maaritykset.NAPPIEN_VALI
        self.kaksinpeli_x = (Maaritykset.LEVEYS_MARGINAALI + Maaritykset.NAPIN_LEVEYS)\
                          * 2 + Maaritykset.NAPPIEN_VALI
        self.tekoalyn_peli_x = (Maaritykset.LEVEYS_MARGINAALI + Maaritykset.NAPIN_LEVEYS)\
                          * 3 + Maaritykset.NAPPIEN_VALI
        self.aloita_peli_x = Maaritykset.IKKUNAN_LEVEYS / 4 + Maaritykset.LEVEYS_MARGINAALI / 2
        self.aloita_peli_leveys = \
                            (Maaritykset.IKKUNAN_LEVEYS - Maaritykset.LEVEYS_MARGINAALI * 2) / 2
        self.pelitapojen_fontti = pygame.font.SysFont(\
                                  Maaritykset.OLETUS_FONTTI, Maaritykset.NAPPIEN_FONTIN_KOKO)
        self.otsikko_fontti = pygame.font.SysFont(\
                                  Maaritykset.OLETUS_FONTTI, Maaritykset.OTSIKOIDEN_FONTIN_KOKO)

    def lue_pelitapa(self):
        '''Aloitusikkuna, josta valitaan pelimuoto ja mahdollisesti aloittaja
        '''

        self.piirra_aloitusikkuna()

        while not self.valmis:
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                    self.tarkista_nappien_painallus(tapahtuma.pos[0], tapahtuma.pos[1])
            self.piirra_aloitusikkuna()
            pygame.display.update()

        return self.pelimuoto, self.aloittaja

    def tarkista_nappien_painallus(self, hiiri_x, hiiri_y):
        '''Tarkistaa napin_painallus funktion avulla onko nappia painettu

        Parametrit:
            hiiri_x: Hiiren painalluksen x koordinaatti
            hiiri_y: Hiiren painalluksen y koordinaatti
        '''

        nappi_x = self.yksinpeli_x
        nappi_y = self.pelitapanapit_y
        napin_leveys = Maaritykset.NAPIN_LEVEYS
        napin_korkeus = Maaritykset.NAPIN_KORKEUS

        #Yksinpeli
        pelimuoto = Pelimuoto.YKSINPELI
        self.tarkista_napin_painallus(pelimuoto, hiiri_x, hiiri_y, \
                                      nappi_x, nappi_y, napin_leveys, \
                                      napin_korkeus, Aloitusikkuna.PELAAJA_ALOITTAA)

        #Helppo yksinpeli
        nappi_x = self.helppo_yksinpeli_x
        pelimuoto = Pelimuoto.HELPPO_YKSINPELI
        self.tarkista_napin_painallus(pelimuoto, hiiri_x, hiiri_y, \
                                      nappi_x, nappi_y, napin_leveys, \
                                      napin_korkeus, Aloitusikkuna.PELAAJA_ALOITTAA)

        #Kaksinpeli
        nappi_x = self.kaksinpeli_x
        pelimuoto = Pelimuoto.KAKSINPELI
        self.tarkista_napin_painallus(pelimuoto, hiiri_x, hiiri_y, \
                                      nappi_x, nappi_y, napin_leveys, \
                                      napin_korkeus, None)

        #Tekoäly
        nappi_x = self.tekoalyn_peli_x
        pelimuoto = Pelimuoto.TEKOALY
        self.tarkista_napin_painallus(pelimuoto, hiiri_x, hiiri_y, \
                                      nappi_x, nappi_y, napin_leveys, \
                                      napin_korkeus, None)

        if self.pelimuoto == Pelimuoto.YKSINPELI or self.pelimuoto == Pelimuoto.HELPPO_YKSINPELI:

            aloittaja = Aloitusikkuna.PELAAJA_ALOITTAA
            nappi_x = self.helppo_yksinpeli_x
            nappi_y = self.aloitusvuoronapit_y
            self.tarkista_napin_painallus(self.pelimuoto, hiiri_x, hiiri_y, \
                                          nappi_x, nappi_y, napin_leveys, \
                                          napin_korkeus, aloittaja)

            aloittaja = Aloitusikkuna.TEKOALY_ALOITTAA
            nappi_x = self.kaksinpeli_x
            self.tarkista_napin_painallus(self.pelimuoto, hiiri_x, hiiri_y, \
                                          nappi_x, nappi_y, napin_leveys, \
                                          napin_korkeus, aloittaja)

        nappi_x = self.aloita_peli_x
        nappi_y = self.aloita_nappi_y
        napin_leveys = self.aloita_peli_leveys
        if hiiri_x > nappi_x and hiiri_x < nappi_x + napin_leveys \
           and hiiri_y > nappi_y and hiiri_y < nappi_y + napin_korkeus:
            self.valmis = True

    def tarkista_napin_painallus(\
            self, pelimuoto, hiiri_x, hiiri_y, \
            nappi_x, nappi_y, napin_leveys, napin_korkeus, aloittaja):
        '''Tarkistaa parametrien avulla onko nappia painettu

        Parametrit:
            pelimuoto: Mikä pelimuoto on kyseessä
            hiiri_x: Hiiren painalluksen x koordinaatti
            hiiri_y: Hiiren painalluksen y koordinaatti
            nappi_x: Napin x koordinaatti
            nappi_y: Napin y koordinaatti
            napin_leveys: Napin leveys
            napin_korkeus: Napin korkeus
            aloittaja: Kumpi aloittaa
        '''

        if hiiri_x > nappi_x and hiiri_x < nappi_x + napin_leveys  \
           and hiiri_y > nappi_y and hiiri_y < nappi_y + napin_korkeus:

            self.pelimuoto = pelimuoto
            teksti = self.pelimuoto.value
            self.aloittaja = aloittaja
            teksti = self.aloittaja

            self.piirra_nappi(nappi_x, nappi_y, napin_leveys, napin_korkeus, teksti, \
                              self.pelitapojen_fontti, Maaritykset.NAPPIEN_TEKSTIN_VARI, \
                              Maaritykset.POHJAVARI, Maaritykset.NAPPIEN_REUNAN_VARI, \
                              Maaritykset.NAPPIEN_REUNAN_KOKO)

    def piirra_aloitusikkuna(self):
        '''Piirtää pelin aloitusikkunan
        '''

        x_koord = self.yksinpeli_x
        y_koord = self.pelitapanapit_y 
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
        self.piirra_teksti(\
            pelitapa, "Valitse pelitapa", self.otsikko_fontti, \
            Maaritykset.OTSIKOIDEN_FONTIN_VARI)

        #Yksinpeli
        self.piirra_nappi(x_koord, y_koord, leveys, korkeus, \
                          Pelimuoto.YKSINPELI.value, fontti, fontin_vari, \
                          taustavari, reunavari, reunan_koko)

        #Helppo yksinpeli
        x_koord = self.helppo_yksinpeli_x
        self.piirra_nappi(x_koord, y_koord, leveys, korkeus, \
                          Pelimuoto.HELPPO_YKSINPELI.value, fontti, fontin_vari, \
                          taustavari, reunavari, reunan_koko)

        #Kaksinpeli
        x_koord = self.kaksinpeli_x
        self.piirra_nappi(x_koord, y_koord, leveys, korkeus, Pelimuoto.KAKSINPELI.value, \
                          fontti, fontin_vari, taustavari, reunavari, reunan_koko)

        #Tekoäly peli
        x_koord = self.tekoalyn_peli_x
        self.piirra_nappi(x_koord, y_koord, leveys, korkeus, Pelimuoto.TEKOALY.value, \
                          fontti, fontin_vari, taustavari, reunavari, reunan_koko)

        if self.pelimuoto == Pelimuoto.YKSINPELI or self.pelimuoto == Pelimuoto.HELPPO_YKSINPELI:
            #Valise aloittaja teksti
            valitse_aloittaja = (Maaritykset.IKKUNAN_LEVEYS / 2, Maaritykset.IKKUNAN_KORKEUS / 2)
            self.piirra_teksti(valitse_aloittaja, "Valitse aloittaja", \
                               self.otsikko_fontti, Maaritykset.OTSIKOIDEN_FONTIN_VARI)
            x_koord = self.helppo_yksinpeli_x
            y_koord = self.aloitusvuoronapit_y
            self.piirra_nappi(x_koord, y_koord, leveys, korkeus, \
                             'Pelaaja aloittaa', fontti, fontin_vari, \
                             taustavari, reunavari, reunan_koko)

            x_koord = self.kaksinpeli_x
            self.piirra_nappi(x_koord, y_koord, leveys, korkeus, \
                              'Tekoäly aloittaa', fontti, fontin_vari, \
                              taustavari, reunavari, reunan_koko)

        #Aloita peli
        x_koord = self.aloita_peli_x
        y_koord = self.aloita_nappi_y
        leveys = self.aloita_peli_leveys

        self.piirra_nappi(x_koord, y_koord, leveys, korkeus, \
                          'Aloita peli', fontti, fontin_vari, \
                          taustavari, reunavari, reunan_koko)

    def piirra_teksti(self, koordinaatti, teksti, fontti, fontin_vari):
        '''Piirtää tekstin käyttäen parametrejä hyväkseen

        Parametrit:
            koordinaatti: Tekstin koordinaatti
            teksti: Teksti
            fontti: Tekstin fontti
            fontin_vari: Tekstin fontin väri
        '''

        teksti = fontti.render(teksti, 1, fontin_vari)
        rect = teksti.get_rect(center=koordinaatti)
        self.ikkuna.blit(teksti, rect)

    def piirra_nappi(self, x_koord, y_koord, leveys, korkeus, \
                     teksti, fontti, fontin_vari, \
                     taustavari, reunavari, reunan_koko):
        '''Piirtaa napin käyttäen parametrejä hyväkseen

        Parametrit:
            x_koord: X koordinaatti
            y_koord: Y koordinaatti
            leveys: Leveys
            korkeus: Korkeus
            teksti: Nappulan teksti
            fontti: Nappulan tekstin fontti
            fontin_vari: Nappulan fontin väri
            taustavari: Napin taustaväri
            reunavari: Napin reunan väri
            reunan_koko: Napin reunan koko
        '''

        koordinaatti = (x_koord,y_koord,leveys,korkeus)
        if teksti == self.pelimuoto.value or teksti == self.aloittaja:
            taustavari = Maaritykset.POHJAVARI

        pygame.draw.rect(self.ikkuna, taustavari, pygame.Rect(koordinaatti))
        pygame.draw.rect(self.ikkuna, reunavari, pygame.Rect(koordinaatti), reunan_koko)
        keskikohta = (x_koord + leveys / 2, y_koord + korkeus / 2)
        self.piirra_teksti(keskikohta, teksti, fontti, fontin_vari)
