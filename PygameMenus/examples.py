from PygameMenus.button import *
from PygameMenus.title import *
from PygameMenus.buttonblock import *
from PygameMenus.menu import *
from PygameMenus.buttoncolors import *
from PygameFloatObjects.objects import *


def main_loop():
    white = (255, 255, 255)

    pygame.init()
    screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
    screen.fill(white)
    pygame.display.update()

    # ---------- colors ------------
    # define colors of buttons

    mouse_out_colors1 = MousePositionButtonColors(button=(0, 255, 255), font=(0, 0, 255), bar=(200, 200, 255))
    mouse_out_colors2 = MousePositionButtonColors(button=(0, 255, 255), font=(0, 0, 255), bar=(200, 200, 255))
    mouse_out_colors3 = MousePositionButtonColors(button=(0, 255, 255), font=(0, 0, 255), bar=(200, 200, 255))
    mouse_out_colors4 = MousePositionButtonColors(button=(0, 255, 255), font=(0, 0, 255))
    mouse_out_colors5 = MousePositionButtonColors(button=(0, 255, 255), font=(0, 0, 255))
    mouse_out_colors6 = MousePositionButtonColors(button=(0, 255, 255), font=(0, 0, 255), width=(200, 200, 255))

    mouse_over_colors1 = MousePositionButtonColors(button=(255, 255, 0), font=(255, 0, 0), bar=(255, 165, 0))
    mouse_over_colors2 = MousePositionButtonColors(button=(255, 255, 0), font=(255, 0, 0), bar=(255, 165, 0))
    mouse_over_colors3 = MousePositionButtonColors(button=(255, 255, 0), font=(255, 0, 0), bar=(255, 165, 0))
    mouse_over_colors4 = MousePositionButtonColors(button=(255, 255, 0), font=(255, 0, 0))
    mouse_over_colors5 = MousePositionButtonColors(button=(255, 255, 0), font=(255, 0, 0))
    mouse_over_colors6 = MousePositionButtonColors(button=(255, 255, 0), font=(255, 0, 0), width=(255, 165, 0))

    title_1_color = (0, 0, 0)
    title_2_color = (0, 0, 0)
    colors1 = ButtonColors(mouse_over_colors1, mouse_out_colors1)
    colors2 = ButtonColors(mouse_over_colors2, mouse_out_colors2)
    colors3 = ButtonColors(mouse_over_colors3, mouse_out_colors3)
    colors4 = ButtonColors(mouse_over_colors4, mouse_out_colors4)
    colors5 = ButtonColors(mouse_over_colors5, mouse_out_colors5)
    colors6 = ButtonColors(mouse_over_colors6, mouse_out_colors6)

    # -------- fonts ----------
    # define fonts of buttons and title

    font1 = FloatFont("Arial", 70)
    font2 = FloatFont("Arial", 70)
    font3 = FloatFont("Arial", 70)
    font4 = FloatFont("calibri", 70)
    font5 = FloatFont("calibri", 70)
    font6 = FloatFont("timesnewroman", 70)
    font7 = FloatFont("timesnewroman", 70)
    font8 = FloatFont("timesnewroman", 70)
    font9 = FloatFont("timesnewroman", 70)
    font10 = FloatFont("calibri", 200)
    font11 = FloatFont("calibri", 200)

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

    title_1 = Title(font10, title_1_color, "Title 1")
    title_2 = Title(font11, title_2_color, "Title 2")

    # ---------- buttons objects ----------

    slide_1 = SlideButton(font1, 10, range1, colors1)
    slide_2 = SlideButton(font2, 10, range2, colors2)
    slide_3 = SlideButton(font3, 10, range3, colors3)
    state_4 = StatesButton(font4, range4, colors4)
    state_5 = StatesButton(font5, range5, colors5)
    redirect_1 = RedirectButton(font6, option1, "STATE_MAIN_MENU", colors6)
    redirect_2 = RedirectButton(font7, option2, "STATE_SEC_MENU", colors6)
    redirect_3 = RedirectButton(font8, option3, "STATE_EXIT", colors6)
    redirect_4 = RedirectButton(font9, option3, "STATE_EXIT", colors6)

    # ---------- Block ----------
    menu_block_1 = Block((500, 500), ((slide_1,), (state_4,), (redirect_2,), (redirect_3,)), 20, 20)
    menu_block_2 = Block((500, 500), ((slide_3,), (state_5,), (redirect_1,), (redirect_4,)), 20, 20)

    # ---------- Menu ----------
    menu_1 = Menu(screen, title_1, menu_block_1, 30, (0.80, 0.80), 0.80, "STATE_MAIN_MENU")
    menu_2 = Menu(screen, title_2, menu_block_2, 30, (0.80, 0.80), 0.80, "STATE_SEC_MENU")

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

    pygame.quit()


def example_1():

    # create display
    pygame.init()
    screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
    screen.fill((255, 255, 255))
    pygame.display.update()

    # ========== Main Menu ==========

    # --- Title ---

    # define title color
    main_title_color = (0, 0, 0)

    # define title font
    main_title_font = FloatFont("Arial", 70)

    # create title
    main_title = Title(main_title_font, main_title_color, "Main")



    # --- Slide buttons ---

    # create slide buttons colors when mouse is outside button
    main_slide_1_mouse_out_colors = MousePositionButtonColors(button=(0, 255, 255), font=(0, 0, 255), bar=(200, 200, 255))
    main_slide_2_mouse_out_colors = MousePositionButtonColors(button=(0, 255, 255), font=(0, 0, 255), bar=(200, 200, 255))
    main_slide_3_mouse_out_colors = MousePositionButtonColors(button=(0, 255, 255), font=(0, 0, 255), bar=(200, 200, 255))

    # create slide buttons colors when mouse is over button
    main_slide_1_mouse_over_colors = MousePositionButtonColors(button=(0, 255, 255), font=(0, 0, 255), bar=(200, 200, 255))
    main_slide_2_mouse_over_colors = MousePositionButtonColors(button=(0, 255, 255), font=(0, 0, 255), bar=(200, 200, 255))
    main_slide_3_mouse_over_colors = MousePositionButtonColors(button=(0, 255, 255), font=(0, 0, 255), bar=(200, 200, 255))

    # create slide buttons colors
    main_slide_1_colors = ButtonColors(main_slide_1_mouse_over_colors, main_slide_1_mouse_out_colors)
    main_slide_2_colors = ButtonColors(main_slide_2_mouse_over_colors, main_slide_2_mouse_out_colors)
    main_slide_3_colors = ButtonColors(main_slide_3_mouse_over_colors, main_slide_3_mouse_out_colors)

    # create slide buttons fonts
    main_slide_1_font = FloatFont("Arial", 70)
    main_slide_2_font = FloatFont("Arial", 70)
    main_slide_3_font = FloatFont("Arial", 70)

    # create slide buttons ranges
    main_slide_1_range = range(101)
    main_slide_2_range = ["a", "e", "i", "o", "u"]
    main_slide_3_range = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

    # define slide buttons bar width
    main_slide_bar_width = 10

    # create slide buttons
    main_slide_1 = SlideButton(main_slide_1_font, main_slide_bar_width, main_slide_1_range, main_slide_1_colors)
    main_slide_2 = SlideButton(main_slide_2_font, main_slide_bar_width, main_slide_2_range, main_slide_2_colors)
    main_slide_3 = SlideButton(main_slide_3_font, main_slide_bar_width, main_slide_3_range, main_slide_3_colors)



    # --- States buttons ---

    # create states buttons colors when mouse is outside button
    main_states_1_mouse_out_colors = MousePositionButtonColors(button=(0, 255, 255), font=(0, 0, 255))

    # create states buttons colors when mouse is over button
    main_states_1_mouse_over_colors = MousePositionButtonColors(button=(0, 255, 255), font=(0, 0, 255))

    # create states buttons colors
    main_states_1_colors = ButtonColors(main_states_1_mouse_over_colors, main_states_1_mouse_out_colors)

    # create states buttons fonts
    main_states_1_font = FloatFont("Arial", 70)

    # create states buttons ranges
    main_states_1_range = ["Difficulty: Very Easy", "Difficulty: Easy", "Difficulty: Medium", "Difficulty: Hard", "Difficulty: Very Hard"]

    # create states buttons
    main_states_button_1 = StatesButton(main_states_1_font, main_states_1_range, main_states_1_colors)



    # --- Redirect buttons ---

    # create redirect buttons colors when mouse is outside button
    main_redirect_1_mouse_out_colors = MousePositionButtonColors(button=(0, 255, 255), font=(0, 0, 255))
    main_redirect_2_mouse_out_colors = MousePositionButtonColors(button=(0, 255, 255), font=(0, 0, 255))

    # create redirect buttons colors when mouse is over button
    main_redirect_1_mouse_over_colors = MousePositionButtonColors(button=(0, 255, 255), font=(0, 0, 255))
    main_redirect_2_mouse_over_colors = MousePositionButtonColors(button=(0, 255, 255), font=(0, 0, 255))

    # create redirect buttons colors
    main_redirect_1_colors = ButtonColors(main_redirect_1_mouse_over_colors, main_redirect_1_mouse_out_colors)
    main_redirect_2_colors = ButtonColors(main_redirect_2_mouse_over_colors, main_redirect_2_mouse_out_colors)

    # create redirect buttons fonts
    main_redirect_1_font = FloatFont("Arial", 70)
    main_redirect_2_font = FloatFont("Arial", 70)

    # create redirect buttons text
    main_redirect_1_text = "Exit"
    main_redirect_2_text = "Next"

    # create redirect buttons redirection states
    main_redirect_1_redirection = "STATE_EXIT"
    main_redirect_2_redirection = "STATE_SEC_MENU"

    # create redirect buttons
    main_redirect_1 = RedirectButton(main_redirect_1_font, main_redirect_1_text, main_redirect_1_redirection, main_redirect_1_colors)
    main_redirect_2 = RedirectButton(main_redirect_2_font, main_redirect_2_text, main_redirect_2_redirection, main_redirect_2_colors)



    # --- Buttons block ---

    # create buttons block initial size
    main_block_size = (500, 500)

    # create buttons matrix
    main_block_buttons_matrix = ((main_slide_1, main_slide_2, main_slide_3),
                                 (main_states_button_1,),
                                 (main_redirect_1, main_redirect_2))

    # create block vertical and horizontal margin
    main_block_vertical_margin = 20
    main_block_horizontal_margin = 20

    # create buttons block
    main_block = Block(main_block_size, main_block_buttons_matrix, main_block_vertical_margin, main_block_horizontal_margin)



    # --- Menu ---

    # define margin between title and block
    main_menu_title_block_margin = 30

    # define horizontal and vertical max size ratio
    main_menu_max_size_ratio = (0.80, 0.80)

    # define resize ratio
    main_menu_resize_ratio = 0.80

    # define menu state
    main_menu_state = "STATE_MAIN_MENU"

    # create menu
    main_menu = Menu(screen, main_title, main_block, main_menu_title_block_margin, main_menu_max_size_ratio, main_menu_resize_ratio, main_menu_state)

