def calcular_dolares(valor_dolar, tipo_peso):
    pesos = input("Cuantos pesos " + tipo_peso + " tienes?: ")
    pesos = float(pesos)
    #valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    calcular_dolares(3875, "colombianos")
elif opcion == 2:
    calcular_dolares(65, "argentinos")
elif opcion == 3:
    calcular_dolares(24, "mexicanos")
else:
    print("Ingresa una opción correcta por favor.")