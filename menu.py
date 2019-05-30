import pygame

white = (255, 255, 255)


class MainMenu:
    def __init__(self, screen_display, title, buttons_block, title_block_margin):

        self.__screen_display = screen_display
        self.__title_block_margin = title_block_margin

        self.__title_size = title.get_size()
        self.__block_size = buttons_block.get_size()
        self.__menu_sizes = None

        self.__position = None
        self.__set_position(self.__calculate_position((screen_display.get_rect()[2], screen_display.get_rect()[3])))
        self.__current_mouse_position = (0, 0)
        self.__current_event = None
        self.__mouse_left_pressed = None
        self.__release_slide_button_bar = True

        # configure title
        self.__title = title
        self.__set_title_position()
        self.__title.set_screen_display(screen_display)

        # configure buttons block
        self.__buttons_block = buttons_block
        self.__set_block_position()
        self.__buttons_block.set_screen_display(screen_display)
        self.__buttons_block.update_buttons()

    def __set_size(self):
        if self.__title_size[0] > self.__block_size[0]:
            self.__menu_sizes = (self.__title_size[0], self.__title_size[1] + self.__title_block_margin + self.__block_size[1])
        else:
            self.__menu_sizes = (self.__block_size[0], self.__title_size[1] + self.__title_block_margin + self.__block_size[1])

    def __calculate_position(self, screen_size):
        self.__set_size()
        return screen_size[0] // 2 - self.__menu_sizes[0] // 2, screen_size[1] // 2 - self.__menu_sizes[1] // 2

    def __set_position(self, position):
        self.__position = position

    def __set_title_position(self):
        if self.__title_size[0] > self.__block_size[0]:
            position = self.__position
        else:
            position = (self.__position[0] + self.__block_size[0] // 2 - self.__title_size[0] // 2, self.__position[1])

        self.__title.set_position(position)

    def __set_block_position(self):
        if self.__title_size[0] > self.__block_size[0]:
            position = (self.__position[0] + self.__title_size[0] // 2 - self.__block_size[0] // 2,
                        self.__position[1] + self.__title_size[1] + self.__title_block_margin)
        else:
            position = (self.__position[0], self.__position[1] + self.__title_size[1] + self.__title_block_margin)

        self.__buttons_block.set_position(position)

    def get_title(self):
        return self.__title

    def get_block(self):
        return self.__buttons_block

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

                    self.__screen_display = pygame.display.set_mode(self.__current_event.size, pygame.RESIZABLE)
                    self.__set_position(self.__calculate_position(self.__current_event.size))
                    self.__set_title_position()
                    self.__set_block_position()
                    self.__buttons_block.update_buttons()

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
