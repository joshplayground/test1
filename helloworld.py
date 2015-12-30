#!/usr/bin/env python3
print ("Hello World")

# coding: utf-8
 
numbers = ('1','2','3','4','5','6','7','8','9','0')
letters = ('a','b','c','d','e','f')
punct = ('.', '!', '?')
charSetDict = {numbers:[], letters:[], punct:[]}
 
def display_cset (cset):
   print
   for x in cset.items():
      if x[0] == numbers:
         print ("Liczby:")
      elif x[0] == letters:
         print ("Litery:")
      elif x[0] == punct:
         print ("Znaki interpunkcyjne:")
      else:
         print ("Nieznane:")
      print (x[1])
 
# Dodanie nowych wartości do kluczy
cSet = input("Wstawienie znakow: ")
for c in cSet:
   for x in charSetDict.keys():
      if c in x:
         charSetDict[x].append(c)
         break;
 
display_cset(charSetDict)
 
# Dodanie nowego klucza i wartości
charSetDict["Special"] = ['%', '$', '^']
display_cset(charSetDict)
 
# Zmiana wartości dla istniejącego klucza
charSetDict["Special"] = '><'
 
display_cset(charSetDict)
