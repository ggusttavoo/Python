nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa?").upper()

#resolvendo o primeiro problema
if doenca_infectocontagiosa == 'SIM':
    print('Encaminhe o paciente para a sala AMARELA')
elif doenca_infectocontagiosa == 'NAO':
    print('Encaminhe o paciente para a sala BRANCA')
else:
    print('Responda a pergunta com apenas SIM ou NAO')

#resolvendo o segundo problema
if idade >= 65:
    print('Paciente POSSUI prioridade')
else:
    genero = input('Qual o genero do paciente, MASCULINO ou FEMININO? ').upper()
    if genero == 'FEMININO' and idade > 10:
        gravidez = input('A paciente está gravida? (SIM ou NAO)').upper()
        if gravidez == 'SIM':
            print('Paciente POSSUI prioridade')
        else:
            print('Paciente NÃO POSSUI prioridade')
    else:
        print('Paciente NÃO POSSUI prioridade')