import pygame
from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE
)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0  # delta time

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            else:
                pygame.Surface.fill(screen, (0, 0, 0))
                pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == '__main__':
    main()