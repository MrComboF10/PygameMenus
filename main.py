import pygame
import button

white = (255, 255, 255)

def menu_loop():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    screen.fill(white)
    pygame.display.update()

    button_position = (100, 100)
    button_sizes = (500, 100)
    states_list = ("Fácil", "Médio", "Difícil")
    pressed_color = (150, 150, 255)
    unpressed_color = (200, 200, 255)

    change_state_button = button.PressButtonChangeState(button_position, button_sizes, states_list, pressed_color, unpressed_color, white, screen)
    loop_exit = False
    mouse_outside_to_inside = True
    mouse_inside_to_outside = True
    mouse_change_location = True
    while not loop_exit:
        for event in pygame.event.get():

            current_mouse_position = pygame.mouse.get_pos()
            mouse_left_pressed = pygame.mouse.get_pressed()[0]

            change_state_button.get_current_mouse_position(current_mouse_position)
            change_state_button.verify_mouse_on_button()

            if event.type == pygame.KEYDOWN:

                # if esc is pressed exit
                if event.key == pygame.K_ESCAPE:
                    loop_exit = True

            # verify if mouse is on button
            if change_state_button.get_mouse_on_button():

                # verify if mouse was outside button before
                if mouse_outside_to_inside:
                    print("INSIDE")
                    change_state_button.draw_pressed_button()
                    pygame.display.update()
                    mouse_outside_to_inside = False
                    mouse_inside_to_outside = True

            else:

                # verify if mouse was inside before
                if mouse_inside_to_outside:
                    print("OUTSIDE")
                    change_state_button.draw_unpressed_button()
                    pygame.display.update()
                    mouse_inside_to_outside = False
                    mouse_outside_to_inside = True


menu_loop()
