import math
import pygame
from lauta import Lauta, Tulos
from maaritykset import Pelimuoto, Maaritykset, Aloitusikkuna

class Neljansuora:
    '''Neljansuora pitää yllään neljänsuoran käyttöliittymän
    '''

    NAPPIEN_MAARA = 3

    def __init__(self):
        '''Konstruktori jossa alustetaan neljansuora alkuun
        '''

        self.on_kaynnissa = False
        self.pelimuoto = Pelimuoto.YKSINPELI
        self.aloittaja = Aloitusikkuna.PELAAJA_ALOITTAA

        self.ikkuna = pygame.display.set_mode(\
                     (Maaritykset.IKKUNAN_LEVEYS, Maaritykset.IKKUNAN_KORKEUS), pygame.NOFRAME)
        self.ikkuna.fill(Maaritykset.POHJAVARI)
        pygame.init()

        self.lauta = Lauta()

    def lue_maaritykset(self):
        '''Alustaa aloitusikkunan
        '''

        aloitusikkuna = Aloitusikkuna(self.ikkuna)
        pelimuoto, aloittaja = aloitusikkuna.lue_pelitapa()
        self.alusta_peli(pelimuoto, aloittaja)
        self.aloita_peli()

    def alusta_peli(self, pelimuoto, aloittaja):
        '''Funktio jossa peli alustetaan uudelleen pelimuodon ja aloittajan mukaan

        Parametrit:
            pelimuoto: Pelimuoto joka on asetettu pelille
            aloittaja: Pelin aloittaja
        '''

        self.on_kaynnissa = True
        self.pelimuoto = pelimuoto
        self.aloittaja = aloittaja
        self.ikkuna.fill(Maaritykset.POHJAVARI)
        self.lauta = Lauta()

    def aloita_peli(self):
        '''Alustaa pygamen ja aloittaa pelin.
           Pyörii loputtomassa for loopissa kunnes painetaan hiiren vasemmalla lautaa.
        '''

        self.piirra_ikkuna()
        self.tarkista_tekoaly()

        while self.on_kaynnissa:

            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    self.on_kaynnissa = False
                elif tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                    self.tarkista_hiiren_painallus(tapahtuma.pos[0], tapahtuma.pos[1])

        pygame.quit()

    def piirra_ikkuna(self):
        '''Piirtää pelille ikkunan
        '''

        self.ikkuna.fill(Maaritykset.POHJAVARI)
        self.piirra_taulukko()
        self.piirra_pelin_napit_ja_tekstit()
        self.piirra_tilanne()
        pygame.display.update()

    def piirra_taulukko(self):
        '''Piirtää taulukon neljänsuora pelille pygamen ikkunaan
        '''

        for rivi in range(0, Maaritykset.IKKUNAN_LEVEYS, \
                          Maaritykset.RUUDUN_KOKO):
            for sarake in range(Maaritykset.VALIKON_KOKO, \
                           Maaritykset.IKKUNAN_KORKEUS, Maaritykset.RUUDUN_KOKO):
                ruutu = pygame.Rect(\
                        rivi, sarake, Maaritykset.IKKUNAN_LEVEYS, \
                        Maaritykset.IKKUNAN_KORKEUS)
                pygame.draw.rect(self.ikkuna, Maaritykset.VASTAVARI, \
                                 ruutu, Maaritykset.VIIVAN_LEVEYS)

    def piirra_pelin_napit_ja_tekstit(self):
        '''Piirtää napit ja tekstit pelille
        '''

        minun_fontti = 'freesansbold'
        fontin_koko = math.ceil(Maaritykset.RUUDUN_KOKO / 3) - 5
        status_fontin_vari = Maaritykset.KELTAINEN
        nappuloiden_fontin_vari = Maaritykset.NAPPIEN_TEKSTIN_VARI
        fontti = pygame.font.SysFont(minun_fontti, fontin_koko)

        #Aloita alusta
        aloita_alusta_x = 0
        aloita_alusta_y = 0
        aloita_alusta_napin_leveys = Maaritykset.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA
        aloita_alusta_napin_korkeus = Maaritykset.VALIKON_KOKO
        self.piirra_nappi(aloita_alusta_x, aloita_alusta_y, aloita_alusta_napin_leveys, \
                          aloita_alusta_napin_korkeus, 'Aloita alusta', \
                          fontti, nappuloiden_fontin_vari, \
                          Maaritykset.NAPPIEN_VARI, Maaritykset.NAPPIEN_REUNAN_VARI, \
                          Maaritykset.NAPPIEN_REUNAN_KOKO)

        #Sulje
        sulje_x = Maaritykset.IKKUNAN_LEVEYS - \
                  Maaritykset.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA
        sulje_y = 0
        sulje_napin_leveys = Maaritykset.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA
        sulje_napin_korkeus = Maaritykset.VALIKON_KOKO
        self.piirra_nappi(sulje_x, sulje_y, sulje_napin_leveys, sulje_napin_korkeus, \
                          'Sulje peli', fontti, nappuloiden_fontin_vari, Maaritykset.NAPPIEN_VARI, \
                          Maaritykset.NAPPIEN_REUNAN_VARI, Maaritykset.NAPPIEN_REUNAN_KOKO)

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
        pygame.draw.rect(self.ikkuna, taustan_vari, \
                         (Maaritykset.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA,\
                                      0, Maaritykset.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA,\
                                                     Maaritykset.VALIKON_KOKO))
        status = (Maaritykset.IKKUNAN_LEVEYS / 2, Maaritykset.VALIKON_KOKO / 2)
        self.piirra_teksti(status, vuoro, fontti, status_fontin_vari)

    def piirra_nappi(self, x_koord, y_koord, leveys, korkeus, teksti, \
                     fontti, fontin_vari, taustavari, reunavari, reunan_koko):
        '''Piirtaa napin käyttäen parametrejä hyväkseen

        Parametrit:
            x: X koordinaatti
            y: Y koordinaatti
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

        pygame.draw.rect(self.ikkuna, taustavari, pygame.Rect(koordinaatti))
        pygame.draw.rect(self.ikkuna, reunavari, pygame.Rect(koordinaatti), reunan_koko)
        keskikohta = (x_koord + leveys / 2, y_koord + korkeus / 2)

        self.piirra_teksti(keskikohta, teksti, fontti, fontin_vari)

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

    def piirra_tilanne(self):
        '''Piirtää tilanteen pygamen ikkunaan Lauta luokan ruudukosta
        '''

        self.piirra_taulukko()

        for x_ruutu in range(0, self.lauta.SARAKKEIDEN_MAARA):
            for y_ruutu in range(0, self.lauta.RIVIEN_MAARA):
                x_koordinaatti = Maaritykset.RUUDUN_KOKO * x_ruutu + \
                                 int(Maaritykset.RUUDUN_KOKO / 2)
                y_koordinaatti = Maaritykset.RUUDUN_KOKO * y_ruutu + \
                                 int(Maaritykset.RUUDUN_KOKO / 2) + Maaritykset.VALIKON_KOKO
                if self.lauta.ruudukko[y_ruutu][x_ruutu] == 'K':
                    pygame.draw.circle(self.ikkuna, Maaritykset.KELTAINEN, \
                                    (x_koordinaatti, y_koordinaatti), \
                                    int(Maaritykset.RUUDUN_KOKO / 2 - Maaritykset.VIIVAN_LEVEYS))
                elif self.lauta.ruudukko[y_ruutu][x_ruutu] == 'P':
                    pygame.draw.circle(self.ikkuna, Maaritykset.PUNAINEN, \
                                    (x_koordinaatti, y_koordinaatti), \
                                    int(Maaritykset.RUUDUN_KOKO / 2 - Maaritykset.VIIVAN_LEVEYS))

    def tarkista_tekoaly(self):
        '''Tarkistaa onko tekoälyn aloituvuoro tai onko pelimuotona tekoälyjen keskinäinen peli
        ja pelaa tarvittavat vuorot
        '''

        vuoro = self.lauta.kenen_vuoro(self.lauta.ruudukko)

        #Jos tekoäly aloittaa tehdään sille ensimmäinen siirto
        if self.aloittaja == Aloitusikkuna.TEKOALY_ALOITTAA:
            self.pelaa_tekoaly(vuoro)
            self.aloittaja = Aloitusikkuna.PELAAJA_ALOITTAA

        #Jos pelimuotona on Demo. Pelataan demo suoraan yhden while loopin sisällä.
        elif self.pelimuoto == Pelimuoto.DEMO:
            tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
            while tilanne == Tulos.MENEILLAAN:
                self.pelaa_tekoaly(vuoro)
                pygame.display.update()
                vuoro = self.lauta.kenen_vuoro(self.lauta.ruudukko)
                tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)

    def tarkista_hiiren_painallus(self, hiiri_x, hiiri_y):
        '''Tarkistaa mihin kohtaan on hiirellä painettu

        Parametrit:
            hiiri_x: X koordinaattii johon painettiin
            hiiri_y: Y koordinaatti johon painettiin
        '''

        tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
        if tilanne == Tulos.MENEILLAAN and hiiri_y > Maaritykset.VALIKON_KOKO:
            self.aseta_merkki(hiiri_x, hiiri_y)
        elif hiiri_x >= Maaritykset.IKKUNAN_LEVEYS - \
                        Maaritykset.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA\
                        and hiiri_y <= Maaritykset.VALIKON_KOKO:
            self.on_kaynnissa = False

        elif hiiri_x < Maaritykset.IKKUNAN_LEVEYS / Neljansuora.NAPPIEN_MAARA\
        and hiiri_y <= Maaritykset.VALIKON_KOKO:
            self.on_kaynnissa = False
            self.lue_maaritykset()

    def aseta_merkki(self, hiiri_x, hiiri_y):
        '''Asettaa merkin oikeaan kohtaan laudalle käyttämällä 
           Lauta luokan metodeita lisaa_nappula tai 
           lisaa_paras_siirto riippuen kumman pelaajan vuoro on

        Parametrit:
            hiiri_x: X koordinaattii johon painettiin
            hiiri_y: Y koordinaatti johon painettiin
        '''

        sarake = math.floor(hiiri_x / Maaritykset.RUUDUN_KOKO)
        rivi = math.floor(hiiri_y / Maaritykset.RUUDUN_KOKO)

        vuoro = self.lauta.kenen_vuoro(self.lauta.ruudukko)

        #Yksinpeli
        if hiiri_y > 100 and self.pelimuoto == Pelimuoto.YKSINPELI:
            if self.aloittaja == Aloitusikkuna.PELAAJA_ALOITTAA:
                rivi = self.pelaa_pelaaja(sarake, vuoro)
                tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
                if tilanne == Tulos.MENEILLAAN and rivi != -1:
                    vuoro = self.lauta.kenen_vuoro(self.lauta.ruudukko)
                    self.pelaa_tekoaly(vuoro)
            else:
                self.pelaa_tekoaly(vuoro)
                tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
                if tilanne == Tulos.MENEILLAAN:
                    vuoro = self.lauta.kenen_vuoro(self.lauta.ruudukko)
                    self.pelaa_pelaaja(sarake, vuoro)

        #Helppo yksinpeli
        elif hiiri_y > 100 and self.pelimuoto == Pelimuoto.HELPPO_YKSINPELI:
            if self.aloittaja == Aloitusikkuna.PELAAJA_ALOITTAA:
                rivi = self.pelaa_pelaaja(sarake, vuoro)
                tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
                if tilanne == Tulos.MENEILLAAN and rivi != -1:
                    vuoro = self.lauta.kenen_vuoro(self.lauta.ruudukko)
                    self.pelaa_tekoaly(vuoro)
            else:
                self.pelaa_tekoaly(vuoro)
                tilanne = self.lauta.tarkista_tilanne(self.lauta.ruudukko)
                if tilanne == Tulos.MENEILLAAN:
                    vuoro = self.lauta.kenen_vuoro(self.lauta.ruudukko)
                    self.pelaa_pelaaja(sarake, vuoro)

        #Kaksinpeli
        elif hiiri_y > 100 and self.pelimuoto == Pelimuoto.KAKSINPELI:
            self.pelaa_pelaaja(sarake, vuoro)

    def pelaa_pelaaja(self, sarake, vuoro):
        '''Pelaa pelaajan vuoron

        Parametrit:
            sarake: Sarake
            vuoro: Kumman vuoro

        Palauttaa:
            Rivin
        '''

        rivi = self.lauta.lisaa_nappula(sarake, self.lauta.ruudukko)
        self.animoi_pudotus(sarake, rivi, vuoro)
        self.piirra_ikkuna()
        return rivi

    def pelaa_tekoaly(self, vuoro):
        '''Pelaa tekoälyn vuoron

        Parametrit:
            vuoro: Kumman vuoro
        '''

        if self.pelimuoto == Pelimuoto.YKSINPELI or self.pelimuoto == Pelimuoto.DEMO:
            sarake, rivi, paras_tulos = self.lauta.lisaa_paras_siirto(Lauta.SYVYYYS)
            self.animoi_pudotus(sarake, rivi, vuoro)
            self.piirra_ikkuna()
        elif self.pelimuoto == Pelimuoto.HELPPO_YKSINPELI:
            rivi, sarake = self.lauta.lisaa_satunnainen(vuoro)
            self.animoi_pudotus(sarake, rivi, vuoro)
            self.piirra_ikkuna()

    def animoi_pudotus(self, sarake, rivi, vuoro):
        '''Animoi pelinappulan pudotuksen

        Parametrit:
            sarake: Sarake mihin nappula pudotetaan
            rivi: Mihin riville nappula pudotetaan
            vuoro: Kumman värinen nappula pudotetaan
        '''

        pygame.mixer.music.load('Pudotus.mp3')
        nappulan_vari = Maaritykset.KELTAINEN
        if vuoro == self.lauta.PUNAINEN:
            nappulan_vari = Maaritykset.PUNAINEN
        x_koord = Maaritykset.RUUDUN_KOKO * sarake + int(Maaritykset.RUUDUN_KOKO / 2)
        y_koord = Maaritykset.VALIKON_KOKO + int(Maaritykset.RUUDUN_KOKO / 2)
        y_loppu = Maaritykset.RUUDUN_KOKO * rivi + \
                  int(Maaritykset.RUUDUN_KOKO / 2) + Maaritykset.VALIKON_KOKO

        for i in range(y_koord, y_loppu):
            self.piirra_taulukko()
            pygame.draw.circle(self.ikkuna, nappulan_vari, (x_koord, i), \
                               int(Maaritykset.RUUDUN_KOKO / 2))
            pygame.display.update()
            pygame.draw.circle(self.ikkuna, Maaritykset.POHJAVARI, (x_koord, i), \
                               int(Maaritykset.RUUDUN_KOKO / 2))
        pygame.mixer.music.play(1)
