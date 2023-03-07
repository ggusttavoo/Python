tabuada=int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número ", tabuada)

#valores deverão estar entre 1 e 11, com incremento de 1 em 1.
for valor in range(1,11,1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))