import pygame
from constants import *
from Player import *


def check_game_over(block_right, block_left, player_x_pos, player_y_pos, players_color):
    if player_x_pos == X_POS_RIGHTEST and ((block_right.get_y_pos() + block_right.get_height()) >= player_y_pos >= block_right.get_y_pos()):
        if players_color != block_right.get_color():
            return True
        else:
            return False
    if player_x_pos == X_POS_LEFTEST and ((block_left.get_y_pos() + block_left.get_height()) >= player_y_pos >= block_left.get_y_pos()):
        if players_color != block_left.get_color():
            return True
        else:
            return False
    else:
        return False


def click_home_button(home_button):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click_pos = event.pos
            if home_button.mouse_in_button(mouse_click_pos):
                return True



def click_question_mark(question_mark, mouse_click_pos):
    # for event in pygame.event.get():
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         mouse_click_pos = event.pos
            if question_mark.mouse_in_button(mouse_click_pos):
                return True
