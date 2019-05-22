class Title:
    def __init__(self, font, font_color, text, center_position, screen_display=None):
        self.__font = font
        self.__font_color = font_color
        self.__text = text
        self.__center_position = center_position
        self.__screen_display = screen_display

        self.__font_surface = font.render(text, True, font_color)
        self.__font_surface_rect = self.__font_surface.get_rect()

    def set_screen_display(self, new_screen):
        self.__screen_display = new_screen

    def set_font_surface_center(self):
        self.__font_surface_rect.center = self.__center_position

    def get_rect(self):
        return self.__font_surface_rect

    def draw(self):
        self.__screen_display.blit(self.__font_surface, self.__font_surface_rect)
