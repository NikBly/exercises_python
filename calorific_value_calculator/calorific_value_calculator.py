# -*- coding: utf-8 -*- 

#Metabolism (PPM) Harrisa-Benedicta

#name
name = input ("What's your name? ")

#W zależności od płci odpowieni wzór
# print ("Enter your sex: ") 

#converting string into float
weight = float (input("How much do you weight? "))

#converting string into float
height = float (input("What is your height? "))

#converting string into integer
age = int (input("How old are you? "))

#PPM for woman
PPM_woman = (655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age))

#PPM for man
PPM_man = (66.5 + (13.75 * weight) + (5.003 * height) - (6.77 * age))

print ("Your PPM is", PPM_woman)

print ("Your PPM is", PPM_man)


#
