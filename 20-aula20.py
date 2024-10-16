def leitura_de_numeros():
    soma = 0
    quantidade = 0

    while True:
          numero = int(input("Digite um número  ou 0 para sair: "))

          if numero == 0:
            break

          soma += numero
          quantidade += 1
 
 
    if quantidade > 0:
             media = soma / quantidade
    else:
             media = 0

    print(f"Quantidade de números digitados: {quantidade}")
    print(f"Soma: {soma}")
    print(f"Média: {media}")

leitura_de_numeros()

print(f"Fim do código!")