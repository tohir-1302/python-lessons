# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 11:05:26 2022

@author: Tohir
"""
ism = "Tohirbek"
familiya = 'Otaqulov'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)

# Misol yana

ism = "James"
familiya = 'Bond'
print(f"Salom, mening\t ismim {familiya}. {ism} {familiya}!")

########## .upper()  ##############

maktab = "mening maktabim 21 - maktab"
katta_harflar_bilan = maktab.upper()
print(katta_harflar_bilan) 

########## .lower()  ##############

maktab = "MENING MAKTABIM 21 - maktab"
kichik_harflar_bilan = maktab.lower()
print(kichik_harflar_bilan) 

########## lstrip() — matn boshidagi bo'shliqni,
########## rstrip() – matn oxiridagi bo`shliqni,
########## strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi 

ism = input("Ismingiz nima?")
print("Assalom alaykum, " + ism)