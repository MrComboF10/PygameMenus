import pygame


class PressButtonChangeState:
    def __init__(self, pos, size, states_text_list, pressed_color, unpressed_color, font_color, screen_display):
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

    def get_current_mouse_position(self, mouse_position):
        self.__current_mouse_position = mouse_position

    def get_mouse_on_button(self):
        return self.__mouse_on_button

    def verify_mouse_on_button(self):
        left_position = self.__position[0]
        right_position = self.__position[0] + self.__size[0]
        up_position = self.__position[1]
        down_position = self.__position[1] + self.__size[1]

        if left_position < self.__current_mouse_position[0] < right_position:
            if up_position < self.__current_mouse_position[1] < down_position:
                self.__mouse_on_button = True

    def draw_button(self, color):

        # draw button rectangle
        pygame.draw.rect(self.__screen_display, color, [self.__position[0], self.__position[1], self.__size[0], self.__size[1]])

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

    def update_index(self):
        self.__current_state_text_index += 1
        self.__current_state_text_index = self.__current_state_text_index % len(self.__state_text_list)




