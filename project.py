import pygame
from PIL import Image, ImageOps
from random import randint
import random
import Vawe
import Shoot

pygame.init()


class Node():
    def __init__(self, v):
        self.value = v
        self.next = None


class List():
    def __init__(self):
        self.tail = None
        self.root = None

    def AddRoot(self, node):
        node.next = self.root
        if self.tail is None:
            self.tail = node
        self.root = node

    def AddTail(self, node):

        if self.tail is None:
            self.root = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def RemoveRoot(self):
        to_remove = self.root
        self.root = self.root.next
        if self.tail == to_remove:
            self.tail = None
        return to_remove

    def At(self, index):
        current = self.root
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def RemoveIndex(self, index):
        if index == 0:
            return self.RemoveRoot()
        current = self.At(index - 1)
        to_remove = current.next
        current.next = to_remove.next
        if self.tail == to_remove:
            self.tail = current
        return to_remove

    def RemoveTail(self):
        if self.root == self.tail:
            return self.RemoveRoot()
        current = self.root
        while current.next != self.tail:
            current = current.next
        to_remove = self.tail
        current.next = None
        self.tail = current
        return to_remove

    def Print(self):
        current = self.root
        while (current != None):
            print(current.value)
            current = current.next
        # print(self.tail.value)

    def Find(self, value):
        current = self.root
        while current.next.value != value:
            if current == None:
                return None
            current = current.next
        return current

    def Remove(self, value):
        if self.root.value == value:
            return self.RemoveRoot()
        current = self.root
        while current.next.value != value:
            current = current.next
        to_remove = current.next
        current.next = to_remove.next
        if self.tail == to_remove:
            self.tail = current
        return to_remove


class Queue():
    def __init__(self):
        self.list = List()

    def push(self, value):
        node = Node(value)
        self.list.AddTail(node)

    def pop(self):
        current = self.list.RemoveIndex(0)
        return current.value


class Picture:
    def __init__(self, PNG):
        self.image = Image.open(PNG)

    def rotate(self):
        self.rotated_img = self.image.rotate(180)
        self.rotated_img.save('rotated.png')
        self.rotated_png = Image.open('rotated.png')
        self.rotated_png.show()

    def cut(self, x, y, hight, wigth):
        self.new_picture = self.image.crop((x, y, hight, wigth))
        self.new_picture.save('cut.png')

    def show(self):
        self.image.show()

    def flip(self):
        self.img = ImageOps.mirror(self.new_picture)
        self.img.save('mirror.png')

    def add_to_queue(self, value):
        self.queue = Queue()
        self.value = value
        if self.value == "flip":
            self.new_pictures = Picture(PNG)
            self.new_pictures.cut(35, 0, 64, 40)
            self.new_pictures.flip()
            self.new_picture_new = Image.open('mirror.png')
            self.new_picture_new.save('mirror_1.png')
            self.queue.push('mirror_1.png')
            self.new_pictures.cut(65, 0, 95, 40)
            self.new_pictures.flip()
            self.new_picture_new = Image.open('mirror.png')
            self.new_picture_new.save('mirror_2.png')
            self.queue.push('mirror_2.png')
            self.new_pictures.cut(0, 0, 32, 40)
            self.new_pictures.flip()
            self.new_picture_new = Image.open('mirror.png')
            self.new_picture_new.save('mirror_3.png')
            self.queue.push('mirror_3.png')
            return self.queue
        elif self.value == "cut":
            self.new_pictures = Picture(PNG)
            self.new_pictures.cut(35, 0, 64, 40)
            self.new_picture_new = Image.open('cut.png')
            self.new_picture_new.save('cut_1.png')
            self.queue.push('cut_1.png')
            self.new_pictures.cut(65, 0, 94, 40)
            self.new_picture_new = Image.open('cut.png')
            self.new_picture_new.save('cut_2.png')
            self.queue.push('cut_2.png')
            self.new_pictures.cut(0, 0, 32, 40)
            self.new_pictures.flip()
            self.new_picture_new = Image.open('cut.png')
            self.new_picture_new.save('cut_3.png')
            self.queue.push('cut_3.png')
            return self.queue

    def go_queue(self, queue):
        self.queue = queue
        self.value = self.queue.pop()
        self.queue.push(self.value)
        return self.value




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
        self.guns = pygame.transform.rotate(self.surf, self.angle)
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


class World:
    def __init__(self, x, y):
        self.x = x / 10
        self.y = y / 10
        self.y = int(self.y)
        self.x = int(self.x)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.surf_few = pygame.Surface((10, 10))
        self.surf = pygame.Surface((10, 10))
        self.pic = self.surf.get_rect(topleft=(self.x, self.y))
        self.surf_few.fill(self.white)
        self.surf.fill(self.red)
        self.N = 6000

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
            self.picture = self.surf.get_rect(topleft=(self.arr_x[i] * 10, self.arr_y[i] * 10))
            if self.picture.collidepoint(cord_x, cord_y + 10):
                cord_y -= 5
            if self.picture.collidepoint(cord_x, cord_y - 10):
                cord_y += 5
            if self.picture.collidepoint(cord_x + 10, cord_y):
                cord_x -= 5
            if self.picture.collidepoint(cord_x - 10, cord_y):
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

    def draw(self, screen):
        self.screen = screen
        for i in range(self.SCREEN_HEIGHT):
            for j in range(self.SCREEN_WIDTH):
                if self.arr_world[i][j] == 1:
                    self.screen.blit(self.surf, (j * 10, i * 10))



class Player(pygame.sprite.Sprite):

    def __init__(self, PNG):
        self.queue = Queue()
        self.state = 0
        self.picture = Picture(PNG)
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


class Enemy:
    def __init__(self):
        pass


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
player = Player(PNG)
world = World(x, y)
world.loc_built(SCREEN_WIDTH, SCREEN_HEIGHT)
X, Y = world.revival(SCREEN_WIDTH,SCREEN_HEIGHT)
Guns = Guns(PNG)

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

    screen.fill((135, 206, 250))

    state, angle = Guns.give_gun(pressed_keys, state, angle)
    screen.blit(player.surf, player.worm)
    Guns.draw(screen, angle, X, Y, state)

    world.draw(screen)
    X, Y = world.update(X, Y)
    pygame.display.flip()

    clock.tick(FPS)