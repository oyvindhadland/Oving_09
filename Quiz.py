# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:29:19 2021

@author: oyvin
"""

# Importerer Fleirvalstest class som Fvt
import Fleirvalstest as Fvt

# Lagar funksjon
def main():
        
    # Setter poengsum for spelarar lik 0
    poeng_spelar_1 = 0
    poeng_spelar_2 = 0
   
    # Leser inn fil og deler opp i spm, fasit og svar alternativ
    with open("sporsmaalsfil.txt", "r", encoding="UTF8") as spm:
        for linje in spm:
            i_linje = linje.split(":")
            liste = i_linje[2]
            liste = liste.replace("[", "")
            liste = liste.replace("]", "")
            liste = liste.split(",")
                       
            # Lagar objekt gjennom __init_ i Fvt
            quiz = Fvt.Fleirvalstest(i_linje[0], int(i_linje[1]),
                             liste)
                
            # Skriver ut spørsmål og alternativ frå __str__ i Fvt
            print(quiz)
            
            # Tek inn svar frå spelarane
            print("Skriv inn svar:")
            svar_spelar_1 = int(input("Spelar 1: "))
            svar_spelar_2 = int(input("Spelar 2: "))
            
            # Sjekker om svaret gjennom sjekka_svar i Fvt,
            # og skriv legg til poeng for kvar   
            if quiz.sjekka_svar(svar_spelar_1):
                poeng_spelar_1 += + 1
            if quiz.sjekka_svar(svar_spelar_2):
                poeng_spelar_2 += + 1
                
            # Skriver ut rett svar
            korrekt_svar = quiz.korrekt_svar_tekst()
            print(korrekt_svar)
        
    # Skriver ut poengsum til spelarane
    print(f"Spelar 1 fekk {poeng_spelar_1} poeng.\n")
    print(f"Spelar 2 fekk {poeng_spelar_2} poeng.\n")
    
    # Skriver ut kven som vann
    if poeng_spelar_1 > poeng_spelar_2:
        print("Spelar 1 vann.")
    elif poeng_spelar_1 == poeng_spelar_2:
        print("Spelarane fekk like mange poeng.")
    else:
        print("Spelar 2 vann.")

# if__name__
if __name__ == "__main__":
    main()