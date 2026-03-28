import pygame
import random
import time
pygame.init()

x = 900
y = 700

screen = pygame.display.set_mode((x, y))

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\kiewj\\Desktop\\pro gd\\recycle\\bin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()

class Recycle(pygame.sprite.Sprite):
     def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\kiewj\\Desktop\\pro gd\\recycle" + img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

class Nonrecycle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\kiewj\\Desktop\\pro gd\\recycle\\plasticbag.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

def changebackground(img):
    bg = pygame.image.load("C:\\Users\\kiewj\\Desktop\\pro gd\\recycle" + img)
    bg = pygame.transform.scale(bg, (x, y))
    screen.blit(bg, (0, 0))

images = ["item1.png", "box.png", "pencil.png"]
item_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
plastic = pygame.sprite.Group()

for i in range(50):
    item = Recycle(random.choice(images))
    item.rect.x = random.randint(0, x)
    item.rect.y = random.randint(0, y)
    item_list.add(item)
    all_sprites.add(item)

for i in range(20):
    item = Nonrecycle()
    item.rect.x = random.randint(0, x)
    item.rect.y = random.randint(0, y)
    plastic.add(item)
    all_sprites.add(item)

bin = Bin()
all_sprites.add(bin)

run = True
score = 0
clock = pygame.time.Clock()
start_time = time.time()
font = pygame.font.SysFont("Arial", 18)
pygame.font.init()
text = font.render(f"Score: {}".format(score), True, "Black")











