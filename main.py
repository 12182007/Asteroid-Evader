import pygame, os
from pygame.locals import *

#Constants
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
FRAMES_PER_SECOND = 60

#Colors
white = (255,255,255)
black = (0,0,0)
blue = (77,215,250,0)

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = DISPLAY_WIDTH, DISPLAY_HEIGHT

    def on_init(self):
        pygame.init()
        self._gameDisplay = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Asteroid Evader')
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
    theApp = App()
    theApp.on_execute()