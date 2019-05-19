import pygame
import button

white = (255, 255, 255)

def menu_loop():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    screen.fill(white)
    pygame.display.update()

    button_position_1, button_position_2, button_position_3 = (100, 100), (100, 300), (100, 500)
    button_sizes = (500, 100)
    states_list = ("Fácil", "Médio", "Difícil")
    pressed_color = (150, 150, 255)
    unpressed_color = (200, 200, 255)

    change_state_button_1 = button.PressButtonChangeState(button_position_1, button_sizes, states_list, pressed_color, unpressed_color, white, screen)
    change_state_button_2 = button.PressButtonChangeState(button_position_2, button_sizes, states_list, pressed_color, unpressed_color, white, screen)
    change_state_button_3 = button.PressButtonChangeState(button_position_3, button_sizes, states_list, pressed_color, unpressed_color, white, screen)

    change_state_buttons = (change_state_button_1, change_state_button_2, change_state_button_3)
    loop_exit = False

    for menu_button in change_state_buttons:
        menu_button.draw_unpressed_button()
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
            for menu_button in change_state_buttons:

                menu_button.get_current_mouse_position(current_mouse_position)

                # get mouse location before and after to verify if mouse location has changed
                mouse_location_before = menu_button.get_mouse_on_button()
                menu_button.verify_mouse_on_button()
                mouse_location_after = menu_button.get_mouse_on_button()

                # verify if mouse location inside or outside button changed
                if mouse_location_before != mouse_location_after:
                    menu_button.insert_mouse_location_changed(True)
                else:
                    menu_button.insert_mouse_location_changed(False)

                # verify if mouse is on button
                if menu_button.get_mouse_on_button():

                    # verify if mouse was outside button before
                    if menu_button.get_mouse_location_changed():
                        menu_button.draw_pressed_button()
                        pygame.display.update()

                    # verify if mouse pressed is the first click
                    if mouse_left_pressed:
                        if menu_button.get_mouse_click_update():
                            menu_button.add_state_text_index()
                            menu_button.draw_pressed_button()
                            pygame.display.update()

                            # disable mouse click after mouse click is made
                            menu_button.insert_mouse_click_update(False)
                    else:
                        # enable mouse click
                        menu_button.insert_mouse_click_update(True)
                else:
                    # verify if mouse was inside before
                    if menu_button.get_mouse_location_changed():
                        menu_button.draw_unpressed_button()
                        pygame.display.update()

                    # disable mouse click if mouse is outside button
                    menu_button.insert_mouse_click_update(False)




menu_loop()
