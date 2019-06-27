import pygame


class Font:
    def __init__(self, name, size, bold=False, italic=False):
        self.__name = name
        self.__size = size
        self.__real_size = size
        self.__bold = bold
        self.__italic = italic
        self.__font = pygame.font.SysFont(self.__name, self.__size, self.__bold, self.__italic)

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def get_real_size(self):
        return self.__real_size

    def get_bold(self):
        return self.__bold

    def get_italic(self):
        return self.__italic

    def get_font(self):
        return self.__font

    def set_name(self, name):
        self.__name = name

    def set_size(self, size):
        self.__size = size

    def set_real_size(self, new_real_size):
        self.__real_size = new_real_size

    def set_bold(self, bold):
        self.__bold = bold

    def set_italic(self, italic):
        self.__italic = italic

    def update(self):
        self.__size = int(self.__real_size)
        self.__font = pygame.font.SysFont(self.__name, self.__size, self.__bold, self.__italic)

