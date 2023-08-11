def media (num1, num2, num3, num4):
    calculo = (num1 + num2 + num3 + num4)/4
    return calculo

def media_ponderada (num1, num2, num3, num4):
    calculo = (num1*0.2) + (num2*0.2) + (num3*0.3) + (num4*0.3)
    return calculo   

def mediana (num1, num2, num3, num4):
    lista = [num1, num2, num3, num4]
    lista.sort()
    tamanho_da_lista = len(lista)
    indice_do_meio = tamanho_da_lista // 2

    if tamanho_da_lista % 2 == 0:
        soma_dois_do_meio = lista[indice_do_meio -1] + lista[indice_do_meio]
        resultado = soma_dois_do_meio /2
    else:
        resultado = lista[indice_do_meio]
    return resultado


def numeros (num1, num2, num3, num4):
    resultadoMedia = media(num1, num2, num3, num4)
    resultadoMediaPonderada = media_ponderada(num1, num2, num3, num4)
    resultadoMediana = mediana(num1, num2, num3, num4)
    return f"media: {resultadoMedia}, media ponderada: {resultadoMediaPonderada}, mediana: {resultadoMediana}"


numero1 = float(input("Digite o primeiro valor: "))
numero2 = float(input("Digite o segundo valor: "))
numero3 = float(input("Digite o terceiro valor: "))
numero4 = float(input("Digite o quarto valor: "))

resultado = numeros(numero1, numero2, numero3, numero4)
print(resultado)