import Vawe
import math
import Shoot
import pygame
import image
import Guns
class Enemy(pygame.sprite.Sprite):
    def __init__(self):

        self.picture = image.Picture("worms.png")
        self.queue = self.picture.add_to_queue("flip")
        self.queue_reverse = self.picture.add_to_queue("cut")
        self.surf = pygame.image.load('mirror.png').convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.worm_enemy = self.surf.get_rect()
        self.ind = 0
        self.Guns = Guns.Guns('worms.png')
        self.state = 0

    def movement(self, Movement,x_cord_enemy,y_cord_enemy):
        self.x_cord_enemy = x_cord_enemy
        self.y_cord_enemy = y_cord_enemy
        self.Movement = Movement
        if self.trace != False:
            if self.ind < len(self.Movement):
                self.x_cord_enemy = self.Movement[self.ind][0] * 10
                self.y_cord_enemy = self.Movement[self.ind][1] * 10
                self.png = self.picture.go_queue(self.queue_reverse)
                self.surf = pygame.image.load(self.png).convert()
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)
                self.worm_enemy = self.surf.get_rect(center=(self.x_cord_enemy, self.y_cord_enemy))
                self.ind += 1
        else:
            self.worm_enemy = self.surf.get_rect(center=(self.x_cord_enemy, self.y_cord_enemy))
            self.state = 1

    def Shoot(self):

        return self.state


    def Trace(self,arr_world, spawn, To):

        self.trace = Vawe.wave(arr_world, (int(spawn[0] / 10), int(spawn[1] / 10)), (int(To[0] / 10), int(To[1] / 10)),80, 60)
        if self.trace != False:
            self.Movement = Vawe.wave_return(self.trace, (int(spawn[0] / 10), int(spawn[1] / 10)),(int(To[0] / 10), int(To[1] / 10)), 80, 60)
            self.Movement_origin = []

            for i in range(1, len(self.Movement) + 1):
                self.Movement_origin.append((self.Movement[-i][0],self.Movement[-i][1]))
            print(self.Movement)
            print(self.Movement_origin)
            return self.Movement_origin

    def Goal_Bullet(self,spawn,To):
        self.angle = self.angle_search(spawn,To)
        self.goal_arr = self.guidance(self.angle,spawn,To)
        if self.goal_arr != None:
            return self.goal_arr , self.angle









    def angle_search(self, From, To):
        if To[1]<From[1] and To[0] > From[0]:
            self.angle = math.atan((To[1]-From[1])/(To[0]-From[0]))
            self.angle = math.degrees(self.angle)

        elif To[0]>From[0] and To[1]>From[1]:
            self.angle = -math.atan((To[1]-From[1])/(To[0]-From[0]))
            self.angle = math.degrees(self.angle)

        elif To[0]<From[0] and To[1] > From[1]:
            self.angle = math.atan((To[1] - From[1]) / (To[0] - From[0]))
            self.angle = math.degrees(self.angle) + 90

        elif To[0] < From[0] and To[1] < From[1]:
            self.angle = math.atan((To[1] - From[1]) / (To[0] - From[0]))
            self.angle = math.degrees(self.angle) + 180

        self.angle = int(self.angle)
        if self.angle % 5 != 0:
            if self.angle % 5 < 3:
                self.angle -= self.angle % 5
            else:
                self.angle += 5 - self.angle % 5
        return self.angle

    def guidance(self, angle, From, To):
        self.angle = angle
        self.From_x, self.From_y = From
        if self.angle > -90 and self.angle < 90:
            while angle < 90 :
                self.trajectori = Shoot.trajectory(self.angle, self.From_x, self.From_y, 800, 600, 40)
                for ind_1 in range(-10,10):
                    for ind_2 in range(-10,10):
                        if (To[0]+ind_1,To[1]+ind_2) in self.trajectori:
                            return self.trajectori,self.angle
                self.angle += 5

        elif self.angle < 270 and angle > 90:
            while self.angle > 90:
                self.trajectori = Shoot.trajectory(angle, self.From_x, self.From_y, 800, 600, 40)
                for ind_1 in range(-10, 10):
                    for ind_2 in range(-10, 10):
                        if (To[0] + ind_1, To[1] + ind_2) in self.trajectori:
                            return self.trajectori, self.angle
                self.angle += 5


from pygame.locals import (
    RLEACCEL,
)
PNG = 'worms.png'


