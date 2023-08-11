def testarLista(numeros):
    lista = list(numeros)
    lista.sort()
    tamanho = len(lista)
    indiceDoMeio = tamanho//2
    return lista[indiceDoMeio -1] + lista[indiceDoMeio]


numeros = (1,5,10,11,25,11,36,35)
resultado = (testarLista(numeros))
print(resultado)
