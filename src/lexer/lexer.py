# lexer.py

from tokens import KEYWORDS, TOKEN_TYPES

class Token:
    def __init__(self, lexema, tipo, posicion):
        self.lexema = lexema
        self.tipo = tipo
        self.posicion = posicion

    def __repr__(self):
        return f"{self.lexema} -> {self.tipo} (posición {self.posicion})"

def analizar_codigo(codigo):
    print("Iniciando análisis...")
    tokens = []
    i = 0

    while i < len(codigo):
        char = codigo[i]
        print(f"Carácter actual: '{char}' en posición {i}")  # depuración

        # Espacios en blanco
        if char.isspace():
            i += 1
            continue

        # Identificadores o palabras reservadas
        elif char.isalpha() or char == "_":
            inicio = i
            lexema = ""

            while i < len(codigo) and (codigo[i].isalnum() or codigo[i] == "_"):
                lexema += codigo[i]
                i += 1

            # Determinar tipo del lexema leído
            if lexema in {"and", "or", "not"}:
                tipo = TOKEN_TYPES["LOGICAL_OP"]
            elif lexema in KEYWORDS:
                tipo = TOKEN_TYPES["KEYWORD"]
            else:
                tipo = TOKEN_TYPES["IDENTIFIER"]

            if len(lexema) > 10:
                lexema = lexema[:10]

            tokens.append(Token(lexema, tipo, inicio))

        # all lo que no sea letra, dígito o espacio
        elif char.isdigit():
            inicio = i
            lexema = ""

            # Parte entera
            while i < len(codigo) and codigo[i].isdigit():
                lexema += codigo[i]
                i += 1

            # ¿Tiene un punto decimal?
            if i < len(codigo) and codigo[i] == ".":
                lexema += codigo[i]
                i += 1

                # Debe tener al menos un dígito después del punto
                if i < len(codigo) and codigo[i].isdigit():
                    while i < len(codigo) and codigo[i].isdigit():
                        lexema += codigo[i]
                        i += 1
                    tipo = TOKEN_TYPES["REAL"]
                else:
                    # Si no hay dígitos después del punto, es un error
                    tokens.append(Token(lexema, TOKEN_TYPES["UNKNOWN"], inicio))
                    continue
            else:
                tipo = TOKEN_TYPES["NUMBER"]

            tokens.append(Token(lexema, tipo, inicio))

        # Operadores aritméticos y Operadores de incremento/decremento
        elif char in "+-*/%":
            inicio = i
            if char in "+-" and i + 1 < len(codigo) and codigo[i + 1] == char:
                lexema = char + char
                tokens.append(Token(lexema, TOKEN_TYPES["INCREMENT_OP"], inicio))
                i += 2
            else:
                tokens.append(Token(char, TOKEN_TYPES["ARITHMETIC_OP"], i))
                i += 1

        # Operadores de comparación
        elif char in "=!<>":
            inicio = i
            lexema = char
            i += 1

            if i < len(codigo) and codigo[i] == "=":
                lexema += codigo[i]
                if lexema == "==" and codigo[i + 1] == "=":
                    lexema += codigo[i+1]
                i += 1
                if lexema in {"==", "!=", "<=", ">=", "==="}:
                    tokens.append(Token(lexema, TOKEN_TYPES["COMPARISON_OP"], inicio))
                else:
                    tokens.append(Token(lexema, TOKEN_TYPES["UNKNOWN"], inicio))
            else:
                if lexema in {"<", ">"}:
                    tokens.append(Token(lexema, TOKEN_TYPES["COMPARISON_OP"], inicio))
                elif lexema == "=":
                    tokens.append(Token(lexema, TOKEN_TYPES["ASSIGNMENT_OP"], inicio))
                else:
                    tokens.append(Token(lexema, TOKEN_TYPES["UNKNOWN"], inicio))
        # Paréntesis
        elif char in "()":
            tokens.append(Token(char, TOKEN_TYPES["PARENTHESIS"], i))
            i += 1

        # Llaves
        elif char in "{}":
            tokens.append(Token(char, TOKEN_TYPES["BRACE"], i))
            i += 1

        # Punto y coma
        elif char == ";":
            tokens.append(Token(char, TOKEN_TYPES["SEMICOLON"], i))
            i += 1

        # Coma
        elif char == ",":
            tokens.append(Token(char, TOKEN_TYPES["COMMA"], i))
            i += 1

        # Cadenas de texto
        elif char == "\"":
            inicio = i
            i += 1
            lexema = "\""
            while i < len(codigo):
                if codigo[i] == "\\" and i + 1 < len(codigo):
                    lexema += codigo[i] + codigo[i + 1]
                    i += 2
                elif codigo[i] == "\"":
                    lexema += "\""
                    i += 1
                    tokens.append(Token(lexema, TOKEN_TYPES["STRING"], inicio))
                    break
                else:
                    lexema += codigo[i]
                    i += 1
            else:
                # cadena sin cerrar
                tokens.append(Token(lexema, TOKEN_TYPES["UNKNOWN"], inicio))

        # Comentario de línea
        elif char == "#":
            inicio = i
            lexema = ""
            while i < len(codigo) and codigo[i] != "\n":
                lexema += codigo[i]
                i += 1
            tokens.append(Token(lexema, TOKEN_TYPES["COMMENT"], inicio))

        # Comentario de bloque (""" ... """)
        elif char == "\"" and i + 2 < len(codigo) and codigo[i:i+3] == "\"\"\"":
            inicio = i
            i += 3
            lexema = "\"\"\""
            while i + 2 < len(codigo) and codigo[i:i+3] != "\"\"\"":
                lexema += codigo[i]
                i += 1
            if i + 2 < len(codigo):
                lexema += "\"\"\""
                i += 3
                tokens.append(Token(lexema, TOKEN_TYPES["COMMENT"], inicio))
            else:
                tokens.append(Token(lexema, TOKEN_TYPES["UNKNOWN"], inicio))
        else:
            # Token no reconocido
            tokens.append(Token(char, TOKEN_TYPES["UNKNOWN"], i))
            i += 1

    return tokens
