
nomes = []

for i in range(10):
    nomePessoa = str(input("Digite seu nome"))
    nomes.append(nomePessoa)

for j in len(nomes):
    print("O nome da pessoa é: ".format(nomes[j]))
    