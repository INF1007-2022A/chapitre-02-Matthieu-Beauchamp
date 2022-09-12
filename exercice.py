#!/usr/bin/env python
# -*- coding: utf-8 -*-

def assertChar(char: str) -> None:
    if len(char) != 1:
        raise ValueError("expected one character string")


def isMin(char: str) -> bool:
    assertChar(char)
    # return ord("a") <= ord(char) and ord(char) <= ord("z")
    return char.islower() # catches accentuated latin letters


def toMaj(char: str) -> str:
    assertChar(char)
    # return char.upper()
    return chr(ord(char) - 0x20) if isMin(char) else char


def majuscule(mot:str ) -> str:
    # return mot.upper()
    chars = [toMaj(char) for char in mot]
    return "".join(chars)


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]

    for i, mot in enumerate(mots):
        upper = majuscule(mot)
        assert upper == mot.upper() 

        mots[i] = upper
        

    print(mots)
