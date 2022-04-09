import pygame
from constants import *
from Player import *
from Block import *
import random
from helpers import *


class App:
    def __init__(self, screen):
        self.screen = screen
        self.curr_screen = None
        self.start_display()
        self.game_over = False

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

    def move_blocks(self, screen, block_list_right, block_list_left, change_y_pos, ball, score):
        clock = pygame.time.Clock()
        game_over = False
        while not self.game_over:
            for i in range(len(block_list_left)):
                if check_game_over(block_list_right[i], block_list_left[i], ball.get_x_pos(), ball.get_y_pos(), ball.get_color()):
                    print("over")
                    # self.ending_game_screen(score)
                    self.game_over = True

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
                block_list_left[i].set_y_pos(change_y_pos)
                block_list_right[i].set_y_pos(change_y_pos)
                pygame.draw.line(screen, block_list_right[i].color, [block_list_right[i].get_x_pos(), block_list_right[i].get_y_pos()],
                                 [block_list_right[i].get_x_pos(), block_list_right[i].get_y_pos() + block_list_right[i].get_height()], BLOCK_WIDTH)
                pygame.draw.line(screen, block_list_left[i].color, [block_list_left[i].get_x_pos(), block_list_left[i].get_y_pos()],
                                 [block_list_left[i].get_x_pos(), block_list_left[i].get_y_pos() + block_list_left[i].get_height()], BLOCK_WIDTH)


                pygame.display.flip()
                clock.tick(50)
            # return game_over


    # def ending_game_screen(self, score):
    #     pass
        # # Set up the game display, clock and headline
        # pygame.init()
        # # Create the screen and show it
        # game_over_screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        # game_over_screen = pygame.display.set_mode(game_over_screen_size)
        # img = pygame.image.load(GAME_OVER)
        # img = pygame.transform.scale(img, (GAME_OVER_WIDTH, GAME_OVER_HEIGHT))
        # self.screen.blit(img, (GAME_OVER_X_POS, GAME_OVER_Y_POS))
        #
        # img = pygame.image.load(HOME_BUTTON)
        # img = pygame.transform.scale(img, (HOME_BUTTON_WIDTH, HOME_BUTTON_HEIGHT))
        # self.screen.blit(img, (HOME_BUTTON_X_POS, HOME_BUTTON_Y_POS))
        #
        # img = pygame.image.load(BACKGROUND)
        # img = pygame.transform.scale(img, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT))
        # self.screen.blit(img, (BACKGROUND_X_POS, BACKGROUND_Y_POS))
        #
        # score_font = pygame.font.SysFont(SCORE_FONT, SCORE_FONT_SIZE)
        # self.screen.blit(score_font.render("SCORE:" + str(score), True, WHITE), (200, 400))












