
class Block:
    def __init__(self, color, x_pos, y_pos, height):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        self.height = height

    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos

    def get_color(self):
        return self.color

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def change_y_pos(self, change_y):
        self.y_pos += change_y

