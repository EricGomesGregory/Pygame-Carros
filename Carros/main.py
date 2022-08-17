from car import Car
import pygame
pygame.init()


width, height = 850, 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Game")

background = pygame.image.load("Carros\\assets\screen.png")
car_img = pygame.image.load("Carros\\assets\\ferrari1.png")

car = Car(50, 50, car_img)
car_h_step = 125
car_speed = 0.5

playing = True

while playing:
    screen.blit(background, (0,0))
    car.draw(screen)
    car.update(screen, car_speed, car_h_step)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                car_speed = max(min(car_speed + 0.25, 2), 0.0)
            if event.key == pygame.K_DOWN:
                car_speed = max(min(car_speed - 0.25, 2), 0.0)

    if car.flip_cout == 3:
        pygame.time.delay(1000)
        playing = False

    pygame.display.update()

pygame.quit()