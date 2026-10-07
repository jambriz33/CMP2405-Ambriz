def ley_de_moore(transistores_iniciales, tiempo_anios, periodo_doblamiento=2):
    """Calcula el número de transistores siguiendo la ley de Moore.
    La cantidad se duplica cada 2 años.
    """
    return transistores_iniciales * (2 ** (tiempo_anios / periodo_doblamiento))


def main():
    try:
        transistores_iniciales = float(input("Ingrese el número inicial de transistores: "))
        tiempo_anios = float(input("Ingrese el tiempo en años: "))

        if transistores_iniciales <= 0 or tiempo_anios < 0:
            raise ValueError

        resultado = ley_de_moore(transistores_iniciales, tiempo_anios)
        duplicaciones = tiempo_anios / 2

        print("\nLey de Moore: la cantidad de transistores se duplica cada 2 años.")
        print(f"Transistores iniciales: {transistores_iniciales:,.0f}")
        print(f"Tiempo: {tiempo_anios} años")
        print(f"Duplicaciones estimadas: {duplicaciones:.2f}")
        print(f"Transistores estimados: {resultado:,.0f}")

    except ValueError:
        print("Entrada inválida. Ingresa números positivos.")


if __name__ == "__main__":
    main()
