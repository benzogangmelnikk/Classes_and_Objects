# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:

	def __init__(self):
		self.name = 'Вода'

	def __str__(self):
		return self.name

	def __eq__(self, other):
		return self.name == other.name

	def __add__(self, other):
		new_obj = None
		if other == Air():
			new_obj = Storm()
		elif other == Fire():
			new_obj = Steam()
		elif other == Earth():
			new_obj = Mud()
		elif other == Sand():
			new_obj = Clay()
		return new_obj


class Air:

	def __init__(self):
		self.name = 'Воздух'

	def __str__(self):
		return self.name

	def __eq__(self, other):
		return self.name == other.name

	def __add__(self, other):
		new_obj = None
		if other == Water():
			new_obj = Storm()
		elif other == Fire():
			new_obj = Lightning()
		elif other == Earth():
			new_obj = Dust()
		elif other == Sand():
			new_obj = Hurricane()
		return new_obj


class Earth:

	def __init__(self):
		self.name = 'Земля'

	def __str__(self):
		return self.name

	def __eq__(self, other):
		return self.name == other.name

	def __add__(self, other):
		new_obj = None
		if other == Water():
			new_obj = Mud()
		elif other == Air():
			new_obj = Dust()
		elif other == Fire():
			new_obj = Lava()
		elif other == Sand():
			new_obj = Ground()
		return new_obj


class Fire:

	def __init__(self):
		self.name = 'Огонь'

	def __str__(self):
		return self.name

	def __eq__(self, other):
		return self.name == other.name

	def __add__(self, other):
		new_obj = None
		if other == Water():
			new_obj = Steam()
		elif other == Air():
			new_obj = Lightning()
		elif other == Earth():
			new_obj = Lava()
		elif other == Sand():
			new_obj = Glass()
		return new_obj


class Storm:
	def __init__(self):
		self.name = 'Шторм'

	def __str__(self):
		return self.name


class Mud:

	def __init__(self):
		self.name = 'Грязь'

	def __str__(self):
		return self.name


class Steam:

	def __init__(self):
		self.name = 'Пар'

	def __str__(self):
		return self.name


class Lightning:

	def __init__(self):
		self.name = 'Молния'

	def __str__(self):
		return self.name


class Dust:

	def __init__(self):
		self.name = 'Пыль'

	def __str__(self):
		return self.name


class Lava:
	def __init__(self):
		self.name = 'Лава'

	def __str__(self):
		return self.name


print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Air(), '+', Earth(), '=', Earth() + Air())
print(Fire(), '+', Earth(), '=', Earth() + Fire())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.


class Sand:
	def __init__(self):
		self.name = 'Песок'

	def __str__(self):
		return self.name

	def __eq__(self, other):
		return self.name == other.name

	def __add__(self, other):
		new_obj = None
		if other == Water():
			new_obj = Clay()
		elif other == Air():
			new_obj = Hurricane()
		elif other == Fire():
			new_obj = Glass()
		elif other == Earth():
			new_obj = Ground()
		return new_obj


class Clay:
	def __init__(self):
		self.name = 'Глина'

	def __str__(self):
		return self.name


class Hurricane:
	def __init__(self):
		self.name = 'Ураган'

	def __str__(self):
		return self.name


class Glass:
	def __init__(self):
		self.name = 'Стекло'

	def __str__(self):
		return self.name


class Ground:
	def __init__(self):
		self.name = 'Грунт'

	def __str__(self):
		return self.name


print('\n', Water(), '+', Sand(), '=', Water() + Sand())
print(Sand(), '+', Air(), '=', Sand() + Air())
print(Sand(), '+', Earth(), '=', Sand() + Earth())
print(Fire(), '+', Sand(), '=', Fire() + Sand())