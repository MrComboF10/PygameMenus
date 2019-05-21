class Block:
    def __init__(self, position, size, buttons, margin):
        self.__position = position
        self.__size = size
        self.__buttons = buttons
        self.__margin = margin

        # calculate buttons sizes
        self.__buttons_sizes = (size[0], (size[1] - margin * (len(buttons) - 1)) // len(buttons))

        # set buttons sizes and positions
        margin_counter = 0
        for button in self.__buttons:
            button.set_position((position[0], position[1] + margin_counter))
            button.set_size(self.__buttons_sizes)
            margin_counter += margin + self.__buttons_sizes[1]

        # separate buttons by type
        self.__press_buttons_static, self.__press_buttons_change_state, self.__slide_buttons = [], [], []
        for button in self.__buttons:
            if type(button).__name__ == "PressButtonStatic":
                self.__press_buttons_static.append(button)

            elif type(button).__name__ == "PressButtonChangeState":
                self.__press_buttons_change_state.append(button)

            elif type(button).__name__ == "SlideButton":
                self.__slide_buttons.append(button)

    def get_press_buttons_static(self):
        return self.__press_buttons_static

    def get_press_buttons_change_state(self):
        return self.__press_buttons_change_state

    def get_slide_buttons(self):
        return self.__slide_buttons


