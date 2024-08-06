import pygame
from pygame.locals import *
from pygame_widgets.slider import Slider

pygame.init()

font = pygame.font.Font('font\kabel.ttf', 16)
medium_font = pygame.font.Font('font\kabel.ttf', 32)
big_font = pygame.font.Font('font\kabel.ttf', 64)

colours = {"black": (0, 0, 0),
           "background": (208, 210, 196),
           "orange": (252, 145, 2),
           "pink": (231, 25, 151),
           "light blue": (164, 233, 251),
           "brown": (149, 80, 49),
           "blue": (0, 114, 194),
           "green": (3, 186, 72),
           "yellow": (254, 243, 1),
           "red": (237, 0, 20)}

font = pygame.font.Font('font\kabel.ttf', 16)
medium_font = pygame.font.Font('font\kabel.ttf', 32)
big_font = pygame.font.Font('font\kabel.ttf', 64)

def displayText(screen, word, x, y, rotation=0):
    text = font.render(word, True, colours["black"])
    text = pygame.transform.rotate(text, rotation)
    screen.blit(text, (x, y))

def displayMediumText(screen, word, x, y, rotation=0):
    text = medium_font.render(word, True, colours["black"])
    text = pygame.transform.rotate(text, rotation)
    screen.blit(text, (x, y))

def displayBigText(screen, word, x, y, rotation=0):
    text = big_font.render(word, True, colours["black"])
    text = pygame.transform.rotate(text, rotation)
    screen.blit(text, (x, y))

def drawBoard(screen):

    displayBigText(screen, "PyMonopoly", 220, 200, 45)

    # Free Parking square
    pygame.draw.rect(screen, colours["black"], pygame.Rect(30, 30, 100, 100), 1)
    displayText(screen, "FREE", 60, 110, 180)
    displayText(screen, "PARKING", 38, 30, 180)

    # Left side of screen
    pygame.draw.rect(screen, colours["orange"], pygame.Rect(105, 130, 25, 60))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(105, 130, 25, 60), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(30, 130, 100, 60), 1) # NEW YORK AVENUE
    displayText(screen, "N.Y.", 85, 142, 270)
    displayText(screen, "AVE", 65, 142, 270)
    displayText(screen, "$200", 29, 140, 270)

    pygame.draw.rect(screen, colours["orange"], pygame.Rect(105, 190, 25, 60))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(105, 190, 25, 60), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(30, 190, 100, 60), 1) # TENNESSEE AVENUE
    displayText(screen, "TEN.", 85, 202, 270)
    displayText(screen, "AVE", 65, 202, 270)
    displayText(screen, "$180", 29, 200, 270)

    pygame.draw.rect(screen, colours["black"], pygame.Rect(30, 250, 100, 60), 1) # COMMUNITY CHEST
    displayText(screen, "COMM", 105, 249, 270)
    displayText(screen, "CHEST", 85, 252, 270)

    pygame.draw.rect(screen, colours["orange"], pygame.Rect(105, 310, 25, 60))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(105, 310, 25, 60), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(30, 310, 100, 60), 1) # ST. JAMES PLACE
    displayText(screen, "ST. J", 85, 317, 270)
    displayText(screen, "PLACE", 65, 311, 270)
    displayText(screen, "$180", 29, 320, 270)

    pygame.draw.rect(screen, colours["black"], pygame.Rect(30, 370, 100, 60), 1) # PENNSYLVANIA RAILROAD
    displayText(screen, "PENN.", 105, 375, 270)
    displayText(screen, "R.R", 85, 383, 270)
    displayText(screen, "$200", 29, 377, 270)

    pygame.draw.rect(screen, colours["pink"], pygame.Rect(105, 430, 25, 60))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(105, 430, 25, 60), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(30, 430, 100, 60), 1) # VIRGINIA AVENUE
    displayText(screen, "VIR.", 85, 445, 270)
    displayText(screen, "AVE", 65, 442, 270)
    displayText(screen, "$180", 29, 440, 270)

    pygame.draw.rect(screen, colours["pink"], pygame.Rect(105, 490, 25, 60))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(105, 490, 25, 60), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(30, 490, 100, 60), 1) # STATES AVENUE
    displayText(screen, "ST.", 85, 507, 270)
    displayText(screen, "AVE", 65, 502, 270)
    displayText(screen, "$180", 29, 500, 270)

    pygame.draw.rect(screen, colours["black"], pygame.Rect(30, 550, 100, 60), 1) # ELECTRIC COMPANY
    displayText(screen, "ELEC", 105, 560, 270)
    displayText(screen, "CO.", 85, 565, 270)
    displayText(screen, "$150", 29, 560, 270)

    pygame.draw.rect(screen, colours["pink"], pygame.Rect(105, 610, 25, 60))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(105, 610, 25, 60), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(30, 610, 100, 60), 1) # ST. CHARLES PLACE
    displayText(screen, "ST. C", 85, 617, 270)
    displayText(screen, "PLACE", 65, 611, 270)
    displayText(screen, "$140", 29, 620, 270)

    # Jail/Just visiting square
    pygame.draw.rect(screen, colours["black"], pygame.Rect(30, 670, 100, 100), 1)
    pygame.draw.rect(screen, colours["orange"], pygame.Rect(51, 669, 80, 80))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(51, 669, 80, 80), 2)
    displayText(screen, "IN JAIL", 60, 672, 0)
    displayText(screen, "JUST", 28, 690, 270)
    displayText(screen, "VISITING", 44, 753, 0)

    # Bottom of screen
    pygame.draw.rect(screen, colours["light blue"], pygame.Rect(130, 670, 60, 25))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(130, 670, 60, 25), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(130, 670, 60, 100), 1) # CONNECTICUT AVENUE
    displayText(screen, "CONN.", 131, 696, 0)
    displayText(screen, "AVE", 140, 716, 0)
    displayText(screen, "$120", 140, 751, 0)

    pygame.draw.rect(screen, colours["light blue"], pygame.Rect(190, 670, 60, 25))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(190, 670, 60, 25), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(190, 670, 60, 100), 1) # VERMONT AVENUE
    displayText(screen, "VER.", 200, 696, 0)
    displayText(screen, "AVE", 200, 716, 0)
    displayText(screen, "$120", 200, 751, 0)

    pygame.draw.rect(screen, colours["black"], pygame.Rect(250, 670, 60, 100), 1) # CHANCE
    displayText(screen, "CHNC.", 253, 675, 0)
    displayBigText(screen, "?", 260, 705, 0)

    pygame.draw.rect(screen, colours["light blue"], pygame.Rect(310, 670, 60, 25))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(310, 670, 60, 25), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(310, 670, 60, 100), 1) # ORIENTAL AVENUE
    displayText(screen, "ORI.", 320, 696, 0)
    displayText(screen, "AVE", 320, 716, 0)
    displayText(screen, "$100", 320, 751, 0)

    pygame.draw.rect(screen, colours["black"], pygame.Rect(370, 670, 60, 100), 1) # READING RAILROAD
    displayText(screen, "READ.", 372, 675, 0)
    displayText(screen, "R.R", 385, 696, 0)
    displayText(screen, "$200", 380, 751, 0)

    pygame.draw.rect(screen, colours["black"], pygame.Rect(430, 670, 60, 100), 1) # INCOME TAX
    displayText(screen, "INC.", 443, 675, 0)
    displayText(screen, "TAX", 440, 696, 0)
    displayText(screen, "PAY", 442, 731, 0)
    displayText(screen, "$200", 440, 751, 0)

    pygame.draw.rect(screen, colours["brown"], pygame.Rect(490, 670, 60, 25))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(490, 670, 60, 25), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(490, 670, 60, 100), 1) # BALTIC AVENUE
    displayText(screen, "BAL.", 500, 696, 0)
    displayText(screen, "AVE", 500, 716, 0)
    displayText(screen, "$60", 505, 751, 0)

    pygame.draw.rect(screen, colours["black"], pygame.Rect(550, 670, 60, 100), 1) # COMMUNITY CHEST
    displayText(screen, "COMM", 550, 675, 0)
    displayText(screen, "CHEST", 552, 696, 0)

    pygame.draw.rect(screen, colours["brown"], pygame.Rect(610, 670, 60, 25))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(610, 670, 60, 25), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(610, 670, 60, 100), 1) # MEDITERRANEAN AVENUE
    displayText(screen, "MED.", 620, 696, 0)
    displayText(screen, "AVE", 620, 716, 0)
    displayText(screen, "$60", 625, 751, 0)

    # GO square
    pygame.draw.rect(screen, colours["black"], pygame.Rect(670, 670, 100, 100), 1)
    displayMediumText(screen, "GO", 693, 685, 0)
    displayBigText(screen, "<--", 670, 710, 0)

    # Right side of screen
    pygame.draw.rect(screen, colours["blue"], pygame.Rect(670, 610, 25, 60)) 
    pygame.draw.rect(screen, colours["black"], pygame.Rect(670, 610, 25, 60), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(670, 610, 100, 60), 1) # BOARDWALK
    displayText(screen, "BRD.", 697, 615, 90)
    displayText(screen, "WALK", 717, 612, 90)
    displayText(screen, "$400", 750, 620, 90)

    pygame.draw.rect(screen, colours["black"], pygame.Rect(670, 550, 100, 60), 1) # LUXURY TAX 
    displayText(screen, "LUX.", 673, 555, 90)
    displayText(screen, "TAX", 693, 559, 90)
    displayText(screen, "PAY", 730, 560, 90)
    displayText(screen, "$100", 750, 560, 90)

    pygame.draw.rect(screen, colours["blue"], pygame.Rect(670, 490, 25, 60))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(670, 490, 25, 60), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(670, 490, 100, 60), 1) # PARK PLACE
    displayText(screen, "PARK", 697, 495, 90)
    displayText(screen, "PLACE", 717, 492, 90)
    displayText(screen, "$350", 750, 500, 90)

    pygame.draw.rect(screen, colours["black"], pygame.Rect(670, 430, 100, 60), 1) # CHANCE
    displayText(screen, "CHNC.", 673, 432, 90)
    displayBigText(screen, "?", 700, 440, 90)

    pygame.draw.rect(screen, colours["black"], pygame.Rect(670, 370, 100, 60), 1) # SHORT LINE
    displayText(screen, "SHRT.", 674, 372, 90)
    displayText(screen, "LINE", 693, 381, 90)
    displayText(screen, "$200", 750, 380, 90)

    pygame.draw.rect(screen, colours["green"], pygame.Rect(670, 310, 25, 60))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(670, 310, 25, 60), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(670, 310, 100, 60), 1) # PENNSYLVANIA AVENUE
    displayText(screen, "PENN.", 697, 313, 90)
    displayText(screen, "AVE", 717, 321, 90)
    displayText(screen, "$320", 750, 320, 90)

    pygame.draw.rect(screen, colours["black"], pygame.Rect(670, 250, 100, 60), 1) # COMMUNITY CHEST
    displayText(screen, "COMM", 674, 250, 90)
    displayText(screen, "CHEST", 693, 252, 90)

    pygame.draw.rect(screen, colours["green"], pygame.Rect(670, 190, 25, 60))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(670, 190, 25, 60), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(670, 190, 100, 60), 1) # NORTH CAROLINA AVENUE
    displayText(screen, "N.C", 697, 204, 90)
    displayText(screen, "AVE", 717, 201, 90)
    displayText(screen, "$300", 750, 200, 90)

    pygame.draw.rect(screen, colours["green"], pygame.Rect(670, 130, 25, 60))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(670, 130, 25, 60), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(670, 130, 100, 60), 1) # PACIFIC AVENUE
    displayText(screen, "PAC.", 697, 136, 90)
    displayText(screen, "AVE", 717, 142, 90)
    displayText(screen, "$300", 750, 140, 90)

    # Go to Jail square
    pygame.draw.rect(screen, colours["black"], pygame.Rect(670, 30, 100, 100), 1)
    displayText(screen, "GO", 708, 110, 180)
    displayText(screen, "TO", 708, 70, 180)
    displayText(screen, "JAIL", 702, 30, 180)

    # Top of screen
    pygame.draw.rect(screen, colours["yellow"], pygame.Rect(610, 105, 60, 25))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(610, 105, 60, 25), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(610, 30, 60, 100), 1) # MARVIN GARDENS
    displayText(screen, "MARV", 611, 85, 180)
    displayText(screen, "GARD.", 610, 65, 180)
    displayText(screen, "$260", 620, 30, 180)

    pygame.draw.rect(screen, colours["black"], pygame.Rect(550, 30, 60, 100), 1) # WATER WORKS
    displayText(screen, "WTR.", 553, 105, 180)
    displayText(screen, "WRKS.", 550, 85, 180)
    displayText(screen, "$150", 560, 30, 180)

    pygame.draw.rect(screen, colours["yellow"], pygame.Rect(490, 105, 60, 25))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(490, 105, 60, 25), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(490, 30, 60, 100), 1) # VENTNOR AVENUE
    displayText(screen, "VEN.", 500, 85, 180)
    displayText(screen, "AVE", 505, 65, 180)
    displayText(screen, "$260", 500, 30, 180)

    pygame.draw.rect(screen, colours["yellow"], pygame.Rect(430, 105, 60, 25))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(430, 105, 60, 25), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(430, 30, 60, 100), 1) # ATLANTIC AVENUE
    displayText(screen, "ATL.", 443, 85, 180)
    displayText(screen, "AVE", 445, 65, 180)
    displayText(screen, "$260", 440, 30, 180)

    pygame.draw.rect(screen, colours["black"], pygame.Rect(370, 30, 60, 100), 1) # B. & O. RAILROAD
    displayText(screen, "B&O", 380, 105, 180)
    displayText(screen, "R.R", 382, 85, 180)
    displayText(screen, "$200", 380, 30, 180)

    pygame.draw.rect(screen, colours["red"], pygame.Rect(310, 105, 60, 25))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(310, 105, 60, 25), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(310, 30, 60, 100), 1) # ILLINOIS AVENUE
    displayText(screen, "ILL.", 323, 85, 180)
    displayText(screen, "AVE", 325, 65, 180)
    displayText(screen, "$240", 320, 30, 180)

    pygame.draw.rect(screen, colours["red"], pygame.Rect(250, 105, 60, 25))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(250, 105, 60, 25), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(250, 30, 60, 100), 1) # INDIANA AVENUE
    displayText(screen, "IND.", 260, 85, 180)
    displayText(screen, "AVE", 265, 65, 180)
    displayText(screen, "$220", 260, 30, 180)

    pygame.draw.rect(screen, colours["black"], pygame.Rect(190, 30, 60, 100), 1) # CHANCE
    displayText(screen, "CHNC.", 194, 105, 180)
    displayBigText(screen, "?", 203, 25, 180)

    pygame.draw.rect(screen, colours["red"], pygame.Rect(130, 105, 60, 25))
    pygame.draw.rect(screen, colours["black"], pygame.Rect(130, 105, 60, 25), 1)
    pygame.draw.rect(screen, colours["black"], pygame.Rect(130, 30, 60, 100), 1) # KENTUCKY AVENUE
    displayText(screen, "KEN.", 140, 85, 180)
    displayText(screen, "AVE", 145, 65, 180)
    displayText(screen, "$200", 140, 30, 180)

    # Drawing additional lines above and below (or left and right to) the properties
    # Makes the line the same size as the line in between neighboring properties
    pygame.draw.line(screen, colours["black"],  [130, 130], [670, 130], 1) # Below top properties
    pygame.draw.line(screen, colours["black"],  [30, 29], [770, 29], 1) # Above top properties

    pygame.draw.line(screen, colours["black"],  [130, 130], [130, 670], 1) # Right of left side properties
    pygame.draw.line(screen, colours["black"],  [29, 30], [29, 770], 1) # Left of left side properties

    pygame.draw.line(screen, colours["black"],  [30, 770], [770, 770], 1) # Below bottom properties
    pygame.draw.line(screen, colours["black"],  [130, 669], [670, 669], 1) # Above bottom properties

    pygame.draw.line(screen, colours["black"],  [770, 30], [770, 770], 1) # Right of right side properties
    pygame.draw.line(screen, colours["black"],  [669, 130], [669, 670], 1) # Left of right side properties

    pygame.display.flip()