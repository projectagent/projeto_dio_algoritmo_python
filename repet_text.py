# Script para repetir uma string um número determinado de vezes
def repetir_string(texto, quantidade):
    """
    Repete uma string o número de vezes especificado, uma em cada linha.
    
    Args:
        texto (str): A string a ser repetida
        quantidade (int): Número de vezes que a string será repetida
    """
    for _ in range(quantidade):
        print(texto)


# Solicitando entrada do usuário
texto = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

# Chamando a função e exibindo o resultado
print(f"\nResultado:")
repetir_string(texto, numero)