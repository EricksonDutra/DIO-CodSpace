# Solicita uma palavra ao usuário
palavra = input("Digite uma palavra: ")

# Inverte a palavra
palavra_invertida = palavra[::-1]

# Verifica se a palavra é um palíndromo
if palavra == palavra_invertida:
    print(f"\nA palavra '{palavra}' é um palíndromo.")
else:
    print(f"\nA palavra '{palavra}' não é um palíndromo.")