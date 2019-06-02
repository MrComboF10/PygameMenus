import pygame

white = (255, 255, 255)


class MainMenu:
    def __init__(self, screen_display, title, buttons_block, title_block_margin, max_menu_size_ratio, resize_ratio):

        self.__screen_display = screen_display
        self.__title_block_margin = title_block_margin
        self.__title_block_real_margin = title_block_margin
        self.__max_menu_size_ratio = max_menu_size_ratio
        self.__max_menu_size = self.__calculate_max_menu_size()
        self.__resize_ratio = resize_ratio
        self.__title = title
        self.__buttons_block = buttons_block

        self.__menu_size = None

        self.__position = None

        # set menu position in screen
        self.__calculate_size()
        self.__set_position(self.__calculate_position((screen_display.get_rect()[2], screen_display.get_rect()[3])))

        # initial mouse position
        self.__current_mouse_position = (0, 0)
        self.__current_event = None
        self.__mouse_left_pressed = None

        # verify if the user released bar when the mouse is outside slide button
        self.__release_slide_button_bar = True

        # verify if menu is bigger max menu size
        self.__menu_too_big = False

        # verify if menu can grow
        self.__menu_too_small = False

        # configure title
        self.__configure_title()

        # configure buttons block
        self.__configure_buttons_block()

    def __set_position(self, position):
        self.__position = position

    def __set_title_position(self):
        if self.__title.get_size()[0] > self.__buttons_block.get_size()[0]:
            position = self.__position
        else:
            position = (self.__position[0] + self.__buttons_block.get_size()[0] // 2 - self.__title.get_size()[0] // 2, self.__position[1])

        self.__title.set_position(position)

    def __configure_title(self):
        self.__set_title_position()
        self.__title.set_screen_display(self.__screen_display)
        self.__title.update_title_text()

    def __configure_buttons_block(self):
        self.__set_block_position()
        self.__buttons_block.set_screen_display(self.__screen_display)
        self.__buttons_block.update_buttons_appearance_in_block()

    def __set_block_position(self):
        if self.__title.get_size()[0] > self.__buttons_block.get_size()[0]:
            position = (self.__position[0] + self.__title.get_size()[0] // 2 - self.__buttons_block.get_size()[0] // 2,
                        self.__position[1] + self.__title.get_size()[1] + self.__title_block_margin)
        else:
            position = (self.__position[0], self.__position[1] + self.__title.get_size()[1] + self.__title_block_margin)

        self.__buttons_block.set_position(position)

    def get_title(self):
        return self.__title

    def get_block(self):
        return self.__buttons_block

    def __calculate_size(self):
        if self.__title.get_size()[0] > self.__buttons_block.get_size()[0]:
            self.__menu_size = (self.__title.get_size()[0], self.__title.get_size()[1] + self.__title_block_margin + self.__buttons_block.get_size()[1])
        else:
            self.__menu_size = (self.__buttons_block.get_size()[0], self.__title.get_size()[1] + self.__title_block_margin + self.__buttons_block.get_size()[1])

    def __calculate_position(self, screen_size):
        return screen_size[0] // 2 - self.__menu_size[0] // 2, screen_size[1] // 2 - self.__menu_size[1] // 2

    def __calculate_max_menu_size(self):
        return int(self.__screen_display.get_size()[0] * self.__max_menu_size_ratio[0]), int(self.__screen_display.get_size()[1] * self.__max_menu_size_ratio[1])

    def __verify_menu_too_big(self):
        if self.__menu_size[0] > self.__max_menu_size[0] or self.__menu_size[1] > self.__max_menu_size[1]:
            self.__menu_too_big = True
        else:
            self.__menu_too_big = False

    def __verify_menu_too_small(self):
        if int(self.__menu_size[0] * (2 - self.__resize_ratio)) <= self.__max_menu_size[0] and int(self.__menu_size[1] * (2 - self.__resize_ratio)) <= self.__max_menu_size[1]:
            self.__menu_too_small = True
        else:
            self.__menu_too_small = False

    def __decrease_size_title_block(self):
        title_current_font_real_size = self.__title.get_font_real_size()
        block_current_real_size = self.__buttons_block.get_real_size()
        block_current_vertical_real_margin = self.__buttons_block.get_vertical_real_margin()
        block_current_horizontal_real_margin = self.__buttons_block.get_horizontal_real_margin()

        new_title_font_real_size = title_current_font_real_size * self.__resize_ratio
        new_block_real_size = block_current_real_size[0] * self.__resize_ratio, block_current_real_size[1] * self.__resize_ratio
        new_block_current_vertical_real_margin = block_current_vertical_real_margin * self.__resize_ratio
        new_block_current_horizontal_real_margin = block_current_horizontal_real_margin * self.__resize_ratio

        # resize title
        self.__title.set_font_real_size(new_title_font_real_size)

        # resize block
        self.__buttons_block.set_real_size(new_block_real_size)

        # resize block margins
        self.__buttons_block.set_vertical_real_margin(new_block_current_vertical_real_margin)
        self.__buttons_block.set_horizontal_real_margin(new_block_current_horizontal_real_margin)

        # resize title block margin
        self.__title_block_real_margin = self.__title_block_real_margin * self.__resize_ratio
        self.__title_block_margin = int(self.__title_block_real_margin)

        # resize buttons text
        for text_button in self.__buttons_block.get_text_buttons():
            button_font_real_size = text_button.get_font_real_size()
            new_button_font_real_size = button_font_real_size * self.__resize_ratio
            text_button.set_font_real_size(new_button_font_real_size)

        # resize slide buttons bar width
        for slide_button in self.__buttons_block.get_slide_buttons():
            slide_button_bar_real_width = slide_button.get_bar_real_width()
            new_slide_button_bar_real_width = slide_button_bar_real_width * self.__resize_ratio
            slide_button.set_bar_real_width(new_slide_button_bar_real_width)

    def __increase_size_title_block(self):
        title_current_font_real_size = self.__title.get_font_real_size()
        block_current_real_size = self.__buttons_block.get_real_size()
        block_current_vertical_real_margin = self.__buttons_block.get_vertical_real_margin()
        block_current_horizontal_real_margin = self.__buttons_block.get_horizontal_real_margin()

        new_title_font_real_size = title_current_font_real_size * (2 - self.__resize_ratio)
        new_block_real_size = block_current_real_size[0] * (2 - self.__resize_ratio), block_current_real_size[1] * (2 - self.__resize_ratio)
        new_block_current_vertical_real_margin = block_current_vertical_real_margin * (2 - self.__resize_ratio)
        new_block_current_horizontal_real_margin = block_current_horizontal_real_margin * (2 - self.__resize_ratio)

        # resize title
        self.__title.set_font_real_size(new_title_font_real_size)

        # resize block
        self.__buttons_block.set_real_size(new_block_real_size)

        # resize block margins
        self.__buttons_block.set_vertical_real_margin(new_block_current_vertical_real_margin)
        self.__buttons_block.set_horizontal_real_margin(new_block_current_horizontal_real_margin)

        # resize title block margin
        self.__title_block_real_margin = self.__title_block_real_margin * (2 - self.__resize_ratio)
        self.__title_block_margin = int(self.__title_block_real_margin)

        # resize buttons text
        for text_button in self.__buttons_block.get_text_buttons():
            button_font_real_size = text_button.get_font_real_size()
            new_button_font_real_size = button_font_real_size * (2 - self.__resize_ratio)
            text_button.set_font_real_size(new_button_font_real_size)

        # resize slide buttons bar width
        for slide_button in self.__buttons_block.get_slide_buttons():
            slide_button_bar_real_width = slide_button.get_bar_real_width()
            new_slide_button_bar_real_width = slide_button_bar_real_width * (2 - self.__resize_ratio)
            slide_button.set_bar_real_width(new_slide_button_bar_real_width)

    def __update_change_state_buttons(self):

        for change_button in self.__buttons_block.get_press_buttons_change_state():

            # get mouse location before and after to verify if mouse location has changed

            # get mouse before change
            mouse_location_before = change_button.get_mouse_over_button()

            # verify if mouse is on button
            change_button.verify_mouse_on_button(self.__current_mouse_position)

            # get mouse after change
            mouse_location_after = change_button.get_mouse_over_button()

            # verify if mouse location inside or outside button changed
            if mouse_location_before != mouse_location_after:

                # mouse location changed is used to draw button if location changed
                change_button.set_mouse_location_changed(True)
            else:
                change_button.set_mouse_location_changed(False)

            # verify if mouse is on button
            if change_button.get_mouse_over_button():

                # verify if mouse was outside button before
                if change_button.get_mouse_location_changed():

                    # draw change button (mouse over button)
                    change_button.draw_mouse_over_change_state_button()
                    pygame.display.update()

                if self.__current_event.type == pygame.MOUSEBUTTONDOWN:

                    # mouse left button
                    if self.__current_event.button == 1:

                        # display inside change button the next text
                        change_button.add_state_text_index()

                        # draw change button (mouse over button)
                        change_button.draw_mouse_over_change_state_button()
                        pygame.display.update()

            else:

                # verify if mouse was inside before
                if change_button.get_mouse_location_changed():

                    # draw change button (mouse out button)
                    change_button.draw_mouse_out_change_state_button()
                    pygame.display.update()

    def __update_slide_buttons(self):

        for slide_button in self.__buttons_block.get_slide_buttons():

            # before cursor mouse location in screen, inside or outside current slide button
            mouse_location_before = slide_button.get_mouse_over_button()

            # verify if current mouse cursor is inside button area
            slide_button.verify_mouse_on_button(self.__current_mouse_position)

            # after cursor mouse location in screen, inside or outside current slide button
            mouse_location_after = slide_button.get_mouse_over_button()

            # verify if mouse location is different before and after verification and
            # if the slide button bar was released
            if mouse_location_before != mouse_location_after or self.__release_slide_button_bar:
                slide_button.set_mouse_location_changed(True)
                self.__release_slide_button_bar = False
            else:
                slide_button.set_mouse_location_changed(False)

            if slide_button.get_mouse_over_button():
                # verify if left button is pressed inside button bar
                if self.__current_event.type == pygame.MOUSEBUTTONDOWN:
                    # mouse left button
                    if self.__current_event.button == 1:
                        slide_button.press_bar()

                if slide_button.get_mouse_location_changed():

                    # calculate current text in button according to current bar position
                    slide_button.calculate_current_item()

                    # draw slide button (mouse over button)
                    slide_button.draw_mouse_over_slide_button()
                    pygame.display.update()

            else:
                if slide_button.get_mouse_location_changed():

                    # calculate current text in button according to current bar position
                    slide_button.calculate_current_item()

                    # draw slide button (mouse out button)
                    slide_button.draw_mouse_out_slide_button()
                    pygame.display.update()

            if self.__current_event.type == pygame.MOUSEBUTTONUP:
                # mouse left button
                if self.__current_event.button == 1:
                    slide_button.release_bar()

                    # if mouse button is released and mouse cursor is outside button, change bar color to released color
                    # if this variable is true, the mouse location changed of the current button will be set to true
                    # in the initial condition of this function
                    self.__release_slide_button_bar = True

            if slide_button.get_bar_is_pressed():

                # calculate bar position when button is pressed
                slide_button.calculate_bar_position(self.__current_mouse_position)

                # calculate current text in button according to current bar position
                slide_button.calculate_current_item()

                # draw slide button (mouse over button)
                slide_button.draw_mouse_over_slide_button()
                pygame.display.update()

    def loop(self):

        loop_exit = False

        # draw title
        self.__title.draw()

        # draw change buttons
        for change_button in self.__buttons_block.get_press_buttons_change_state():
            change_button.draw_mouse_out_change_state_button()
        pygame.display.update()

        # draw slide buttons
        for slide_button in self.__buttons_block.get_slide_buttons():
            slide_button.draw_mouse_out_slide_button()
        pygame.display.update()

        while not loop_exit:
            for self.__current_event in pygame.event.get():

                # exit menu
                if self.__current_event.type == pygame.QUIT:
                    loop_exit = True

                if self.__current_event.type == pygame.KEYDOWN:

                    # if esc is pressed exit
                    if self.__current_event.key == pygame.K_ESCAPE:
                        loop_exit = True

                # resize screen
                if self.__current_event.type == pygame.VIDEORESIZE:

                    # set new screen display
                    self.__screen_display = pygame.display.set_mode(self.__current_event.size, pygame.RESIZABLE)

                    # update menu size
                    self.__max_menu_size = self.__calculate_max_menu_size()

                    # verify if menu is bigger than max menu size
                    self.__verify_menu_too_big()

                    # verify if menu can grow
                    self.__verify_menu_too_small()

                    while self.__menu_too_big:

                        # resize title and block
                        self.__decrease_size_title_block()

                        # update title
                        self.__configure_title()

                        # set new block position
                        self.__configure_buttons_block()

                        # set new menu size
                        self.__calculate_size()

                        # verify if menu is bigger than max menu size
                        self.__verify_menu_too_big()

                    while self.__menu_too_small:
                        # resize title and block
                        self.__increase_size_title_block()

                        # update title
                        self.__configure_title()

                        # set new block position
                        self.__configure_buttons_block()

                        # set new menu size
                        self.__calculate_size()

                        # verify if menu can grow
                        self.__verify_menu_too_small()

                    # set new menu size
                    self.__calculate_size()

                    # set new menu position
                    self.__set_position(self.__calculate_position(self.__current_event.size))

                    # set new title position
                    self.__set_title_position()

                    # set new block position
                    self.__configure_buttons_block()

                    # update screen display background
                    self.__screen_display.fill((255, 255, 255))

                    # draw title
                    self.__title.draw()

                    # draw change buttons
                    for change_button in self.__buttons_block.get_press_buttons_change_state():
                        change_button.draw_mouse_out_change_state_button()
                    pygame.display.update()

                    # draw slide buttons
                    for slide_button in self.__buttons_block.get_slide_buttons():
                        slide_button.draw_mouse_out_slide_button()
                    pygame.display.update()

                self.__current_mouse_position = pygame.mouse.get_pos()
                self.__mouse_left_pressed = pygame.mouse.get_pressed()[0]

                self.__update_change_state_buttons()

                self.__update_slide_buttons()
