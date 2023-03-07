import random as r

def dado(x):
    i = 0
    valor = [r.randint(1, 10) for i in range(x)]
    ordem = sorted(valor, reverse=True)
    return ordem

QntdDado = int(input('Digite a quantidade de vezes que você deseja jogar o dado: '))
resultado = dado(QntdDado)
print(resultado)


