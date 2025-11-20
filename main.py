import pygame
import sys
from logger import log_state, log_event
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    #loop start
    running = True
    while running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        updatable.update(dt)
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    if asteroid.radius <= ASTEROID_MIN_RADIUS:
                        score += 100
                    else:
                        score += 50
                    asteroid.split()
                    shot.kill()
                    log_event("asteroid_shot")
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                pygame.quit()
                sys.exit()
        for obj in drawable:
            obj.draw(screen)
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    #loop end
if __name__ == "__main__":
    main()
