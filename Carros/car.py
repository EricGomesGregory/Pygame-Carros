import pygame

class Car (object):
    def __init__(self, x, y, img) -> None:
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.image = img
        self.fliped = False
        self.flip_cout = 0

    def update(self, screen : pygame.Surface, speed: float, step: int):
        self.speed = speed
        
        if self.flip_cout == 3:
            return

        if not self.fliped:
            if self.x < screen.get_width():
                self.x += speed
            else:
                self.y += step
                self.fliped = True
                self.flip_cout += 1
        
        if self.fliped:
            if self.x > 0 - self.image.get_width():
                self.x -= speed
            else:
                self.y += step
                self.fliped = False
                self.flip_cout += 1

        self.pos = (self.x, self.y)
        print("Car: {} speed: {}".format(self.pos, self.speed))

    def draw(self, screen : pygame.Surface):
        if self.fliped:
            fliped_img = pygame.transform.flip(self.image, True, False)
            screen.blit(fliped_img, self.pos)
        else:
            screen.blit(self.image, self.pos)