# Script para realizar operações matemáticas simples com dois números

def operacoes_matematicas(num1, num2):
    """
    Realiza operações matemáticas simples entre dois números.
    
    Args:
        num1 (float): Primeiro número
        num2 (float): Segundo número
    """
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2 if num2 != 0 else "Divisão por zero não permitida"
    
    print(f"\nOperações entre {num1} e {num2}:")
    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}")


# Solicitando entrada do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Chamando a função
operacoes_matematicas(num1, num2)
