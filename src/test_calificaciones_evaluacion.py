from calificaciones import *


def main():
    cuestionarios = solicitar_cuestionarios()
    parciales = solicitar_parciales()
    proyectos = solicitar_proyectos()

    print(f"{calcula_nota_evaluacion_continua(cuestionarios, parciales, proyectos)=}")


if __name__ == "__main__":
    main()
