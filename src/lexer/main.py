# main.py
from lexer import analizar_codigo

# Texto de ejemplo
codigo = '''
# Esto es un comentario
""" Comentario de bloque """
def saludo() {
  nombre = "Juan \"el grande\"";
  edad = 25;
  mostrar(nombre, edad);
}
'''




resultado = analizar_codigo(codigo)

for token in resultado:
    print(token)
