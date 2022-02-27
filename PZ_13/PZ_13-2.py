# Составить генератор (yield), который выводит из строки только буквы

from string import ascii_letters


def letters(lst):
    yield from [n for n in lst if n in ascii_letters]


A = "need to accept 23 questions for the test"

list1 = ""
for i in letters(A):
    list1 += i
print(list1)
