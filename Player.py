import Stack_List_Queue
import pygame
import image
class Player(pygame.sprite.Sprite):

    def __init__(self, PNG):
        self.state = 0
        self.picture = image.Picture(PNG)
        self.queue = self.picture.add_to_queue("flip")
        self.queue_1 = self.picture.add_to_queue("cut")
        super(Player, self).__init__()
        self.surf = pygame.image.load('mirror.png').convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.worm = self.surf.get_rect()

    def update(self, pressed_keys, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        if pressed_keys[K_UP]:
            self.worm.move_ip(0, -5)
            self.y -= 5
        if pressed_keys[K_DOWN]:
            self.worm.move_ip(0, 5)
            self.y += 5
        if pressed_keys[K_LEFT]:
            self.worm.move_ip(-5, 0)
            self.x -= 5
        if pressed_keys[K_RIGHT]:
            self.worm.move_ip(5, 0)
            self.x += 5
        if pressed_keys[K_e]:
            if self.angle >= 270:
                self.angle -= 5
            self.angle += 5
        if pressed_keys[K_r]:
            if self.angle <= -90:
                self.angle += 5
            self.angle -= 5

        if self.worm.left < 0:
            self.worm.left = 0
            self.x = 15
        if self.worm.right > SCREEN_WIDTH:
            self.worm.right = SCREEN_WIDTH
            self.x = SCREEN_WIDTH - 15
        if self.worm.top < 0:
            self.worm.top = 0
            self.y = 18
        if self.worm.bottom >= SCREEN_HEIGHT:
            self.worm.bottom = SCREEN_HEIGHT
            self.y = SCREEN_HEIGHT - 18

        return self.x, self.y, self.angle

    def move(self, pressed_keys):
        if pressed_keys[K_RIGHT]:
            self.png = self.picture.go_queue(self.queue)
            self.surf = pygame.image.load(self.png).convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.worm = self.surf.get_rect(center=(self.x, self.y))
            self.state = 0

        elif pressed_keys[K_LEFT]:
            self.png = self.picture.go_queue(self.queue_1)
            self.surf = pygame.image.load(self.png).convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.worm = self.surf.get_rect(center=(self.x, self.y))
            self.state = 1

        else:
            if self.state == 0:
                self.surf = pygame.image.load('mirror.png').convert()
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            elif self.state == 1:
                self.surf = pygame.image.load('cut.png').convert()
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            self.worm = self.surf.get_rect(center=(self.x, self.y))

            return

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_e,
    K_r,
    K_m,
    K_n,
    K_SPACE,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600