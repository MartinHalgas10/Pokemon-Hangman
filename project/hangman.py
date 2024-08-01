import json
import pygame
import random

class Button():
    def __init__(self, x, y, image, number):
        self.image = image
        self.image = pygame.transform.scale(image, (BUTTON_WIDTH, BUTTON_HEIGHT,))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.number = number

    def draw(self):
        global button_hover_arr
        global button_img_arr

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.image = button_hover_arr[self.number - 1]
            self.image = pygame.transform.scale(self.image, (BUTTON_WIDTH, BUTTON_HEIGHT,))
        else:
            self.image = button_img_arr[self.number - 1]
            self.image = pygame.transform.scale(self.image, (BUTTON_WIDTH, BUTTON_HEIGHT,))

        screen.blit(self.image, (self.rect.x, self.rect.y))

class Pokemon():

    def __init__(self, number):
        global pokemon_names
        self.name = pokemon_names[number + 1]
        self.number = number

def print_text(text, x, y):
    font = pygame.font.SysFont("arialblack", 40)
    text = font.render(text, True, ( 255, 0, 0))
    screen.blit(text, ( x, y))


f = open('resources/jsons/pokemon.json')

global pokemon_names
pokemon_names = json.load(f)

# pygame setup
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 75

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
menu = True

button_arr = []

global button_hover_arr
global button_img_arr
button_img_arr = []
button_hover_arr = []

for i in range(9):
    gen_image = pygame.image.load('resources/images/gen' + str(i + 1) + '.png')
    gen_hover = pygame.image.load('resources/images/gen' + str(i + 1) + '_hover.png')
    button_hover_arr.append(gen_hover)
    button_img_arr.append(gen_image)
    if i < 3:
        gen_button = Button( (SCREEN_WIDTH) / 3 * i + 100  , 200 , gen_image, i+1)
        button_arr.append(gen_button)
    elif i < 6:
        gen_button = Button( (SCREEN_WIDTH) / 3 * (i - 3) + 100  , 400 , gen_image, i+1)
        button_arr.append(gen_button)
    elif i < 9:
        gen_button = Button( (SCREEN_WIDTH) / 3 * (i - 6) + 100  , 600 , gen_image, i+1)
        button_arr.append(gen_button)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    while menu:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                running = False

        for button in button_arr:
            button.draw()

        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.display.flip()

    clock.tick(60)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

f.close()

pygame.quit()