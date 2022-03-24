import pygame
from constants import *
from Player import *


class App:
    def __init__(self, screen):
        self.screen = screen
        self.curr_screen = None
        self.start_display()

    def start_display(self):
        self.home_screen(self.screen)

    def home_screen(self, screen):
        # img = pygame.image.load(BALL_PATH)
        # img = pygame.transform.scale(img, (BALL_WIDTH, BALL_HEIGHT))
        # screen.blit(ball.get_player(), (X_POS_START,Y_POS_START))
        img = pygame.image.load(BLOCK_PATH)
        img = pygame.transform.scale(img, (BLOCK_WIDTH, BLOCK_HEIGHT))
        screen.blit(img, (0,0))

    def game_screen(self):
        pass

    def ending_game_screen(self):
        pass