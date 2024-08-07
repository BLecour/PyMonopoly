import pygame
import random
from board import *

random.seed()

def roll_one():
    return random.randint(1,6)

def roll_two():
    return random.randint(1,6), random.randint(1,6)

def draw_one(screen, x, y):
    dice = pygame.Rect(x, y, 50, 50)
    pygame.draw.rect(screen, colours["white"], dice)
    pygame.draw.rect(screen, colours["black"], dice, 4)
    pygame.draw.circle(screen, colours["black"], dice.center, 5)

def draw_two(screen, x, y):
    dice = pygame.Rect(x, y, 50, 50)
    pygame.draw.rect(screen, colours["white"], dice)
    pygame.draw.rect(screen, colours["black"], dice, 4)
    pygame.draw.circle(screen, colours["black"], (x+15, y+15), 5)
    pygame.draw.circle(screen, colours["black"], (x+35, y+35), 5)

def draw_three(screen, x, y):
    dice = pygame.Rect(x, y, 50, 50)
    pygame.draw.rect(screen, colours["white"], dice)
    pygame.draw.rect(screen, colours["black"], dice, 4)
    pygame.draw.circle(screen, colours["black"], dice.center, 5)
    pygame.draw.circle(screen, colours["black"], (x+12, y+12), 5)
    pygame.draw.circle(screen, colours["black"], (x+38, y+38), 5)

def draw_four(screen, x, y):
    dice = pygame.Rect(x, y, 50, 50)
    pygame.draw.rect(screen, colours["white"], dice)
    pygame.draw.rect(screen, colours["black"], dice, 4)
    pygame.draw.circle(screen, colours["black"], (x+12, y+12), 5)
    pygame.draw.circle(screen, colours["black"], (x+38, y+38), 5)
    pygame.draw.circle(screen, colours["black"], (x+12, y+38), 5)
    pygame.draw.circle(screen, colours["black"], (x+38, y+12), 5)

def draw_five(screen, x, y):
    dice = pygame.Rect(x, y, 50, 50)
    pygame.draw.rect(screen, colours["white"], dice)
    pygame.draw.rect(screen, colours["black"], dice, 4)
    pygame.draw.circle(screen, colours["black"], dice.center, 5)
    pygame.draw.circle(screen, colours["black"], (x+12, y+12), 5)
    pygame.draw.circle(screen, colours["black"], (x+38, y+38), 5)
    pygame.draw.circle(screen, colours["black"], (x+12, y+38), 5)
    pygame.draw.circle(screen, colours["black"], (x+38, y+12), 5)

def draw_six(screen, x, y):
    dice = pygame.Rect(x, y, 50, 50)
    pygame.draw.rect(screen, colours["white"], dice)
    pygame.draw.rect(screen, colours["black"], dice, 4)
    pygame.draw.circle(screen, colours["black"], (x+12, y+12), 5)
    pygame.draw.circle(screen, colours["black"], (x+38, y+38), 5)
    pygame.draw.circle(screen, colours["black"], (x+12, y+38), 5)
    pygame.draw.circle(screen, colours["black"], (x+38, y+12), 5)
    pygame.draw.circle(screen, colours["black"], (x+12, y+25), 5)
    pygame.draw.circle(screen, colours["black"], (x+38, y+25), 5)

def do_starting_rolls(player_count):
    rolls = [0] * player_count
    for i in range(player_count):
        rolls[i] = roll_one()

    while True:
        # Find the top value
        top_value = max(rolls)
        # Count occurrences of the top value
        top_count = rolls.count(top_value)

        if top_count <= 1:
            break

        # Reroll duplicates of the top value
        for i in range(player_count):
            if rolls[i] == top_value:
                rolls[i] = roll_one()

    return rolls