class Cat:

    def __init__(self, age):
        self.age = age
        self.average_speed = self._set_average_speed()
        self.saturation_level = 50
        self.cats_product = {'fodder': 10, 'apple': 5, 'milk': 2, 'gazelle': 30, 'rabbit': 15}

    def eat(self, product):
        try:
            self._increase_saturation_level(self.cats_product[product])
        except KeyError:
            print('wrong')

    def run(self, hours):
        ran_km = self._set_average_speed() * hours
        if ran_km in range(0, 26):
            self._reduce_saturation_level(2)
        elif ran_km in range(26, 51):
            self._reduce_saturation_level(5)
        elif ran_km in range(51, 101):
            self._reduce_saturation_level(15)
        elif ran_km in range(101, 201):
            self._reduce_saturation_level(25)
        else:
            self._reduce_saturation_level(50)
        return f'Your cat ran {ran_km} kilometers'

    def get_saturation_level(self):
        if self.saturation_level == 0:
            result = 'Your cat is died :('
        else:
            result = self.saturation_level
        return result

    def get_average_speed(self):
        return self.average_speed

    def _reduce_saturation_level(self, value):
        if (self.saturation_level - value) < 0:
            self.saturation_level = 0
        else:
            self.saturation_level -= value

    def _increase_saturation_level(self, value):
        if (self.saturation_level + value) > 100:
            self.saturation_level = 100
        else:
            self.saturation_level += value

    def _set_average_speed(self):
        if self.age <= 7:
            result = 12
        elif self.age >= 11:
            result = 6
        else:
            result = 9
        return result


class Cheetah(Cat):

    def _set_average_speed(self):
        if self.age <= 5:
            result = 90
        elif self.age >= 16:
            result = 40
        else:
            result = 75
        return result


class Wall:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def wall_square(self):
        return self.width * self.height

    def number_of_rolls_of_wallpaper(self, roll_width_m, roll_length_m):
        count_lines_roll = round(roll_length_m / self.height)
        count_lines = round(self.width / roll_width_m)
        return count_lines / count_lines_roll


class Roof:

    def __init__(self, width, height, roof_type):
        if not (roof_type in ['gable', 'single-pitch']):
            raise ValueError('Sorry there is only two types of roofs')
        self.width = width
        self.height = height
        self.roof_type = roof_type
        self.square = {'gable': self.width * self.height * 2, 'single-pitch': self.width * self.height}

    def roof_square(self):
        return self.square[self.roof_type]


class Window:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def window_square(self):
        return self.width * self.height


class Door:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.wood_price = 10
        self.metal_price = 3

    def door_square(self):
        return self.width * self.height

    def door_price(self, material):
        if not (material in ['wood', 'metal']):
            raise ValueError('Sorry there is only two types of material')
        elif material == 'wood':
            result = self.door_square() * self.wood_price
        else:
            result = self.door_square() * self.metal_price
        return result

    def update_wood_price(self, new_price):
        self.wood_price = new_price

    def update_metal_price(self, new_price):
        self.metal_price = new_price


class House:

    def __init__(self):
        self.__walls = []
        self.__windows = []
        self.__roof = None
        self.__door = None

    def create_wall(self, width, height):
        if width == 0 or height == 0:
            raise ValueError('Value must be not 0')
        elif len(self.__walls) > 3:
            raise ValueError('Our house can not have more than 4 walls')
        else:
            self.__walls.append(Wall(width, height))

    def create_roof(self, width, height, roof_type):
        if self.__roof:
            raise ValueError('The house can not have two roofs')
        elif width == 0 or height == 0:
            raise ValueError('Value must be not 0')
        else:
            self.__roof = Roof(width, height, roof_type)

    def create_window(self, width, height):
        if width == 0 or height == 0:
            raise ValueError('Value must be not 0')
        else:
            self.__windows.append(Window(width, height))

    def create_door(self, width, height):
        if self.__door:
            raise ValueError('The house can not have two doors')
        elif width == 0 or height == 0:
            raise ValueError('Value must be not 0')
        else:
            self.__door = Door(width, height)

    def get_count_of_walls(self):
        return len(self.__walls)

    def get_count_of_windows(self):
        return len(self.__windows)

    def get_door_price(self, material):
        return self.__door.door_price(material)

    def update_wood_price(self, new_price):
        self.__door.update_wood_price(new_price)

    def update_metal_price(self, new_price):
        self.__door.update_metal_price(new_price)

    def get_roof_square(self):
        return self.__roof.roof_square()

    def get_walls_square(self):
        return sum([i.wall_square() for i in self.__walls])

    def get_windows_square(self):
        return sum([i.window_square() for i in self.__windows])

    def get_door_square(self):
        return self.__door.door_square()

    def get_number_of_rolls_of_wallpapers(self, roll_width_m, roll_length_m):
        if roll_width_m == 0 or roll_length_m == 0:
            raise ValueError('Sorry length must be not 0')
        return round(sum([i.number_of_rolls_of_wallpaper(roll_width_m, roll_length_m) for i in self.__walls]))

    def get_room_square(self):
        return self.get_walls_square() - (self.get_windows_square() + self.get_door_square())
