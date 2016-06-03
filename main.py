import pygame
from pygame.locals import*

# 1.0 - Display & screen variables
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height),pygame.HWSURFACE)
background = pygame.Surface(gameDisplay.get_size())
background.convert()

# 1.1 Colors Declaration
white = (255,255,255)
black = (0,0,0)
red = (223,0,0)
pink = (189,15,224)
orange = (255,137,0)
amber = (247,218,0)
blue = (77,215,250,0)
dark_blue = (182, 239, 252)
green = (0, 216, 29)

#  1.2 - Backgrounds & Game Screens
intro_screen = pygame.image.load('assets/images/screens/intro_screen.jpg')
menu_screen = pygame.image.load('assets/images/screens/menu_screen.png')
how_to_screen = pygame.image.load('assets/images/screens/how_to_play.png')
gaming_screen = pygame.image.load('assets/images/screens/gaming_screen.png')
gender_select = pygame.image.load('assets/images/screens/gender_select.png')
character_maleimg = pygame.image.load('assets/images/screens/character_male.png')
character_femaleimg = pygame.image.load('assets/images/screens/character_female.png')
highscore_screen = pygame.image.load('assets/images/screens/highscore.png')
dashboard = pygame.image.load('assets/images/screens/dashboard.png')
name_screen = pygame.image.load('assets/images/screens/name_select.png')
settings_screen = pygame.image.load('assets/images/screens/settings.png')
gameover_screen = pygame.image.load('assets/images/screens/Game_screen.png')
paused_screen = pygame.image.load('assets/images/screens/Paused_screen.png')

class DisplayText:
    def __init__(self,text,font):
        self.text = text
        self.font = font
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def buttons(self,x,y,width,height,active,inactive,text_size, action=None):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse_pos[0] > x and y + height > mouse_pos[1] > y:
            pygame.draw.rect(gameDisplay, active,(x,y,width,height))

            if click[0] == 1 and action is not None:

                action()
        else:
            pygame.draw.rect(gameDisplay, inactive, (x,y,width,height))

        buttonfont = pygame.font.Font('fonts/Montserrat-Hairline.otf',text_size)
        textSurf, textRect = texts(self.text, buttonfont)
        textRect.center = ( (x+(width/2)) , (y +(height/2)) )
        gameDisplay.blit(textSurf, textRect)
    def show(self,x,y):
        gameDisplay.blit(self.text,(self.x,self.y))

class DisplayScreens:
    def __init__(self,image,x,y):
        self.image = image
        self.x = x
        self.y = y
    def fade(self,time):
        self.time = time
        fading = True
        if fading:
            for i in range(255):
                self.image.set_alpha(i)
                gameDisplay.blit(self.image,(0,0))
                pygame.display.flip()
                pygame.time.delay(time)
            for i in range(255):
                background.fill(black)
                background.set_alpha(i)
                gameDisplay.blit(background,(0,0))
                pygame.display.flip()
                pygame.time.delay(time)
    def show(self):
        gameDisplay.blit(self.image,(0,0))

class Game:
    def __init__(self):
        self.running = True
        self.display_surf = None
        self.size = gameDisplay
    def on_init(self):
        pygame.init()
        self._display_surf = gameDisplay, pygame.display.set_caption('Asteroid Evader')
        self._running = True
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_cleanup(self):
        pygame.quit()
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        while (self.running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

game_intro = DisplayScreens(intro_screen,0,0)

game_intro.fade(5)

if __name__ == "__main__":
    theGame = Game()
    theGame.on_execute()