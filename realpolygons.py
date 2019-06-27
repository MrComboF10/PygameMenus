import pygame


class RealRect:
    def __init__(self, screen_display, color, real_top_left_point, real_size, real_width=0):
        self.__screen_display = screen_display
        self.__color = color
        self.__real_top_left_point = real_top_left_point
        self.__real_size = real_size
        self.__real_width = real_width

        # top left point
        self.__round_top_left_point = self.__calculate_round_top_left_point()

        # down left point
        self.__round_down_left_point = self.__calculate_round_down_left_point()

        # top right point
        self.__round_top_right_point = self.__calculate_round_top_right_point()

        # down right point
        self.__round_down_right_point = self.__calculate_round_down_right_point()

    def __calculate_round_top_left_point(self):
        return round(self.__real_top_left_point[0]), round(self.__real_top_left_point[1])

    def __calculate_round_down_left_point(self):
        return round(self.__real_top_left_point[0]), round(self.__real_top_left_point[1] + self.__real_size[1])

    def __calculate_round_top_right_point(self):
        return round(self.__real_top_left_point[0] + self.__real_size[0]), round(self.__real_top_left_point[1])

    def __calculate_round_down_right_point(self):
        return round(self.__real_top_left_point[0] + self.__real_size[0]), round(self.__real_top_left_point[1] + self.__real_size[1])

    def draw(self):
        pygame.draw.polygon(self.__screen_display, self.__color, [self.__round_top_left_point, self.__round_down_left_point, self.__round_down_right_point, self.__round_top_right_point], round(self.__real_width))

