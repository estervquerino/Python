valor_pagamento = int(input("Digite o valor do pagamento: "))

if valor_pagamento <= 0:
    print("Por favor, insira um valor inteiro positivo.")
else:
    cedula_50 = 0
    cedula_20 = 0
    cedula_10 = 0
    cedula_5 = 0
    cedula_1 = 0

    while valor_pagamento >= 50:
        cedula_50 += 1
        valor_pagamento -= 50

    while valor_pagamento >= 20:
        cedula_20 += 1
        valor_pagamento -= 20

    while valor_pagamento >= 10:
        cedula_10 += 1
        valor_pagamento -= 10

    while valor_pagamento >= 5:
        cedula_5 += 1
        valor_pagamento -= 5

    cedula_1 = valor_pagamento

    print("Quantidade mínima de cédulas necessárias:")
    print(f"50 R$: {cedula_50}")
    print(f"20 R$: {cedula_20}")
    print(f"10 R$: {cedula_10}")
    print(f"5 R$: {cedula_5}")
    print(f"1 R$: {cedula_1}")
   

