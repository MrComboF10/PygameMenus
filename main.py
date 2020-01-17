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

    font1 = font.Font("Arial", 70)
    font2 = font.Font("Arial", 70)
    font3 = font.Font("Arial", 70)
    font4 = font.Font("calibri", 70)
    font5 = font.Font("calibri", 70)
    font6 = font.Font("timesnewroman", 70)
    font7 = font.Font("timesnewroman", 70)
    font8 = font.Font("timesnewroman", 70)
    font9 = font.Font("timesnewroman", 70)
    font10 = font.Font("calibri", 200)
    font11 = font.Font("calibri", 200)

    # ---------- ranges ----------
    range1 = range(201)
    range2 = range(201)
    range3 = range(1, 6)
    range4 = ["lava", "oceano"]
    range5 = ["olá", "adeus"]
    option1 = "BACK"
    option2 = "NEXT"
    option3 = "EXIT"

    # --------- title objects ----------

    title_1 = title.Title(font10, colours0, "Title 1")
    title_2 = title.Title(font11, colours0, "Title 2")

    # ---------- buttons objects ----------

    slide_1 = button.SlideButton(font1, 10, range1, colours1)
    slide_2 = button.SlideButton(font2, 10, range2, colours2)
    slide_3 = button.SlideButton(font3, 10, range3, colours3)
    state_4 = button.PressButtonChangeState(font4, range4, colours4)
    state_5 = button.PressButtonChangeState(font5, range5, colours5)
    redirect_1 = button.PressButtonRedirect(font6, option1, "STATE_MAIN_MENU", colours6)
    redirect_2 = button.PressButtonRedirect(font7, option2, "STATE_SEC_MENU", colours6)
    redirect_3 = button.PressButtonRedirect(font8, option3, "STATE_EXIT", colours6)
    redirect_4 = button.PressButtonRedirect(font9, option3, "STATE_EXIT", colours6)

    # ---------- Block ----------
    menu_block_1 = buttonblock.Block((500, 500), ((slide_1,), (state_4,), (redirect_2,), (redirect_3,)), 20, 20)
    menu_block_2 = buttonblock.Block((500, 500), ((slide_3,), (state_5,), (redirect_1,), (redirect_4,)), 20, 20)

    # ---------- Menu ----------
    menu_1 = menu.Menu(screen, title_1, menu_block_1, 30, (0.80, 0.80), 0.80, "STATE_MAIN_MENU")
    menu_2 = menu.Menu(screen, title_2, menu_block_2, 30, (0.80, 0.80), 0.80, "STATE_SEC_MENU")

    # ---------- Tests ---------

    exit_game = False
    current_state = "STATE_MAIN_MENU"
    current_screen_display = screen

    while not exit_game:

        if current_state == "STATE_MAIN_MENU":

            menu_1.set_screen_display(current_screen_display)
            menu_1.loop()
            if menu_1.get_pressed_exit():
                exit_game = True

            else:
                current_state = menu_1.get_next_state()
                current_screen_display = menu_1.get_screen_display()

            screen.fill(white)
            pygame.display.update()

        elif current_state == "STATE_SEC_MENU":

            menu_2.set_screen_display(current_screen_display)
            menu_2.loop()
            if menu_2.get_pressed_exit():
                exit_game = True

            else:
                current_state = menu_2.get_next_state()
                current_screen_display = menu_2.get_screen_display()

            screen.fill(white)
            pygame.display.update()

        elif current_state == "STATE_EXIT":
            exit_game = True

        else:
            print("Invalid state!")


menu_loop()

pygame.quit()
