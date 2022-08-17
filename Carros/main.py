import pygame
pygame.init()


width, height = 850, 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Game")

background = pygame.image.load("Carros\\assets\screen.png")
car = pygame.image.load("Carros\\assets\\ferrari1.png")

playing = True

while playing:
    screen.blit(background, (0,0))
    screen.blit(car, (int(width/2), int(height/2)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    pygame.display.update()

pygame.quit()