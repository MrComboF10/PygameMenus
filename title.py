class Title:
    def __init__(self, font, font_color, text, screen_display=None):
        self.__font = font
        self.__font_color = font_color
        self.__text = text
        self.__screen_display = screen_display

        self.__font_surface = font.get_font().render(text, True, font_color)
        self.__font_surface_rect = self.__font_surface.get_rect()

    def set_screen_display(self, new_screen):
        self.__screen_display = new_screen

    def set_position(self, new_position):
        self.__font_surface_rect.topleft = new_position

    def set_font_real_size(self, size):
        self.__font.set_real_size(size)
        self.__font.update()

    def get_font_real_size(self):
        return self.__font.get_real_size()

    def get_rect(self):
        return self.__font_surface_rect

    def get_size(self):
        return self.__font_surface_rect.size

    def update_title_text(self):
        self.__font_surface = self.__font.get_font().render(self.__text, True, self.__font_color)
        self.__font_surface_rect = self.__font_surface.get_rect()

    def draw(self):
        self.__screen_display.blit(self.__font_surface, self.__font_surface_rect)
