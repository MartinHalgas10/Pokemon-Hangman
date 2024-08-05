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

    def gen_btn_draw(self):
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

    def end_btn_draw(self, basic, hover):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.image = hover
            self.image = pygame.transform.scale(self.image, (BUTTON_WIDTH, BUTTON_HEIGHT,))
            self.hover = True
        else:
            self.image = basic
            self.image = pygame.transform.scale(self.image, (BUTTON_WIDTH, BUTTON_HEIGHT,))
            self.hover = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

    def generate_pokemon(self, generation):
        global pokemon
        if (generation == 1):
            rand = random.randint(0, 150)
            pokemon = Pokemon(rand)
        elif (generation == 2):
            rand = random.randint(151, 250)
            pokemon = Pokemon(rand)
        elif (generation == 3):
            rand = random.randint(251, 385)
            pokemon = Pokemon(rand)
        elif (generation == 4):
            rand = random.randint(386, 492)
            pokemon = Pokemon(rand)
        elif (generation == 5):
            rand = random.randint(493, 648)
            pokemon = Pokemon(rand)
        elif (generation == 6):
            rand = random.randint(649, 720)
            pokemon = Pokemon(rand)
        elif (generation == 7):
            rand = random.randint(721, 808)
            pokemon = Pokemon(rand)
        elif (generation == 8):
            rand = random.randint(809, 904)
            pokemon = Pokemon(rand)
        elif (generation == 9):
            rand = random.randint(905, 1024)
            pokemon = Pokemon(rand)

class Pokemon():

    def __init__(self,  num):
        global pokemon_names
        self.name = pokemon_names[num]['name']['english']
        self.number = num + 1
        self.types = pokemon_names[num]['type']

        picture_id = num + 1
        if picture_id < 10:
            picture_id = '00' + str(picture_id)
        elif picture_id < 100:
            picture_id = '0' + str(picture_id)
        else:
            picture_id = str(picture_id)
        self.picture = pygame.image.load('resources/images/pokedex/' + picture_id + '.png')

def print_text(text, x, y):
    font = pygame.font.SysFont("arialblack", 40)
    text = font.render(text, True, ( 255, 0, 0))
    screen.blit(text, ( x, y))

def add_letter(letter):
    global blank_pokemon
    global pokemon
    global lives
    found = False
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
                if blank_char == '-':
                    found = True
                break
        if not written:
            final = final + '-'
    blank_pokemon = final
    if found == False:
        lives += 1




f = open('resources/jsons/pokedex.json', encoding='utf-8')

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
global lives

lives = 0
menu = True
blank_pokemon = ''
letter_arr = []
button_img_arr = []
button_hover_arr = []
lives_img_arr = []
end_menu = False
bg_print = True

bg_game = pygame.transform.scale(pygame.image.load('resources/images/background_game.jpg'), (SCREEN_WIDTH,SCREEN_HEIGHT))
retry_image = pygame.transform.scale(pygame.image.load('resources/images/buttons/retry.png'), (BUTTON_WIDTH, BUTTON_HEIGHT))
retry_hover = pygame.transform.scale(pygame.image.load('resources/images/buttons/retry_hover.png'), (BUTTON_WIDTH, BUTTON_HEIGHT))
blank = pygame.image.load('resources/images/blank.png')

for i in range(5):
    live_img = pygame.transform.scale(pygame.image.load('resources/images/lives/pikachu_' + str(i + 1) + '.png'), (200, 200)).convert_alpha()
    lives_img_arr.append(live_img)
lives_img_arr.append(blank)

for i in range(8):
    gen_image = pygame.image.load('resources/images/buttons/gen' + str(i + 1) + '.png')
    gen_hover = pygame.image.load('resources/images/buttons/gen' + str(i + 1) + '_hover.png')
    button_hover_arr.append(gen_hover)
    button_img_arr.append(gen_image)
    if i < 3:
        gen_button = Button( (SCREEN_WIDTH) / 3 * i + 100  , 50 , gen_image, i+1)
        button_arr.append(gen_button)
    elif i < 6:
        gen_button = Button( (SCREEN_WIDTH) / 3 * (i - 3) + 100  , 250 , gen_image, i+1)
        button_arr.append(gen_button)
    elif i < 9:
        gen_button = Button( (SCREEN_WIDTH) / 3 * (i - 6) + 100  , 450 , gen_image, i+1)
        button_arr.append(gen_button)

screen.blit(bg_game, (0, 0))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    while menu:
        if bg_print:
            blank_pokemon = ''
            screen.blit(bg_game, (0, 0))
            bg_print = False
            lives = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                running = False
                end_menu = False
            elif event.type == pygame.MOUSEBUTTONUP:
                for button in button_arr:
                    if button.hover:
                        button.generate_pokemon(button.number)
                        menu = False
            
            for button in button_arr:
                button.gen_btn_draw()

        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.display.flip()

    clock.tick(60)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
            running = False
            end_menu = False
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
                case pygame.K_t:
                    add_letter('t')
                case pygame.K_z:
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
                case pygame.K_MINUS:
                    add_letter('-')
                case pygame.K_PERIOD:
                    add_letter('.')               

    while end_menu:
        retry_button = Button( 20 , SCREEN_HEIGHT - 95 , retry_image, 10)
        retry_button.end_btn_draw(retry_image, retry_hover)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                running = False
                end_menu = False
            elif event.type == pygame.MOUSEBUTTONUP:
                for button in button_arr:
                    if retry_button:
                        end_menu = False
                        menu = True
                        bg_print = True
                        letter_arr = []
                        pokemon.types = []
                        pokemon.picture = blank

        pygame.display.flip()
        clock.tick(60)

    if pokemon.name != blank_pokemon or lives >= 5:
        # fill the screen with a color to wipe away anything from last frame
        if lives >= 5:
            screen.blit(bg_game, (0,0))
            screen.blit(pokemon.picture, (SCREEN_WIDTH / 2 - 225, 200))
            print_text(pokemon.name, SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT - 120)
        else:
            screen.blit(bg_game, (0, 0))
            screen.blit(lives_img_arr[lives], (SCREEN_WIDTH / 2 -100, 10))

        element_counter = 0
        for element in pokemon.types:
            print_text(element, 0, 40 * element_counter)
            element_counter += 1

    if len(blank_pokemon) == 0:
            for i in range(len(pokemon.name)):
                blank_pokemon = blank_pokemon + '-'

    # RENDER YOUR GAME HERE

    if ((pokemon.name == blank_pokemon and blank_pokemon != '') or lives >= 5) and menu == False:
        screen.blit(bg_game, (0,0))
        screen.blit(pokemon.picture, (SCREEN_WIDTH / 2 - 225, 200))
        print_text(pokemon.name, SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT - 120)
        screen.blit(lives_img_arr[lives], (SCREEN_WIDTH / 2 -100, 10))

        element_counter = 0
        for element in pokemon.types:
            print_text(element, 0, 40 * element_counter)
            element_counter += 1

        end_menu = True

    print_text(blank_pokemon, SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT - 80)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

f.close()

pygame.quit()