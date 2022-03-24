import pygame
from constants import *


class App:
    def __init__(self, screen):
        self.screen = screen
        self.curr_screen = None
        self.start_display()

    def start_display(self):
        self.home_screen(self.screen)

    def home_screen(self, screen, ball):
        pygame.draw.circle(screen, (255, 0, 0), (X_POS_START, Y_POS_START), RADIUS)

    def game_screen(self):
        pass

    def ending_game_screen(self):
        pass