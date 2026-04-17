contador = 0

numero = int(input("digite um numero(0 para parar):"))

while numero != 0:
    if numero % 2 == 0:
        contador = contador + 1
    numero = int(input("digite um numero(0 para parar):"))

print("quantidade de números pares:", contador)