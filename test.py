import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))

font = pygame.font.SysFont("Arial", 100)

font_surface = font.render("Test", True, (255, 255, 255))

font_surface_rect = font_surface.get_rect()

font_surface_rect.topleft = (100, 100)

resize = font_surface_rect.size

screen.blit(font_surface, font_surface_rect)

pygame.display.update()

loop_exit = False

while not loop_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop_exit = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                resize = int(resize[0] * 0.80), int(resize[1] * 0.80)
                screen.fill((0, 0, 0))
                font_surface = pygame.transform.scale(font_surface, resize)
                font_surface_rect = font_surface.get_rect()
                font_surface_rect.topleft = (100, 100)
                screen.blit(font_surface, font_surface_rect)
                pygame.display.update()
