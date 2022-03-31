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
        # block = Block(self.screen, 420, 340, RED)
        self.home_screen(self.screen, ball.get_color(), ball.get_x_pos(), ball.get_y_pos())
        # self.game_screen(self.screen, block.get_color(), block.get_x_pos(), block.get_y_pos())

    def home_screen(self, screen, ball_color, x_start_ball, y_start_ball):
        pygame.draw.circle(screen, ball_color, (x_start_ball, y_start_ball), RADIUS)
        # img = pygame.image.load(BALL_PATH)
        # img = pygame.transform.scale(img, (BALL_WIDTH, BALL_HEIGHT))
        # screen.blit(ball.get_player(), (X_POS_START,Y_POS_START))
        # img = pygame.image.load(BLOCK_PATH)
        # img = pygame.transform.scale(img, (BLOCK_WIDTH, BLOCK_HEIGHT))
        # screen.blit(img, (0, 0))

    def game_screen(self, screen, color, x_start_block, y_start_block):
        print(type(x_start_block))
        print(type(y_start_block))
        pygame.draw.line(screen, color, [x_start_block, y_start_block], [x_start_block, y_start_block + BLOCK_HEIGHT], BLOCK_WIDTH)

    def ending_game_screen(self):
        pass
