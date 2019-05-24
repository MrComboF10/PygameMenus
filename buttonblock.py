class Block:
    def __init__(self, size, buttons, position=None, screen_display=None):
        self._position = position
        self._size = size
        self._screen_display = screen_display
        self._buttons = buttons

        # separate buttons by type
        self._press_buttons_static, self._press_buttons_change_state, self._slide_buttons = [], [], []
        self._separate_buttons_type()

    def set_position(self, new_position):
        self._position = new_position

    def set_screen_display(self, new_screen):
        self._screen_display = new_screen

    def _separate_buttons_type(self):
        for button in self._buttons:
            if type(button).__name__ == "PressButtonStatic":
                self._press_buttons_static.append(button)

            elif type(button).__name__ == "PressButtonChangeState":
                self._press_buttons_change_state.append(button)

            elif type(button).__name__ == "SlideButton":
                self._slide_buttons.append(button)

    def get_press_buttons_static(self):
        return self._press_buttons_static

    def get_press_buttons_change_state(self):
        return self._press_buttons_change_state

    def get_slide_buttons(self):
        return self._slide_buttons

    def get_size(self):
        return self._size


class BlockType1(Block):
    def __init__(self, size, buttons, margin, position=None, screen_display=None):

        super().__init__(size, buttons, position, screen_display)
        self.__margin = margin

        # calculate buttons sizes
        self.__buttons_sizes = None
        self.calculate_buttons_sizes()

    def calculate_buttons_sizes(self):
        self.__buttons_sizes = (self._size[0], (self._size[1] - self.__margin * (len(self._buttons) - 1)) // len(self._buttons))

    def update_buttons(self):
        # set buttons display, sizes and positions
        margin_counter = 0
        for button in self._buttons:
            button.set_position((self._position[0], self._position[1] + margin_counter))
            button.set_size(self.__buttons_sizes)
            button.set_screen_display(self._screen_display)
            margin_counter += self.__margin + self.__buttons_sizes[1]


class BlockType2(Block):
    def __init__(self, size, buttons, margin_height, margin_width, position=None, screen_display=None):
        super().__init__(size, buttons, position, screen_display)

        self.__margin_height = margin_height
        self.__margin_width = margin_width

        # calculate buttons sizes
        self.__buttons_sizes = None
        self.calculate_buttons_sizes()

    def calculate_buttons_sizes(self):
        self.__buttons_sizes = ((self._size[0] - self.__margin_width) // 2, (self._size[1] - self.__margin_height * (len(self._buttons) - 1)) // len(self._buttons))

    def update_buttons(self):
        # set buttons display, sizes and positions
        margin_height_counter = 0
        par = False
        for button in self._buttons:
            button.set_position(self.__calculate_position(par, margin_height_counter))
            button.set_size(self.__buttons_sizes)
            button.set_screen_display(self._screen_display)
            # update next line buttons
            if par:
                margin_height_counter += self.__margin_height + self.__buttons_sizes[1]
            par = not par

    def __calculate_position(self, par, margin_height_counter):
        if par:
            # left buttons
            return self._position[0], self._position[1] + margin_height_counter
        # right buttons
        return self._position[0] + self.__buttons_sizes[0] + self.__margin_width, self._position[1] + margin_height_counter
