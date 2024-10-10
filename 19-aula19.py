def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def kelvin_para_celsius(k):
    return k - 273.15

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def menu():
   print("\nMenu de conversão de temperaturas")
   print("1. Converter fahrenheit para kelvin")
   print("2. Converter fahrenheit para celsius")
   print("3. Converter kelvin para fahrenheit")
   print("4. Converter ckelvin para celsius")
   print("5. Converter celsius para fahrenheit")
   print("6. Converter celsius para kelvin")
   print("7. Sair do programa")

while True:
    menu()
    
    opcao = input("Selecione a conversão desejada ou digite 7 para sair: ")

    if opcao == '7':
        print ("Programa encerrado!")
        break
    elif opcao == '1':
        fahrenheit = float(input("digite a temperatura em fahrenheit: "))
        print(f"{fahrenheit}°F é igual a {fahrenheit_para_kelvin(fahrenheit):.2f}K")

    elif opcao == '2':
        fahrenheit = float(input("digite a temperatura em fahrenheit: "))
        print(f"{fahrenheit}°F é igual a {fahrenheit_para_celsius(fahrenheit):.2f}°C")

    elif opcao == '3':
        kelvin = float(input("digite a temperatura em kelvin: "))
        print(f"{kelvin}K é igual a {kelvin_para_fahrenheit(kelvin):.2f}°F")

    elif opcao == '4':
        kelvin = float(input("digite a temperatura em kelvin: "))
        print(f"{kelvin}K é igual a {kelvin_para_celsius(kelvin):.2f}°C")

    elif opcao == '5':
        celsius = float(input("digite a temperatura em celsius: "))
        print(f"{celsius}°C é igual a {celsius_para_fahrenheit(celsius):.2f}°F")

    elif opcao == '6':
        celsius = float(input("digite a temperatura em celsius: "))
        print(f"{celsius}°C é igual a {celsius_para_kelvin(celsius):.2f}K")

    else:
        print("Opção inválida!")
        

     



    


    
