#!/usr/bin/env python3
"""Módulo que contiene la lógica del juego Ahorcado."""


def normalize_letter(letter):
    """Convierte las vocales con tilde en vocales sin tilde."""
    return letter.translate(
        str.maketrans("áéíóú", "aeiou")
    )


class HangmanGame:
    """Clase que representa una partida de Ahorcado."""

    def __init__(self, word):
        """Inicializa una nueva partida."""

        self.word = word.lower()
        self.guessed_letters = []
        self.attempted_letters = []
        self.max_errors = 6
        self.errors = 0
