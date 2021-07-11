# -*- coding: utf-8 -*-

resources = ['Трава', 'Бокситы', 'Уран', 'Маковая соломка', 'Сталь']

class Resources:

    def __init__(self, object_id, data):
        self.object_id = object_id
        self.data = data

        for res in resources:
            if res in ' '.join(data):
                self.type = res

        

    def __str__(self):
        return f'type:{self.type}'

    def __repr__(self):
        return self.__str__()


class Resource:

    def __init__(self, data):
        pass
