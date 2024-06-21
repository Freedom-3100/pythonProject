import Vawe
import math
import Shoot
import Stack_List_Queue
import pygame
import image

def animation(png):


    elif pressed_keys[K_LEFT]:
        png = picture.go_queue(queue_1)
        surf = pygame.image.load(png).convert()
        surf.set_colorkey((255, 255, 255), RLEACCEL)
        worm = surf.get_rect(center=(x,y))
        state = 1

    else:
        if state == 0:
            surf = pygame.image.load('mirror.png').convert()
            surf.set_colorkey((255, 255, 255), RLEACCEL)
        elif state == 1:
            surf = pygame.image.load('cut.png').convert()
            surf.set_colorkey((255, 255, 255), RLEACCEL)

        worm = surf.get_rect(center=(self.x, self.y))

        return

def movement(arr_world, From , To):
    picture = image.Picture("worms.png")
    queue = picture.add_to_queue("flip")
    queue_reverse = picture.add_to_queue("cut")
    trace = Vawe.wave()
    if trace != False:
        movement = Vawe.wave_return()

    else:
        pass





def spawn(self, SCREEN_WIDTH, SCREEN_HIGHT):
    self.cur = Vawe.wave_search(self.arr_world, (30, 30), SCREEN_WIDTH, SCREEN_HIGHT)
    if self.cur == False:
        while self.cur == False:
            self.loc_built(SCREEN_WIDTH, SCREEN_HIGHT)
            self.cur = Vawe.wave_search(self.arr_world, (30, 30), SCREEN_WIDTH, SCREEN_HIGHT)
        return self.cur[0] * 10, self.cur[1] * 10

    else:
        return self.cur[0] * 10, self.cur[1] * 10

def angle_search(From, To):
    if To[1]<From[1] and To[0] > From[0]:
        angle = math.atan((To[1]-From[1])/(To[0]-From[0]))
        angle = math.degrees(angle)

    elif To[0]>From[0] and To[1]>From[1]:
        angle = -math.atan((To[1]-From[1])/(To[0]-From[0]))
        angle = math.degrees(angle)

    elif To[0]<From[0] and To[1] > From[1]:
        angle = math.atan((To[1] - From[1]) / (To[0] - From[0]))
        angle = math.degrees(angle) + 90

    elif To[0] < From[0] and To[1] < From[1]:
        angle = math.atan((To[1] - From[1]) / (To[0] - From[0]))
        angle = math.degrees(angle) + 180

    angle = int(angle)
    if angle % 5 != 0:
        if angle % 5 < 3:
            angle -= angle % 5
        else:
            angle += 5 - angle % 5
    return angle

def guidance(angle,From,To):
    From_x, From_y = From
    if angle > -90 and angle < 90:
        while angle < 90 :
            trajectori = Shoot.trajectory(angle, From_x, From_y, 800, 600, 40)
            for ind_1 in range(-10,10):
                for ind_2 in range(-10,10):
                    if (To[0]+ind_1,To[1]+ind_2) in trajectori:
                        return trajectori
            angle += 5

    elif angle < 270 and angle > 90:
        while angle > 90:
            trajectori = Shoot.trajectory(angle, From_x, From_y, 800, 600, 40)
            for ind_1 in range(-10, 10):
                for ind_2 in range(-10, 10):
                    if (To[0] + ind_1, To[1] + ind_2) in trajectori:
                        return trajectori
            angle += 5


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
