from calificaciones import (
    calcula_nota_evaluacion_continua,
    nota_cuestionario,
    solicitar_cuestionarios,
    solicitar_datos,
    solicitar_parciales,
    solicitar_proyectos,
)


def main():
    # print(f"{nota_cuestionario(errores=3, aciertos=23, total_respuestas=27)=}")
    # valores = solicitar_datos()
    # print(nota_cuestionario(*valores))

    cuestionarios = solicitar_cuestionarios()
    parciales = solicitar_parciales()
    proyectos = solicitar_proyectos()

    print(f"{calcula_nota_evaluacion_continua(cuestionarios, parciales, proyectos)=}")


if __name__ == "__main__":
    main()
