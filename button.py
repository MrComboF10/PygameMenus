import pygame


class Button:
    def __init__(self, position, size, font, font_color, screen_display):
        self._position = position
        self._size = size
        self._font = font
        self._font_color = font_color
        self._screen_display = screen_display

        self._mouse_over_button = False

        self._mouse_location_changed = False

    # set if mouse cursor was inside or outside button area
    def set_mouse_location_changed(self, change):
        self._mouse_location_changed = change

    # get if mouse is over button area
    def get_mouse_over_button(self):
        return self._mouse_over_button

    # get if mouse cursor was inside or outside button area
    def get_mouse_location_changed(self):
        return self._mouse_location_changed

    # verify if current mouse cursor is over button area
    def verify_mouse_on_button(self, current_mouse_position):
        self._mouse_over_button = False
        if self._position[0] < current_mouse_position[0] < self._position[0] + self._size[0]:
            if self._position[1] < current_mouse_position[1] < self._position[1] + self._size[1]:
                self._mouse_over_button = True

    # draw button on screen
    def draw_button(self, color, text):

        # draw button rectangle
        pygame.draw.rect(self._screen_display, color, (self._position[0], self._position[1], self._size[0], self._size[1]))

        # get font surface
        font_surface = self._font.render(text, True, self._font_color)

        # get rect font surface
        font_surface_rect = font_surface.get_rect()

        # move rect to center of button rectangle
        font_surface_rect.center = (self._position[0] + (self._size[0] // 2), self._position[1] + (self._size[1] // 2))

        # draw font surface on rectangle
        self._screen_display.blit(font_surface, font_surface_rect)


class PressButton(Button):
    def __init__(self, position, size, font, font_color, screen_display, mouse_out_button_color, mouse_over_button_color):

        super().__init__(position, size, font, font_color, screen_display)

        # self._position = super()._position
        # self._size = super()._size

        self._mouse_out_button_color = mouse_out_button_color
        self._mouse_over_button_color = mouse_over_button_color
        pass

    def draw_mouse_out_button(self, text):
        super().draw_button(self._mouse_out_button_color, text)

    def draw_mouse_over_button(self, text):
        super().draw_button(self._mouse_over_button_color, text)


class PressButtonRedirect(PressButton):
    def __init__(self, font, font_color, mouse_out_button_color, mouse_over_button_color, text, pointer, position=None, size=None, screen_display=None):

        super().__init__(position, size, font, font_color, screen_display, mouse_out_button_color, mouse_over_button_color)

        self.__text = text
        self.__pointer = pointer

        self.__pressed = False

    def set_position(self, new_position):
        self._position = new_position

    def set_size(self, new_size):
        self._size = new_size

    def set_screen_display(self, new_screen):
        self._screen_display = new_screen

    def get_pointer(self):
        return self.__pointer

    def get_pressed(self):
        return self.__pressed

    def press(self):
        self.__pressed = True

    def release(self):
        self.__pressed = False

    def draw_mouse_out_static_button(self):
        super().draw_mouse_out_button(self.__text)

    def draw_mouse_over_static_button(self):
        super().draw_mouse_over_button(self.__text)


class PressButtonChangeState(PressButton):
    def __init__(self, font, font_color, mouse_out_button_color, mouse_over_button_color, states_text_list, position=None, size=None, screen_display=None):

        super().__init__(position, size, font, font_color, screen_display, mouse_out_button_color, mouse_over_button_color)

        self.__states_text_list = states_text_list

        self.__current_state_text_index = 0

    def set_position(self, new_position):
        self._position = new_position

    def set_size(self, new_size):
        self._size = new_size

    def set_screen_display(self, new_screen):
        self._screen_display = new_screen

    def add_state_text_index(self):
        self.__current_state_text_index += 1
        self.__current_state_text_index = self.__current_state_text_index % len(self.__states_text_list)

    def draw_mouse_out_change_state_button(self):
        super().draw_mouse_out_button(self.__states_text_list[self.__current_state_text_index])

    def draw_mouse_over_change_state_button(self):
        super().draw_mouse_over_button(self.__states_text_list[self.__current_state_text_index])


class SlideButton(Button):
    def __init__(self, font, font_color, bar_width, range_items, mouse_out_bar_color, mouse_over_bar_color, button_color, position=None, size=None, screen_display=None):

        super().__init__(position, size, font, font_color, screen_display)

        self.__bar_width = bar_width
        self.__range_items = range_items
        self.__mouse_out_bar_color = mouse_out_bar_color
        self.__mouse_over_bar_color = mouse_over_bar_color
        self.__button_color = button_color

        self.__current_item = range_items[0]
        self.__current_bar_position = position
        self.__bar_pressed = False

    def set_position(self, new_position):
        self._position = new_position
        self.__current_bar_position = new_position

    def set_size(self, new_size):
        self._size = new_size

    def set_screen_display(self, new_screen):
        self._screen_display = new_screen

    def get_position(self):
        return self._position

    def get_size(self):
        return self._size

    def get_bar_is_pressed(self):
        return self.__bar_pressed

    def get_current_item(self):
        return self.__current_item

    def press_bar(self):
        self.__bar_pressed = True

    def release_bar(self):
        self.__bar_pressed = False

    def calculate_bar_position(self, current_mouse_position):
        if current_mouse_position[0] >= self._position[0] + self._size[0] - self.__bar_width // 2:
            self.__current_bar_position = (self._position[0] + self._size[0] - self.__bar_width, self._position[1])

        elif current_mouse_position[0] <= self._position[0] + self.__bar_width // 2:
            self.__current_bar_position = self._position

        else:
            self.__current_bar_position = (current_mouse_position[0] - self.__bar_width // 2, self._position[1])

    def calculate_current_item(self):
        self.__current_item = self.__range_items[int((self.__current_bar_position[0] - self._position[0]) * ((len(self.__range_items) - 1) / (self._size[0] - self.__bar_width)))]

    def draw_font_surface(self):
        # create font surface
        font_surface = self._font.render(str(self.__current_item), True, self._font_color)

        # get font surface rect
        font_surface_rect = font_surface.get_rect()

        # move rect to center of button
        font_surface_rect.center = (self._position[0] + self._size[0] // 2, self._position[1] + self._size[1] // 2)

        # draw font surface
        self._screen_display.blit(font_surface, font_surface_rect)

    def draw_mouse_over_slide_button(self):
        pygame.draw.rect(self._screen_display, self.__button_color, (self._position[0], self._position[1], self._size[0], self._size[1]))

        pygame.draw.rect(self._screen_display, self.__mouse_over_bar_color, (self.__current_bar_position[0], self.__current_bar_position[1], self.__bar_width, self._size[1]))

        self.draw_font_surface()

    def draw_mouse_out_slide_button(self):
        pygame.draw.rect(self._screen_display, self.__button_color, (self._position[0], self._position[1], self._size[0], self._size[1]))

        pygame.draw.rect(self._screen_display, self.__mouse_out_bar_color, (self.__current_bar_position[0], self.__current_bar_position[1], self.__bar_width, self._size[1]))

        self.draw_font_surface()
