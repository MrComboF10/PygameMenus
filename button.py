import pygame


class PressButtonStatic:
    def __init__(self, pos, size, text, unpressed_color, pressed_color, font_color, screen_display):
        self.__position = pos
        self.__size = size
        self.__text = text
        self.__pressed_color = pressed_color
        self.__unpressed_color = unpressed_color
        self.__screen_display = screen_display
        self.__font_color = font_color

        self.__font = pygame.font.SysFont("Arial", 25)
        self.__current_mouse_position = (0, 0)
        self.__mouse_on_button = False
        self.__mouse_location_changed = False

    def insert_current_mouse_position(self, mouse_position):
        self.__current_mouse_position = mouse_position

    def get_mouse_on_button(self):
        return self.__mouse_on_button

    def get_mouse_location_changed(self):
        return self.__mouse_location_changed

    def insert_mouse_location_changed(self, changed):
        self.__mouse_location_changed = changed

    def verify_mouse_on_button(self):
        self.__mouse_on_button = False
        left_position = self.__position[0]
        right_position = self.__position[0] + self.__size[0]
        up_position = self.__position[1]
        down_position = self.__position[1] + self.__size[1]

        if left_position < self.__current_mouse_position[0] < right_position and up_position < self.__current_mouse_position[1] < down_position:
            self.__mouse_on_button = True

    def draw_button(self, color):

        # draw button rectangle
        pygame.draw.rect(self.__screen_display, color, (self.__position[0], self.__position[1], self.__size[0], self.__size[1]))

        # get font surface
        font_surface = self.__font.render(self.__text, True, self.__font_color)

        # get rect font surface
        font_surface_rect = font_surface.get_rect()

        # move rect to center of button rectangle
        font_surface_rect.center = (self.__position[0] + (self.__size[0] // 2), self.__position[1] + (self.__size[1] // 2))

        # draw font surface on rectangle
        self.__screen_display.blit(font_surface, font_surface_rect)

    def draw_unpressed_button(self):
        self.draw_button(self.__unpressed_color)

    def draw_pressed_button(self):
        self.draw_button(self.__pressed_color)


########################################################################################################################


class PressButtonChangeState:
    def __init__(self, pos, size, states_text_list, unpressed_color, pressed_color, font_color, screen_display):
        # up left corner position
        self.__position = pos

        self.__size = size
        self.__state_text_list = states_text_list
        self.__pressed_color = pressed_color
        self.__unpressed_color = unpressed_color
        self.__screen_display = screen_display
        self.__font_color = font_color

        self.__font = pygame.font.SysFont("Arial", 25)
        self.__current_mouse_position = (0, 0)
        self.__current_state_text_index = 0
        self.__mouse_on_button = False
        self.__mouse_location_changed = False

    def insert_current_mouse_position(self, mouse_position):
        self.__current_mouse_position = mouse_position

    def get_mouse_on_button(self):
        return self.__mouse_on_button

    def get_text_index(self):
        return self.__current_state_text_index

    def get_mouse_location_changed(self):
        return self.__mouse_location_changed

    def insert_mouse_location_changed(self, changed):
        self.__mouse_location_changed = changed

    def verify_mouse_on_button(self):
        self.__mouse_on_button = False
        left_position = self.__position[0]
        right_position = self.__position[0] + self.__size[0]
        up_position = self.__position[1]
        down_position = self.__position[1] + self.__size[1]

        if left_position < self.__current_mouse_position[0] < right_position and up_position < self.__current_mouse_position[1] < down_position:
            self.__mouse_on_button = True

    def draw_button(self, color):

        # draw button rectangle
        pygame.draw.rect(self.__screen_display, color, (self.__position[0], self.__position[1], self.__size[0], self.__size[1]))

        # get font surface
        current_state_text = self.__state_text_list[self.__current_state_text_index]
        font_surface = self.__font.render(current_state_text, True, self.__font_color)

        # get rect font surface
        font_surface_rect = font_surface.get_rect()

        # move rect to center of button rectangle
        font_surface_rect.center = (self.__position[0] + (self.__size[0] // 2), self.__position[1] + (self.__size[1] // 2))

        # draw font surface on rectangle
        self.__screen_display.blit(font_surface, font_surface_rect)

    def draw_unpressed_button(self):
        self.draw_button(self.__unpressed_color)

    def draw_pressed_button(self):
        self.draw_button(self.__pressed_color)

    def add_state_text_index(self):
        self.__current_state_text_index += 1
        self.__current_state_text_index = self.__current_state_text_index % len(self.__state_text_list)


########################################################################################################################


class SlideButton:
    def __init__(self, pos, size, bar_width, range_items, font_color, bar_unpressed_color, bar_pressed_color, button_color, screen_display):
        self.__position = pos
        self.__size = size
        self.__bar_width = bar_width
        self.__range_items = range_items
        self.__font_color = font_color
        self.__bar_unpressed_color = bar_unpressed_color
        self.__bar_pressed_color = bar_pressed_color
        self.__button_color = button_color
        self.__screen_display = screen_display

        self.__current_item = range_items[0]
        self.__font = pygame.font.SysFont("Arial", 25)
        self.__current_mouse_position = (0, 0)
        self.__current_bar_position = pos
        self.__mouse_on_button = False
        self.__bar_pressed = False
        self.__mouse_location_changed = False

    def get_bar_is_pressed(self):
        return self.__bar_pressed

    def get_mouse_on_button(self):
        return self.__mouse_on_button

    def get_mouse_location_changed(self):
        return self.__mouse_location_changed

    def get_current_item(self):
        return self.__current_item

    def insert_current_mouse_position(self, mouse_position):
        self.__current_mouse_position = mouse_position

    def insert_bar_is_pressed(self, pressed):
        self.__bar_pressed = pressed

    def insert_mouse_location_changed(self, changed):
        self.__mouse_location_changed = changed

    def verify_mouse_on_button(self):
        self.__mouse_on_button = False
        if self.__position[0] < self.__current_mouse_position[0] < self.__position[0] + self.__size[0]:
            if self.__position[1] < self.__current_mouse_position[1] < self.__position[1] + self.__size[1]:
                self.__mouse_on_button = True

    def calculate_bar_position(self):
        if self.__current_mouse_position[0] > self.__position[0] + self.__size[0] - self.__bar_width:
            self.__current_bar_position = (self.__position[0] + self.__size[0] - self.__bar_width, self.__position[1])

        elif self.__current_mouse_position[0] < self.__position[0]:
            self.__current_bar_position = self.__position

        else:
            self.__current_bar_position = (self.__current_mouse_position[0], self.__position[1])

    def calculate_current_item(self):
        self.__current_item = self.__range_items[int((self.__current_bar_position[0] - self.__position[0]) * ((len(self.__range_items) - 1) / (self.__size[0] - self.__bar_width)))]
        # self.__current_item = self.__current_bar_position[0] - self.__position[0]
        # self.__current_item = len(self.__range_items) // self.__size[0]

    def draw_font_surface(self):
        # create font surface
        font_surface = self.__font.render(str(self.__current_item), True, self.__font_color)

        # get font surface rect
        font_surface_rect = font_surface.get_rect()

        # move rect to center of button
        font_surface_rect.center = (self.__position[0] + self.__size[0] // 2, self.__position[1] + self.__size[1] // 2)

        # draw font surface
        self.__screen_display.blit(font_surface, font_surface_rect)

    def draw_mouse_on_button(self):
        pygame.draw.rect(self.__screen_display, self.__button_color, (self.__position[0], self.__position[1], self.__size[0], self.__size[1]))

        pygame.draw.rect(self.__screen_display, self.__bar_pressed_color, (self.__current_bar_position[0], self.__current_bar_position[1], self.__bar_width, self.__size[1]))

        self.draw_font_surface()

    def draw_mouse_out_button(self):
        pygame.draw.rect(self.__screen_display, self.__button_color, (self.__position[0], self.__position[1], self.__size[0], self.__size[1]))

        pygame.draw.rect(self.__screen_display, self.__bar_unpressed_color, (self.__current_bar_position[0], self.__current_bar_position[1], self.__bar_width, self.__size[1]))

        self.draw_font_surface()








