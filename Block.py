import pygame
from constants import *


class Block:
    def __init__(self, screen):
        self.x_pos = 0
        self.y_pos = 0
        self.color = (255, 0, 0)
        img_path = BLOCK_PATH
        img = pygame.image.load(BLOCK_PATH)
        img = pygame.transform.scale(img, (BLOCK_WIDTH, BLOCK_HEIGHT))
        screen.blit(img, (self.x_pos, self.y_pos))
        self.block = img
