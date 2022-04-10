import pygame
from constants import *
from classes.Player import *
from classes.Block import *
import random
from helpers import *


class App:
    def __init__(self, screen, ball):
        self.screen = screen
        self.start_display(ball)
        self.game_over = False

    def start_display(self, ball):
        """
            The function loads the main screen
            <ball> - Player (class)
            :return: None
        """
        pygame.draw.circle(self.screen, ball.get_color(), (ball.get_x_pos(), ball.get_y_pos()), RADIUS)

    def game_screen(self, screen, block_list):
        """
            The function loads the game screen (draw blocks)
            <block_list> - contains blocks - Block (class)
            :return: None
        """
        for block in block_list:
            pygame.draw.line(screen, block.get_color(), [block.get_x_pos(), block.get_y_pos()],
                             [block.get_x_pos(), block.get_y_pos() + block.get_height()], BLOCK_WIDTH)

    def move_blocks(self, screen, block_list_right, block_list_left, y_pos_to_change, ball):
        """
            The function is moving the blocks on the screen
            <block_list_right> - contains blocks - Block (class)
            <block_list_left> - contains blocks - Block (class)
            <y_pos_change> - int
            <ball> - Player (class)
            :return: None
        """
        clock = pygame.time.Clock()
        # move blocks loop
        while not self.game_over:
            # goes over every block in the block lists
            for i in range(len(block_list_left)):
                # checks if the game is over
                if check_game_over(block_list_right[i], block_list_left[i], ball.get_x_pos(), ball.get_y_pos(), ball.get_color()):
                    self.game_over = True
                # hide this block
                pygame.draw.line(screen, BLACK, [block_list_left[i].get_x_pos(), block_list_left[i].get_y_pos()],
                                 [block_list_left[i].get_x_pos(), block_list_left[i].get_y_pos() + block_list_left[i].get_height()], BLOCK_WIDTH)
                pygame.draw.line(screen, BLACK, [block_list_right[i].get_x_pos(), block_list_right[i].get_y_pos()],
                                 [block_list_right[i].get_x_pos(), block_list_right[i].get_y_pos() + block_list_right[i].get_height()], BLOCK_WIDTH)
                # check if the block moved through the whole screen
                if block_list_right[len(block_list_right) - 1].get_y_pos() == 0:
                    current_block_height = BLOCK_HEIGHT_LIST[random.randint(0, 5)]
                    # add to the lists new blocks
                    if block_list_right[len(block_list_right) - 1].get_color() == RED:
                        block_list_right.append(Block(YELLOW, X_POS_RIGHT_BLOCK, -current_block_height, current_block_height))
                        block_list_left.append(Block(RED, X_POS_LEFT_BLOCK, -current_block_height, current_block_height))
                    else:
                        block_list_right.append(Block(RED, X_POS_RIGHT_BLOCK, -current_block_height, current_block_height))
                        block_list_left.append(Block(YELLOW, X_POS_LEFT_BLOCK, -current_block_height, current_block_height))
                # change blocks position
                block_list_left[i].change_y_pos(y_pos_to_change)
                block_list_right[i].change_y_pos(y_pos_to_change)
                # draw new blocks in the new position
                pygame.draw.line(screen, block_list_right[i].color, [block_list_right[i].get_x_pos(), block_list_right[i].get_y_pos()],
                                 [block_list_right[i].get_x_pos(), block_list_right[i].get_y_pos() + block_list_right[i].get_height()], BLOCK_WIDTH)
                pygame.draw.line(screen, block_list_left[i].color, [block_list_left[i].get_x_pos(), block_list_left[i].get_y_pos()],
                                 [block_list_left[i].get_x_pos(), block_list_left[i].get_y_pos() + block_list_left[i].get_height()], BLOCK_WIDTH)
                # update the screen
                pygame.display.flip()
                clock.tick(50)




















