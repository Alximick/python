#!/usr/bin/python -tt
# encoding: utf-8

# Реализуйте функцию, которая возвращала бы побайтовое 
# представление строки в заданной кодировке
# в виде списка чисел в десятичной системе счисления
# 
# Подсказка: ord(x) возвращает десятичное значение кода символа x
import sys
def ordinal(text, encoding='utf-8'):
    # +++your code here+++
    a = []
    text = text.encode(encoding)
    for i in text:
        a.append(ord(i))
    return a

def test(got, expected):
    print('{} got: {} expected: {}'.format(
       ' OK ' if got == expected else '  X ', 
       repr(got), repr(expected)))


if __name__ == '__main__':
    test(ordinal('cat'), [99, 97, 116])
    test(ordinal(u'кот', 'cp1251'), [234, 238, 242])
    test(ordinal(u'кот', 'utf8'), [208, 186, 208, 190, 209, 130])
    test(ordinal(u'γάτα', 'cp1253'), [227, 220, 244, 225])
    test(ordinal(u'côté', 'latin1'), [99, 244, 116, 233])
    test(ordinal('cat', 'utf16'), [255, 254, 99, 0, 97, 0, 116, 0])

