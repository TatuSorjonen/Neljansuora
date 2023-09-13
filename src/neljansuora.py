import pygame
from lauta import Lauta, Tulos


class Neljansuora:

    def __init__(self):
        pygame.init()
        self.lauta = Lauta()
        self.RUUDUN_KOKO = 150
        self.IKKUNAN_LEVEYS = self.RUUDUN_KOKO * self.lauta.SARAKKEIDEN_MAARA
        self.IKKUNAN_KORKEUS = self.RUUDUN_KOKO * self.lauta.RIVIEN_MAARA
        self.POHJAVARI = (200, 200, 200)
        self.VASTAVARI = (255, 50, 25)
        self.KELTAINEN = pygame.transform.scale(pygame.image.load\
        ("src/kuvat/keltainen.jpeg"), (self.RUUDUN_KOKO, self.RUUDUN_KOKO))
        self.PUNAINEN = pygame.transform.scale(pygame.image.load\
        ("src/kuvat/punainen.jpeg"), (self.RUUDUN_KOKO, self.RUUDUN_KOKO))
        self.VIIVAN_LEVEYS = 5
        
        self.ikkuna = pygame.display.set_mode((self.IKKUNAN_LEVEYS, self.IKKUNAN_KORKEUS))
        self.ikkuna.fill(self.POHJAVARI)

        
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
                    self.piirra_merkki()
    
            self.piirra_taulukko()
            pygame.display.update()
        
    
    def piirra_taulukko(self):
        for x in range(0, self.IKKUNAN_LEVEYS, self.RUUDUN_KOKO):
            for y in range(0, self.IKKUNAN_KORKEUS, self.RUUDUN_KOKO):
                ruutu = pygame.Rect(x, y, self.IKKUNAN_LEVEYS, self.IKKUNAN_KORKEUS)
                pygame.draw.rect(self.ikkuna, self.VASTAVARI, ruutu, self.VIIVAN_LEVEYS)
        
    def piirra_merkki(self):
        #Tee piirtää merkin Lauta luokan taulukosta
        self.ikkuna.blit(self.PUNAINEN, (0, 0))

