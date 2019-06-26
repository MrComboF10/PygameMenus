import pygame
import button
import title
import buttonblock
import menu
import font
import mousestatebutton

white = (255, 255, 255)


def menu_loop():
    pygame.init()
    app_name = "PESTINHA"
    pygame.display.set_caption(app_name)
    screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
    screen.fill(white)
    pygame.display.update()


    # ========== menu style ============

    '''
        Título
        
        [slide_button, (0,200)] [slide_button, (0, 200)] [slide_button, (0, 5)]
        [change_state, (lava, oceano)] [change_state, (olá, abracadabra)]
        [redirect, BACK]
    '''

    # ---------- colors ------------

    mouse_out_colors1 = mousestatebutton.MouseStateButtonColors(button=(0, 255, 255), font=(0, 0, 255), bar=(200, 200, 255))
    mouse_out_colors2 = mousestatebutton.MouseStateButtonColors(button=(0, 255, 255), font=(0, 0, 255), bar=(200, 200, 255))
    mouse_out_colors3 = mousestatebutton.MouseStateButtonColors(button=(0, 255, 255), font=(0, 0, 255), bar=(200, 200, 255))
    mouse_out_colors4 = mousestatebutton.MouseStateButtonColors(button=(0, 255, 255), font=(0, 0, 255))
    mouse_out_colors5 = mousestatebutton.MouseStateButtonColors(button=(0, 255, 255), font=(0, 0, 255))
    mouse_out_colors6 = mousestatebutton.MouseStateButtonColors(button=(0, 255, 255), font=(0, 0, 255), width=(200, 200, 255))

    mouse_over_colors1 = mousestatebutton.MouseStateButtonColors(button=(255, 255, 0), font=(255, 0, 0), bar=(255, 165, 0))
    mouse_over_colors2 = mousestatebutton.MouseStateButtonColors(button=(255, 255, 0), font=(255, 0, 0), bar=(255, 165, 0))
    mouse_over_colors3 = mousestatebutton.MouseStateButtonColors(button=(255, 255, 0), font=(255, 0, 0), bar=(255, 165, 0))
    mouse_over_colors4 = mousestatebutton.MouseStateButtonColors(button=(255, 255, 0), font=(255, 0, 0))
    mouse_over_colors5 = mousestatebutton.MouseStateButtonColors(button=(255, 255, 0), font=(255, 0, 0))
    mouse_over_colors6 = mousestatebutton.MouseStateButtonColors(button=(255, 255, 0), font=(255, 0, 0), width=(255, 165, 0))

    colours0 = (0, 0, 0)
    colours1 = mousestatebutton.MouseAllStatesButtonColors(mouse_over_colors1, mouse_out_colors1)
    colours2 = mousestatebutton.MouseAllStatesButtonColors(mouse_over_colors2, mouse_out_colors2)
    colours3 = mousestatebutton.MouseAllStatesButtonColors(mouse_over_colors3, mouse_out_colors3)
    colours4 = mousestatebutton.MouseAllStatesButtonColors(mouse_over_colors4, mouse_out_colors4)
    colours5 = mousestatebutton.MouseAllStatesButtonColors(mouse_over_colors5, mouse_out_colors5)
    colours6 = mousestatebutton.MouseAllStatesButtonColors(mouse_over_colors6, mouse_out_colors6)

    # -------- fonts ----------

    font0 = font.Font("calibri", 200)
    font1 = font.Font("Arial", 70)
    font2 = font.Font("Arial", 70)
    font3 = font.Font("Arial", 70)
    font4 = font.Font("calibri", 70)
    font5 = font.Font("calibri", 70)
    font6 = font.Font("timesnewroman", 70)

    # ---------- ranges ----------
    range1 = range(201)
    range2 = range(201)
    range3 = range(1, 6)
    range4 = ["lava", "oceano"]
    range5 = ["olá", "abracadabra"]
    range6 = "BACK"

    # --------- title objects ----------

    titulo = "Título"
    title_1 = title.Title(font0, colours0, titulo)

    # ---------- buttons objects ----------

    slide_1 = button.SlideButton(font1, 10, range1, colours1)
    slide_2 = button.SlideButton(font2, 10, range2, colours2)
    slide_3 = button.SlideButton(font3, 10, range3, colours3)
    state_4 = button.PressButtonChangeState(font4, range4, colours4)
    state_5 = button.PressButtonChangeState(font5, range5, colours5)
    redirect_6 = button.PressButtonRedirect(font6, range6, None, colours6)

    # ---------- Block ----------
    menu_block = buttonblock.Block((500, 500), ((slide_1, slide_2, slide_3), (state_4, state_5), (redirect_6,)), 20, 20)

    # ---------- Menu ----------
    menu0 = menu.MainMenu(screen, title_1, menu_block, 30, (0.80, 0.80), 0.80)

    menu0.loop()


    # mouse_out_colors1 = mousestatebutton.MouseStateButtonColors(button=(200, 200, 255), font=(255, 255, 255), bar=(200, 200, 255), width=(0, 0, 0))
    # mouse_out_colors2 = mousestatebutton.MouseStateButtonColors(button=(200, 200, 255), font=(255, 255, 255), bar=(200, 200, 255), width=(0, 0, 0))
    # mouse_out_colors3 = mousestatebutton.MouseStateButtonColors(button=(230, 200, 255), font=(255, 255, 255), bar=(200, 200, 255), width=(0, 0, 0))
    # mouse_out_colors4 = mousestatebutton.MouseStateButtonColors(button=(230, 200, 255), font=(255, 255, 255), bar=(200, 200, 255), width=(0, 0, 0))
    # mouse_out_colors5 = mousestatebutton.MouseStateButtonColors(button=(230, 200, 255), font=(255, 255, 255), bar=(200, 200, 255), width=(0, 0, 0))
    # mouse_out_colors6 = mousestatebutton.MouseStateButtonColors(button=(230, 200, 255), font=(255, 255, 255), bar=(200, 200, 255), width=(0, 0, 0))
    #
    # mouse_over_colors1 = mousestatebutton.MouseStateButtonColors(button=(150, 150, 255), font=(255, 0, 255), bar=(150, 150, 255), width=(255, 0, 0))
    # mouse_over_colors2 = mousestatebutton.MouseStateButtonColors(button=(150, 150, 255), font=(255, 0, 255), bar=(150, 150, 255), width=(255, 0, 0))
    # mouse_over_colors3 = mousestatebutton.MouseStateButtonColors(button=(230, 200, 255), font=(255, 0, 255), bar=(150, 150, 255), width=(255, 0, 0))
    # mouse_over_colors4 = mousestatebutton.MouseStateButtonColors(button=(230, 200, 255), font=(255, 0, 255), bar=(150, 150, 255), width=(255, 0, 0))
    # mouse_over_colors5 = mousestatebutton.MouseStateButtonColors(button=(230, 200, 255), font=(255, 0, 255), bar=(150, 150, 255), width=(255, 0, 0))
    # mouse_over_colors6 = mousestatebutton.MouseStateButtonColors(button=(230, 200, 255), font=(255, 0, 255), bar=(150, 150, 255), width=(255, 0, 0))
    #
    # colors1 = mousestatebutton.MouseAllStatesButtonColors(mouse_over_colors1, mouse_out_colors1)
    # colors2 = mousestatebutton.MouseAllStatesButtonColors(mouse_over_colors2, mouse_out_colors2)
    # colors3 = mousestatebutton.MouseAllStatesButtonColors(mouse_over_colors3, mouse_out_colors3)
    # colors4 = mousestatebutton.MouseAllStatesButtonColors(mouse_over_colors4, mouse_out_colors4)
    # colors5 = mousestatebutton.MouseAllStatesButtonColors(mouse_over_colors5, mouse_out_colors5)
    # colors6 = mousestatebutton.MouseAllStatesButtonColors(mouse_over_colors6, mouse_out_colors6)
    #
    # buttons_font1 = font.Font("Arial", 70)
    # buttons_font2 = font.Font("Arial", 70)
    # buttons_font3 = font.Font("Arial", 70)
    # buttons_font4 = font.Font("Arial", 70)
    # buttons_font5 = font.Font("Arial", 70)
    # buttons_font6 = font.Font("Arial", 70)
    # buttons_font7 = font.Font("Arial", 70)
    # title_font = font.Font("Arial", 120, True)
    #
    # states_list = ("Fácil", "Médio", "Difícil")
    # mouse_over_button_color = (150, 150, 255)
    # mouse_out_button_color = (200, 200, 255)
    # slide_button_color = (230, 200, 255)
    # bar_width = 15
    # range_items = range(101)
    # alpha = list("aeiou")
    # for letter in range(len(alpha)):
    #     alpha[letter] = "Dificuldade: " + alpha[letter]
    #
    # title_1 = title.Title(title_font, (200, 200, 200), "MINESWEEPER")
    #
    # change_state_button_2 = button.PressButtonChangeState(buttons_font1, states_list, colors1, real_width=0.05)
    # change_state_button_3 = button.PressButtonChangeState(buttons_font2, states_list, colors2)
    #
    # slide_button_1 = button.SlideButton(buttons_font3, bar_width, alpha, colors3)
    # slide_button_2 = button.SlideButton(buttons_font4, bar_width, range_items, colors4, real_width=0.05)
    # slide_button_3 = button.SlideButton(buttons_font5, bar_width, range_items, colors5)
    # slide_button_4 = button.SlideButton(buttons_font6, bar_width, range_items, colors6)
    # slide_button_5 = button.SlideButton(buttons_font7, bar_width, range_items, colors6)
    #
    # block2 = buttonblock.Block((500, 500), ((change_state_button_2, change_state_button_3), (slide_button_1,), (slide_button_2, slide_button_3, slide_button_4)), 20, 30)
    #
    # main_menu = menu.MainMenu(screen, title_1, block2, 50, (0.80, 0.80), 0.80)

    # main_menu.loop()


menu_loop()

pygame.quit()
