nome = input('Digite um funcionário: ')
empresa = input('Digite a instituição: ')
qtde_funcionarios = int(input('Digite a quantidade de funcionários: '))
mediaMensalidade = float(input('Digite a média da mensalidade: '))

# Para strings utilizamos o '+', para inteiros utilizamos ','
# para números decimais utilizamos o '+', mas com a função
# str() para transformar em string.

print(nome + ' trabalha na empresa ' + empresa)
print('Possui: ', qtde_funcionarios, 'Funcionários.')
print('A média da mensalidade é de: ' + str(mediaMensalidade))

# A função type() retorna o tipo do dado do que estiver dentro dos seus parênteses
# Ex: O tipo de dado da váriavel [nome] é:  <class 'str'>

print('O tipo de dado da váriavel [nome] é: ', type(nome))
print('O tipo de dado da váriavel [empresa] é: ', type(empresa))
print('O tipo de dado da váriavel [qtde_funcionarios] é: ', type(qtde_funcionarios))
print('O tipo de dado da váriavel [mediaMensalidade] é: ', type(mediaMensalidade))