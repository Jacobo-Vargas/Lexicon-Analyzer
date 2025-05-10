# tokens.py

# Palabras reservadas por Elixir
KEYWORDS = {
        "def", "do", "end", "if", "else", "case", "when", "fn", "true", "false"
}

TOKEN_TYPES = {
    "IDENTIFIER": "Identificador",
    "KEYWORD": "Palabra reservada",
    "NUMBER": "Número natural",
    "REAL": "Número real",
    "LOGICAL_OP": "Operador lógico",
    "ARITHMETIC_OP": "Operador aritmético",
    "COMPARISON_OP": "Operador de comparación",
    "ASSIGNMENT_OP": "Operador de asignación",
    "INCREMENT_OP": "Operador de incremento/decremento",
    "PARENTHESIS": "Paréntesis",
    "BRACE": "Llave",
    "SEMICOLON": "Fin de sentencia",
    "COMMA": "Separador",
    "STRING": "Cadena de texto",
    "COMMENT": "Comentario",
    "UNKNOWN": "Token no reconocido",
}
