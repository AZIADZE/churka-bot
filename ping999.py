from pygame import *
from random import randint
clock = time.Clock()
FPS = 60

game = True
finish = False

heigth = 700
width = 700

window = display.set_mode((heigth,width))
display.set_caption("ping pong")

bg_color = (62, 147, 167)

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed,height,width):
        super().__init__()
        self.height = height
        self.width = width
        self.image = transform.scale(image.load(player_image),(self.height,self.width))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < width - 100:
            self.rect.y += self.speed
        display.update()
    def update_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < width - 100:
            self.rect.y += self.speed
        display.update()
    def update_3(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < width - 100:
            self.rect.y += self.speed
        display.update()
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < width - 100:
            self.rect.x += self.speed

racket1 = Player("racket.png", 20, 350, 5, 25, 250)
racket2 = Player("racket.png", 680, 350, 5, 25, 250)
ball = Player("ball.png", 350, 350, 5, 100, 100)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(bg_color)
        racket1.reset()
        racket2.reset()
        ball.reset()


    racket1.update_1()
    racket2.update_2()
    ball.update_3()

    display.update()
    clock.tick(FPS)