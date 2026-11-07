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

    def display_progress(self):
        """Mostramos las letras adivinadas y ocultamos las restantes.
        Las iniciales de cada palabra las mostramos en mayúsculas
        cuando son descubiertas.
        """
        progress = ""

        # Recorremos el título obteniendo la posición y cada carácter.
        for posicion, letter in enumerate(self.word):

            # Normalizamos la letra para comparar sin tildes.
            normalized = normalize_letter(letter)

            # Mostramos automáticamente espacios y signos de puntuación.
            if not letter.isalpha():
                progress += letter

            # Comprobamos si es la primera letra de una palabra.
            elif posicion == 0 or self.word[posicion - 1] == " ":

                # Mostramos la inicial en mayúscula si fue adivinada.
                if normalized in self.guessed_letters:
                    progress += letter.upper()
                else:
                    progress += "_"

            # Mostramos las demás letras si fueron adivinadas.
            elif normalized in self.guessed_letters:
                progress += letter

            # Ocultamos las letras que todavía no fueron adivinadas.
            else:
                progress += "_"

        # Imprimimos el progreso actual de la película.
        print(progress)
        