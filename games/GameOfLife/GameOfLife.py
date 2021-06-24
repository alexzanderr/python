
import os
import pygame
from time import sleep
from random import randint
import json
from core.json_module import *

# dont know what this is
os.environ["SDL_VIDEO_CENTERED"]= "1"

# window size
window_width, window_height = 1200, 1000
window_size_tuple = (window_width, window_height)

# init
pygame.init()
pygame.display.set_caption("implemented_game_of_life")

# modifying icon
game_icon = "icons/gameoflife.png"
program_icon = pygame.image.load(game_icon)
pygame.display.set_icon(program_icon)

# pygame window stuff
game_screen = pygame.display.set_mode(window_size_tuple)
game_clock = pygame.time.Clock()

class GameColors:
    black = (0, 0, 0)
    blue = (0, 121, 150)
    blueish = (0, 14, 71)
    white = (255, 255, 255)
    grey = (128, 128, 128)
    yellow = (255, 229, 124)

scaler = 40
offset = 1

def EmptyMatrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]
    
def RandomMatrix(rows, cols):
    return [[randint(0, 1) for _ in range(cols)] for _ in range(rows)]

class TheGrid:
    def __init__(self):
        self.wid = window_width
        self.hei = window_height
        self.scale = scaler
        self.offset = offset
        
        self.rows = self.wid // self.scale
        self.cols = self.hei // self.scale
        
        self.size_tuple = (self.rows, self.cols)
        
        self.current_generation_2darray = RandomMatrix(self.rows, self.cols)
    
    def __update_game_window(self, game_screen):
        for x in range(self.rows):
            for y in range(self.cols):
                x_pos = x * self.scale
                y_pos = y * self.scale
                
                scale_offset = self.scale - self.offset
                if self.current_generation_2darray[x][y] == 1:
                    pygame.draw.rect(game_screen, GameColors.yellow, [x_pos, y_pos, scale_offset, scale_offset])
                else:
                    pygame.draw.rect(game_screen, GameColors.grey, [x_pos, y_pos, scale_offset, scale_offset])
                    
    def GameOfLife(self, screen):
        self.__update_game_window(screen)
        
        next_generation_2darray = EmptyMatrix(self.rows, self.cols)
        
        # validation every cell in the old matrix
        for x in range(self.rows):
            for y in range(self.cols):
                state = self.current_generation_2darray[x][y]
                neighbours = self.get_neighbours(x, y)
                if state == 0 and neighbours == 3:
                    next_generation_2darray[x][y] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    next_generation_2darray[x][y] = 0
                else:
                    next_generation_2darray[x][y] = state
        
        self.current_generation_2darray = next_generation_2darray 
                
    def get_neighbours(self, x, y):
        total = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                x_edge = (x + i + self.rows) % self.rows
                y_edge = (y + j + self.cols) % self.cols
                total += self.current_generation_2darray[x_edge][y_edge]
                
        total -= self.current_generation_2darray[x][y]
        return total


game_grid = TheGrid()
frames_per_second = 10

run = 1
while run:
    game_clock.tick(frames_per_second)
    game_screen.fill(GameColors.black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
            
    # the actual game
    game_grid.GameOfLife(game_screen)
    
    pygame.display.update()
    

pygame.quit()