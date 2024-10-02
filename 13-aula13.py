# Declaração da função exibirMensagem(nome)
def exibirMensagem(nome, idade):
    print(f"Olá, {nome} com {idade} anos!")


def somar(a, b):
    return a + b


def calcularAreaCirculo(raio):
    area = 3.1415 * raio**2
    return area


# início do meu algoritmo
nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
exibirMensagem(nome, idade)  # Exibe a mensagem com o nome do usúario.

# chamando função com retorno
valorA = int(input("Digite o primeiro número: "))
valorB = int(input("Digite o segundo número: "))
resultado = somar(valorA, valorB)
print(f"O resultado da soma = {resultado}")


# Calcular área do circulo
print("Área do círculo!")
raio = float(input("Digite o valor dp raio: "))
area = calcularAreaCirculo(raio)
print(f"A área do círculo: {area:.2f}")