
def soma(*valores):
    valor = 0
    for i in range(len(valores)):
        valor += valores[i]
    print(valor)


soma(10,19,40, 60, 70, 10)