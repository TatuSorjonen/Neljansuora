import pygame
pygame.init()

valkoinen = (200, 200, 200)
musta = (0, 0, 0)
#rivi = 6
#sarake = 7
#lauta = [[0] * sarake for _ in range(ROWS)]
#pygame.display.flip()

ikkuna = pygame.display.set_mode((1000,1000))
    #CLOCK = pygame.time.Clock()
ikkuna.fill(valkoinen)


    
def piirra_taulukko():
    ruudun_koko = 100
    for x in range(0, 1000, ruudun_koko):
        for y in range(0, 1000, ruudun_koko):
            rect = pygame.Rect(x, y, 1000, 1000)
            pygame.draw.rect(ikkuna, musta, rect, 1)

#def main():
while True:
    ruudun_koko = 100

    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
    
    piirra_taulukko()        
    pygame.display.update()
