import pygame
from constants import *
from classes.Block import *
import random
from helpers import *
from os import path
import time


class App:
    def __init__(self, screen, score):
        self.screen = screen
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
            self.draw_text("NEW BEST SCORE!", BEST_SCORE_SIZE, WHITE, BEST_SCORE_WIDTH, BEST_SCORE_HEIGHT)
            with open(path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text("Best Score: " + str(self.high_score), BEST_SCORE_SIZE, WHITE, BEST_SCORE_WIDTH, NEW_BEST_SCORE_HEIGHT)

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

    def start_animation(self):
        """
            Displays the loading screen (animation).
            :return: None
        """
        # goes over all the images in animation folder (images)
        for image_number in range(AMOUNT_OF_LOADING_SCREENS):
            # animation sound
            animation_sound = pygame.mixer.Sound(ANIMATION_SOUND)
            pygame.mixer.Sound.play(animation_sound)
            # load img path
            current_img_path = LOADING_SCREEN_IMAGE_PATH + str(image_number + 1) + LOADING_SCREEN_PATH_EXTENSION
            # show current image
            show_img(self.screen, current_img_path, WINDOW_WIDTH, IMG_HEIGHT, IMG_X, IMG_Y)
            time.sleep(0.2)
            pygame.display.flip()
        # hide images
        show_img(self.screen, BACKGROUND, WINDOW_WIDTH, IMG_HEIGHT, IMG_X, IMG_Y)

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

    def draw_change_color(self, ball, change_color_ball):
        """
                 The function is moving the blocks on the screen
                 <block_list_right> - contains blocks - Block (class)
                 <block_list_left> - contains blocks - Block (class)
                 <y_pos_change> - int
                 <ball> - Player (class)
                 :return: None
        """
        # set color of the change_color_ball
        ball_color = ball.get_color()
        change_color = RED if ball_color == YELLOW else YELLOW
        change_color_ball.set_color(change_color)
        # set change_color_ball position
        ball_x = ball.get_x_pos()
        x_to_draw = X_POS_RIGHTEST if ball_x == X_POS_LEFTEST else X_POS_LEFTEST
        change_color_ball.set_x_pos(x_to_draw)
        # draw change_color_ball on the screen
        pygame.draw.circle(self.screen, change_color_ball.get_color(), (change_color_ball.get_x_pos(), Y_POS_START), 12)





