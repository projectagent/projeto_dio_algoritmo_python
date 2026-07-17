# Script para verificar se um número é par ou ímpar

def verificar_par_impar(numero):
    """
    Verifica se um número é par ou ímpar.
    
    Args:
        numero (int): Número a ser verificado
    
    Returns:
        str: Mensagem indicando se é par ou ímpar
    """
    if numero % 2 == 0:
        return f"{numero} é PAR"
    else:
        return f"{numero} é ÍMPAR"


# Solicitando entrada do usuário
numero = int(input("Digite um número inteiro: "))

# Exibindo o resultado
resultado = verificar_par_impar(numero)
print(f"\nResultado: {resultado}")
