# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 22:13:37 2022

@author: Tohir
"""


narxlar = [1200, 33400, 12, -5, -10.6]

mevalar = ['Olma', 'Behi', 'o\'rik', 'shaftoli', 'uzum']

mevalar.sort()  
mevalar.sort(reverse=True)

narxlar.sort(reverse=True)

print(narxlar)

print(sorted(mevalar))

print(sorted(mevalar, reverse=True))

# listni indexsi buyicha teskari ↓

narxlar.reverse()

print(narxlar)

# list uzunligini topish len()

print(len(mevalar))

# range metodi

sonlar = list(range(30))
print(sonlar) 

sonlar = list(range(20,30))
print(sonlar) 

sonlar = list(range(1,30,2))  #qadam bilan renge qilish
print(sonlar) 

# max min qiymatlar

max_qiymat = max(narxlar)
min_qiymat = min(narxlar)

print(min_qiymat)
print(max_qiymat)

# yig`indisini chiqarish

print(sum(narxlar))

print(mevalar[0:3])

print(mevalar[:2])

print(mevalar[2:])

# listdan nuxsa olish

my_meva = mevalar[:]

print(my_meva)

#tuple list  →  o`zgarmas ro`yxatlar

toys = (12, 67, 'salom', 23.9)
print(toys)

