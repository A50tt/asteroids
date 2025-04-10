# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #Screen (filled black)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(color=(0, 0, 0))
    #FPS limiter
    clock = pygame.time.Clock()
    dt = 0
    # Game loop
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                return
        #Each frame, tick and save the milliseconds passed in 'dt'
        dt = clock.tick(60)
        print(f"dt --> {dt}")


if __name__ == "__main__":
    main()
