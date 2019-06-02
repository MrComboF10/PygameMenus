class Block:
    def __init__(self, size, buttons_matrix, vertical_margin, horizontal_margin, position=None, screen_display=None):
        self.__size = size
        self.__buttons_matrix = buttons_matrix
        self.__vertical_margin = vertical_margin
        self.__horizontal_margin = horizontal_margin
        self.__position = position
        self.__screen_display = screen_display

        # separate buttons by type
        self.__press_buttons_redirect, self.__press_buttons_change_state, self.__slide_buttons = [], [], []
        self.__separate_buttons_type()

    def set_position(self, new_position):
        self.__position = new_position

    def set_screen_display(self, new_screen):
        self.__screen_display = new_screen

    def set_size(self, new_size):
        self.__size = new_size

    def get_press_buttons_redirect(self):
        return self.__press_buttons_redirect

    def get_press_buttons_change_state(self):
        return self.__press_buttons_change_state

    def get_slide_buttons(self):
        return self.__slide_buttons

    def get_size(self):
        return self.__size

    def get_position(self):
        return self.__position

    # this function is used in menu loop to update each list of buttons by type on screen
    def __separate_buttons_type(self):

        # store buttons by type
        for buttons_row in self.__buttons_matrix:
            for button in buttons_row:
                if type(button).__name__ == "PressButtonRedirect":
                    self.__press_buttons_redirect.append(button)

                elif type(button).__name__ == "PressButtonChangeState":
                    self.__press_buttons_change_state.append(button)

                elif type(button).__name__ == "SlideButton":
                    self.__slide_buttons.append(button)

    def __calculate_buttons_width_current_row(self, current_buttons_row):
        return (self.__size[0] - self.__horizontal_margin * (len(current_buttons_row) - 1)) // len(
            current_buttons_row)

    def __calculate_buttons_height(self):
        return (self.__size[1] - self.__vertical_margin * (len(self.__buttons_matrix) - 1)) // len(
            self.__buttons_matrix)

    def set_buttons_font_size(self, font_size):
        for row_buttons in self.__buttons_matrix:
            for button in row_buttons:
                button.set_font_size(font_size)

    # set buttons new position, size and screen display
    def update_buttons_appearance_in_block(self):
        current_position = self.__position

        # get height of all buttons
        buttons_height = self.__calculate_buttons_height()

        for row_buttons in self.__buttons_matrix:

            # get width of all buttons in the row
            buttons_width = self.__calculate_buttons_width_current_row(row_buttons)

            for button in row_buttons:
                if button is not None:
                    button.set_position(current_position)
                    button.set_size((buttons_width, buttons_height))
                    button.set_screen_display(self.__screen_display)

                    # when slide button position is changed we have to update bar position
                    if type(button).__name__ == "SlideButton":
                        button.calculate_bar_width()
                        button.update_bar_position()

                # move position to the right
                current_position = (current_position[0] + buttons_width + self.__horizontal_margin, current_position[1])

            # move position x to initial position
            current_position = (self.__position[0], current_position[1])

            # move position to down
            current_position = (current_position[0], current_position[1] + buttons_height + self.__vertical_margin)

