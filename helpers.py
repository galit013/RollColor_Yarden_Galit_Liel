from classes.Player import *


def check_game_over(block_right, block_left, player_x_pos, player_y_pos, players_color):
    """
        The function checks if the game is over
        <block_right> - Block (class)
        <block_left> - Block (class)
        <player_x_pos> - int
        <player_y_pos> - int
        <players_color> - tuple
        :return: True - if the game is over
                False - if the game is not over
    """
    # check if the ball touches the current block on the right side
    if player_x_pos == X_POS_RIGHTEST and ((block_right.get_y_pos() + block_right.get_height()) >= player_y_pos >= block_right.get_y_pos()):
        # check if the color of the ball is different than the color of the current block
        if players_color != block_right.get_color():
            return True
        else:
            return False
    # check if the ball touches the current block on the left side
    if player_x_pos == X_POS_LEFTEST and ((block_left.get_y_pos() + block_left.get_height()) >= player_y_pos >= block_left.get_y_pos()):
        # check if the color of the ball is different than the color of the current block
        if players_color != block_left.get_color():
            return True
        else:
            return False
    else:
        return False


def click_home_button(home_button):
    """
        The function checks if the home button was clicked based on mouse click events
        <home_button> - Button (class)
        :return: True - if the home button was clicked
                 False - if the home button was not clicked
    """
    # Going through all the events that happened
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # checks if the user pressed the mouse button
            mouse_click_pos = event.pos
            # check if the button was clicked
            if home_button.mouse_in_button(mouse_click_pos):
                return True


def show_img(screen, img_path, img_width, img_height, img_x_pos, img_y_pos):
    """
        The function loads an image and shows it on the screen
        <img_path> - string
        <img_width> - int
        <img_height> - int
        <img_x_pos> - int
        <img_y_pos> - int
        :return: None
    """
    img = pygame.image.load(img_path)
    img = pygame.transform.scale(img, (img_width, img_height))
    screen.blit(img, (img_x_pos, img_y_pos))


def show_text(screen, font, text, color, text_x_pos, text_y_pos):
    """
        The function shows text on the screen
        <font> - pygame.font.Font (class)
        <text> - string
        <color> - tuple
        <text_x_pos> - int
        <text_y_pos> - int
        :return: None
    """
    screen.blit(font.render(text, True, color), (text_x_pos, text_y_pos))

def change_players_color(ball):
    print("kk")
    if ball.get_color() == RED:
        ball.set_color(YELLOW)
    else:
        ball.set_color(RED)



