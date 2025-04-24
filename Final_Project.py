# Final Project: Crossword Game
## repushed code because I forgot to add a comment to the code that I pushed
# Import Modules
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200,200,200)
#set up the screen 
SCREEN_WIDTH = 560
SCREEN_HEIGHT = 560
GRID_COLS = 7  # 
GRID_ROWS = 7  # 7 rows of tiles
BLANK_BOX_WIDTH = 500
tile_size = 80
SCREEN_WIDTH = (GRID_COLS * tile_size) + BLANK_BOX_WIDTH
SCREEN_HEIGHT = GRID_ROWS * tile_size
# create the screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
## initailizing grid with zeros 
matrix_grid = [[0 for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

def draw_grid(tile_size):
    ## fill screen 
    SCREEN.fill(WHITE)
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            rect = pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size)
            if matrix_grid[row][col] == 1:
                pygame.draw.rect(SCREEN, BLACK, rect)
            else:
                pygame.draw.rect(SCREEN, WHITE, rect)
                pygame.draw.rect(SCREEN, BLACK, rect, 1)

## draw blank box 
blank_box = pygame.Rect(GRID_COLS * tile_size,0, BLANK_BOX_WIDTH, SCREEN_HEIGHT)
pygame.draw.rect(SCREEN, GREY, blank_box)
## drawing parts of the crossword 
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