import pygame

white = (255, 255, 255)


class MainMenu:
    def __init__(self, position, screen_display, title, buttons_block, margin):

        self.__position = position
        self.__screen_display = screen_display
        self.__margin = margin

        self.__title_size = title.get_size()
        self.__block_size = buttons_block.get_size()

        self.__current_mouse_position = (0, 0)
        self.__current_event = None
        self.__mouse_left_pressed = None
        self.__change_location = True

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

    def __update_change_state_buttons(self):

        for change_button in self.__buttons_block.get_press_buttons_change_state():

            change_button.set_current_mouse_position(self.__current_mouse_position)

            # get mouse location before and after to verify if mouse location has changed
            mouse_location_before = change_button.get_mouse_over_button()
            change_button.verify_mouse_on_button()
            mouse_location_after = change_button.get_mouse_over_button()

            # verify if mouse location inside or outside button changed
            if mouse_location_before != mouse_location_after:
                change_button.set_mouse_location_changed(True)
            else:
                change_button.set_mouse_location_changed(False)

            # verify if mouse is on button
            if change_button.get_mouse_over_button():

                # verify if mouse was outside button before
                if change_button.get_mouse_location_changed():
                    change_button.draw_mouse_over_change_state_button()
                    pygame.display.update()

                if self.__current_event.type == pygame.MOUSEBUTTONDOWN:
                    # mouse left button
                    if self.__current_event.button == 1:
                        change_button.add_state_text_index()
                        change_button.draw_mouse_over_change_state_button()
                        pygame.display.update()

            else:
                # verify if mouse was inside before
                if change_button.get_mouse_location_changed():
                    change_button.draw_mouse_out_change_state_button()
                    pygame.display.update()

    def __update_slide_buttons(self):

        for slide_button in self.__buttons_block.get_slide_buttons():

            slide_button.set_current_mouse_position(self.__current_mouse_position)

            mouse_location_before = slide_button.get_mouse_over_button()
            slide_button.verify_mouse_on_button()
            mouse_location_after = slide_button.get_mouse_over_button()

            if mouse_location_before != mouse_location_after or self.__change_location:
                slide_button.set_mouse_location_changed(True)
                self.__change_location = False
            else:
                slide_button.set_mouse_location_changed(False)

            if slide_button.get_mouse_over_button():
                # verify if left button is pressed inside button bar
                if self.__current_event.type == pygame.MOUSEBUTTONDOWN:
                    # mouse left button
                    if self.__current_event.button == 1:
                        slide_button.press_bar()

                if slide_button.get_mouse_location_changed():
                    slide_button.calculate_current_item()
                    slide_button.draw_mouse_over_slide_button()
                    pygame.display.update()

            else:
                if slide_button.get_mouse_location_changed():
                    slide_button.calculate_current_item()
                    slide_button.draw_mouse_out_slide_button()
                    pygame.display.update()

            if self.__current_event.type == pygame.MOUSEBUTTONUP:
                # mouse left button
                if self.__current_event.button == 1:
                    slide_button.release_bar()
                    # update button draw
                    self.__change_location = True

            if slide_button.get_bar_is_pressed():
                slide_button.calculate_bar_position()
                slide_button.calculate_current_item()
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

                self.__current_mouse_position = pygame.mouse.get_pos()
                self.__mouse_left_pressed = pygame.mouse.get_pressed()[0]

                self.__update_change_state_buttons()

                self.__update_slide_buttons()
