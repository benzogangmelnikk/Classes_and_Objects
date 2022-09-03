# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint


# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            self.fullness += 20
            cprint('{} поел'.format(self.name), color='yellow')
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 30:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 30
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness < 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.house.food < 20:
            self.shopping()
        elif self.fullness < 20:
            self.eat()
        elif self.house.money < 50:
            self.work()
        elif self.house.food_for_cat < 10:
            self.buy_cats_food()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.clean_house()
        else:
            self.watch_MTV()

    def take_cat(self, cat):
        if self.house:
            cat.house = self.house
            cprint('{} взял в дом кота {}'.format(self.name, cat.name), color="green")
        else:
            cprint('У {} нет дома! Какой кот?'.format(self.name), color="red")

    def buy_cats_food(self):
        if self.house.money > 30:
            self.house.food_for_cat += 50
            self.house.money -= 30
            cprint('{} купил еды для кота'.format(self.name), color="cyan")
        else:
            cprint('{} нет денег'.format(self.name), color="red")

    def clean_house(self):
        if self.house.mud >= 50:
            self.house.mud -= 50
            self.fullness -= 20
            cprint('{} убрался в доме'.format(self.name), color="magenta")


class Cat:

    def __init__(self, name):
        self.fullness = 20
        self.house = None
        self.name = name

    def __str__(self):
        return 'Я кот {}, сытость {}'.format(self.name, self.fullness)

    def sleep(self):
        self.fullness -= 10
        cprint('Кот {} поспал'.format(self.name), color="blue")

    def eat(self):
        self.fullness += 10
        self.house.food_for_cat -= 10
        cprint('Кот {} поел'.format(self.name), color="green")

    def scratch_wallpapers(self):
        self.fullness -= 10
        self.house.mud += 5
        cprint('Кот {} подрал обои'.format(self.name), color="yellow")

    def act(self):
        if self.fullness <= 0:
            cprint('Кот {} умер...'.format(self.name), color="red")
            return
        sleep_or_scratch = randint(1, 3)
        if self.fullness <= 10:
            self.eat()
        elif sleep_or_scratch == 1:
            self.sleep()
        elif sleep_or_scratch == 2:
            self.scratch_wallpapers()
        else:
            self.eat()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.food_for_cat = 0
        self.mud = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, еды для кота осталось {}, количество грязи в доме {}'.format(
            self.food, self.money, self.food_for_cat, self.mud)


kenny = Man(name='Кенни')

cats = [
    Cat(name='Барсик'),
    Cat(name='Вася'),
    Cat(name='Марго')
]

taked_cats = []

my_sweet_home = House()

kenny.go_to_the_house(house=my_sweet_home)


for cat_number, cat in enumerate(cats):
    if cat_number < 3:
        kenny.take_cat(cat)
        taked_cats.append(cat)
    else:
        print('Слишком много котов для ' + kenny.name)
        break

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    kenny.act()
    for cat in taked_cats:
        cat.act()
    print('--- в конце дня ---')
    print(kenny)
    for cat in taked_cats:
        print(cat)

    print(my_sweet_home)

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
