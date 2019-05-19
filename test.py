import pygame

exit_loop = False

pygame.init()

screen = pygame.display.set_mode((1000, 1000))

while not exit_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_loop = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.button)

        if event.type == pygame.MOUSEBUTTONUP:
            print(event.button)