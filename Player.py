import pygame
from constants import *

class Player:
    def __init__(self, screen):
        self.x_pos = X_POS_START
        self.y_pos = Y_POS_START
        self.color = RED
        # img_path = BALL_PATH
        # img = pygame.image.load(img_path)
        # img = pygame.transform.scale(img, (BALL_WIDTH, BALL_HEIGHT))
        # screen.blit(img, (self.x_pos, self.y_pos))
        # self.player = img

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos

    def set_x_pos(self, change_x):
        self.x_pos += change_x

    def move_player(self, screen, direction):
        clock = pygame.time.Clock()
        loop_times = 0
        if direction == "left":
            x_pos_change = X_POS_CHANGE_LEFT
            if self.get_x_pos() == X_POS_LEFTEST:
                loop_times = CANT_MOVE_LOOP_TIMES
            elif self.get_x_pos() == X_POS_START:
                loop_times = START_MOVE_LEFT_LOOP_TIMES
            else:
                loop_times = MOVE_LOOP_TIMES
        elif direction == "right":
            x_pos_change = X_POS_CHANGE_RIGHT
            if self.get_x_pos() == X_POS_RIGHTEST:
                loop_times = CANT_MOVE_LOOP_TIMES
            elif self.get_x_pos() == X_POS_START:
                loop_times = START_MOVE_RIGHT_LOOP_TIMES
            else:
                loop_times = MOVE_LOOP_TIMES
        for i in range(loop_times):
            pygame.draw.circle(screen, BLACK, (self.get_x_pos(), self.get_y_pos()), RADIUS)
            self.set_x_pos(x_pos_change)
            pygame.draw.circle(screen, self.get_color(), (self.get_x_pos(), self.get_y_pos()), RADIUS)
            pygame.display.flip()
            clock.tick(120)

    # def move_player_left(self, screen):
    #     clock = pygame.time.Clock()
    #     if self.get_x_pos() == X_POS_LEFTEST:
    #         loop_times = CANT_MOVE_LOOP_TIMES
    #     elif self.get_x_pos() == X_POS_START:
    #         loop_times = START_MOVE_LEFT_LOOP_TIMES
    #     else:
    #         loop_times = MOVE_LOOP_TIMES
    #     for i in range(loop_times):
    #         pygame.draw.circle(screen, BLACK, (self.get_x_pos(), self.get_y_pos()), RADIUS)
    #         self.set_x_pos(X_POS_CHANGE_LEFT)
    #         pygame.draw.circle(screen, self.get_color(), (self.get_x_pos(), self.get_y_pos()), RADIUS)
    #         pygame.display.flip()
    #         clock.tick(120)
    #
    # def move_player_right(self, screen):
    #     clock = pygame.time.Clock()
    #     if self.get_x_pos() == X_POS_RIGHTEST:
    #         loop_times = CANT_MOVE_LOOP_TIMES
    #     elif self.get_x_pos() == X_POS_START:
    #         loop_times = START_MOVE_RIGHT_LOOP_TIMES
    #     else:
    #         loop_times = MOVE_LOOP_TIMES
    #     for i in range(loop_times):
    #         pygame.draw.circle(screen, BLACK, (self.get_x_pos(), self.get_y_pos()), RADIUS)
    #         self.set_x_pos(X_POS_CHANGE_RIGHT)
    #         pygame.draw.circle(screen, self.get_color(), (self.get_x_pos(), self.get_y_pos()), RADIUS)
    #         pygame.display.flip()
    #         clock.tick(120)
    #
    #



