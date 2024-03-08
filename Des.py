# ============================================================================#
# = IMPORTS DES BIBLIOTHEQUES ET DES CLASSES                                 =#
# ============================================================================#
from random import *


class Des:

    # ============================================================================#
    # = CONSTRUCTEURS / DESTRUCTEUR                                              =#
    # ============================================================================#
    def __init__(self):
        self.__des_1 = 0
        self.__des_2 = 0
        self.__somme = 0
        self.__double = False

    # ============================================================================#
    # = ACCESSEURS                                                               =#
    # ============================================================================#
    @property
    def de_1(self):
        return self.__des_1

    @property
    def de_2(self):
        return self.__des_2

    @property
    def somme(self):
        return self.__somme

    @property
    def double(self):
        return self.__double

    # ============================================================================#
    # = METHODE                                                                  =#
    # ============================================================================#
    def lancer_des(self):
        self.__des_1 = randint(1, 6)
        self.__des_2 = randint(1, 6)

        self.__somme = self.__des_1 + self.__des_2

        if self.__des_1 == self.__des_2:
            self.__double = True
        else:
            self.__double = False

        return (self.__somme, self.__double)
