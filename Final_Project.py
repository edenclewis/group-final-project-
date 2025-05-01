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
LIGHT_BLUE = (173, 216, 230)
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
font = pygame.font.Font(None, 30)
active = True ## CHANGE SOON
text = ''
numbers = [x for x in range(1, 12)] ## list of numbers to be displayed in the blank box

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
            elif matrix_grid[row][col] == 3:
                color = LIGHT_BLUE
            pygame.draw.rect(SCREEN, color, rect)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)
            
## draw blank box 
blank_box = pygame.Rect(GRID_COLS * tile_size, 0, BLANK_BOX_WIDTH, SCREEN_HEIGHT)
pygame.draw.rect(SCREEN, GREY, blank_box)
## drawing parts of the crossword --> try to make this part of the code more efficent 
def clear_grid():
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            if matrix_grid[row][col] == 2 or matrix_grid[row][col] == 3:
                matrix_grid[row][col] = 0 ## reset the grid to white
clickCount = 0
first_click = None
second_click = None
direction = "horizontal"
# Add event handling to the main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos ## get the mouse position
            ## converts that position to grid coordinates
            col = mouse_x // tile_size
            row = mouse_y // tile_size 
            ## check if mouse position within grid 
            if 0 <= row < GRID_ROWS and 0 <= col < GRID_COLS and matrix_grid[row][col] != 1: ## if the mouse position is in the grid and not black
                if clickCount == 0:      ## first click  
                    clear_grid()
                    first_click = (row,col)  ## store the first click index 
                    matrix_grid[row][col] = 2 ## box clicked on turns yellow 
                    direction = "horizontal" ## default direction 
                    next_col = col + 1 ## check to the right of the box
                    prev_col = col - 1 ## check to the left of the box

                    while next_col < GRID_COLS and matrix_grid[row][next_col] != 1: ## if the right of the box is in the matrix and not black
                        matrix_grid[row][next_col] = 3 ## change color of that box to light blue 
                        next_col += 1 ## move to the box two away from the one you clicked on 
                        clickCount = 1 ## set the click count to 1 

                    while prev_col < GRID_COLS and matrix_grid[row][prev_col] != 1: ## if the left of the box is in the matrix and not black
                        matrix_grid[row][prev_col] = 3 ## change color of that box to light blue 
                        prev_col -= 1 ## move to the box two away from the one you clicked on 
                        clickCount = 1 ## set the click count to 1

                elif clickCount == 1:  ## this would technically be the second click 
                    clear_grid()
                    second_click = (row,col) ## store the second click index
                    if second_click == first_click:  ## if the second click is the same as the first click 
                        direction = "vertical" # change the direction to vertical 
                        matrix_grid[row][col] = 2
                        next_row, j = row + 1, col # now check the box below the first click 

                        while next_row < GRID_ROWS and matrix_grid[next_row][j] != 1: ## if the box below the first click is in the matrix and not black 
                            matrix_grid[next_row][j] = 3 ## change the color of that box to light blue 
                            next_row += 1 ## move to the box two below the one that you clicked 
                        
                        prev_row, j = row - 1, col # now check the box above the first click

                        while prev_row < GRID_ROWS and matrix_grid[prev_row][j] != 1: ## if the box above the first click is in the matrix and not black 
                            matrix_grid[prev_row][j] = 3 ## change the color of that box to light blue 
                            prev_row -= 1 ## move to the box two above the one that you clicked 

                    else: ## if the first and second click aren't the same
                        clear_grid()
                        row,col = second_click  # store index of the second click 
                        matrix_grid[row][col] = 2 ## change the color of the box to yellow 
                        next_col = col + 1 ## check the box to the right of the clicked box
                        prev_col = col - 1 ## check to the left of the box

                        while next_col < GRID_COLS and matrix_grid[row][next_col] != 1:
                            matrix_grid[row][next_col] = 3 # change the color of the box to the right of the clicked box to light blue 
                            next_col += 1

                        while prev_col < GRID_COLS and matrix_grid[row][prev_col] != 1:
                            matrix_grid[row][prev_col] = 3 # change the color of the box to the left of the clicked box to light blue 
                            prev_col -= 1

                        direction = "horizontal" ## change direction to default 
                        
                    first_click = second_click ## make the second click the first click 
                    clickCount = 0 # reset the click counter to 0
        if event.type == KEYDOWN:
            if active:
                if event.key == K_a:
                    text += 'A'
                    print(text)
                elif event.key == K_b:
                    text += 'B'
                    print(text)
                elif event.key == K_BACKSPACE:
                    text = text[:-1]
                

    draw_grid(tile_size)

    numSurfaceArray = []
    coordinateArray = [[405,5],
                       [5,85],
                       [85,85],
                       [245,85],
                       [485,85],
                       [405,165],
                       [5,245],
                       [325,245],
                       [245,325],
                       [85,485],
                       [485,485]] ## x,y coordinates of the numbers in the blank box
    
    ## CREATE FUNCTION CALLED DRAW_NUMBERS AND CALL IT HERE
    for i in numbers:
        ## create a surface for each number in the numbers list, render the number on the surface, append the surface to the numSurfaceArray
        numSurfaceArray.append(font.render(str(i), True, BLACK))

        ## looks like this: [font.render(numbers[0], True, BLACK), font.render(numbers[1], True, BLACK), font.render(numbers[2], True, BLACK), ...]

    for i, j in enumerate(range(len(numbers))):
        SCREEN.blit(numSurfaceArray[i], (coordinateArray[j][0], coordinateArray[j][1]))


    pygame.display.update()
    
pygame.quit()
