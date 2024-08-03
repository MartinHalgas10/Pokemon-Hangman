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
        self.hover = False

    def draw(self):
        global button_hover_arr
        global button_img_arr

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.image = button_hover_arr[self.number - 1]
            self.image = pygame.transform.scale(self.image, (BUTTON_WIDTH, BUTTON_HEIGHT,))
            self.hover = True
        else:
            self.image = button_img_arr[self.number - 1]
            self.image = pygame.transform.scale(self.image, (BUTTON_WIDTH, BUTTON_HEIGHT,))
            self.hover = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

    def generate_pokemon(self, generation):
        global pokemon
        if (generation == 1):
            rand = random.randint(0, 151)
            pokemon = Pokemon(rand)
        elif (generation == 2):
            rand = random.randint(151, 251)
            pokemon = Pokemon(rand)
        elif (generation == 3):
            rand = random.randint(251, 386)
            pokemon = Pokemon(rand)
        elif (generation == 4):
            rand = random.randint(386, 493)
            pokemon = Pokemon(rand)
        elif (generation == 5):
            rand = random.randint(493, 649)
            pokemon = Pokemon(rand)
        elif (generation == 6):
            rand = random.randint(649, 721)
            pokemon = Pokemon(rand)
        elif (generation == 7):
            rand = random.randint(721, 809)
            pokemon = Pokemon(rand)
        elif (generation == 8):
            rand = random.randint(809, 905)
            pokemon = Pokemon(rand)
        elif (generation == 9):
            rand = random.randint(905, 1025)
            pokemon = Pokemon(rand)

class Pokemon():

    def __init__(self,  num):
        global pokemon_names
        self.name = pokemon_names[num]
        self.number = num + 1

def print_text(text, x, y):
    font = pygame.font.SysFont("arialblack", 40)
    text = font.render(text, True, ( 255, 0, 0))
    screen.blit(text, ( x, y))

def add_letter(letter):
    global blank_pokemon
    global pokemon
    written = False
    blank_iterator = -1
    final = ''
    for blank_char in blank_pokemon:
        blank_iterator += 1
        pokemon_iterator = -1
        written = False
        for pokemon_char in pokemon.name:
            let_upper = letter.upper()
            popk_upper = pokemon_char.upper()
            pokemon_iterator += 1
            if (blank_char != '-' and blank_iterator == pokemon_iterator) or (pokemon_char.upper() == letter.upper() and blank_iterator == pokemon_iterator):
                if blank_iterator == 0:
                    final = final + pokemon_char.upper()
                else:
                    final = final + pokemon_char
                written = True
                break
        if not written:
            final = final + '-'
    blank_pokemon = final




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

button_arr = []

global button_hover_arr
global button_img_arr
global menu
global pokemon
global blank_pokemon
global letter_arr
menu = True
blank_pokemon = ''
letter_arr = []
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
            elif event.type == pygame.MOUSEBUTTONUP:
                for button in button_arr:
                    if button.hover:
                        button.generate_pokemon(button.number)
                        menu = False
            
            for button in button_arr:
                button.draw()

        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.display.flip()

    clock.tick(60)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_q:
                    add_letter('q')
                case pygame.K_w:
                    add_letter('w')
                case pygame.K_e:
                    add_letter('e')
                case pygame.K_r:
                    add_letter('r')
                case pygame.K_q:
                    add_letter('t')
                case pygame.K_q:
                    add_letter('z')
                case pygame.K_u:
                    add_letter('u')
                case pygame.K_i:
                    add_letter('i')
                case pygame.K_o:
                    add_letter('o')
                case pygame.K_p:
                    add_letter('p')
                case pygame.K_a:
                    add_letter('a')
                case pygame.K_s:
                    add_letter('s')
                case pygame.K_d:
                    add_letter('d')
                case pygame.K_f:
                    add_letter('f')
                case pygame.K_g:
                    add_letter('g')
                case pygame.K_h:
                    add_letter('h')
                case pygame.K_j:
                    add_letter('j')
                case pygame.K_k:
                    add_letter('k')
                case pygame.K_l:
                    add_letter('l')
                case pygame.K_y:
                    add_letter('y')
                case pygame.K_x:
                    add_letter('x')
                case pygame.K_c:
                    add_letter('c')
                case pygame.K_v:
                    add_letter('v')
                case pygame.K_b:
                    add_letter('b')
                case pygame.K_n:
                    add_letter('n')
                case pygame.K_m:
                    add_letter('m')
                

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")


    if len(blank_pokemon) == 0:
        for i in range(len(pokemon.name)):
            blank_pokemon = blank_pokemon + '-'

    print_text(blank_pokemon, SCREEN_WIDTH / 2 - len(pokemon.name) * 20, SCREEN_HEIGHT / 2)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

f.close()

pygame.quit()