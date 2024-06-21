import pygame
import Guns
class Bullet():
    def __init__(self,x_cord,y_cord,angle,world):
        self.world = world
        self.Gun = Guns.Guns('worms.png')
        self.i = 0
        self.bullets = []
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.angle = angle


    def change(self,pressed_key,screen):
        self.arr_bullet = self.Gun.shoot(self.angle, self.x_cord, self.y_cord, self.state)
        if self.arr_bullet != None:
            if pressed_key[K_SPACE]:
                for i in self.arr_bullet:
                    self.draw_bullet(screen,i)
                    if self.world.arr_world[int(i[1] / 10) - 1][int(i[0] / 10) - 1] == 1:
                        if int(i[0] / 10) - 1 < 0 or int(i[1] / 10) - 1 < 0:
                            break
                        self.world.arr_world[int(i[1] / 10) - 1][int(i[0] / 10) - 1] = 0
                        self.world.arr_x.remove(int(i[0] / 10) - 1)
                        self.world.arr_y.remove(int(i[1] / 10) - 1)
                        break

    def draw_bullet(self,screen,i):
        self.screen = screen
        pygame.draw.circle(self.screen, (255, 255, 255), (i[0], i[1]), 5)







from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_e,
    K_r,
    K_SPACE
)