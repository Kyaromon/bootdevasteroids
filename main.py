import pygame
from logger import log_state
from constants import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")

    running = True
    while running:
	log_state()
	for event in pygame.event.get():
	    if event.type == pygame.QUIT
		running = False
	screen.fill("black")
	pygame.display.flip()

if __name__ == "__main__":
    main()
