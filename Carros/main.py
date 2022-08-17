from car import Car
import pygame
pygame.init()


width, height = 850, 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Game")

background = pygame.image.load("Carros\\assets\screen.png")
car_img = pygame.image.load("Carros\\assets\\ferrari1.png")

car = Car(50, 50, car_img)

playing = True

while playing:
    screen.blit(background, (0,0))
    car.draw(screen)
    car.update(screen, 1, 120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    if car.flip_cout == 3:
        pygame.time.delay(1000)
        playing = False

    pygame.display.update()

pygame.quit()