#ESTUDIANTES: Emmanuel Aguero y Johan Blanco, Grupo 6pm.
import TablaDeSibolos
F1 = "funcion1.txt"
F2 = "funcion2.txt"
F3 = "funcionCorrecta.txt"
F4 = "funcionIncorrecta.txt"

if __name__ == '__main__':
    tabla = TablaDeSibolos.TablaDeSimbolos()
    tabla.analizar(F1)

    tabla2 = TablaDeSibolos.TablaDeSimbolos()
    tabla2.analizar(F2)

    tabla3 = TablaDeSibolos.TablaDeSimbolos()
    tabla3.analizar(F3)

    tabla4 = TablaDeSibolos.TablaDeSimbolos()
    tabla4.analizar(F4)