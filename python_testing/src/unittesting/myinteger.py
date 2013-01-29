#!/usr/bin/env python
"""
MyInteger is an example class for the purpose of discussing tests.

>>> i = MyInteger(2)
>>> i.add(2)
4
>>> i.subtract(2)
0
>>> i.divide(2)
1
>>> i.multiply(3)
6
"""


class MyInteger(object):

    def __init__(self, i):
        self.myint = i

    def add(self, j):
        return self.myint + j

    def subtract(self, j):
        return self.myint - j

    def op(self, j, op):
        if op == 'divide':
            return self.myint / j
        elif op == 'multiply':
            return self.myint * j

    def divide(self, j):
        return self.op(j, 'divide')

    def multiply(self, j):
        return self.op(j, 'multiply')
