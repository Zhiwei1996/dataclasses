#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import *


@dataclass
class Person(object):
    __annotations__ = {'name': str, 'age': int, 'tel': str}

    name = field(default_factory=str, hash=True)


@dataclass
class InventoryItem(object):
    """Class for keeping track of an item in inventory."""
    __annotations__ = {'name': str, 'unit_price': float, 'quantity_on_hand': int}
    quantity_on_hand = 0

    def total_cost(self):
        return self.unit_price * self.quantity_on_hand


if __name__ == '__main__':
    item = InventoryItem(name='hammers', unit_price=10.49, quantity_on_hand=12)
    # data = {'name': 'hammers', 'unit_price': 10.49, 'quantity_on_hand': 12}
    # item = InventoryItem(**data)
    print(item.__dict__)
    print('total_cost: {}'.format(item.total_cost()))
    person = Person(name='xiaoming', age='25', tel='10086')
    print(person.__dict__)
