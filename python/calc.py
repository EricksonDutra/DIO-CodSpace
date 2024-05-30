# Solicita dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Exibe as opções de operações
print("\nEscolha a operação matemática:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

# Solicita a escolha do usuário
escolha = input("\nDigite o número da operação desejada (1/2/3/4): ")

# Realiza a operação escolhida
if escolha == '1':
    resultado = num1 + num2
    print(f"\nResultado da adição: {num1} + {num2} = {resultado}")
elif escolha == '2':
    resultado = num1 - num2
    print(f"\nResultado da subtração: {num1} - {num2} = {resultado}")
elif escolha == '3':
    resultado = num1 * num2
    print(f"\nResultado da multiplicação: {num1} * {num2} = {resultado}")
elif escolha == '4':
    if num2 != 0:
        resultado = num1 / num2
        print(f"\nResultado da divisão: {num1} / {num2} = {resultado}")
    else:
        print("\nErro: Divisão por zero não é permitida.")
else:
    print("\nOperação inválida. Por favor, escolha uma opção válida (1/2/3/4).")