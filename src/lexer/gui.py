import tkinter as tk
from tkinter import ttk, scrolledtext
from lexer import analizar_codigo

class LexerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico")

        # etrada de texto
        self.code_input = scrolledtext.ScrolledText(root, width=80, height=15, wrap=tk.WORD)
        self.code_input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Boton analizador
        self.analyze_button = ttk.Button(root, text="Analizar", command=self.analizar)
        self.analyze_button.grid(row=1, column=1, pady=5)

        # Table para resultados
        self.tree = ttk.Treeview(root, columns=("Lexema", "Tipo", "Posición"), show="headings", height=15)
        self.tree.heading("Lexema", text="Lexema")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Posición", text="Posición")

        self.tree.column("Lexema", width=200)
        self.tree.column("Tipo", width=200)
        self.tree.column("Posición", width=100)

        self.tree.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Scrol para tabla
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=2, column=3, sticky="ns")

    def analizar(self):
        # Obtener cdigo fuente
        codigo = self.code_input.get("1.0", tk.END)

        # para limpiar tabla
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Analizar código
        tokens = analizar_codigo(codigo)

        # Mostrar tokens en tabla
        for token in tokens:
            self.tree.insert("", tk.END, values=(token.lexema, token.tipo, token.posicion))

if __name__ == "__main__":
    root = tk.Tk()
    app = LexerGUI(root)
    root.mainloop()
