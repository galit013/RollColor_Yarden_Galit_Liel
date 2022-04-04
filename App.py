import pygame
from constants import *
from Player import *
from Block import *
import random


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

    def game_screen(self, screen, block_list):
        for block in block_list:
            pygame.draw.line(screen, block.get_color(), [block.get_x_pos(), block.get_y_pos()],
                             [block.get_x_pos(), block.get_y_pos() + block.get_height()], BLOCK_WIDTH)

    def move_blocks(self, screen, block_list_right, block_list_left):
        clock = pygame.time.Clock()
        while True:# for i in range(130):
            for i in range(len(block_list_left)):
                pygame.draw.line(screen, BLACK, [block_list_left[i].get_x_pos(), block_list_left[i].get_y_pos()],
                                 [block_list_left[i].get_x_pos(), block_list_left[i].get_y_pos() + block_list_left[i].get_height()], BLOCK_WIDTH)
                pygame.draw.line(screen, BLACK, [block_list_right[i].get_x_pos(), block_list_right[i].get_y_pos()],
                                 [block_list_right[i].get_x_pos(), block_list_right[i].get_y_pos() + block_list_right[i].get_height()], BLOCK_WIDTH)
                if block_list_right[len(block_list_right) - 1].get_y_pos() == 0:
                    current_block_height = BLOCK_HEIGHT_LIST[random.randint(0, 5)]
                    if block_list_right[len(block_list_right) - 1].get_color() == RED:
                        block_list_right.append(Block(screen, YELLOW, X_POS_RIGHT_BLOCK, -current_block_height, current_block_height))
                        block_list_left.append(Block(screen, RED, X_POS_LEFT_BLOCK, -current_block_height, current_block_height))
                    else:
                        block_list_right.append(Block(screen, RED, X_POS_RIGHT_BLOCK, -current_block_height, current_block_height))
                        block_list_left.append(Block(screen, YELLOW, X_POS_LEFT_BLOCK, -current_block_height, current_block_height))
                block_list_left[i].set_y_pos(Y_POS_CHANGE)
                block_list_right[i].set_y_pos(Y_POS_CHANGE)
                pygame.draw.line(screen, block_list_right[i].color, [block_list_right[i].get_x_pos(), block_list_right[i].get_y_pos()],
                                 [block_list_right[i].get_x_pos(), block_list_right[i].get_y_pos() + block_list_right[i].get_height()], BLOCK_WIDTH)
                pygame.draw.line(screen, block_list_left[i].color, [block_list_left[i].get_x_pos(), block_list_left[i].get_y_pos()],
                                 [block_list_left[i].get_x_pos(), block_list_left[i].get_y_pos() + block_list_left[i].get_height()], BLOCK_WIDTH)

                pygame.display.flip()
                clock.tick(120)

    # def move_block_list_right(self, screen, block_list):
    #     clock = pygame.time.Clock()
    #     while True:# for i in range(130):
    #         for block in block_list:
    #             pygame.draw.line(screen, BLACK, [block.get_x_pos(), block.get_y_pos()],
    #                              [block.get_x_pos(), block.get_y_pos() + block.get_height()], BLOCK_WIDTH)
    #             if block_list[len(block_list) - 1].get_y_pos() == 0:
    #                 current_block_height = BLOCK_HEIGHT_LIST[random.randint(0, 5)]
    #                 if block_list[len(block_list) - 1].get_color() == RED:
    #                     block_list.append(Block(screen, YELLOW, 419, -current_block_height, current_block_height))
    #                 else:
    #                     block_list.append(Block(screen, RED, 419, -current_block_height, current_block_height))
    #             block.set_y_pos(5)
    #             pygame.draw.line(screen, block.color, [block.get_x_pos(), block.get_y_pos()],
    #                              [block.get_x_pos(), block.get_y_pos() + block.get_height()], BLOCK_WIDTH)
    #
    #             pygame.display.flip()
    #             clock.tick(120)
    #             print(block.get_height())
    #
    # def move_block_list_left(self, screen, block_list):
    #     clock = pygame.time.Clock()
    #     while True:  # for i in range(130):
    #         for block in block_list:
    #             pygame.draw.line(screen, BLACK, [block.get_x_pos(), block.get_y_pos()],
    #                              [block.get_x_pos(), block.get_y_pos() + block.get_height()], BLOCK_WIDTH)
    #             if block_list[len(block_list) - 1].get_y_pos() == 0:
    #                 current_block_height = BLOCK_HEIGHT_LIST[random.randint(0, 5)]
    #                 if block_list[len(block_list) - 1].get_color() == RED:
    #                     block_list.append(Block(screen, YELLOW, 79, -current_block_height, current_block_height))
    #                 else:
    #                     block_list.append(Block(screen, RED, 79, -current_block_height, current_block_height))
    #             block.set_y_pos(5)
    #             pygame.draw.line(screen, block.color, [block.get_x_pos(), block.get_y_pos()],
    #                              [block.get_x_pos(), block.get_y_pos() + block.get_height()], BLOCK_WIDTH)
    #
    #             pygame.display.flip()
    #             clock.tick(120)
    #             print(block.get_height())

    def ending_game_screen(self):
        pass



