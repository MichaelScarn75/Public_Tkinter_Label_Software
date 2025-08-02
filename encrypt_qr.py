# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 22:46:51 2023

@author: user
"""
from decrypt_qr import *
from random import randint

def encrypt_qr(qr_string):
    date = qr_string[0:10]
    qr_string = qr_string.replace(date, "")
    qr_string = date[0:5] + qr_string
    qr_string = qr_string + date[5:10]
    lookup = {
    "0" : "$",
    "1" : "[",
    "2" : "#",
    "3" : "&",
    "4" : "]",
    "5" : "@",
    "6" : "*",
    "7" : "}",
    "8" : ".",
    "9" : ";",
    "-" : "=",
    "." : "+",
    "/" : "{",
    " " : "^",
    "A" : "r",
    "B" : "x",
    "C" : "z",
    "D" : "y",
    "E" : "q",
    "F" : "d",
    "G" : "f",
    "H" : "p",
    "I" : "e",
    "J" : "m",
    "K" : "b",
    "L" : "n",
    "M" : "w",
    "N" : "o",
    "O" : "g",
    "P" : "a",
    "Q" : "v",
    "R" : "h",
    "S" : "u",
    "T" : "s",
    "U" : "c",
    "V" : "k",
    "W" : "i",
    "X" : "j",
    "Y" : "l",
    "Z" : "t",
    "a" : "R",
    "b" : "F",
    "c" : "N",
    "d" : "X",
    "e" : "S",
    "f" : "Y",
    "g" : "A",
    "h" : "E",
    "i" : "M",
    "j" : "Z",
    "k" : "D",
    "l" : "P",
    "m" : "O",
    "n" : "Q",
    "o" : "B",
    "p" : "L",
    "q" : "T",
    "r" : "U",
    "s" : "V",
    "t" : "C",
    "u" : "H",
    "v" : "W",
    "w" : "G",
    "x" : "J",
    "y" : "K",
    "z" : "I"
    }
    
    final_string = ""
    for each in qr_string:
        for keys, values in lookup.items():
            if each == keys:
                final_string += values
    final_string = "==" + final_string + "$$$$"
    return final_string

