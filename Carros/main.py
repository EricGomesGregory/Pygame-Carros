from car import Car
import pygame
pygame.init()


width, height = 850, 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Game")

font_size = 80
my_font = pygame.font.SysFont("arial", font_size, bold=True,italic=False)
endgame_text = my_font.render("GAME OVER",True,(255,255,255),(0,0,0))
background = pygame.image.load("Carros\\assets\screen.png")
car_img = pygame.image.load("Carros\\assets\\ferrari1.png")

car = Car(50, 50, car_img)
car_h_step = 125
car_speed = 0.0
car_max_speed = 2.0
car_min_speed = 0.0
car_speed_change = 0.25

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
                car_speed = max(min(car_speed + car_speed_change, car_max_speed), car_min_speed)
            if event.key == pygame.K_DOWN:
                car_speed = max(min(car_speed - car_speed_change, car_max_speed), car_min_speed)

    if car.flip_cout == 3:
        screen.fill('black')
        x = int(width/2 - font_size * 3)
        y = int(height/2 - font_size / 2)
        screen.blit(endgame_text,(x,y))
        pygame.display.update()
        pygame.time.delay(3000)
        playing = False

    pygame.display.update()

pygame.quit()
