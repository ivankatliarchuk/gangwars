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

    def describe(self):
    # self is the member here
        return self.name, self.value

    def __str__(self):
        return f'{self.value}'
