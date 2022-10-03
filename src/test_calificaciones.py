from calificaciones import *


def main():
    # print(f"{nota_cuestionario(errores=3, aciertos=23, total_respuestas=27)=}")
    valores = solicitar_datos()
    print(nota_cuestionario(*valores))


if __name__ == "__main__":
    main()
