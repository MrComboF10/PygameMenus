import pygame

class MainMenu:
    def __init__(self, screen_display, title, buttons_block):
        self.__screen_display = screen_display

        title.set_screen_display(screen_display)
        self.__title = title

        buttons_block.set_screen_display(screen_display)
        self.__buttons_block = buttons_block

    def get_title(self):
        return self.__title

    def get_block(self):
        return self.__buttons_block

