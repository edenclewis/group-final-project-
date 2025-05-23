# Final Project: Crossword Game
# Import Modules
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()
## colors used in the game 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200,200,200)
LIGHT_GREY = (211,211,211)
YELLOW = (225, 225, 0)
LIGHT_BLUE = (173, 216, 230)
RED = (255,0,0)
GREEN = (0,128,0)

# set up the display 
GRID_COLS = 12  # 12 columns of tiles
GRID_ROWS = 9  # 9 rows of tiles
BLANK_BOX_WIDTH = 500 ## width of the blank box
TITLE_BOX_HEIGHT = 100 ## height of the blank box
tile_size = 80 ## size of each tile in the grid
SCREEN_WIDTH = (GRID_COLS * tile_size) + BLANK_BOX_WIDTH ## size of entire screen
SCREEN_HEIGHT = TITLE_BOX_HEIGHT + (GRID_ROWS * tile_size) ## height of entire screen
button_width = 200 ## width of buttons
button_height = 60 ## height of buttons
button_x = GRID_COLS * tile_size + (BLANK_BOX_WIDTH - button_width) // 2 ## x position where buttons on screen (centers buttons)
button_y = 650 ## y position for check button
button_y2 = 725 ## y position for clear button

# create the screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) ## create a screen for the grid
INTRO_SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) ## create a screen for the instructions


numbers = [x for x in range(1, 14)] ## list of numbers to be displayed in the blank box

# font setup
font = pygame.font.Font(None, 24) ## font for the crossword clues
timer_font = pygame.font.Font(None, 50) ## font for the timer
font_for_grid = pygame.font.Font(None, 50) ## font for the grid
title_font = pygame.font.Font(None, 100) ## font for the title 

# Set up the screen
char_grid = [["" for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)] ## creates a 2D empty list to store the characters typed by the user into the grid 
color_grid = [["black" for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)] ## creates a 2D empty list to store the colors of the characters typed by the user into the grid 

# CROSSWORD CLUES 
## crossword clue text
text_lines = [
    "DOWN",
    "1. Programming language developed by Mathworks",
    "3. The button you press to make a code execute",
    "4. Platform used for storing, managing, and collaborating",
    "on code",
    "5. *",
    "8. What you use when you’ve been working for 7 hours on",
    "one line of code",
    "10. Students who help Alekh with teaching responsibilities",
    "(and help us too!)",

    "",

    "ACROSS",
    "2. Sequence of instructions a computer executes to perform",
    "a task",
    "6. Ordered sequence of immutable values",
    "9. What you go into after finishing your final exam",
    "7. Download",
    "11. Smallest unit of data represented in 0s or 1s (abv)",
    "12. Collections of prewritten code (abv)",
    "13. Python library used for data analysis and manipulation"
]

# lists to hold variables and colors of boxes in the grid
char_grid = [["" for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)] ## creates a 2D empty list to store the characters typed by the user into the grid 
color_grid = [["black" for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)] ## creates a 2D empty list to store the colors of the characters typed by the user into the grid 

# crossword clues 
def crossword_clues(surface, text_list, x_start, y_start, line_spacing = 25): #function to display the crossword clues
    for ii, line in enumerate(text_list): 
        text_surface = font.render(line, False, "black") ## create a surface for the text
        surface.blit(text_surface, (x_start, TITLE_BOX_HEIGHT + y_start + ii * line_spacing)) #blit the crossword text on the screen

        
# TITLE
title_text = ["P.E.M Crossword Puzzle"]
def title(surface, title_text, x_start, y_start, line_spacing = 25): #function to display the title
    title_font.set_bold(True) ## make the title bold
    for ii, line in enumerate(title_text): ## loop through the title text 
        text_surface = title_font.render(line, False, "black") ## create a surface for the title text
        surface.blit(text_surface, (x_start, y_start + ii * line_spacing)) ## blit the title text on the screen

# creating the matrix with white (0) and black (1) squares
matrix_grid =      [[1,1,1,1,1,0,1,1,1,1,1,1], 
                   [0,0,0,0,0,0,0,1,1,1,1,1], 
                   [1,0,1,0,1,0,0,0,0,0,1,1],
                   [0,0,0,0,0,0,0,1,1,1,1,1], 
                   [1,1,1,0,0,0,0,0,0,1,1,1], 
                   [1,1,1,0,1,0,0,0,1,1,1,1], 
                   [1,0,0,0,0,1,0,0,0,0,0,0],
                   [1,1,1,1,1,1,0,1,1,1,1,1],
                   [1,1,1,1,1,1,0,1,1,1,1,1]
                   ]

# matrix to store the crossword solutions 
answer_grid = [
    ["",  "",  "",  "",  "",  "M", "",  "",  "",  "",  "",  ""],
    ["P", "R", "O", "G", "R", "A", "M", "",  "",  "",  "",  ""],
    ["",  "U", "",  "I", "",  "T", "U", "P", "L", "E", "",  ""],
    ["I", "N", "S", "T", "A", "L", "L", "",  "",  "",  "",  ""],
    ["",  "",  "",  "H", "I", "A", "T", "U", "S", "",  "",  ""],
    ["",  "",  "",  "U", "",  "B", "I", "T", "",  "",  "",  ""],
    ["",  "L", "I", "B", "S", "",  "P", "A", "N", "D", "A", "S"],
    ["",  "",  "",  "",  "",  "",  "L", "",  "",  "",  "",  ""],
    ["",  "",  "",  "",  "",  "",  "Y", "",  "",  "",  "",  ""]
]
## Draw introduction screen function 
show_intro_screen = True ## variable to show the introduction screen 
def draw_instructions():
    INTRO_SCREEN.fill(WHITE) ## fill the screen with white
    instructions = [
        "Instructions",
        "Guess each word in the crossword.",
        "Use the CHECK button to check if the words are correct once you are done with the puzzle.",
        "If the letter in the box is correct, the letter will turn GREEN, and if the letter is incorrect the letter will turn RED.",
        "Use the CLEAR button to clear the grid.",
        "Click on a box to start typing a word, and click on the same box again to change the direction of the word.",
        "Press BACKSPACE to delete a letter.",
        "Press SPACE to start the game."
    ]
    introtitle_font = pygame.font.Font(None, 64)  ### Bigger font for the title
    introtitle_font.set_bold(True)  ### Make it bold
    body_font = pygame.font.Font(None, 32)  ### Slightly larger body text
    body_font.set_bold(False) ## Normal font for the body text
    
    ## draw the title 
    title_surface = introtitle_font.render(instructions[0], True, BLACK) ## create a surface for the title 
    title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, 80)) ## center the title on the screen
    INTRO_SCREEN.blit(title_surface, title_rect) ## put the title on the screen
    
    # Draw body instructions
    y = 160   # Push body text lower
    body_spacing = 40    # Greater spacing between lines for body text 
    for i, line in enumerate(instructions[1:]): ## loop through the instruction list starting from the second line
        body_surface = body_font.render(line, True, BLACK) ## create surface for the body text 
        body_rect = body_surface.get_rect(center=(SCREEN_WIDTH // 2, y+i * body_spacing)) ## center the text on the screen
        INTRO_SCREEN.blit(body_surface, body_rect) ## put the body text on the screen 

# empty array to store puzzle numbers
numSurfaceArray = []

# array to store the coordinates of the numbers in the matrix_grid
coordinateArray = [    [405,105],    #1
                       [5,185],     #2
                       [85,185],    #3
                       [245,185],   #4
                       [485,185],   #5
                       [405,265],  #6
                       [5,345],    #7
                       [325,345],  #8
                       [245,425],  #9
                       [565,425],  #10
                       [405,505],  #11
                       [85,585],   #12
                       [485,585],  #13
                       ]   ## x,y coordinates of the numbers in the matrix_grid 

# Draw grid function
def draw_grid(tile_size):
    ## fill screen 
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            rect = pygame.Rect(col * tile_size, TITLE_BOX_HEIGHT + row * tile_size, tile_size, tile_size) ## create a rectangle for each tile in the grid
            if matrix_grid[row][col] == 0: ## if the number of the matrix is 0, fill the tile with white
                color = WHITE
            elif matrix_grid[row][col] == 1: ## if the number of the matrix is 1, fill the tile with black
                color = BLACK
            elif matrix_grid[row][col] == 2: ## if the number of the matrix is 2, fill the tile with yellow
                color = YELLOW
            elif matrix_grid[row][col] == 3: ## if the number of the matrix is 3, fill the tile with light blue
                color = LIGHT_BLUE
            pygame.draw.rect(SCREEN, color, rect) ## fill the tile with a color
            pygame.draw.rect(SCREEN, BLACK, rect, 1) ## draw a black border around the tile 

            if char_grid[row][col] != "": ## if the character grid is not empty, draw the character in the tile
                text_surface = font_for_grid.render(char_grid[row][col].upper(), True, color_grid[row][col]) ## create a surface for the character text 
                text_rect = text_surface.get_rect(center=rect.center) ## center the characteer on the cell
                SCREEN.blit(text_surface, text_rect) ## put the character on the screen 

# Draw numbers function
def draw_numbers():
        for i in numbers:
            ## create a surface for each number in the numbers list, render the number on the surface, append the surface to the numSurfaceArray
            numSurfaceArray.append(font.render(str(i), True, BLACK))

        for i, j in enumerate(range(len(numbers))): ## loop through the numbers list and the coordinates list
            SCREEN.blit(numSurfaceArray[i], (coordinateArray[j][0], coordinateArray[j][1])) ## put the number on the screen at the coordinates of that number
# Draw hints and title            
def draw_hints_title():
    # displaying hints in the blank box
    SCREEN.fill(WHITE)     # fill the blank box with white                     
    draw_grid(tile_size) 
    crossword_clues(SCREEN, text_lines, x_start=GRID_COLS * tile_size + 20, y_start=20)  #call the crossword clues function  

    title(SCREEN, title_text, x_start= 400, y_start=20) # call the title function

# Draw buttons function
def draw_buttons():
    ## displaying the button to check the answers with the typed words 
    button_font = pygame.font.Font(None, 48) ## button font 
    pygame.draw.rect(SCREEN, LIGHT_GREY, check_button, border_radius=3) ## button color
    button_text = button_font.render("Check", True, BLACK) ## button text 
    text_center = button_text.get_rect(center=check_button.center) ## center the text on the button 
    SCREEN.blit(button_text, text_center) ## blit the text on the button (basically put the text on top of the button)
    
    ## displaying the button to clear the grid
    pygame.draw.rect(SCREEN, LIGHT_GREY, clear_button, border_radius=3) ## button color
    button_text2 = button_font.render("Clear", True, BLACK) ## button text
    text_center2 = button_text2.get_rect(center=clear_button.center) ## center the text on the button
    SCREEN.blit(button_text2, text_center2) ## blit the text on the button (basically put the text on top of the button)

# Draw timer function
def draw_timer():
    ticks = pygame.time.get_ticks()  # Get the current time in milliseconds
    seconds = (ticks - start_time) / 1000  # Convert to seconds
    minutes = seconds // 60  # Get the number of minutes
    output = f"{int(minutes):02}:{int(seconds % 60):02}"  # Format the output as MM:SS
    timer_text = timer_font.render(output, (150, 40), RED)  # Render the output on the title box
    SCREEN.blit(timer_text, (150, 40))  # Blit the output on the screen
    pygame.display.set_caption(f"Time: {output}")  # Update the window title with the elapsed time

# draw title box
title_box = pygame.Rect(0, 0, SCREEN_WIDTH, TITLE_BOX_HEIGHT) ## create a rectangle for the title box
pygame.draw.rect(SCREEN, GREY, title_box) ## fill the title box with grey color 

## draw blank box 
blank_box = pygame.Rect(GRID_COLS * tile_size, 0, BLANK_BOX_WIDTH, SCREEN_HEIGHT) ## create a rectangle for the blank box
pygame.draw.rect(SCREEN, GREY, blank_box) ## fill the blank box with grey color

## add two buttons: (1) to guess your answers and (2) to clear the grid 
check_button = pygame.Rect(button_x, button_y, button_width, button_height) ## button to check whether the guessed words are correct 
clear_button = pygame.Rect(button_x, button_y2, button_width, button_height) ## button to clear the grid

## clear the grid of colors  
def clear_grid():
    for row in range(GRID_ROWS): 
        for col in range(GRID_COLS):
            if matrix_grid[row][col] == 2 or matrix_grid[row][col] == 3: ## if the box is yellow or blue 
                matrix_grid[row][col] = 0 ## reset the grid to white

# checks if guessed letters are correct --> red if wrong, green if right
def check_puzzle():
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            if matrix_grid[row][col] != 1 and char_grid[row][col] != "":  ## if the box is not black and the character grid is not empty 
                if char_grid[row][col].upper() == answer_grid[row][col].upper(): ## if the character in the grid at row, col is equal to the the character in answer grid at row,col
                    color_grid[row][col] = GREEN   ## change the color of the character to green
                else:
                    color_grid[row][col] = RED ## change the color of the character to red

## initalizing variables that will be used in the main loop
clickCount = 0 ## used to count the number of mouse clicks the user has made
first_click = None ## used to store the first click index
second_click = None ## used to store the second click index
direction = "horizontal" ## used to store the direction of the word
row, col = 0,0 ## used to store the row and column of the clicked box 

# Set up the clock
clock = pygame.time.Clock() ## create a clock object 
start_time = 0 ## used to store the start time of the clock/timer


run = True ## main loop
while run:
    for event in pygame.event.get(): ## loop through all the events in the list of events 
        if event.type == QUIT: ## if the user clicks the close button 
            run = False ## exit the game
        
        if show_intro_screen: ## if the intro screen is shown 
            if event.type == KEYDOWN and event.key == K_SPACE : ## if the space key is pressed
                show_intro_screen = False  # Hide instructions
                start_time = pygame.time.get_ticks() ## start the timer
                continue  ## get out of the loop and go to the next iteration 

        if event.type == MOUSEBUTTONDOWN: ## if the mouse button is pressed
            mouse_x, mouse_y = event.pos ## get the mouse position
            ## converts that position to grid coordinates 
            col = mouse_x // tile_size ## column of the grid
            row = (mouse_y - TITLE_BOX_HEIGHT) // tile_size ## row of the grid 
            
            if clear_button.collidepoint(mouse_x,mouse_y): ## if the clear button has been pressed 
                clear_grid() ## clear the grid of all its colors
                char_grid = [["" for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)] ## reset the char_grid to empty
                color_grid = [["black" for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)] ## reset the color_grid to black

            rect = pygame.Rect(col * tile_size, TITLE_BOX_HEIGHT + row * tile_size, tile_size, tile_size) ## initaliaze the rectangle for the clicked box

            if check_button.collidepoint(mouse_x, mouse_y): #if the check button has been pressed
                check_puzzle() ## check the puzzle

            ## check if mouse position within grid 
            if 0 <= row < GRID_ROWS and 0 <= col < GRID_COLS and matrix_grid[row][col] != 1: ## if the mouse position is in the grid and not black
                if clickCount == 0:      ## first click  
                    clear_grid() ## clear the grid of all its colors
                    first_click = (row,col)  ## store the first click index 
                    matrix_grid[row][col] = 2 ## box clicked on turns yellow 
                    direction = "horizontal" ## default direction 

                    next_col = col + 1 ## check to the right of the box
                    prev_col = col - 1 ## check to the left of the box

                    while next_col < GRID_COLS and matrix_grid[row][next_col] != 1: ## if the right of the box is in the matrix and not black
                        matrix_grid[row][next_col] = 3 ## change color of that box to light blue 
                        next_col += 1 ## move to the box two away from the one you clicked on 
                    
                    while prev_col < GRID_COLS and matrix_grid[row][prev_col] != 1: ## if the left of the box is in the matrix and not black
                        matrix_grid[row][prev_col] = 3 ## change color of that box to light blue 
                        prev_col -= 1 ## move to the box two away from the one you clicked on 
                    
                    clickCount = 1 ## set the click count to 1, so the next click will be the second click and the first click is complete 

                elif clickCount == 1:  ## second click 
                    clear_grid() ## clear the grid of all its colors
                    second_click = (row,col) ## store the second click index
                    if second_click == first_click:  ## if the cordinates of the first and second click are the same
                        direction = "vertical" # change the direction to vertical 
                        matrix_grid[row][col] = 2 ## change the box color to yellow
                        next_row, j = row + 1, col # now check the box below the second click 

                        while next_row < GRID_ROWS and matrix_grid[next_row][j] != 1: ## if the box below the second click is in the matrix and not black 
                            matrix_grid[next_row][j] = 3 ## change box color to light blue 
                            next_row += 1 ## move to next row
                        
                        prev_row, j = row - 1, col # now check the box above the second click

                        while prev_row < GRID_ROWS and matrix_grid[prev_row][j] != 1: ## if the row above the second click is in the matrix and not black 
                            matrix_grid[prev_row][j] = 3 ## change box color to light blue 
                            prev_row -= 1 ## move to previous row

                    else: ## if the first and second click coordinates aren't the same
                        clear_grid() ## clear the grid of all its color 
                        row,col = second_click  # store index of the second click 
                        matrix_grid[row][col] = 2 ## change box color to yellow 

                        next_col = col + 1 ## check the box to the right of the clicked box
                        prev_col = col - 1 ## check to the left of the box

                        while next_col < GRID_COLS and matrix_grid[row][next_col] != 1: ## if the box to the right of the clicked box is in the matrix and not black
                            matrix_grid[row][next_col] = 3 # change box color to the right of the clicked box to light blue 
                            next_col += 1 ## move to the next column

                        while prev_col < GRID_COLS and matrix_grid[row][prev_col] != 1: ## if the box to the left of the clicked box is in the matrix and not black
                            matrix_grid[row][prev_col] = 3 # change box color to the left of the clicked box to light blue 
                            prev_col -= 1 ## move to the previous column

                        direction = "horizontal" ## change direction to default 
                        
                    first_click = second_click ## coordinates of the first click are now the coordinates of the second click (bascially reseting the first click to the second click so logic works)
                    clickCount = 0 # reset the click counter to 0

        if event.type == pygame.KEYDOWN: ## if the key is pressed      
            if event.key == pygame.K_BACKSPACE: ## if the backspace key is pressed
                char_grid[row][col] = "" ## clear the character in the cell char_grid
                if direction == "horizontal":  ## if the direction is horizontal 
                    if col - 1 >= 0 and matrix_grid[row][col - 1] != 1: ## if the column behind the current column is in the matrix and not black
                        col-= 1 # go back to the previous column
                else: ## if the direction is vertical     
                    if row - 1 >= 0 and matrix_grid[row - 1][col] != 1: ## if the row behind the current row is in the matrix and not black
                        row -= 1 ## go back to the previous row
            else: ## if the key pressed is not backspace 
                if matrix_grid[row][col] != 1: ## if the box is not black
                     char_grid[row][col] = event.unicode ## stores the character that was typed
                if direction == "horizontal": ## if the direction is horizontal 
                    if col + 1 < GRID_COLS and matrix_grid[row][col + 1] != 1: ## if the column next to current column is in the matrix and not black
                        col+= 1 # go to the next column
                    ## avoiding going out of bounds
                elif direction == "vertical": ## if the direction is vertical 
                    if row + 1 < GRID_ROWS and matrix_grid[row + 1][col] != 1: ## if the row next to current row is in the matrix and not black
                        row+=1 # go to the next row 
                        
            if 0 <= row < GRID_ROWS and 0 <= col < GRID_COLS and matrix_grid[row][col] != 1: ## if in grid and not black 
                first_click = (row,col) ## store the first click index
            else:
                first_click = None ## if the next cell is out of bounds, set the first click to None  
        
    draw_hints_title() ## draw the hints and the title
    draw_buttons() ## draw the buttons 
    draw_timer() ## draw the timer

    if show_intro_screen: ## if the intro screen is shown
        draw_instructions() ## draw the instructions
    else:
        draw_grid(tile_size) ## draw the grid
        draw_numbers() ## draw the numbers inside the grid

        
    pygame.display.update() ## update the display 
    
pygame.quit()
