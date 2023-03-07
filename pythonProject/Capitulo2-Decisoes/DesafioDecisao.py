nivel = input('Digite o seu nível de acesso: ').upper()

if nivel == 'ADM' or nivel == 'USR':
    genero = input('Qual o seu genero, masculino ou feminino? ').upper()
    if genero == 'MASCULINO' and nivel == 'ADM':
        print('Olá Administrador')
    elif genero == 'MASCULINO' and nivel == 'USR':
        print('Olá Usuário')
    elif genero == 'FEMININO' and nivel == 'ADM':
        print('Olá Administradora')
    elif genero == 'FEMININO' and nivel =='USR':
        print('Olá Usuária')
elif nivel == 'GUEST':
    print('Olá Visitante')
else:
    print('Olá Desconhecido(a)')