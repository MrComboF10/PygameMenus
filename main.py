import pygame
import button
import title
import buttonblock
import menu

white = (255, 255, 255)


def menu_loop():
    pygame.init()
    screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
    screen.fill(white)
    pygame.display.update()

    font = pygame.font.SysFont("Arial", 30)
    title_font = pygame.font.SysFont("Arial", 80, True)

    states_list = ("Fácil", "Médio", "Difícil")
    mouse_over_button_color = (150, 150, 255)
    mouse_out_button_color = (200, 200, 255)
    slide_button_color = (230, 200, 255)
    bar_width = 15
    range_items = range(101)

    title_1 = title.Title(title_font, (200, 200, 200), "MINESWEEPER")

    change_state_button_2 = button.PressButtonChangeState(font, white, mouse_out_button_color, mouse_over_button_color, states_list)
    change_state_button_3 = button.PressButtonChangeState(font, white, mouse_out_button_color, mouse_over_button_color, states_list)

    slide_button_1 = button.SlideButton(font, white, bar_width, range_items, mouse_out_button_color, mouse_over_button_color, slide_button_color)
    slide_button_2 = button.SlideButton(font, white, bar_width, range_items, mouse_out_button_color, mouse_over_button_color, slide_button_color)

    long_block = buttonblock.Block1Column((500, 500), (change_state_button_2, change_state_button_3, slide_button_1, slide_button_2), 20)
    short_block = buttonblock.Block2Columns((500, 400), (change_state_button_2, change_state_button_3, slide_button_1, slide_button_2), 20, 20)

    main_menu = menu.MainMenu(screen, title_1, short_block, 50)

    main_menu.loop()


menu_loop()

pygame.quit()
