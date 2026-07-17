# Script para calcular a média de três notas

def calcular_media(nota1, nota2, nota3):
    """
    Calcula a média aritmética de três notas.
    
    Args:
        nota1 (float): Primeira nota
        nota2 (float): Segunda nota
        nota3 (float): Terceira nota
    
    Returns:
        float: Média das três notas
    """
    media = (nota1 + nota2 + nota3) / 3
    return media

def verificar_situacao(media):
    """
    Verifica a situação do aluno baseado na média.
    
    Args:
        media (float): Média do aluno
    
    Returns:
        str: Situação (Aprovado/Reprovado)
    """
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# Solicitando entrada do usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calculando a média
media = calcular_media(nota1, nota2, nota3)
situacao = verificar_situacao(media)

# Exibindo os resultados
print(f"\nNotas: {nota1}, {nota2}, {nota3}")
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
