class Block:
    def __init__(self, size, buttons, margin, position=None, screen_display=None):
        self.__position = position
        self.__size = size
        self.__screen_display = screen_display
        self.__buttons = buttons
        self.__margin = margin

        # calculate buttons sizes
        self.__buttons_sizes = (size[0], (size[1] - margin * (len(buttons) - 1)) // len(buttons))

        # separate buttons by type
        self.__press_buttons_static, self.__press_buttons_change_state, self.__slide_buttons = [], [], []
        for button in self.__buttons:
            if type(button).__name__ == "PressButtonStatic":
                self.__press_buttons_static.append(button)

            elif type(button).__name__ == "PressButtonChangeState":
                self.__press_buttons_change_state.append(button)

            elif type(button).__name__ == "SlideButton":
                self.__slide_buttons.append(button)

    def set_position(self, new_position):
        self.__position = new_position

    def set_screen_display(self, new_screen):

        self.__screen_display = new_screen

        # set buttons sizes and positions
        margin_counter = 0
        for button in self.__buttons:
            button.set_position((self.__position[0], self.__position[1] + margin_counter))
            button.set_size(self.__buttons_sizes)
            button.set_screen_display(new_screen)
            margin_counter += self.__margin + self.__buttons_sizes[1]

    def get_press_buttons_static(self):
        return self.__press_buttons_static

    def get_press_buttons_change_state(self):
        return self.__press_buttons_change_state

    def get_slide_buttons(self):
        return self.__slide_buttons

    def get_size(self):
        return self.__size


