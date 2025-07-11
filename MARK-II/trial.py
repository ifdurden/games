import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Alien invasion")

    while True : 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
run_game()