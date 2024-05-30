# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(f"\nO número {numero} é par.")
else:
    print(f"\nO número {numero} é ímpar.")