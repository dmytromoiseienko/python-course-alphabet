import random
import uuid

from constants import *


class Car:

    def __init__(self, price, type, producer, number, mileage):
        """ initialization attributes class Car """
        self.price = price
        self.type = type
        self.producer = producer
        self.number = number
        self.mileage = mileage

    def change_number(self):
        """ change car number """
        self.number = uuid.uuid4()

    def expensive(self, *args):
        """ display cars from more expansive to cheaper """
        cont_cars = {}
        for i in args:
            cont_cars[i.price] = '{} with number {}'.format(i.producer, i.number)
        cont_cars = sorted(cont_cars.items(), key=lambda kv: kv[0])
        [print('{}$ for {}'.format(i[0], i[1])) for i in reversed(cont_cars)]

    def cheaper(self, *args):
        """ display cars from more cheaper to more expensive """
        cont_cars = {}
        for i in args:
            cont_cars[i.price] = '{} with number {}'.format(i.producer, i.number)
        cont_cars = sorted(cont_cars.items(), key=lambda kv: kv[0])
        [print('{}$ for {}'.format(i[0], i[1])) for i in cont_cars]

    def __repr__(self):
        """ display attributes class Car """
        # print('вызвал repr')
        return 'Car atributes: ' \
               'price - {}$, ' \
               'type - {}, ' \
               'producer - {}, ' \
               'number - {}, ' \
               'mileage - {}'.format(self.price, self.type, self.producer, self.number, self.mileage)

    def __str__(self):
        # print('вызвал str')
        return self.__repr__()


class Garage:

    def __init__(self, town, cars, places, owner=None):
        """ initialization attributes class Garage """
        self.town = town
        self.cars = cars
        self.places = places
        self.owner = owner
        if len(self.cars) > self.places:
            print('Garage can include only {} car\nPLS reload Garage'.format(self.places))

    def hit_hat(self):
        """ Sum all prices cars in Garage and display it """
        sum = 0
        for i in self.cars:
            sum += i.price
        # print('Total price of all cars in garage: {}$'.format(sum))
        return sum

    def add(self, new_car):
        """ Add car to Garage """
        if len(self.cars) < self.places:
            self.cars.append(new_car)
            print('Successful add new car to Garage')
        else:
            return 'No free place'

    def remove(self, old_car):
        """ Remove car from Garage """
        if old_car in self.cars:
            self.cars.remove(old_car)
            print('Successful remove car from Garage')
        else:
            print('No such car in the Garage')

    def __repr__(self):
        return 'This is class Garage' \
               'you can use dir() to see it attributes'

    def __str__(self):
        # print('вызвал str')
        return self.__repr__()


class Cesar:

    def __init__(self, name, garages, register_id):
        """ initialization attributes class Garage """
        self.name = name
        self.garages = garages
        self.register_id = register_id

    def hit_hat(self):
        """ Sum all prices cars in all garages and display it """
        sum_all_cars = 0
        for i in self.garages:
            sum_all_cars += i.hit_hat()
        # print('Total price of all cars in all garages: {}$'.format(sum_all_cars))
        return sum_all_cars

    def garage_count(self):
        """ Sum all count garages and display it """
        print('Total count of garages: {}'.format(len(self.garages)))

    def cars_count(self):
        """ Sum all count cars in all garages and display it """
        sum_count = 0
        for i in self.garages:
            sum_count += len(i.cars)
        print('Total count of cars: {}'.format(sum_count))

    def add_car(self, new_car, chosen_garage):
        """ Add car to garage if it possibly """
        if chosen_garage.add(new_car) != 'No free place':
            chosen_garage.add(new_car)
        elif self.free_garage() != 'No free place':
            self.free_garage().add(new_car)
        else:
            print('No free place')

    def free_garage(self):
        """ looking for more free garage """
        more_free = cesar.garages[0]
        for i in cesar.garages:
            if len(i.cars) < len(more_free.cars):
                more_free = i
        if len(more_free.cars) == more_free.places:
            return 'No free place'
        else:
            return more_free

    def expensive(self, *args):
        """ display cesar from richest to poorer """
        price_cars = {}
        for i in args:
            price_cars[i.hit_hat()] = i.name
        price_cars = sorted(price_cars.items(), key=lambda kv: kv[0])
        [print('{}$ total price cars of cesar - {}'.format(i[0], i[1])) for i in reversed(price_cars)]

    def cheaper(self, *args):
        """ display cesar from poorer to richest """
        price_cars = {}
        for i in args:
            price_cars[i.hit_hat()] = i.name
        price_cars = sorted(price_cars.items(), key=lambda kv: kv[0])
        [print('{}$ total price cars of cesar - {}'.format(i[0], i[1])) for i in price_cars]

    def __repr__(self):
        pass

    def __str__(self):
        # print('вызвал str')
        return self.__repr__()
