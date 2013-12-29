# -*- coding: utf-8 -*-
import os

while(True):
    annee = input("Saisissez une année : ") # On attend que l'utilisateur saisisse l'année qu'il désire tester
    if annee.isdigit():
        annee = int(annee)
        if annee%400 == 0 or (annee%4 == 0 and annee % 100 != 0):
            os.system("cls")
            print("c'est une année bissextile")
        else:
            os.system("cls")
            print("ce n'est pas une année bissextile")#Sinon, elle est bissextile.
    else:
        os.system("cls")
        print("variable incorrect")
         
         
