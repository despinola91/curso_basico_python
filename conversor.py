pesos = input("¿Cuantos pesos argentinos tienes?: ")
pesos = float(pesos)

valor_dolar = input("¿Cuanto es el tipo de cambio de pesos a dolares?: ")
valor_dolar = float(valor_dolar)

#valor_dolar = 3875

dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes USD " + dolares + " dólares.")