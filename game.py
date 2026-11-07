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

    def process_guess(self, letter):
            """Procesamos una letra y actualizamos el estado de la partida.
            Pasamos como argumento:
                letter (es un string): Letra ingresada por el jugador.
            Retornamos:
                booleano: True si la letra está en la película; False en caso contrario.
            """
            # Normalizamos la letra ingresada.
            normalized_letter = normalize_letter(letter)
    
            # Normalizamos el título completo para comparar sin tildes.
            normalized_word = normalize_letter(self.word)
    
            # Guardamos todas las letras ingresadas por el jugador.
            self.attempted_letters.append(normalized_letter)
    
            # Comprobamos si la letra aparece en el título.
            if normalized_letter in normalized_word:
    
                # Guardamos la letra correcta.
                self.guessed_letters.append(normalized_letter)
    
                return True
    
            else:
                # Incrementamos el contador cuando la letra es incorrecta.
                self.errors += 1
    
                return False
        