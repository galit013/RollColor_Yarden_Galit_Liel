
class Button:
    def __init__(self, x_pos, y_pos, width, height):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height

    def mouse_in_button(self, mouse_pos):
        """
            The function checks if a button was clicked based on mouse click position
            :param mouse_pos: The position of the mouse click.
            <mouse_pos> - tuple
            :return: True - if the button was clicked
                     False - if the button was not clicked
        """
        if self.x_pos + self.width > mouse_pos[0] > self.x_pos and \
                self.y_pos < mouse_pos[1] < self.y_pos + self.height:
            return True
        return False
