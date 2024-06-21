import pygame
from PIL import Image, ImageOps
import Stack_List_Queue
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
        self.queue = Stack_List_Queue.Queue()
        self.value = value
        if self.value == "flip":
            self.new_pictures = Picture(PNG='worms.png')
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
            self.new_pictures = Picture(PNG='worms.png')
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

