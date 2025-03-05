def verificar_probabilidade(valores):
    for valor in valores:
        if 0 <= valor <= 1:
            print(f"{valor} pode representar uma probabilidade.")
        else:
            print(f"{valor} NÃO pode representar uma probabilidade.")

# Lista de valores a serem verificados
valores = [0, 0.001, -1, 0.5, 745/1262, 45/31]

# Executa a verificação
verificar_probabilidade(valores)
