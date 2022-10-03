from calificaciones import *


def main():
    cuestionarios = solicitar_cuestionarios(3)
    parciales = solicitar_parciales(1)
    proyectos = solicitar_proyectos(1)

    print(f"{calcula_nota_cuatrimestre(cuestionarios, parciales[0], proyectos[0])=}")


if __name__ == "__main__":
    main()
