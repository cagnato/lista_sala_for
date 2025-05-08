import random
vetor = [0] * 10

for i in range(10):
    vetor[i] = random.randint(1, 100)

numero = int(input("Digite um número: "))

print(vetor)

existe = False

for i in range(10):
    if numero == vetor[i]:
        existe = True
        break
    else:
        exise = False

if existe:
    print(f"O número digitado foi {numero} e existe na posição {i}.")
else:
    print(f"O número digitado foi {numero} e não existe.")

