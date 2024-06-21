from PIL import Image, ImageOps
import pygame
import Shoot
class Guns:
    def __init__(self, PNG):
        self.image = Image.open(PNG)

    def draw(self, screen, angle, cord_x, cord_y, state):
        self.state = state
        self.screen = screen
        self.angle = angle
        self.gun = self.image.crop((0, 100, 55, 135))
        self.gun.save('gun_1.png')
        self.gun = Image.open('gun_1.png')
        self.gun = ImageOps.mirror(self.gun)
        self.gun.save('gun_1.png')
        self.surf = pygame.image.load('gun_1.png').convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.guns = pygame.transform.rotate(self.surf, -self.angle)
        self.guns_rect = self.guns.get_rect(center=(cord_x, cord_y))
        if self.state == 1:
            self.screen.blit(self.guns, self.guns_rect)

    def give_gun(self, pressed_key, state, angle):
        self.angle = angle
        self.state = state
        if pressed_key[K_m]:
            if self.state == 1:
                self.state = 0
                self.angle = 0
        if pressed_key[K_n]:
            if self.state == 0:
                self.state = 1
        return self.state, self.angle

    def shoot(self,angle, x_cord,y_cord, state):
        if state == 1:
            return Shoot.trajectory(angle, x_cord,y_cord, 800, 600, 40)

from pygame.locals import (
    RLEACCEL,
    K_m,
    K_n,
)