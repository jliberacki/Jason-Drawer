import pygame
import re
import sys
from math import sqrt

def convert_color(color, pallet):
    if color in pallet.keys():
        color = pallet[color]
    if color[0] == '#':
        #strip from unnecesary character and then convert hex to rgb
        color = color.lstrip('#')
        color = tuple([int(color[i:i + 2], 16) for i in (0, 2, 4)])
    elif color[0] == '(':
        #finds any decimal values 1 to 3 characters long and turn them to int
        color = tuple([int(string) for string in re.findall(r'\d{1,3}', color)])
    return color

def draw(Figures,Screen,Palette,save_png):
    pygame.init()
    screen = pygame.display.set_mode((Screen["width"], Screen["height"]))
    screen.fill(convert_color(Screen["bg_color"],Palette))
    
    fg_color = convert_color(Screen["fg_color"],Palette)

    for figure in Figures:
        if "type" not in list(figure.keys()):
            raise Exception("Provide proper figure type")
        figure_type = figure["type"]
        figure_color = figure["color"] if "color" in list(figure.keys()) else fg_color
        #print (figure_color)
        if figure_type == "point":
            screen.set_at([figure["x"], figure["y"]], convert_color(figure_color,Palette))
        elif figure_type == "circle":
            pygame.draw.circle(screen, convert_color(figure_color,Palette), [figure["x"], figure["y"]], fig["radius"])
        elif figure_type == "polygon":
            pygame.draw.polygon(screen, convert_color(figure_color,Palette), figure["points"])
        elif figure_type == "square":
            if "size" in list(figure.keys()): length = figure["size"]
            elif "radius" in list(figure.keys()): length = figure["radius"]/(sqrt(2))
            left = figure["x"] - (length/2)
            top = figure["y"] - (length/2)
            pygame.draw.rect(screen, convert_color(figure_color,Palette), pygame.Rect(left, top, length, length))
        elif figure_type == "rectangle":
            width = figure["width"]
            height = figure["height"]
            left = figure["x"] - (width/2)
            top = figure["y"] - (height/2)
            pygame.draw.rect(screen, convert_color(figure_color,Palette), pygame.Rect(left, top, width, height))

    pygame.display.flip()
    if save_png:
        if save_png[-4:] != '.png': save_png += '.png'
        pygame.image.save(screen,save_png)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
