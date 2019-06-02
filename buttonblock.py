class Block:
    def __init__(self, size, buttons_matrix, vertical_margin, horizontal_margin, position=None, screen_display=None):
        self.__size = size
        self.__real_size = size
        self.__buttons_matrix = buttons_matrix
        self.__vertical_margin = vertical_margin
        self.__horizontal_margin = horizontal_margin
        self.__position = position
        self.__screen_display = screen_display

        # separate buttons by type
        self.__text_buttons = []
        self.__separate_buttons_type()

        # separate text buttons by type
        self.__press_buttons_redirect, self.__press_buttons_change_state, self.__slide_buttons = [], [], []
        self.__separate_text_buttons_type()

    def set_position(self, new_position):
        self.__position = new_position

    def set_screen_display(self, new_screen):
        self.__screen_display = new_screen

    def set_size(self, new_size):
        self.__size = new_size

    def set_real_size(self, new_real_size):
        self.__real_size = new_real_size
        self.__size = int(self.__real_size[0]), int(self.__real_size[1])

    def get_buttons(self):
        return self.get_press_buttons_redirect() + self.get_press_buttons_change_state() + self.get_slide_buttons()

    def get_text_buttons(self):
        return self.__text_buttons

    def get_press_buttons_redirect(self):
        return self.__press_buttons_redirect

    def get_press_buttons_change_state(self):
        return self.__press_buttons_change_state

    def get_slide_buttons(self):
        return self.__slide_buttons

    def get_size(self):
        return self.__size

    def get_real_size(self):
        return self.__real_size

    def get_position(self):
        return self.__position

    def __separate_buttons_type(self):
        for buttons_row in self.__buttons_matrix:
            for button in buttons_row:
                try:
                    button.get_font()
                except AttributeError:
                    pass
                else:
                    # store text button
                    self.__text_buttons.append(button)

    def __separate_text_buttons_type(self):
        for button in self.__text_buttons:
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

    def set_slide_buttons_bar_width(self, new_bar_width):
        for button in self.__slide_buttons:
            button.set_bar_width(new_bar_width)

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
                        button.update_bar_position()

                # move position to the right
                current_position = (current_position[0] + buttons_width + self.__horizontal_margin, current_position[1])

            # move position x to initial position
            current_position = (self.__position[0], current_position[1])

            # move position to down
            current_position = (current_position[0], current_position[1] + buttons_height + self.__vertical_margin)

