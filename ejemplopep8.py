"""Programa para calcular el promedio de un estudiante."""


def calcular_promedio(nota_uno, nota_dos, nota_tres):
    """Calcula el promedio de tres notas."""
    promedio = (nota_uno + nota_dos + nota_tres) / 3
    return promedio


def verificar_resultado(promedio):
    """Determina si el estudiante aprobó o reprobó."""
    if promedio >= 3.0:
        return "El estudiante aprobó."
    else:
        return "El estudiante reprobó."


def main():
    """Ejecuta el programa principal."""
    print("===== PROMEDIO DE NOTAS =====")

    nota_uno = float(input("Ingrese la primera nota: "))
    nota_dos = float(input("Ingrese la segunda nota: "))
    nota_tres = float(input("Ingrese la tercera nota: "))

    if not all(0 <= nota <= 5 for nota in (
        nota_uno,
        nota_dos,
        nota_tres
    )):
        print("Error: las notas deben estar entre 0 y 5.")
        return

    promedio = calcular_promedio(
        nota_uno,
        nota_dos,
        nota_tres
    )

    print(f"\nEl promedio es: {promedio:.2f}")
    print(verificar_resultado(promedio))


if _name_ == "_main_":
    main()
