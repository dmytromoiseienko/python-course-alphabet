import random
import uuid

from constants import *


class Car:

    def __init__(self, price, type, producer, number, mileage):
        """ initialization attributes class Car and check it on type """
        self.price = price
        self.type = type
        self.producer = producer
        self.number = number
        self.mileage = mileage
        assert isinstance(price, float), 'type price expected "float"'
        assert type in CARS_TYPES, 'choose type from CARS_TYPES'
        assert producer in CARS_PRODUCER, 'choose producer from CARS_PRODUCER'
        assert isinstance(number, uuid.UUID), 'type number expected "uuid"'
        assert isinstance(mileage, float), 'type mileage expected "float"'

    def change_number(self):
        """ change car number """
        self.number = uuid.uuid4()

    def compare(self, other):
        """ compare prices cars and display it """
        if self.__eq__(other):
            print(f'price car {self.producer} == {other.producer}')
        elif self.__lt__(other):
            print(f'price car {self.producer} < {other.producer}')
        elif self.__ge__(other):
            print(f'price car {self.producer} > {other.producer}')

    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        return self.price == other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __str__(self):
        return f'Object of class Car() has 5 attributes: self.price - {self.price}$\n' \
            f'{" " * 40}self.type - {self.type}\n' \
            f'{" " * 40}self.producer - {self.producer}\n' \
            f'{" " * 40}self.number - {self.number}\n' \
            f'{" " * 40}self.mileage - {self.mileage}\n'


class Garage:

    def __init__(self, town, cars, places, owner=None):
        """ initialization attributes class Garage and check it on type """
        self.town = town
        self.cars = cars
        self.places = places
        self.owner = owner
        assert town in TOWNS, 'choose town from TOWNS'
        assert isinstance(cars, list), 'type cars expected "list"'
        assert isinstance(places, int), 'type places expected "int"'
        assert self.__le__(places), f'Garage can include only {self.places} car\n' \
            f'{" " * 16}PLS reload Garage'
        if owner:
            assert isinstance(places, uuid.UUID), 'type owner expected "uuid"'

    def hit_hat(self):
        """ display total price all cars in garage """
        print(f'Total price of all cars in garage: {self._sum_prices()}$')

    def add(self, new_car):
        """ Add car to Garage if it possible """
        if len(self.cars) < self.places:
            self.cars.append(new_car)
            print('Successful add new car to Garage')
        else:
            return 'No free place'

    def remove(self, old_car):
        """ Remove car from Garage if it possible """
        if old_car in self.cars:
            self.cars.remove(old_car)
            print('Successful remove car from Garage')
        else:
            print('No such car in the Garage')

    def _sum_prices(self):
        """ Sum all prices cars in Garage """
        return sum([i.price for i in self.cars])

    def __le__(self, other):
        return len(self.cars) <= other

    def __str__(self):
        return 'This is class Garage' \
               'you can use dir() to see it attributes'


class Cesar:

    def __init__(self, name, garages, register_id):
        """ initialization attributes class Garage and check it on type """
        self.name = name
        self.garages = garages
        self.register_id = register_id
        assert isinstance(name, str), 'type name expected "str"'
        assert isinstance(garages, list), 'type garages expected "list"'
        assert isinstance(register_id, uuid.UUID), 'type register_id expected "uuid"'

    def hit_hat(self):
        """ Display total price of all cars in all garages """
        print(f'Total price of all cars in all garages: {self._sum_prices()}$')

    def garage_count(self):
        """ Display total count of garages """
        print('Total count of garages: {}'.format(len(self.garages)))

    def cars_count(self):
        """ Display total cars in all garages """
        print(f'Amount cars in all garages: {sum([len(i.cars) for i in self.garages])}')

    def add_car(self, new_car, chosen_garage):
        """ Add car to garage if it possible """
        if chosen_garage.add(new_car) != 'No free place':
            chosen_garage.add(new_car)
        elif self._free_garage() != 'No free place':
            self._free_garage().add(new_car)
        else:
            print('No free place')

    def compare(self, other):
        """ compare cesar's """
        if self.__eq__(other):
            print(f'Cesar {self.name} and {other.name} are equal')
        elif self.__lt__(other):
            print(f'Cesar {self.name} less richer then {other.name}')
        elif self.__ge__(other):
            print(f'Cesar {self.name} richer {other.name}')

    def __lt__(self, other):
        return self._sum_prices() < other._sum_prices()

    def __eq__(self, other):
        return self._sum_prices() == other._sum_prices()

    def __ge__(self, other):
        return self._sum_prices() >= other._sum_prices()

    def _free_garage(self):
        """ looking for more free garage """
        more_free = cesar.garages[0]
        for i in cesar.garages:
            if (i.places - len(i.cars)) > (i.places - len(more_free.cars)):
                more_free = i
        if len(more_free.cars) == more_free.places:
            return 'No free place'
        else:
            return more_free

    def _sum_prices(self):
        """ Sum all prices cars in all garages """
        return sum([i._sum_prices() for i in self.garages])

    def __str__(self):
        return 'This is class Cesar' \
               'you can use dir() to see it attributes'


if __name__ == '__main__':
    car = Car(float(random.choice(range(20000, 50000))),
              random.choice(CARS_TYPES),
              random.choice(CARS_PRODUCER),
              uuid.uuid4(),
              float(random.choice(range(3000, 15000)))
              )
    car1 = Car(float(random.choice(range(20000, 50000))),
               random.choice(CARS_TYPES),
               random.choice(CARS_PRODUCER),
               uuid.uuid4(),
               float(random.choice(range(3000, 15000)))
               )
    # car.compare(car1)
    # print(car)
    cont_cars = [car]
    garage = Garage(random.choice(TOWNS),
                    cont_cars,
                    2,
                    )
    cont_cars = [car1]
    garage1 = Garage(random.choice(TOWNS),
                     cont_cars,
                     1,
                     )
    # garage.hit_hat()
    cont_garage = [garage, garage1]
    cesar = Cesar('I am',
                  cont_garage,
                  uuid.uuid4()
                  )
    cont_garage = [garage]
    cesar1 = Cesar('Hi',
                   cont_garage,
                   uuid.uuid4()
                   )
    cesar.compare(cesar1)
    # cesar.hit_hat()
    # cesar.cars_count()
    # cesar.add_car(car, garage)
    # print(cesar.garage_count().doc)
