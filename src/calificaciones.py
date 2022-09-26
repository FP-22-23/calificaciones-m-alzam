def nota_cuestionario(errores: int, aciertos: int, total_respuestas: int) -> float:
    return max(0, (aciertos * 10) / total_respuestas - (errores * 10) / (50 - total_respuestas))


def solicitar_datos() -> tuple[int]:
    errores = int(input("Errores: "))
    aciertos = int(input("Aciertos: "))
    respuestas = int(input("Total de respuestas: "))

    return errores, aciertos, respuestas
