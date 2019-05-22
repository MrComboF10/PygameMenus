class MainMenu:
    def __init__(self, position, screen_display, title, buttons_block, margin):

        self.__position = position
        self.__screen_display = screen_display
        self.__margin = margin

        self.__title_size = title.get_size()
        self.__block_size = buttons_block.get_size()

        # configure title
        self.__title = title
        self.__set_title_position()
        self.__title.set_screen_display(screen_display)

        # configure buttons block
        self.__buttons_block = buttons_block
        self.__set_block_position()
        self.__buttons_block.set_screen_display(screen_display)

    def __set_title_position(self):
        if self.__title_size[0] > self.__block_size[0]:
            position = self.__position
        else:
            position = (self.__position[0] + self.__block_size[0] // 2 - self.__title_size[0] // 2, self.__position[1])

        self.__title.set_position(position)

    def __set_block_position(self):
        if self.__title_size[0] > self.__block_size[0]:
            position = (self.__position[0] + self.__title_size[0] // 2 - self.__block_size[0] // 2,
                        self.__position[1] + self.__title_size[1] + self.__margin)
        else:
            position = (self.__position[0], self.__position[1] + self.__title_size[1] + self.__margin)

        self.__buttons_block.set_position(position)

    def get_title(self):
        return self.__title

    def get_block(self):
        return self.__buttons_block
