#!/usr/bin/env python3
"""Módulo para importar la lista y la seleccion de la palabra."""

# Importamos la función que selecciona una película aleator desde la lista.
from utils import get_random_word

# Importamos la clase que contiene la lógica del juego.
from game import HangmanGame


word = get_random_word(filename="wordlist.txt")
print(word)
print(len(word))

# Creamos una instancia de la clase HangmanGame.
# La película seleccionada será la palabra que debe adivinar el jugador.
game = HangmanGame(word)

