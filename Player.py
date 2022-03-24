import pygame
from constants import *

class Player:
    def __init__(self, screen):
        self.x_pos = X_POS_START
        self.y_pos = Y_POS_START
        self.color = (255, 0, 0)
        img_path = BALL_PATH
        img = pygame.image.load(img_path)
        img = pygame.transform.scale(img, (BALL_WIDTH, BALL_HEIGHT))
        screen.blit(img, (self.x_pos, self.y_pos))
        self.player = img

