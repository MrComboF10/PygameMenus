import pygame
import button

white = (255, 255, 255)

def menu_loop():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    screen.fill(white)
    pygame.display.update()

    button_position_1, button_position_2, button_position_3, button_position_4, button_position_5 = (100, 100), (100, 250), (100, 400), (100, 550), (100, 700)
    button_sizes = (500, 100)
    states_list = ("Fácil", "Médio", "Difícil")
    pressed_color = (150, 150, 255)
    unpressed_color = (200, 200, 255)
    slide_button_color = (230, 200, 255)
    bar_width = 15
    range_items = range(4)

    change_state_button_1 = button.PressButtonChangeState(button_position_1, button_sizes, states_list, unpressed_color, pressed_color, white, screen)
    change_state_button_2 = button.PressButtonChangeState(button_position_2, button_sizes, states_list, unpressed_color, pressed_color, white, screen)
    change_state_button_3 = button.PressButtonChangeState(button_position_3, button_sizes, states_list, unpressed_color, pressed_color, white, screen)

    slide_button_1 = button.SlideButton(button_position_4, button_sizes, bar_width, range_items, white, unpressed_color, pressed_color, slide_button_color, screen)
    slide_button_2 = button.SlideButton(button_position_5, button_sizes, bar_width, range_items, white, unpressed_color, pressed_color, slide_button_color, screen)

    change_state_buttons = (change_state_button_1, change_state_button_2, change_state_button_3)
    slide_buttons = (slide_button_1, slide_button_2)
    loop_exit = False

    for change_button in change_state_buttons:
        change_button.draw_unpressed_button()
    pygame.display.update()

    for slide_button in slide_buttons:
        slide_button.draw_mouse_out_button()
    pygame.display.update()

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

                change_button.insert_current_mouse_position(current_mouse_position)

                # get mouse location before and after to verify if mouse location has changed
                mouse_location_before = change_button.get_mouse_on_button()
                change_button.verify_mouse_on_button()
                mouse_location_after = change_button.get_mouse_on_button()

                # verify if mouse location inside or outside button changed
                if mouse_location_before != mouse_location_after:
                    change_button.insert_mouse_location_changed(True)
                else:
                    change_button.insert_mouse_location_changed(False)

                # verify if mouse is on button
                if change_button.get_mouse_on_button():

                    # verify if mouse was outside button before
                    if change_button.get_mouse_location_changed():
                        change_button.draw_pressed_button()
                        pygame.display.update()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # mouse left button
                        if event.button == 1:
                            change_button.add_state_text_index()
                            change_button.draw_pressed_button()
                            pygame.display.update()

                else:
                    # verify if mouse was inside before
                    if change_button.get_mouse_location_changed():
                        change_button.draw_unpressed_button()
                        pygame.display.update()

            # ========== change slide buttons ==========

            for slide_button in slide_buttons:

                slide_button.insert_current_mouse_position(current_mouse_position)

                mouse_location_before = slide_button.get_mouse_on_button()
                slide_button.verify_mouse_on_button()
                mouse_location_after = slide_button.get_mouse_on_button()

                if mouse_location_before != mouse_location_after:
                    slide_button.insert_mouse_location_changed(True)
                else:
                    slide_button.insert_mouse_location_changed(False)

                if slide_button.get_mouse_on_button():
                    # verify if left button is pressed inside button bar
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # mouse left button
                        if event.button == 1:
                            slide_button.insert_bar_is_pressed(True)

                    if slide_button.get_mouse_location_changed():
                        slide_button.calculate_current_item()
                        slide_button.draw_mouse_on_button()
                        pygame.display.update()

                else:
                    if slide_button.get_mouse_location_changed():
                        slide_button.calculate_current_item()
                        slide_button.draw_mouse_out_button()
                        pygame.display.update()

                if event.type == pygame.MOUSEBUTTONUP:
                    # mouse left button
                    if event.button == 1:
                        slide_button.insert_bar_is_pressed(False)

                if slide_button.get_bar_is_pressed():
                    slide_button.calculate_bar_position()
                    print(slide_button.get_current_item())
                    slide_button.calculate_current_item()
                    slide_button.draw_mouse_on_button()
                    pygame.display.update()







menu_loop()
