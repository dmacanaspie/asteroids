import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE,
)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0  # delta time

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # add containers to class prior to creating variables
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    asteroidField = AsteroidField()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            else:
                pygame.Surface.fill(screen, (0, 0, 0))
                updatable.update(dt)
                for item in drawable:
                    item.draw(screen=screen)
                pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == '__main__':
    main()