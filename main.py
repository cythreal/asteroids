import sys
import pygame 
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    FPS = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    dt = 0
    
    while screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)
        for model in drawable:
            model.draw(screen)
        for asteroid in asteroids:
            if player.collision(asteroid) == True:
                print("Game Over!"); sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid) == True:
                    shot.kill()
                    asteroid.split()
        pygame.display.flip()
        
        dt = FPS.tick(60) / 1000 #pause game loop until 1/60 of second passes,
        #AND return value in milliseconds to dt

if __name__ == "__main__":
    main()