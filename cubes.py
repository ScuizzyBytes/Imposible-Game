import pygame

CELL = 25
GRID = 20

def create_cubes(screen):
    for row in range(GRID):
        for col in range(GRID):

            x = col * CELL
            y = row * CELL

            pygame.draw.rect(screen, (0, 0, 0), (x + 1, y + 1, CELL - 2, CELL - 2))