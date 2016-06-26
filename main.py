import pygame, os.path, sys, random
from pygame.locals import *

#Constants
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
FRAMES_PER_SECOND = 60
GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)

# Backgrounds & Game Screen
intro_screen = pygame.image.load('screens/Intro Screen.jpg')
menu_screen = pygame.image.load('screens/menu_screen.png')
how_to_screen = pygame.image.load('screens/how_to_play.png')
gaming_screen = pygame.image.load('screens/gaming_screen.png')
gender_select = pygame.image.load('screens/gender_select.png')
character_maleimg = pygame.image.load('screens/character_male.png')
character_femaleimg = pygame.image.load('screens/character_female.png')
highscore_screen = pygame.image.load('screens/highscore.png')
dashboard = pygame.image.load('screens/dashboard.png')
name_screen = pygame.image.load('screens/name_select.png')
settings_screen = pygame.image.load('screens/settings.png')
gameover_screen = pygame.image.load('screens/Game_screen.png')
paused_screen = pygame.image.load('screens/Paused_screen.png')

#Colors
white = (255,255,255)
black = (0,0,0)
blue = (77,215,250,0)

base_dir = os.path.split(os.path.abspath(__file__))[0]  # game's diretory

class Game:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = DISPLAY_WIDTH, DISPLAY_HEIGHT

    def on_init(self):
        pygame.init()
        self._display_surf = GAME_DISPLAY
        pygame.display.set_caption('Asteroid Evader')

        # defining utility functions & components.

        #allows for the displaying text to screen
        def texts(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()

        #creates clickable button
        def buttons(text,x,y,width,height,inactive,active,text_size, action=None):
            mouse_pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            #checks if mouse is hovered above button
            if x + width > mouse_pos[0] > x and y + height > mouse_pos[1] > y:
                pygame.draw.rect(GAME_DISPLAY, active,(x,y,width,height))

                if click[0] == 1 and action is not None:

                    action()
            else:
                pygame.draw.rect(GAME_DISPLAY, inactive, (x,y,width,height))

            buttonText = pygame.font.Font('fonts/Montserrat-Hairline.otf',text_size)
            textSurf, textRect = texts(text, buttonText)
            textRect.center = ( (x+(width/2)) , (y +(height/2)) )
            GAME_DISPLAY.blit(textSurf, textRect)

        #function for loading image
        def load_image(image, transparent):
            image = os.path.join(base_dir, 'data',image)
            try:
                display = pygame.image.load(image)
            except pygame.error:
                raise SystemExit('Could not load image "%s" %s' % (image, pygame.get_error()))
            if transparent:
                corner = display.get_at((0,0))
                display.set_colorkey(corner,RLEACCEL)
            return display.convert()

        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_cleanup(self):
        pygame.quit()
    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = Game()
    theApp.on_execute()