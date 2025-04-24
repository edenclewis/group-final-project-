# Final Project: Crossword Game
## repushed code because I forgot to add a comment to the code that I pushed
# Import Modules
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 560
SCREEN_HEIGHT = 560
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
tile_size = 80
pygame.display.set_caption("Crossword Game")


## making grided matrix to hold the crossword 
ROWS = SCREEN_HEIGHT // tile_size
COLS = SCREEN_WIDTH // tile_size
## initailizing grid with zeros 
matrix_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

def draw_grid(tile_size):
    ## fill screen 
    SCREEN.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size)
            if matrix_grid[row][col] == 1:
                pygame.draw.rect(SCREEN, BLACK, rect)
            else:
                pygame.draw.rect(SCREEN, WHITE, rect)
                pygame.draw.rect(SCREEN, BLACK, rect, 1)
    matrix_grid[0][0] = 1
    matrix_grid[0][1] = 1
    matrix_grid[0][5] = 1
    matrix_grid[0][6] = 1
    matrix_grid[1][0] = 1
    matrix_grid[5][0] = 1
    matrix_grid[6][0] = 1
    matrix_grid[6][1] = 1
    matrix_grid[6][5] = 1
    matrix_grid[6][6] = 1
    matrix_grid[5][6] = 1
    matrix_grid[1][6] = 1
    matrix_grid[3][3] = 1

run = True
while run:
    draw_grid(tile_size)
    pygame.display.update()
pygame.quit()