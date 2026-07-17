# Script para verificar se uma palavra é um palíndromo

def verificar_palindromo(palavra):
    """
    Verifica se uma palavra é um palíndromo.
    Um palíndromo é uma palavra que se lê igual de frente para trás.
    
    Args:
        palavra (str): Palavra a ser verificada
    
    Returns:
        bool: True se for palíndromo, False caso contrário
    """
    # Remove espaços e converte para minúsculas
    palavra_limpa = palavra.replace(" ", "").lower()
    
    # Inverte a palavra usando slicing
    palavra_invertida = palavra_limpa[::-1]
    
    # Compara a palavra original com a invertida
    return palavra_limpa == palavra_invertida


# Solicitando entrada do usuário
palavra = input("Digite uma palavra para verificar se é palíndromo: ")

# Verificando se é palíndromo
eh_palindromo = verificar_palindromo(palavra)

# Exibindo o resultado
if eh_palindromo:
    print(f"\n'{palavra}' É um PALÍNDROMO! 🎉")
else:
    print(f"\n'{palavra}' NÃO é um palíndromo.")
