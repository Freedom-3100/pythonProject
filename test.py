import image
picture = image.Picture(PNG = 'worms.png')
queue = picture.add_to_queue('flip')
print(queue)
picture.rotate()