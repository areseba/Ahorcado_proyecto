#!/usr/bin/env python3
"""Módulo para importar la lista y la seleccion de la palabra."""

# Importamos la función que selecciona una película aleator desde la lista.
from utils import get_random_word

words = get_random_word(filename="wordlist.txt")
print(words)
print(len(words))
