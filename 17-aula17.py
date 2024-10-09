# Ferramenta continue
# A ferramenta continue no phyton vai interromper o loop,
# mas vai dar continuidade a ele.

contador = 0

while contador <= 40:
    contador += 1

    # Verfirica se o valor de 'contador' é múltiplo de 4
    if (contador % 4 == 0):
        print("pim") # Se for múltiplo de 4, imprime "pim"
        continue # Interrompe a iteração atual e volta para o início do loop

    # Se o número não for múltiplo de 4, imprime o valor do contador
    print(contador)
# Após o término do loop, imprime a mensagem de finalização
print("Fim do programa")