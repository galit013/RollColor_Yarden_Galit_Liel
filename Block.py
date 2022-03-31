import pygame
from constants import *


class Block:
    def __init__(self, screen, color, x_pos, y_pos, width, height):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        self.width = width
        self.height = height
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x_pos, self.y_pos, self.width, self.height))

    def get_block(self):
        pass

    def get_block_color(self):
        return self.color

    def get_block_x_pos(self):
        return self.x_pos

    def get_block_y_pos(self):
        return self.y_pos

    def get_block_width(self):
        return self.width

    def get_block_height(self):
        return self.height

    def set_x_pos(self, change_x):
        self.x_pos += change_x
