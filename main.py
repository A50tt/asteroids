# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from  asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    #Screen (filled black)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #FPS limiter
    clock = pygame.time.Clock()
    dt = 0

    #Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #Instantiate static containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable

    # Instantiate objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    # -- -- -- -- GAME LOOP -- -- -- --

    # Event handler
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        # Redraw player
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)

        #Refreshes the 'Screen' object
        pygame.display.flip()
        # Each frame, tick and save the milliseconds passed in 'dt'
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
