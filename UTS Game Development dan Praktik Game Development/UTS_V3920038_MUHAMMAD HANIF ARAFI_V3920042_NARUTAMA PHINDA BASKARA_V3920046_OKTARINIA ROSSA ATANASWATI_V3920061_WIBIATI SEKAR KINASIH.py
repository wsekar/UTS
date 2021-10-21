import pygame #Mengimport Modul Pygame
import sys #Mengimport Modul Sys
pygame.init() #menginisialisasi semua modul yang diperlukan untuk PyGame

WINDOW_WIDTH = 1100 #lebar window
WINDOW_HEIGHT = 650 #tinggi window
FPS = 20 #frame per second bernilai  20
white = (255, 255, 255) #warna putih
black = (0, 0, 0) #warna hitam
gray = (50, 50, 50) #warna abu-abu
red = (255, 0, 0) #warna merah
green = (0, 255, 0) #warna hijau
blue = (0, 0, 255) #warna biru
yellow = (255, 255, 0) #warna kuning
ADD_NEW_FLAME_RATE = 25 #warna hitam
bg = pygame.image.load('Background.png') #meload gambar background.png
bricks_img = pygame.image.load('bricks.png') #meload gambar bricks.png untuk bagian atas
bricks_img_rect = bricks_img.get_rect()
bricks_img_rect.left = 0
fire_img = pygame.image.load('fire_bricks.png')#meload gambar fire_bricks.png untuk bagian bawah
fire_img_rect = fire_img.get_rect()
fire_img_rect.left = 0
CLOCK = pygame.time.Clock() #untuk dapat membaca waktu
font = pygame.font.SysFont('forte', 20) #memberikan jenis font firte dengan ukuran 20

canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #menset lebar dan tinggi window

pygame.display.set_caption('Satria Hero') #caption program pada window game
clock = pygame.time.Clock()#untuk dapat membaca waktu
FPS = 30 #frame per second bernilai 30
font_external = "Retro.ttf" #font untuk menu

#mengatur top score
class Topscore:
    def __init__(self):
        self.high_score = 0

    def top_score(self, score):
        if score > self.high_score:
            self.high_score = score
        return self.high_score


topscore = Topscore()

#mengatur alien sekaligus sebagai AI(Artificial Intelegence)
class Alien:
    alien_velocity = 10

    def __init__(self):
        self.alien_img = pygame.image.load('baspalbot.png') #meload gambar untuk alien
        self.alien_img_rect = self.alien_img.get_rect()
        self.alien_img_rect.width -= 10
        self.alien_img_rect.height -= 10
        self.alien_img_rect.top = WINDOW_HEIGHT/2
        self.alien_img_rect.right = WINDOW_WIDTH
        self.up = True
        self.down = False

    def update(self):
        canvas.blit(self.alien_img, self.alien_img_rect)
        if self.alien_img_rect.top <= bricks_img_rect.bottom:
            self.up = False
            self.down = True
        elif self.alien_img_rect.bottom >= fire_img_rect.top:
            self.up = True
            self.down = False

        if self.up:
            self.alien_img_rect.top -= self.alien_velocity
        elif self.down:
            self.alien_img_rect.top += self.alien_velocity

#mengatur pergerakan dari bola api
class Flames:
    flames_velocity = 20

    def __init__(self):
        self.flames = pygame.image.load('fireball.png') #meload gambar untuk bola api
        self.flames_img = pygame.transform.scale(self.flames, (40, 40))
        self.flames_img_rect = self.flames_img.get_rect()
        self.flames_img_rect.right = alien.alien_img_rect.left
        self.flames_img_rect.top = alien.alien_img_rect.top + 30

    def update(self):
        canvas.blit(self.flames_img, self.flames_img_rect)

        if self.flames_img_rect.left > 0:
            self.flames_img_rect.left -= self.flames_velocity

#mengatur pemain utama / satria hero 
class Satria_hero:
    velocity = 10

    def __init__(self):
        self.satria_hero_img = pygame.image.load('hero.png') #meload gambar untuk si pemain utama / satria hero
        self.satria_hero_img = pygame.transform.scale(
            self.satria_hero_img, (80, 80))
        self.satria_hero_img_rect = self.satria_hero_img.get_rect()
        self.satria_hero_img_rect.left = 20
        self.satria_hero_img_rect.top = WINDOW_HEIGHT/2 - 100
        self.down = True
        self.up = False

    def update(self):
        canvas.blit(self.satria_hero_img, self.satria_hero_img_rect)
        if self.satria_hero_img_rect.top <= bricks_img_rect.bottom:
            game_over()
            if SCORE > self.satria_hero_score:
                self.satria_hero_score = SCORE
        if self.satria_hero_img_rect.bottom >= fire_img_rect.top:
            game_over()
            if SCORE > self.satria_hero_score:
                self.satria_hero_score = SCORE
        if self.up:
            self.satria_hero_img_rect.top -= 10
        if self.down:
            self.satria_hero_img_rect.bottom += 10

#ketika game over
def game_over():
    pygame.mixer.music.stop()
    music = pygame.mixer.Sound('satria_hero_dies.wav') #meload suara ketika game over
    music.play()
    topscore.top_score(SCORE)
    game_over_img = pygame.image.load('GameOper.png') #meload tampilan gambar ketika game over
    game_over_img = pygame.transform.scale(game_over_img, (500, 300))
    game_over_img_rect = game_over_img.get_rect()
    game_over_img_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    canvas.blit(game_over_img, game_over_img_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                music.stop()
                game_loop()
        pygame.display.update()

#memberikan text format untuk menu awal
def text_format(message, textFont, textSize, textColor):
    pygame.init()
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    
    return newText

#main menu game
def start_game():
    menu = True
    selected = "start"
    game_start_img = pygame.image.load('start.png')
    game_start_img = pygame.transform.scale(game_start_img, (1100, 700))
    game_start_img_rect = game_start_img.get_rect()
    game_start_img_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    canvas.blit(game_start_img, game_start_img_rect)
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "start"
                elif event.key == pygame.K_DOWN:
                    selected = "quit"
                if event.key == pygame.K_RETURN: 
                    if selected == "start": #ketika ditekan start maka akan langsung diarahkan ke fungsi game_loop dan game langsung dimulai
                        game_loop()
                    if selected == "quit": #ketika dietekan quit maka game akan langsung keluar dari game
                        pygame.quit()

        # Main Menu UI
        if selected == "start":
            text_start = text_format("START", font_external, 75, blue)
        else:
            text_start = text_format("START", font_external, 75, black)
        if selected == "quit":
            text_quit = text_format("QUIT",font_external, 75, blue)
        else:
            text_quit = text_format("QUIT",font_external, 75, black)

        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        canvas.blit(text_start, (WINDOW_WIDTH/2 - (start_rect[2]/2), 300))
        canvas.blit(text_quit, (WINDOW_WIDTH/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)

#mengatur level pemain yang dimulai dari level 1-4 dengan sebuah kenaikan 10 disetiap level 
#dan ketika score lebih dari 30 artinya akan masuk level 4
def check_level(SCORE):
    global LEVEL
    if SCORE in range(0, 10):
        bricks_img_rect.bottom = 50
        fire_img_rect.top = WINDOW_HEIGHT - 50
        LEVEL = 1
    elif SCORE in range(10, 20):
        bricks_img_rect.bottom = 100
        fire_img_rect.top = WINDOW_HEIGHT - 100
        LEVEL = 2
    elif SCORE in range(20, 30):
        bricks_img_rect.bottom = 150
        fire_img_rect.top = WINDOW_HEIGHT - 150
        LEVEL = 3
    elif SCORE > 30:
        bricks_img_rect.bottom = 200
        fire_img_rect.top = WINDOW_HEIGHT - 200
        LEVEL = 4

#aturan arena dalam bermain game, sebagai bagian utama dari game ini
def game_loop():
    while True:
        global alien
        alien = Alien() #menginisialisasi def fungsi Alien
        flames = Flames() #menginisialisasi def fungsi Flames
        satria_hero = Satria_hero() #menginisialisasi def fungsi Satria_hero
        add_new_flame_counter = 0
        global SCORE
        SCORE = 0
        global HIGH_SCORE
        flames_list = []
        pygame.mixer.music.load('bgmusic.wav') #menambahkan background musik ketika bermain
        pygame.mixer.music.play(-1, 0.0)
        while True:
            canvas.fill(black)
            canvas.blit(bg, (0, 0))
            check_level(SCORE)
            alien.update()
            add_new_flame_counter += 1

            if add_new_flame_counter == ADD_NEW_FLAME_RATE:
                add_new_flame_counter = 0
                new_flame = Flames()
                flames_list.append(new_flame)
            for f in flames_list:
                if f.flames_img_rect.left <= 0:
                    flames_list.remove(f)
                    SCORE += 1
                f.update()
            #mengatur pergerakan satria hero / pemain utama
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        satria_hero.up = True
                        satria_hero.down = False
                    elif event.key == pygame.K_DOWN:
                        satria_hero.down = True
                        satria_hero.up = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        satria_hero.up = False
                        satria_hero.down = True
                    elif event.key == pygame.K_DOWN:
                        satria_hero.down = True
                        satria_hero.up = False
            
            #Mencetak UI untuk Score,Level,Top Score
            score_font = font.render('Score:'+str(SCORE), True, white)
            score_font_rect = score_font.get_rect()
            score_font_rect.center = (
                200, bricks_img_rect.bottom + score_font_rect.height/2)
            canvas.blit(score_font, score_font_rect)

            level_font = font.render('Level:'+str(LEVEL), True, white)
            level_font_rect = level_font.get_rect()
            level_font_rect.center = (
                500, bricks_img_rect.bottom + score_font_rect.height/2)
            canvas.blit(level_font, level_font_rect)

            top_score_font = font.render(
                'Top Score:'+str(topscore.high_score), True, white)
            top_score_font_rect = top_score_font.get_rect()
            top_score_font_rect.center = (
                800, bricks_img_rect.bottom + score_font_rect.height/2)
            canvas.blit(top_score_font, top_score_font_rect)

            canvas.blit(bricks_img, bricks_img_rect)
            canvas.blit(fire_img, fire_img_rect)
            satria_hero.update()
            for f in flames_list:
                if f.flames_img_rect.colliderect(satria_hero.satria_hero_img_rect):
                    game_over()
                    if SCORE > satria_hero.satria_hero_score:
                        satria_hero.satria_hero_score = SCORE
            pygame.display.update()
            CLOCK.tick(FPS)


start_game()
