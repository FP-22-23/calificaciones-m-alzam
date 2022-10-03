def nota_cuestionario(errores: int, aciertos: int, total_respuestas: int) -> float:
    return max(0, (aciertos * 10) / total_respuestas - (errores * 10) / (50 - total_respuestas))


def solicitar_datos() -> tuple[int]:
    errores = int(input("Errores: "))
    aciertos = int(input("Aciertos: "))
    respuestas = int(input("Total de respuestas: "))

    return errores, aciertos, respuestas


def calcula_nota_cuatrimestre(cuestionarios: tuple[float], parcial: float, proyecto: float) -> float:
    if proyecto < 5:
        return 3.0
    return 0.1 * sum(cuestionarios) + 0.6 * parcial + 0.1 * proyecto


def calcula_nota_evaluacion_continua(cuestionarios: tuple[float], parciales: tuple[float], proyectos: tuple[float]):
    cuatrimestre_1 = calcula_nota_cuatrimestre(cuestionarios[:3], parciales[0], proyectos[0])
    cuatrimestre_2 = calcula_nota_cuatrimestre(cuestionarios[3:], parciales[1], proyectos[1])

    if cuatrimestre_1 < 4 or cuatrimestre_2 < 4:
        return 4

    return (cuatrimestre_2 + cuatrimestre_2) / 2


def solicitar_cuestionarios(n=6) -> list[float]:
    notas = []
    for i in range(n):
        notas.append(float(input(f"Nota del cuestionario {i+1}: ")))

    return notas


def solicitar_parciales(n=2) -> list[float]:
    notas = []
    for i in range(n):
        notas.append(float(input(f"Nota del parcial {i+1}: ")))

    return notas


def solicitar_proyectos(n=2) -> list[float]:
    notas = []
    for i in range(n):
        notas.append(float(input(f"Nota del proyecto {i+1}: ")))

    return notas
