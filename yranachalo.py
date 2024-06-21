import pygame
import random
import Vawe
import Player
import Guns
import Enemy
pygame.init()

class World:
    def __init__(self, x, y):
        self.x = x / 10
        self.y = y / 10
        self.y = int(self.y)
        self.x = int(self.x)
        self.surf = pygame.Surface((10, 10))
        self.pic = self.surf.get_rect(topleft=(self.x, self.y))
        self.surf.fill((255, 0, 0))
        self.N = 500
        self.Guns = Guns.Guns(PNG)
        self.i = 0
        self.bullets = []

    def revival(self,SCREEN_WIDTH,SCREEN_HIGHT):
        self.cur = Vawe.wave_search(self.arr_world, (0, 3),SCREEN_WIDTH,SCREEN_HIGHT)
        if self.cur == False:
            while self.cur == False:
                self.loc_built(SCREEN_WIDTH,SCREEN_HIGHT)
                self.cur = Vawe.wave_search(self.arr_world, (0, 3),SCREEN_WIDTH,SCREEN_HIGHT)
            return  self.cur[0] * 10 , self.cur[1] * 10

        else:
            return self.cur[0] * 10 , self.cur[1] * 10

    def spawn_enemy(self, SCREEN_WIDTH, SCREEN_HIGHT):
        self.cur_enemy = Vawe.wave_search(self.arr_world, (40, 40), SCREEN_WIDTH, SCREEN_HIGHT)
        if self.cur_enemy == False:
            while self.cur_enemy == False:
                self.loc_built(SCREEN_WIDTH, SCREEN_HIGHT)
                self.cur_enemy = Vawe.wave_search(self.arr_world, (40, 40), SCREEN_WIDTH, SCREEN_HIGHT)
            return self.cur_enemy[0] * 10, self.cur_enemy[1] * 10

        else:
            return self.cur_enemy[0] * 10, self.cur_enemy[1] * 10

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
            #self.arr_world[self.y][self.x] = 0
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
        self.arr_bullet = self.Guns.shoot(angle, x_cord, y_cord, state)
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

    def change_en_world(self):
        self.Enemy = Enemy.Enemy
        goal_arr , goal_angle =self.Enemy.Goal_Bullet()
        goal_state = self.Enemy.Shoot()
        if goal_state == 1:
            for i in self.arr_bullet:
                if goal_arr[int(i[1] / 10) - 1][int(i[0] / 10) - 1] == 1:
                    if int(i[0] / 10) - 1 < 0 or int(i[1] / 10) - 1 < 0:
                        break
                    self.arr_world[int(i[1] / 10) - 1][int(i[0] / 10) - 1] = 0
                    self.arr_x.remove(int(i[0] / 10) - 1)
                    self.arr_y.remove(int(i[1] / 10) - 1)
                    break
        return self.arr_world



from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    K_SPACE,
    QUIT,
)

pygame.init()

FPS = 15  # число кадров в секунду
clock = pygame.time.Clock()
x = 100
y = 100
state = 0
angle = 0
PNG = 'worms.png'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player.Player(PNG)
world = World(x, y)
world.loc_built(SCREEN_WIDTH, SCREEN_HEIGHT)
X, Y = world.revival(SCREEN_WIDTH,SCREEN_HEIGHT)
print(X,Y)
X_enemy , Y_enemy = world.spawn_enemy(SCREEN_WIDTH,SCREEN_HEIGHT)
print(X_enemy,Y_enemy)
Guns = Guns.Guns(PNG)
enemy = Enemy.Enemy()
correct = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()

    X, Y, angle = player.update(pressed_keys, X, Y, angle)
    player.move(pressed_keys)
    #движения enemy
    if correct == 0:
        trace = enemy.Trace(world.arr_world,(X_enemy,Y_enemy),(X,Y))
        correct = 1
    enemy.movement(trace,X_enemy,Y_enemy)
    screen.fill((135, 206, 250))


    state, angle = Guns.give_gun(pressed_keys, state, angle)
    screen.blit(player.surf, player.worm)
    #рисовка соперника
    screen.blit(enemy.surf, enemy.worm_enemy)
    #
    Guns.draw(screen, angle, X, Y, state)

    world.draw(screen,X,Y,pressed_keys)
    X, Y = world.update(X, Y)
    pygame.display.flip()

    clock.tick(FPS)