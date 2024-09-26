a = float(input("Informe o coeficiente de a: "))
b = float(input("Informe o coeficiente de b: "))
c = float(input("Informe o coeficiente de c: "))

while a == 0:
    print("O coeficiente a não pode ser zero.")
    a = float(input("Informe o coeficiente a: "))

# cálculo do delta
delta = b**2 - 4*a*c

# Verificando o delta
if delta < 0:
    print("A equação não possui raízes reais")
elif delta == 0:
    x = -b / (2 * a)
    print(f"A única raiz real é {x}")
else:
    x1 = (-b + delta ** 0.5) / (2 * a) 
    x2 = (-b - delta ** 0.5) / (2 * a) 
    print(f"As raízes reais são {1} e {2}")


 

  
