"""
Напишите программу, которая принимает текст и выводит два слова: то, которое встречается в тексте чаще всего, и самое длинное.
"""
from collections import Counter

text = 'лалава хочет поесть что-нибудь очень вкусное и вкусное чтобы поесть было очень вкусное'

words = text.split(' ')
collect = Counter(words)

most_common, counts = collect.most_common(1)[0]

longest = max(words, key=len)

print(most_common,longest)