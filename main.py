import pygame, os
from pygame.locals import *

#Constants
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
FRAMES_PER_SECOND = 60
GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)


#Colors
white = (255,255,255)
black = (0,0,0)
blue = (77,215,250,0)

class Game:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = DISPLAY_WIDTH, DISPLAY_HEIGHT
    def on_init(self):
        pygame.init()
        self._display_surf = GAME_DISPLAY
        pygame.display.set_caption('Asteroid Evader')

        def texts(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()

        def buttons(text,x,y,width,height,inactive,active,text_size, action=None):
            mouse_pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
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