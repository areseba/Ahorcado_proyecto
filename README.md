Proyecto  — Juego del Ahorcado

# Introducción

Nuestro proyecto consiste en desarrollar el juego del Ahorcado utilizando Python.

El objetivo es que el jugador descubra el título de una película ingresando letras. Tiene un máximo de seis errores antes de perder la partida.

El programa selecciona una película aleatoriamente desde un archivo de texto y permite jugar desde la terminal.

## Arquitectura del proyecto

El proyecto está organizado en tres módulos principales y un archivo de datos.

### utils.py

Se encarga de trabajar con el archivo de películas.

load_words(): carga las películas desde el archivo.

get_random_word(): selecciona una película aleatoria.

### game.py

Contiene la clase HangmanGame, que administra el funcionamiento de la partida.

display_progress(): muestra las letras descubiertas.

process_guess(): procesa cada letra ingresada.

is_won(): comprueba si el jugador ganó.

is_lost(): comprueba si el jugador perdió.

display_guessed_letters(): muestra las letras ingresadas.

display_attempts(): muestra los intentos restantes.

normalize_letter(), que permite comparar vocales con y sin tilde.

### main.py

Es el módulo principal.

Se encarga de iniciar el juego, solicitar las letras, validar las entradas y controlar el ciclo de la partida.

### wordlist.txt

Contiene los títulos de las películas que utiliza el programa.
