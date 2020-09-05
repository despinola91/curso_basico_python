#Prueba de primalidad
def es_primo(numero):
    # contador = 0

    # for i in range(1, numero + 1):
    #     if i == 1 or i == numero:
    #         continue
    #     if numero % i == 0:
    #         contador += 1

    # if contador == 0:
    #     return True
    # else:
    #     return False

    # Para saber si un número es primo (divisible sólo por el mismo y por uno), lo dividimos sucesivamente por los primeros números primos: 2, 3, 5, 7, 11, ..
    # ¿Cuándo paramos de dividir?

    # - Si obtenemos división exacta --> no es primo
    # - Si el cociente es menor que el divisor .. paramos --> es primo

    # Ejemplo: 113

    # - 113 no es divisible por 2 (divisor: 2 , cociente: 56.5)
    # - 113 no es divisible por 3 (divisor: 3 , cociente: 37’ ..)
    # - 113 no es divisible por 5 (divisor: 5 , cociente: 22’ ..)
    # - 113 no es divisible por 7 (divisor: 7 , cociente: 16’ ..)
    # - 113 no es divisible por 11 (divisor: 11 , cociente: 10’ ..)
    # Paramos pues el cociente es menor que el divisor --> 113 es primo

    primeros_primos = [2,3,5,7,11]
    for primo in primeros_primos:
        cociente = numero / primo
        resto = numero % primo
        print("Primo: " + str(primo))
        print("Cociente: " + str(cociente))
        print("Resto: " + str(resto))
        if resto == 0:
            return False
        elif cociente < primo:
            return True


def run():
    numero = int(input("Escribe un numero: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")


if __name__ == "__main__":
    run()