import pygame
from constants import *
from classes.Player import *
from classes.Block import *
import random
from helpers import *
from os import path


class App:
    def __init__(self, screen, ball, score):
        self.screen = screen
        self.start_display(ball)
        self.game_over = False
        self.score = score
        self.font_name = pygame.font.match_font("ariel")
        self.load_data()

    def load_data(self):
        """
            The function loads the high score from data base and shows it on the screen
            :return: None
        """
        # load high score
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, HS_FILE), 'r') as f:
            try:
                self.high_score = int(f.read())
            except:
                self.high_score = 0
        # change high score if needed and show it on the screen
        if self.score > self.high_score:
            self.high_score = self.score
            self.draw_text("NEW HIGH SCORE!", 22, WHITE, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 40)
            with open(path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text("High Score: " + str(self.high_score), 22, WHITE, WINDOW_WIDTH / 2, 30)

    def draw_text(self, text, size, color, x, y):
        """
            The function shows text from data base on the screen
            <text> - string
            <size> - int
            <color> - tuple
            <x> - int
            <ty> - int
            :return: None
        """
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

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
                if check_game_over(block_list_right[i], block_list_left[i], ball.get_x_pos(), ball.get_y_pos(),
                                   ball.get_color()):
                    self.game_over = True
                # hide this block
                pygame.draw.line(screen, BLACK, [block_list_left[i].get_x_pos(), block_list_left[i].get_y_pos()],
                                 [block_list_left[i].get_x_pos(),
                                  block_list_left[i].get_y_pos() + block_list_left[i].get_height()], BLOCK_WIDTH)
                pygame.draw.line(screen, BLACK, [block_list_right[i].get_x_pos(), block_list_right[i].get_y_pos()],
                                 [block_list_right[i].get_x_pos(),
                                  block_list_right[i].get_y_pos() + block_list_right[i].get_height()], BLOCK_WIDTH)
                # check if the block moved through the whole screen
                if block_list_right[len(block_list_right) - 1].get_y_pos() == 0:
                    current_block_height = BLOCK_HEIGHT_LIST[random.randint(0, 5)]
                    # add to the lists new blocks
                    if block_list_right[len(block_list_right) - 1].get_color() == RED:
                        block_list_right.append(
                            Block(YELLOW, X_POS_RIGHT_BLOCK, -current_block_height, current_block_height))
                        block_list_left.append(
                            Block(RED, X_POS_LEFT_BLOCK, -current_block_height, current_block_height))
                    else:
                        block_list_right.append(
                            Block(RED, X_POS_RIGHT_BLOCK, -current_block_height, current_block_height))
                        block_list_left.append(
                            Block(YELLOW, X_POS_LEFT_BLOCK, -current_block_height, current_block_height))
                # change blocks position
                block_list_left[i].change_y_pos(y_pos_to_change)
                block_list_right[i].change_y_pos(y_pos_to_change)
                # draw new blocks in the new position
                pygame.draw.line(screen, block_list_right[i].color,
                                 [block_list_right[i].get_x_pos(), block_list_right[i].get_y_pos()],
                                 [block_list_right[i].get_x_pos(),
                                  block_list_right[i].get_y_pos() + block_list_right[i].get_height()], BLOCK_WIDTH)
                pygame.draw.line(screen, block_list_left[i].color,
                                 [block_list_left[i].get_x_pos(), block_list_left[i].get_y_pos()],
                                 [block_list_left[i].get_x_pos(),
                                  block_list_left[i].get_y_pos() + block_list_left[i].get_height()], BLOCK_WIDTH)
                # update the screen
                pygame.display.flip()
                clock.tick(50)

    def get_high_score(self):
        return self.high_score

    def set_high_score(self, high_score):
        self.high_score = high_score

