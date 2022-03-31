class Button:
    def __init__(self, x_pos, y_pos, width, height):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height

    def mouse_in_button(self, mouse_pos):
        if self.x_pos + self.width > mouse_pos[0] > self.x_pos and \
                self.y_pos < mouse_pos[1] < self.y_pos + self.height:
            return True
