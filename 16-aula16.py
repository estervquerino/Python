while True:
    nome = input('Digite o seu nome ou escreva "sair": ')
    
    if nome == 'sair':
        break # para execução do while, sai do loop de repetição

    print(f'Seu nome é {nome}')

print('Acabou')