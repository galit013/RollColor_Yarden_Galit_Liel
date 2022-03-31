import pygame
from constants import *


class Block:
    def __init__(self, screen, color, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        # img_path = BLOCK_PATH
        # img = pygame.image.load(BLOCK_PATH)
        # img = pygame.transform.scale(img, (BLOCK_WIDTH, BLOCK_HEIGHT))
        # screen.blit(img, (self.x_pos, self.y_pos))
        # self.block = img

    def get_color(self):
        return self.color

    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos

    def set_y_pos(self, change_y):
        self.y_pos += change_y

    def move_block(self, screen):
        clock = pygame.time.Clock()
        for i in range(50):
            pygame.draw.line(screen, BLACK, [self.get_x_pos(), self.get_y_pos()], [self.get_x_pos(), self.get_y_pos() + BLOCK_HEIGHT], BLOCK_WIDTH)
            self.set_y_pos(5)
            pygame.draw.line(screen, self.color, [self.get_x_pos(), self.get_y_pos()], [self.get_x_pos(), self.get_y_pos() + BLOCK_HEIGHT], BLOCK_WIDTH)
            pygame.display.flip()
            clock.tick(120)
            print(self.get_y_pos())

    # def set_x_pos(self, change_x):
    #     self.x_pos += change_x
