# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 10:42:26 2021

@author: oyvin
"""

# Lager klasse
class Fleirvalstest:
    
    # Konstruktør av spørsmål, svar alternativ og fasit
    def __init__(self, spm, fasit, svar_alt):
        self.__spm = spm
        self.__svar_alt = svar_alt
        self.__fasit = fasit
    
    # Sjekk metode
    def sjekka_svar(self, sjekk):
        if sjekk == self.__fasit + 1:
            return True
        return False
    
    # Korrekt svar metode
    def korrekt_svar_tekst(self):
        return f"\nRett svar var{self.__svar_alt[self.__fasit]}.\n"
    
    # __str__ metode: print av spørsmål og alternativ    
    def __str__(self):
        testtekst = self.__spm  + "\n"
        for key, value in enumerate(self.__svar_alt):
            testtekst += f"({key+1}) {value} \n" 
        return testtekst
    
    test
