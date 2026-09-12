def calcular_consumo(kilometros, dinero):
    precio_gasolina = 3.24

    galones = dinero / precio_gasolina
    litros = galones * 3.785

    consumo = kilometros / litros

    return consumo


if __name__ == "__main__":
    kilometros = 335
    dinero = 8.30

    resultado = calcular_consumo(kilometros, dinero)

    print("Kilómetros recorridos:", kilometros)
    print("Dinero gastado en gasolina: $", dinero)
    print("Consumo de la moto:", round(resultado, 2), "km/L")