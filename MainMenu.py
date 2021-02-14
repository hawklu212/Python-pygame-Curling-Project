import pygame
from pygame.locals import*
import os
import main
import pregame

# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))


# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText

white = pygame.image.load("Pictures/white1.png")
brown = pygame.image.load("Pictures/brown1.png")
white = pygame.transform.scale(white, (350, 350))
brown = pygame.transform.scale(brown, (350, 350))

# Colors
whiteC = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Game Fonts
font = "NOTMK___.ttf"

# Game Framerate
clock = pygame.time.Clock()
FPS = 10
bg1 = pygame.image.load("Pictures/Mock_Sweeper_1.png")
bg2 = pygame.image.load("Pictures/Mock_Sweeper_2.png")
white1 = pygame.image.load("Pictures/white1.png")
white1 = pygame.transform.scale(white1, (300, 300))
white2 = pygame.image.load("Pictures/white2.png")
white2 = pygame.transform.scale(white2, (300, 300))

def button(text, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("NOTMK___.ttf",30)
    textSurf, textRect = text_objects(text, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# Main Menu
def main_menu():
    mouse = pygame.mouse.get_pos()
    menu = True
    image = 1
    while menu:
        image *= -1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Main Menu UI
        screen.fill(gray)

        title = text_format("BCS Cats Curling", font, 90, yellow)
        title_rect = title.get_rect()

        # Main Menu Text
        if image == 1:
            screen.blit(bg1, (0, -25))
            screen.blit(white1, (600, 300))
        else:
            screen.blit(bg2, (0, -25))
            screen.blit(white2, (600, 300))

        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
        button("Start", (screen_width / 2), 300, 100, 50, green, green, pregame)
        button("How to Play", (screen_width / 2) - 8, 400, 120, 50, yellow, yellow, howtoplay)
        button("Quit", (screen_width / 2), 500, 100, 50, red, red, pygame.quit)

        pygame.display.update()
        clock.tick(FPS)

#How to Play screen
def howtoplay():
    howto = True
    font = pygame.font.Font("NOTMK___.ttf", 30)
    text = font.render("Start the game, click to scrub and enjoy the show", True, black, whiteC)
    textRect = text.get_rect()
    textRect.center = (screen_width // 2, screen_height // 2)
    screen.fill(gray)
    screen.blit(text, textRect)

    button("Back", 50, 50, 100, 50, whiteC, whiteC, main_menu)

    while howto:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                pygame.quit()
                quit()

            button("Back", 50, 50, 100, 50, whiteC, whiteC, main_menu)
            pygame.display.update()
            clock.tick(FPS)

def draw_rect_black(x, y):
    rect_upper = pygame.Rect(x-10, y-10, 370, 10)
    rect_left = pygame.Rect(x-10, y, 10, 360)
    rect_lower = pygame.Rect(x, y+350, 360, 10)
    rect_right = pygame.Rect(x+350, y, 10, 350)
    pygame.draw.rect(screen, black, rect_upper)
    pygame.draw.rect(screen, black, rect_left)
    pygame.draw.rect(screen, black, rect_lower)
    pygame.draw.rect(screen, black, rect_right)

def draw_rect_white(x, y):
    rect_upper = pygame.Rect(x-10, y-10, 370, 10)
    rect_left = pygame.Rect(x-10, y, 10, 360)
    rect_lower = pygame.Rect(x, y+350, 360, 10)
    rect_right = pygame.Rect(x+350, y, 10, 350)
    pygame.draw.rect(screen, whiteC, rect_upper)
    pygame.draw.rect(screen, whiteC, rect_left)
    pygame.draw.rect(screen, whiteC, rect_lower)
    pygame.draw.rect(screen, whiteC, rect_right)

def pregame():
    run = True
    team = 0
    xb = 30
    xw = 510
    y = 150

    while run:

        screen.fill(gray)
        title = text_format("Choose Your Team", font, 80, yellow)
        title_rect = title.get_rect()

        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 30))

        screen.blit(brown, (30, 150))
        screen.blit(white, (510, 150))

        pointer = pygame.mouse.get_pos()
        brownpointer = brown.get_rect(x = 30, y=150)
        whitepointer = white.get_rect(x=510, y=150)

        if brownpointer.collidepoint(pointer):
            draw_rect_white(30, 150)
            pygame.display.update()
        elif whitepointer.collidepoint(pointer):
            draw_rect_black(510, 150)
            pygame.display.update()

        if team == 1:
            button("Grizzlies Start", (screen_width / 2 - 100), 600, 200, 50, whiteC, whiteC, main.main)
        if team == 2:
            button("Polars Start", (screen_width / 2 - 100), 600, 200, 50, whiteC, whiteC, main.main)

        for event in pygame.event.get():
            button("Back", 50, 550, 100, 50, whiteC, whiteC, main_menu)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if brownpointer.collidepoint(pos):
                    team = 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if whitepointer.collidepoint(pos):
                    team = 2

        pygame.display.update()
        clock.tick(FPS)

#Initialize the Game
main_menu()
pygame.quit()
quit()