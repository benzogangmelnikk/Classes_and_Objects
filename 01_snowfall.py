# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self, x_cord, y_cord, length):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.length = length

    def clear_previous_picture(self):
        sd.snowflake(sd.get_point(self.x_cord, self.y_cord), self.length, sd.background_color)

    def move(self):
        self.x_cord += sd.random_number(-25, 25)
        self.y_cord -= 10

    def draw(self):
        sd.snowflake(sd.get_point(self.x_cord, self.y_cord), self.length, sd.COLOR_YELLOW)

    def can_fall(self):
        return self.y_cord > 5


flakes_list = []


def get_flakes(count):
    for i in range(0, count):
        new_flake = Snowflake(sd.random_number(150, 500), sd.random_number(150, 500), sd.random_number(20, 150))
        flakes_list.append(new_flake)
    return flakes_list


def get_fallen_flakes():
    fallen_flakes = 0
    for flake in flakes_list:
        if not flake.can_fall():
            fallen_flakes += 1
    return fallen_flakes


def append_flakes(count):
    for i in range(0, count):
        clear_fallen_flake = flakes_list[i].clear_previous_picture()
        delete_fallen_flake = flakes_list.pop(i)
        new_flake = Snowflake(sd.random_number(150, 500), sd.random_number(150, 500), sd.random_number(20, 150))
        flakes_list.append(new_flake)
# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке


flakes = get_flakes(count=10)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
        fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
