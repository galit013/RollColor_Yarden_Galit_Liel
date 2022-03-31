import pygame
from constants import *
from Player import *
from Block import *


class App:
    def __init__(self, screen):
        self.screen = screen
        self.curr_screen = None
        self.start_display()

    def start_display(self):
        ball = Player(self.screen)
        self.home_screen(self.screen, ball.get_color(), ball.get_x_pos(), ball.get_y_pos())

    def home_screen(self, screen, ball_color, x_start_ball, y_start_ball):
        pygame.draw.circle(screen, ball_color, (x_start_ball, y_start_ball), RADIUS)
        # img = pygame.image.load(BALL_PATH)
        # img = pygame.transform.scale(img, (BALL_WIDTH, BALL_HEIGHT))
        # screen.blit(ball.get_player(), (X_POS_START,Y_POS_START))
        # img = pygame.image.load(BLOCK_PATH)
        # img = pygame.transform.scale(img, (BLOCK_WIDTH, BLOCK_HEIGHT))
        # screen.blit(img, (0, 0))

    def game_screen(self):
        pass

    def ending_game_screen(self):
        pass
