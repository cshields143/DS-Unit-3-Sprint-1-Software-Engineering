#!/usr/bin/python
# -*- coding: utf-8 -*-
import random


class Product:

    def __init__(self, name, price=10, weight=20, flam=0.5):
        self.name = name
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = float(flam)
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        rat = self.price / self.weight
        if rat < 0.5:
            return 'Not so stealable...'
        elif rat < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        rat = self.weight * self.flammability
        if rat < 10.0:
            return '...fizzle.'
        elif rat < 50.0:
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):

    def __init__(self, name, price=10, weight=10, flam=0.5):
        super().__init__(name, price, weight, flam)

    def explode(self):
        return '...it\'s a glove.'

    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
