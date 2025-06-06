import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main ():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for thing in updateable:
            thing.update(dt)

        for thing in asteroids:
            if thing.isColliding(player):
                print("Game Over!")
                exit()

        for a in asteroids:
            for b in shots:
                if b.isColliding(a):
                    a.split()
                    b.kill()


        screen.fill(000)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60)/1000)

if __name__ == "__main__":
    main()