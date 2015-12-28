#!/usr/bin/python -tt
# encoding: utf-8
from __future__ import print_function
import re

# Найдите в тексте англ слова, заканчивающиеся на ly
# и выделите их при помощи тегов <i> и </i>,
# например "drive carefully" -> "drive <i>carefully</i>"
def mark_adverbs(text):
    import re
    # +++your code here+++

    text = re.sub(u'(\w+ly)', r'<i>\1</i>', text)
    return text

# Найдите англ. и русские слова, в которые есть три (возможно, разных) 
# гласных подряд и возвратите их в нижнем регистре в виде списка
def find_triple_vowel_words(text):
    #p = re.compile(r'(\b\w+)\s+\1')
    #p.search(text).group()
    # +++your code here+++
    return 

# Найдите слова, в которые есть две гласных подряд:
# они могут быть разные, если аргумент "same" имеет значение "ложь"
# и должны быть одинаковы, если "истина".
# Возвратите отсортированный список без повторов
def find_double_vowel_words(text, same=False):
    # +++your code here+++
    return

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
    print('mark_adverbs')
    test(mark_adverbs('He spoke quickly and angrily'), 
                      'He spoke <i>quickly</i> and <i>angrily</i>')
    test(mark_adverbs('Free lyrics web sites are "completely illegal"'),
                      'Free lyrics web sites are "<i>completely</i> illegal"')
    test(mark_adverbs('He meticulously called everybody from la to ly in the phonebook'), 
                      'He <i>meticulously</i> called everybody from la to ly in the phonebook')
  
    print()
    print('find_triple_vowel_words')
    test(find_triple_vowel_words('He saw a sihlouette of a a a a beautiful queen.'), \
          ['sihlouette', 'beautiful', 'queen'])
    test(find_triple_vowel_words('The ravioli was rather DELICIOUS!!'), ['delicious'])
    test(find_triple_vowel_words(u'Жираф - животное длинношеее'), ['длинношеее'])

    print()
    print('find_double_vowel_words')
    test(find_double_vowel_words('When Harry met Sally'), [])
    test(find_double_vowel_words('They found many fishhooks as they stood by the brook.'), \
            ['brook', 'fishhooks', 'found', 'stood', 'they'])
    test(find_double_vowel_words('They found many fishhooks as they stood by the brook.', True), \
            ['brook', 'fishhooks', 'stood'])
    
if __name__ == '__main__':
    main()
