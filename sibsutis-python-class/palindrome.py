#!/usr/bin/python -tt
# encoding: utf-8
from __future__ import print_function
import re

# Проверьте, является ли строка палиндромом, то есть читается
# ли она справа налево так же, как слева направо
# Используйте регулярные выражения для того, чтобы исклчюить знаки
# пунктуации, саму проверку лучше сделать обычными строковыми операциями
def is_palindrome(string):
    # +++your code here+++
    string = string.lower()
    string = string.replace('_','')
    #print (string)
    string = re.sub(u'\W+', u'', string)
    #print (string)
    if string == string[::-1]:
        return True
    else:
        return False
    

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print((u'%s got: %s expected: %s' % (prefix, repr(got), repr(expected))))


def main():
    print('words')
    test(is_palindrome(u'level'), True)
    test(is_palindrome(u'paper'), False)
    test(is_palindrome(u'aiboh_phobia'), True)
    test(is_palindrome(u'топот'), True)
    test(is_palindrome(u'ворон'), False)
    
    print()
    print('sentences')
    test(is_palindrome(u'Step on no pets'), True)
    test(is_palindrome(u'Madam, I\'m Adam'), True)
    test(is_palindrome(u'Was it a car or a cat I saw?'), True)
    test(is_palindrome(u'A Toyota\'s a Toyota'), True)
    test(is_palindrome(u'А роза упала на лапу Азора.'), True)
    test(is_palindrome(u'Аргентина манит негра'), True)
    test(is_palindrome(u'"Пустите!" - Летит супу миска Максиму. - "Пустите, летит суп!"'), True)
    
    print()
    print('other languages')
    test(is_palindrome(u'שבדבש'), True)
    test(is_palindrome(u'Ελληνικά'), False)
    test(is_palindrome(u'Νιψον ανομηματα μη μοναν οψιν'), True)
    test(is_palindrome(u'上海自来水来自海上'), True)

if __name__ == '__main__':
    main()
