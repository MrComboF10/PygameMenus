class Block:
    def __init__(self, size, buttons_matrix, vertical_margin, horizontal_margin, position=None, screen_display=None):
        self.__real_size = size
        self.__buttons_matrix = buttons_matrix
        self.__real_vertical_margin = vertical_margin
        self.__real_horizontal_margin = horizontal_margin
        self.__real_position = position
        self.__screen_display = screen_display

        # separate buttons by type
        self.__text_buttons = []
        self.__separate_buttons_type()

        # separate text buttons by type
        self.__press_buttons_redirect, self.__press_buttons_change_state, self.__slide_buttons = [], [], []
        self.__separate_text_buttons_type()

    def set_real_position(self, new_position):
        self.__real_position = new_position

    def set_screen_display(self, new_screen):
        self.__screen_display = new_screen

    def set_real_size(self, new_real_size):
        self.__real_size = new_real_size

    def set_real_vertical_margin(self, new_real_vertical_margin):
        self.__real_vertical_margin = new_real_vertical_margin

    def set_real_horizontal_margin(self, new_real_horizontal_margin):
        self.__real_horizontal_margin = new_real_horizontal_margin

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

    def get_real_size(self):
        return self.__real_size

    def get_real_position(self):
        return self.__real_position

    def get_real_vertical_margin(self):
        return self.__real_vertical_margin

    def get_real_horizontal_margin(self):
        return self.__real_horizontal_margin

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

    def __calculate_buttons_real_width_current_row(self, current_buttons_row):
        return (self.__real_size[0] - self.__real_horizontal_margin * (len(current_buttons_row) - 1)) / len(current_buttons_row)

    def __calculate_buttons_real_height(self):
        return (self.__real_size[1] - self.__real_vertical_margin * (len(self.__buttons_matrix) - 1)) / len(self.__buttons_matrix)

    def set_slide_buttons_bar_width(self, new_bar_real_width):
        for button in self.__slide_buttons:
            button.set_bar_real_width(new_bar_real_width)

    # set buttons new position, size and screen display
    def update_buttons_appearance_in_block(self):

        current_real_position = self.__real_position

        # get height of all buttons
        buttons_real_height = self.__calculate_buttons_real_height()

        for row_buttons in self.__buttons_matrix:

            # get width of all buttons in the row
            buttons_real_width = self.__calculate_buttons_real_width_current_row(row_buttons)

            for button in row_buttons:
                if button is not None:
                    button.set_real_position(current_real_position)
                    button.set_real_size((buttons_real_width, buttons_real_height))
                    button.set_screen_display(self.__screen_display)
                    button.update_real_width()

                    # when slide button position is changed we have to update bar position
                    if type(button).__name__ == "SlideButton":
                        button.update_bar_position()

                # move position to the right
                current_real_position = (current_real_position[0] + buttons_real_width + self.__real_horizontal_margin, current_real_position[1])

            # move position x to initial position
            current_real_position = (self.__real_position[0], current_real_position[1])

            # move position to down
            current_real_position = (current_real_position[0], current_real_position[1] + buttons_real_height + self.__real_vertical_margin)

