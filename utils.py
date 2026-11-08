#!/usr/bin/env python3
"""Módulo para cargar películas desde el archivo y elegimos una al azar."""

import random


def load_words(filename):
    """Cargamos las películas almacenadas en un archivo de texto.
    Abrimos el archivo indicado, leemos todas sus líneas y eliminamos los
    espacios y saltos de línea sobrantes.
    Pasamos como argumento:
        Nombre del archivo que contiene las películas.
    Retornamos:
        Lista de películas disponibles.
    """
    with open(filename, encoding="utf-8") as file:
        lines = file.readlines()
        words = []
        for line in lines:
            words.append(line.strip())
        return words


def get_random_word(filename):
    """Seleccionamos una película aleatoria de la lista.
    Pasamos como argumento:
        Nombre del archivo de películas.
    Retornamos:
        Título de la película seleccionada.
    """
    movies = load_words(filename)
    movie = random.choice(movies)
    return movie
