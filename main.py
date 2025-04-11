# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    #Screen (filled black)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #FPS limiter
    clock = pygame.time.Clock()
    dt = 0

    #Groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    #Instantiate PLAYER
    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # -- GAME LOOP --

    # Event handler
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        # Redraw player
        updatables.update(dt)
        for drawable in drawables:
            drawable.draw(screen)

        #Refreshes the 'Screen' object
        pygame.display.flip()
        # Each frame, tick and save the milliseconds passed in 'dt'
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
