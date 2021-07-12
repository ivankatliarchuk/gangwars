# -*- coding: utf-8 -*-

class Cost:

    def __init__(self, operation, type):
        self.operation = operation
        self.type = type
        self.total = 0
        self.costs = set()
        if self.operation == 'sell':
            self.experience = 0


    def add(self, total, cost):
        # if self.operation == 'sell':
        #     units = total / cost
        #     units= units % self.type.experience()['units']
        #     self.experience = units * self.type.experience()['value']
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
