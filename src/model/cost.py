# -*- coding: utf-8 -*-

class Cost:

    def __init__(self, operation, type):
        self.operation = operation
        self.type = type
        self.total = 0
        self.costs = set()
        if self.operation == 'sell':
            self.experience = 0
            self.units = 0


    def add(self, total, cost):
        if self.operation == 'sell':
            units = total / cost
            per_unit = self.type.experience(self.type)['units']
            per_value = self.type.experience(self.type)['value']
            self.units= units / per_unit
            self.experience += int(self.units * per_value)
        self.total += total
        self.costs.add(cost)


    def cost(self):
        result = ''
        count = 0
        for el in self.costs:
            count += 1
            if count < len(self.costs):
                result += f'{el},'
            else:
                result += f'{el}'
        return result

    def __str__(self):
        return f'cost. total:{self.total}, cost:{self.cost}'

    def __repr__(self):
        return self.__str__()
