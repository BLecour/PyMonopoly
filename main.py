import sys
import pygame
from dice import *
from board import *
from player import *
from pygame.locals import *

clock = pygame.time.Clock() 
screen = pygame.display.set_mode((1600, 800))

draw_functions = {
    1: draw_one,
    2: draw_two,
    3: draw_three,
    4: draw_four,
    5: draw_five,
    6: draw_six
}

def draw_button(screen, button_rect, text, selected):
    if selected == 0:
        pygame.draw.rect(screen, colours["blue"], button_rect, 2)
    else:
        pygame.draw.rect(screen, colours["blue"], button_rect)

pygame.display.set_caption("PyMonopoly")

screen.fill(colours["background"])

displayMediumText(screen, "Welcome to PyMonopoly!", 540, 30)
displayText(screen, "Select the amount of players and select either a human player or a computer player:", 390, 100)
displayMediumText(screen, "Player 1:", 100, 300)
displayMediumText(screen, "Player 2:", 500, 300)
displayMediumText(screen, "Player 3:", 900, 300)
displayMediumText(screen, "Player 4:", 1300, 300)

pygame.display.flip() 

# Default selections are Human, Human, None, None
# 0 = Human
# 1 = CPU
# 2 = None
selections = [0, 0, 2, 2]

# Display the Buttons
p1_human_button = pygame.Rect(100, 350, 30, 30)
displayText(screen, "Human", p1_human_button.x+50, p1_human_button.y+5)

p2_human_button = pygame.Rect(500, 350, 30, 30)
displayText(screen, "Human", p2_human_button.x+50, p2_human_button.y+5)
p2_cpu_button = pygame.Rect(500, 400, 30, 30)
displayText(screen, "CPU", p2_cpu_button.x+50, p2_cpu_button.y+5)

p3_human_button = pygame.Rect(900, 350, 30, 30)
displayText(screen, "Human", p3_human_button.x+50, p3_human_button.y+5)
p3_cpu_button = pygame.Rect(900, 400, 30, 30)
displayText(screen, "CPU", p3_cpu_button.x+50, p3_cpu_button.y+5)
p3_none_button = pygame.Rect(900, 450, 30, 30)
displayText(screen, "None", p3_none_button.x+50, p3_none_button.y+5)

p4_human_button = pygame.Rect(1300, 350, 30, 30)
displayText(screen, "Human", p4_human_button.x+50, p4_human_button.y+5)
p4_cpu_button = pygame.Rect(1300, 400, 30, 30)
displayText(screen, "CPU", p4_cpu_button.x+50, p4_cpu_button.y+5)
p4_none_button = pygame.Rect(1300, 450, 30, 30)
displayText(screen, "None", p4_none_button.x+50, p4_none_button.y+5)

play_button = pygame.Rect(730, 700, 100, 40)
  
begin_game = False

while begin_game == False: 
    for event in pygame.event.get(): 
  
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit() 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle clicking of the buttons
            if p2_human_button.collidepoint(event.pos):
                pygame.draw.rect(screen, colours["background"], p2_cpu_button) # Reset the colour for the other button
                selections[1] = 0
            elif p2_cpu_button.collidepoint(event.pos):
                pygame.draw.rect(screen, colours["background"], p2_human_button)
                selections[1] = 1
            elif p3_human_button.collidepoint(event.pos):
                pygame.draw.rect(screen, colours["background"], p3_cpu_button)
                pygame.draw.rect(screen, colours["background"], p3_none_button)
                selections[2] = 0
            elif p3_cpu_button.collidepoint(event.pos):
                pygame.draw.rect(screen, colours["background"], p3_human_button)
                pygame.draw.rect(screen, colours["background"], p3_none_button)
                selections[2] = 1
            elif p3_none_button.collidepoint(event.pos):
                pygame.draw.rect(screen, colours["background"], p3_human_button)
                pygame.draw.rect(screen, colours["background"], p3_cpu_button)
                selections[2] = 2
            elif p4_human_button.collidepoint(event.pos):
                pygame.draw.rect(screen, colours["background"], p4_cpu_button)
                pygame.draw.rect(screen, colours["background"], p4_none_button)
                selections[3] = 0
            elif p4_cpu_button.collidepoint(event.pos):
                pygame.draw.rect(screen, colours["background"], p4_human_button)
                pygame.draw.rect(screen, colours["background"], p4_none_button)
                selections[3] = 1
            elif p4_none_button.collidepoint(event.pos):
                pygame.draw.rect(screen, colours["background"], p4_human_button)
                pygame.draw.rect(screen, colours["background"], p4_cpu_button)
                selections[3] = 2
            elif play_button.collidepoint(event.pos):
                begin_game = True
                break
    
    # Draw all the buttons for the player selections creen
    draw_button(screen, p1_human_button, "Human", True)

    if selections[1] == 0:
        draw_button(screen, p2_human_button, "Human", True)
        draw_button(screen, p2_cpu_button, "CPU", False)
    elif selections[1] == 1:
        draw_button(screen, p2_human_button, "Human", False)
        draw_button(screen, p2_cpu_button, "CPU", True)

    if selections[2] == 0:
        draw_button(screen, p3_human_button, "Human", True)
        draw_button(screen, p3_cpu_button, "CPU", False)
        draw_button(screen, p3_none_button, "None", False)
    elif selections[2] == 1:
        draw_button(screen, p3_human_button, "Human", False)
        draw_button(screen, p3_cpu_button, "CPU", True)
        draw_button(screen, p3_none_button, "None", False)
    elif selections[2] == 2:
        draw_button(screen, p3_human_button, "Human", False)
        draw_button(screen, p3_cpu_button, "CPU", False)
        draw_button(screen, p3_none_button, "None", True)

    if selections[3] == 0:
        draw_button(screen, p4_human_button, "Human", True)
        draw_button(screen, p4_cpu_button, "CPU", False)
        draw_button(screen, p4_none_button, "None", False)
    elif selections[3] == 1:
        draw_button(screen, p4_human_button, "Human", False)
        draw_button(screen, p4_cpu_button, "CPU", True)
        draw_button(screen, p4_none_button, "None", False)
    elif selections[3] == 2:
        draw_button(screen, p4_human_button, "Human", False)
        draw_button(screen, p4_cpu_button, "CPU", False)
        draw_button(screen, p4_none_button, "None", True)

    draw_button(screen, play_button, "", True)
    displayMediumText(screen, "PLAY", play_button.x, play_button.y+3)

    pygame.display.flip() 
      
    clock.tick(60) 

screen.fill(colours["background"])

drawBoard(screen)

num_players = 2

# Display the player names
displayMediumText(screen, "Player 1", 1100, 20)
displayMediumText(screen, "Player 2", 1100, 220)

# Only display P2 and P3 if they were selected
if selections[2] != 2:
    displayMediumText(screen, "Player 3", 1100, 420)
    num_players = 3

if selections[3] != 2:
    displayMediumText(screen, "Player 4", 1100, 620)
    num_players = 4

starting_rolls = do_starting_rolls(num_players)

# Draw the player names for each player that will be in the game
draw_function = draw_functions[starting_rolls[0]]
draw_function(screen, 1040, 10)

draw_function = draw_functions[starting_rolls[1]]
draw_function(screen, 1040, 210)

if num_players >= 3:

    draw_function = draw_functions[starting_rolls[2]]
    draw_function(screen, 1040, 410)

    if num_players == 4:

        draw_function = draw_functions[starting_rolls[3]]
        draw_function(screen, 1040, 610)

# Decide who will be starting
turn = starting_rolls.index(max(starting_rolls)) + 1

print("player " + str(turn) + " starts")

# Display a message indicating which player will start
if turn == 1:
    displayMediumText(screen, "Player 1 will start!", 1000, 80)
    pygame.display.flip() 
    pygame.time.wait(5000)
    clear_object(screen, 1000, 80, 1000, 50)
elif turn == 2:
    displayMediumText(screen, "Player 2 will start!", 1000, 280)
    pygame.display.flip() 
    pygame.time.wait(5000)
    clear_object(screen, 1000, 280, 1000, 50)
elif turn == 3:
    displayMediumText(screen, "Player 3 will start!", 1000, 480)
    pygame.display.flip() 
    pygame.time.wait(5000)
    clear_object(screen, 1000, 480, 1000, 50)
elif turn == 4:
    displayMediumText(screen, "Player 4 will start!", 1000, 680)
    pygame.display.flip() 
    pygame.time.wait(5000)
    clear_object(screen, 1000, 680, 1000, 50)

# Clear all the starting die from the screen
clear_object(screen, 1040, 10, 50, 50)
clear_object(screen, 1040, 210, 50, 50)
clear_object(screen, 1040, 410, 50, 50)
clear_object(screen, 1040, 610, 50, 50)

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
        #elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle clicking of the buttons
            #if roll_button.collidepoint(event.pos):

    pygame.display.flip() 

    clock.tick(60) 