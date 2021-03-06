"""
Напишите программу, которая принимает текст и выводит два слова: то, которое встречается в тексте чаще всего, и самое длинное.
"""

from collections import Counter

text = 'Существуют две основные трактовки понятия «текст»: имманентная (расширенная, философски нагруженная) и репрезентативная (более частная). ' \
       'Имманентный подход подразумевает отношение к тексту как к автономной реальности, нацеленность на выявление его внутренней структуры. ' \
       'Репрезентативный — рассмотрение текста как особой формы представления информации о внешней тексту действительности.'

words = [i for i in text.split(' ')]
collect = Counter(words)

most, *occupancy = collect.most_common()
largest = max(words,key=len)

print(most[0], largest)
