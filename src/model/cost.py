# -*- coding: utf-8 -*-

class Cost:

    def __init__(self, operation):
        self.operation = operation
        self.total = 0
        self.cost = set()


    def add(self, total, cost):
        self.total += total
        self.cost.add(cost)

    def __str__(self):
        return f'cost. total:{self.total}, cost:{self.cost}'

    def __repr__(self):
        return self.__str__()
