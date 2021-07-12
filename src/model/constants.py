# -*- coding: utf-8 -*-

from enum import Enum, unique

@unique
class Res(Enum):
    TRAVA = 'Трава'
    URAN = 'Уран'
    MAK = 'Маковая соломка'
    BOXITY = 'Бокситы'
    STAL = 'Сталь'
    ALUMINII = 'Алюминий'
    GANJIUM = 'Ганджиум'

    def describe(self):
    # self is the member here
        return self.name, self.value

    def experience(self):
        return {
            Res.URAN : {
                'units': 10,
                'value': 1
            },
            Res.TRAVA : {
                'units': 10,
                'value': 1
            },
            Res.STAL : {
                'units': 5,
                'value': 1
            },
            Res.BOXITY: {
                'units': 5,
                'value': 1
            },
            Res.MAK: {
                'units': 10,
                'value': 1
            },
            Res.ALUMINII: {
                'units': 5,
                'value': 1
            },
            Res.GANJIUM: {
                'units': 5,
                'value': 1
            }
        }[self.name]

    def __str__(self):
        return f'{self.value}'
