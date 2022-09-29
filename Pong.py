from pygame import *
from random import randint
# create the window object
WIDTH = 800
HEIGHT = 640
window = display.set_mode((WIDTH, HEIGHT))
# create the clock object
clock = time.Clock()

class ImageSprite(sprite.Sprite):
    def __init__(self, file_name, pos, size, speed): # constructor (a function that runs when a new object is created)
        super().__init__()
        self.image = image.load(file_name)
        self.image = transform.scale(self.image, size)
        self.rect = Rect(pos, size)
        self.speed = Vector2(speed)
        self.original_position = self.rect.topleft
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
    def reset(self):
        self.rect.topleft = self.original_position
class Player(ImageSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed.y
        if keys[K_s]:
            self.rect.y += self.speed.y
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
class Player2(ImageSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed.y
        if keys[K_DOWN]:
            self.rect.y += self.speed.y
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
class Ball(ImageSprite):
    def bounce_x(self):
        self.speed.x *= -1
    def bounce_y(self):
        self.speed.y *= -1
    def update(self):
        self.rect.topleft += self.speed
bg = ImageSprite(file_name="backgroundpong.png", pos=(0,0),size = (WIDTH,HEIGHT),speed=(0,0))
p1 = Player(file_name="redpong.png", pos =(40,HEIGHT/2), size=(40,80), speed=(0,15))
p2 = Player2(file_name="bluepong.png", pos =(WIDTH-80,HEIGHT/2), size=(40,80), speed=(0,15))
ball = Ball(file_name="ballpong.png", pos =(WIDTH/2,HEIGHT/2),size=(90,50),speed=(10,10))
p2_wins = ImageSprite(file_name="red_wins.png", pos=(0,0), size=(WIDTH,HEIGHT),speed=(0,0))
while not event.peek(QUIT):
    if ball.rect.top < 0 or ball.rect.bottom > HEIGHT:
        ball.bounce_y()
    if sprite.collide_rect(ball,p1):
        ball.bounce_x()
        ball.rect.left = p1.rect.right
    if sprite.collide_rect(ball,p2):
        ball.bounce_x()
        ball.rect.right = p2.rect.left
    bg.draw(window)
    p1.update()
    p1.draw(window)
    p2.update()
    p2.draw(window)
    ball.update()
    ball.draw(window)
    if ball.rect.left < 0:
        pass
    if ball.rect.right > WIDTH:
        p2_wins.draw(window)
    display.update()
    clock.tick(20)