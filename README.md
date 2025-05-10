# Analizador Léxico en Python para Elixir

Este proyecto implementa un analizador léxico desarrollado completamente en Python sin expresiones regulares, diseñado para identificar tokens del lenguaje de programación Elixir. El propósito es recorrer el código fuente carácter por carácter utilizando estructuras como while, if y for, simulando autómatas, y generar una lista de tokens válidos con su tipo y posición. Se construyó como parte de un proyecto para la materia 'teoría de lenguajes formales'.

El programa es capaz de reconocer números naturales, números reales, palabras reservadas del lenguaje, identificadores con máximo 10 caracteres, operadores aritméticos, de comparación, lógicos y de asignación, operadores de incremento y decremento, paréntesis, llaves, punto y coma, coma, cadenas de texto con caracteres de escape, así como comentarios de línea y de bloque. También identifica y reporta tokens no reconocidos o errores léxicos como cadenas sin cerrar.

El analizador puede ejecutarse desde consola para pruebas directas o mediante una interfaz gráfica simple construida con Tkinter que permite escribir el código fuente en un área de texto, hacer clic en un botón "Analizar", y ver los resultados en forma de tabla que muestra: lexema, tipo y posición.

El proyecto no utiliza expresiones regulares ni bibliotecas externas. Solo usa Python puro y la biblioteca estándar.

## Características implementadas

- Reconocimiento de:
  - Números naturales (ej: 123)
  - Números reales (ej: 3.14)
  - Identificadores (máx. 10 caracteres)
  - Palabras reservadas: def, do, end, if, else, case, when, fn, true, false
  - Operadores:
    - Aritméticos: +, -, *, /, %
    - Comparación: ===, ==, !=, <, >, <=, >=
    - Lógicos: and, or, not
    - Asignación: =
    - Incremento/Decremento: ++, --
  - Paréntesis: ( )
  - Llaves: { }
  - Punto y coma (;)
  - Coma (,)
  - Cadenas de texto con comillas dobles y caracteres escapados (ej: "Hola \"mundo\"")
  - Comentarios:
    - De línea: comienza con #
    - De bloque: delimitado con """ comillas triples """
- Detección de errores léxicos:
  - Cadenas sin cerrar
  - Tokens no reconocidos
- Interfaz gráfica opcional con entrada de texto, botón para analizar y tabla de salida

## Estructura del proyecto

El proyecto se compone de los siguientes archivos:

- lexer.py → lógica principal del analizador léxico (autómatas)
- tokens.py → definición de tipos de token y palabras clave
- main.py → prueba del analizador desde consola
- gui.py → interfaz gráfica opcional con Tkinter

## Ejecución

Este proyecto puede ejecutarse de dos formas:

1. Desde consola:

   Ejecuta el archivo main.py desde una terminal:

   ```bash
   python3 main.py

Puedes modificar el contenido de la variable codigo en main.py para ingresar tu código Elixir de prueba.

2. Desde la interfaz gráfica:

    Requiere tener instalada la biblioteca tkinter (viene por defecto con Python, pero en Linux puedes instalarla con: sudo apt install python3-tk).

    Ejecuta:

       python3 gui.py

    Se abrirá una ventana donde puedes escribir el código y presionar “Analizar”. Los resultados aparecerán en una tabla con columnas: Lexema, Tipo y Posición.

    Python 3.8 o superior

    Tkinter (solo si se desea ejecutar la GUI)

    No requiere instalar paquetes externos

Autores

    Este proyecto fue desarrollado por Jacobo Vargas García,
    Juan Jose Contreras Molina y Julian Andres Naranjo Alzate
    como parte de un trabajo académico en la carrera de Ingeniería en Sistemas y computación.
