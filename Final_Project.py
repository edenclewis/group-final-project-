# Final Project: Crossword Game
# Import Modules
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200,200,200)
YELLOW = (225, 225, 0)
#set up the screen 
SCREEN_WIDTH = 560
SCREEN_HEIGHT = 560
GRID_COLS = 12  # 
GRID_ROWS = 8  # 7 rows of tiles
BLANK_BOX_WIDTH = 500
tile_size = 80
SCREEN_WIDTH = (GRID_COLS * tile_size) + BLANK_BOX_WIDTH
SCREEN_HEIGHT = GRID_ROWS * tile_size
# create the screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#creating the matrix with white (0) and black (1) squares
matrix_grid =      [[1,1,1,1,1,0,1,1,1,1,1,1], 
                   [0,0,0,0,0,0,0,1,1,1,1,1], 
                   [1,0,1,0,1,0,0,0,0,0,1,1],
                   [0,0,0,0,0,0,0,1,1,1,1,1], 
                   [1,1,1,0,0,0,0,0,0,1,1,1], 
                   [1,1,1,0,1,0,0,1,1,1,1,1], 
                   [1,0,0,0,0,1,0,0,0,0,0,0],
                   [1,1,1,1,1,1,0,1,1,1,1,1]]

def draw_grid(tile_size):
    ## fill screen 
    SCREEN.fill(WHITE)
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            rect = pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size)
            if matrix_grid[row][col] == 0:
                color = WHITE
            elif matrix_grid[row][col] == 1:
                color = BLACK
            elif matrix_grid[row][col] == 2:
                color = YELLOW
            pygame.draw.rect(SCREEN, color, rect)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)
            

## draw blank box 
blank_box = pygame.Rect(GRID_COLS * tile_size,0, BLANK_BOX_WIDTH, SCREEN_HEIGHT)
pygame.draw.rect(SCREEN, GREY, blank_box)
## drawing parts of the crossword --> try to make this part of the code more efficent 

clickCount = 1
# Add event handling to the main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == MOUSEBUTTONDOWN:
            clickCount += 1
            print(clickCount)
            mouse_x, mouse_y = event.pos ## get the mouse position
            ## converts that position to grid coordinates
            col = mouse_x // tile_size
            row = mouse_y // tile_size
            ## check if mouse position within grid 
            if 0 <= row < GRID_ROWS and 0 <= col < GRID_COLS:
                ## if its within the grid, turn the tile on or off
                if matrix_grid[row][col] == 0:
                     ##set color of box equal to yellow color 
                    matrix_grid[row][col] = 2
                    pygame.draw.rect(SCREEN, YELLOW, (col * tile_size, row * tile_size, tile_size, tile_size))

                elif matrix_grid[row][col] == 2: 
                    matrix_grid[row][col] = 0

    draw_grid(tile_size)
    pygame.display.update()
pygame.quit()