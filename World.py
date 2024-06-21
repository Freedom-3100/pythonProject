import Guns
import pygame
import Vawe
import random
class World:
    def __init__(self, x, y, angle, state):
        self.x = x / 10
        self.y = y / 10
        self.y = int(self.y)
        self.x = int(self.x)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.surf = pygame.Surface((10, 10))
        self.pic = self.surf.get_rect(topleft=(self.x, self.y))
        self.surf.fill(self.red)
        self.N = 6000
        self.Guns = Guns.Guns(PNG)
        self.i = 0
        self.bullets = []
        self.angle  = angle
        self.state = state

    def revival(self,SCREEN_WIDTH,SCREEN_HIGHT):
        self.cur  = Vawe.wave_search(self.arr_world, (0, 3),SCREEN_WIDTH,SCREEN_HIGHT)
        if self.cur == False:
            while self.cur == False:
                self.loc_built(SCREEN_WIDTH,SCREEN_HIGHT)
                self.cur = Vawe.wave_search(self.arr_world, (0, 3),SCREEN_WIDTH,SCREEN_HIGHT)
            return  self.cur[0] * 10 , self.cur[1] * 10

        else:
            return self.cur[0] * 10 , self.cur[1] * 10

    def update(self, cord_x, cord_y):
        for i in range(len(self.arr_x)):
            if self.arr_world[int(cord_y / 10) + 1][int(cord_x / 10)] == 1:
                cord_y -= 5
            if self.arr_world[int(cord_y / 10) - 1][int(cord_x / 10)] == 1:
                cord_y += 5
            if self.arr_world[int(cord_y / 10)][int(cord_x / 10) + 1] == 1:
                cord_x -= 5
            if self.arr_world[int(cord_y / 10)][int(cord_x / 10) - 1] == 1:
                cord_x += 5
        return cord_x, cord_y

    def loc_built(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.SCREEN_HEIGHT = SCREEN_HEIGHT / 10
        self.SCREEN_WIDTH = SCREEN_WIDTH / 10
        self.SCREEN_WIDTH = int(self.SCREEN_WIDTH)
        self.SCREEN_HEIGHT = int(self.SCREEN_HEIGHT)
        self.arr_world = []
        self.arr_x = [self.x / 10]
        self.arr_y = [self.y / 10]

        for i in range(self.SCREEN_HEIGHT):
            self.arr_world.append([0] * self.SCREEN_WIDTH)
        for i in range(self.N):
            self.arr_world[self.y][self.x] = 1
            self.y += random.choice([-1, 1, 0])
            self.x += random.choice([-1, 1, 0])
            if self.x < 0:
                self.x = 80 + self.x
            if self.y < 0:
                self.y = 60 + self.y
            if self.x > 79:
                self.x = 10
            if self.y > 59:
                self.y = 10
            self.arr_x.append(self.x)
            self.arr_y.append(self.y)

    def draw(self, screen,  x_cord,y_cord,  pressed_key):
        self.screen = screen
        self.arr_world = self.change(pressed_key,x_cord,y_cord)
        for i in range(self.SCREEN_HEIGHT):
            for j in range(self.SCREEN_WIDTH):
                if self.arr_world[i][j] == 1:
                    self.screen.blit(self.surf, (j * 10, i * 10))
        if pressed_key[K_SPACE]:
            if self.arr_bullet != None:
                while self.i < len(self.arr_bullet):
                    self.bullets.append(self.arr_bullet[self.i])
                    pygame.draw.circle(self.screen, (255, 255, 255), (self.bullets[0][0], self.bullets[0][1]), 5)
                    self.bullets.pop(0)
                    self.i += 1
        self.i = 0


    def change(self,pressed_key,x_cord,y_cord):
        self.arr_bullet = self.Guns.shoot(self.angle, x_cord, y_cord, self.state)
        if self.arr_bullet != None:
            if pressed_key[K_SPACE]:
                for i in self.arr_bullet:
                    if self.arr_world[int(i[1] / 10) - 1][int(i[0] / 10) - 1] == 1:
                        if int(i[0] / 10) - 1 < 0 or int(i[1] / 10) - 1 < 0:
                            break
                        self.arr_world[int(i[1] / 10) - 1][int(i[0] / 10) - 1] = 0
                        self.arr_x.remove(int(i[0] / 10) - 1)
                        self.arr_y.remove(int(i[1] / 10) - 1)
                        break
        return self.arr_world

PNG = 'worms.png'

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