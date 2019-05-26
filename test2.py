import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))

font = pygame.font.SysFont("Comic Sans MS", 10)

font_surface = font.render("asfhcasuGYUGYUgmacisdc", True, (255, 255, 255))

font_surface_rect = font_surface.get_rect()

print(font_surface_rect[3])

# exit_loop = False
#
# while not exit_loop:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit_loop = True


pygame.quit()