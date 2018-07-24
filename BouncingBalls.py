import sys
import pygame
from pygame.locals import *
pygame.init()
screen_info = pygame.display.Info()

# set the width and height to the size of the screen
size = (width, height) = (screen_info.current_w - 20,screen_info.current_h - 20)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (26, 255, 255)

def main():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        screen.fill(color)
        pygame.display.flip()

if __name__ == '__main__':
    main()