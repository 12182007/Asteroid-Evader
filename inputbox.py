import pygame,pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *


def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font('fonts/Montserrat-Light.otf',16)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 171,
                    (screen.get_height() / 2) - 52,
                    349,52), 0)

  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (0,0,0)),
                ((screen.get_width() / 2) - 140, (screen.get_height() / 2) - 37))
  pygame.display.update()


def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question + " " + "".join(current_string))
  name = None
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      return ("").join(current_string)
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))

    display_box(screen, question + "".join(current_string))
    name = ("").join(current_string)

  return name[0].upper() + name[1:]

def main():
  screen = pygame.display.set_mode((320,240))
  ask(screen, "Name") + " was entered"
if __name__ == '__main__': main()
