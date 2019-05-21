import pygame
import button
import title
import buttonblock

white = (255, 255, 255)


def menu_loop():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    screen.fill(white)
    pygame.display.update()

    font = pygame.font.SysFont("Arial", 25)
    title_font = pygame.font.SysFont("Arial", 100, True)

    button_position_1, button_position_2, button_position_3, button_position_4, button_position_5 = (100, 100), (100, 250), (100, 400), (100, 550), (100, 700)
    button_sizes = (500, 100)
    states_list = ("Fácil", "Médio", "Difícil")
    mouse_over_button_color = (150, 150, 255)
    mouse_out_button_color = (200, 200, 255)
    slide_button_color = (230, 200, 255)
    bar_width = 15
    range_items = range(101)

    title_1 = title.Title(title_font, (200, 200, 200), "MINESWEEPER", (500, 100), screen)

    # change_state_button_1 = button.PressButtonChangeState(button_position_1, button_sizes, font, white, screen, mouse_out_button_color, mouse_over_button_color, states_list)

    change_state_button_2 = button.PressButtonChangeState(font, white, screen, mouse_out_button_color, mouse_over_button_color, states_list)
    change_state_button_3 = button.PressButtonChangeState(font, white, screen, mouse_out_button_color, mouse_over_button_color, states_list)

    slide_button_1 = button.SlideButton(font, white, screen, bar_width, range_items, mouse_out_button_color, mouse_over_button_color, slide_button_color)
    slide_button_2 = button.SlideButton(font, white, screen, bar_width, range_items, mouse_out_button_color, mouse_over_button_color, slide_button_color)

    block = buttonblock.Block((300, 300), (410, 410), (change_state_button_2, change_state_button_3, slide_button_1, slide_button_2), 20)

    change_state_buttons = block.get_press_buttons_change_state()
    slide_buttons = block.get_slide_buttons()
    # slide_buttons = []
    print(slide_buttons[0].get_position())
    print(slide_buttons[0].get_size())
    loop_exit = False

    # draw title
    title_1.set_font_surface_center()
    title_1.draw()

    # draw change buttons
    for change_button in change_state_buttons:
        change_button.draw_mouse_out_change_state_button()
    pygame.display.update()

    # draw slide buttons
    for slide_button in slide_buttons:
        slide_button.draw_mouse_out_slide_button()
    pygame.display.update()

    change_location = True

    while not loop_exit:
        for event in pygame.event.get():

            # exit menu
            if event.type == pygame.QUIT:
                loop_exit = True

            if event.type == pygame.KEYDOWN:

                # if esc is pressed exit
                if event.key == pygame.K_ESCAPE:
                    loop_exit = True

            current_mouse_position = pygame.mouse.get_pos()
            mouse_left_pressed = pygame.mouse.get_pressed()[0]

            # ========== change state buttons ==========
            for change_button in change_state_buttons:

                change_button.set_current_mouse_position(current_mouse_position)

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

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # mouse left button
                        if event.button == 1:
                            change_button.add_state_text_index()
                            change_button.draw_mouse_over_change_state_button()
                            pygame.display.update()

                else:
                    # verify if mouse was inside before
                    if change_button.get_mouse_location_changed():
                        change_button.draw_mouse_out_change_state_button()
                        pygame.display.update()

            # ========== change slide buttons ==========

            for slide_button in slide_buttons:

                slide_button.set_current_mouse_position(current_mouse_position)

                mouse_location_before = slide_button.get_mouse_over_button()
                slide_button.verify_mouse_on_button()
                mouse_location_after = slide_button.get_mouse_over_button()

                if mouse_location_before != mouse_location_after or change_location:
                    slide_button.set_mouse_location_changed(True)
                    change_location = False
                else:
                    slide_button.set_mouse_location_changed(False)

                if slide_button.get_mouse_over_button():
                    # verify if left button is pressed inside button bar
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # mouse left button
                        if event.button == 1:
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

                if event.type == pygame.MOUSEBUTTONUP:
                    # mouse left button
                    if event.button == 1:
                        slide_button.release_bar()
                        # update button draw
                        change_location = True

                if slide_button.get_bar_is_pressed():
                    slide_button.calculate_bar_position()
                    slide_button.calculate_current_item()
                    slide_button.draw_mouse_over_slide_button()
                    pygame.display.update()


menu_loop()
