import pygame
import button
import title
import buttonblock
import menu
import font

white = (255, 255, 255)


def menu_loop():
    pygame.init()
    app_name = "PESTINHA"
    pygame.display.set_caption(app_name)
    screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
    screen.fill(white)
    pygame.display.update()

    buttons_font1 = font.Font("Arial", 90)
    buttons_font2 = font.Font("Arial", 90)
    buttons_font3 = font.Font("Arial", 90)
    buttons_font4 = font.Font("Arial", 90)
    buttons_font5 = font.Font("Arial", 90)
    buttons_font6 = font.Font("Arial", 90)
    buttons_font7 = font.Font("Arial", 90)
    title_font = font.Font("Arial", 120, True)

    states_list = ("Fácil", "Médio", "Difícil")
    mouse_over_button_color = (150, 150, 255)
    mouse_out_button_color = (200, 200, 255)
    slide_button_color = (230, 200, 255)
    bar_width = 15
    range_items = range(101)

    title_1 = title.Title(title_font, (200, 200, 200), "MINESWEEPER")

    change_state_button_2 = button.PressButtonChangeState(buttons_font1, white, mouse_out_button_color, mouse_over_button_color, states_list)
    change_state_button_3 = button.PressButtonChangeState(buttons_font2, white, mouse_out_button_color, mouse_over_button_color, states_list)

    slide_button_1 = button.SlideButton(buttons_font3, white, bar_width, range_items, mouse_out_button_color, mouse_over_button_color, slide_button_color)
    slide_button_2 = button.SlideButton(buttons_font4, white, bar_width, range_items, mouse_out_button_color, mouse_over_button_color, slide_button_color)
    slide_button_3 = button.SlideButton(buttons_font5, white, bar_width, range_items, mouse_out_button_color, mouse_over_button_color, slide_button_color)
    slide_button_4 = button.SlideButton(buttons_font6, white, bar_width, range_items, mouse_out_button_color,mouse_over_button_color, slide_button_color)
    slide_button_5 = button.SlideButton(buttons_font7, white, bar_width, range_items, mouse_out_button_color,mouse_over_button_color, slide_button_color)

    block2 = buttonblock.Block((500, 500), ((change_state_button_2,), (change_state_button_3, slide_button_1,), (slide_button_2, slide_button_3, slide_button_4)), 20, 30)

    main_menu = menu.MainMenu(screen, title_1, block2, 50, (0.80, 0.80), 0.80)

    main_menu.loop()


menu_loop()

pygame.quit()
