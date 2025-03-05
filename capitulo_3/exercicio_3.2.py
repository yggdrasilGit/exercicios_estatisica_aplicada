def verificar_frase_probabilidade(probabilidade):
    if 0 <= probabilidade <= 1:
        print(f"\n A frase está correta: A probabilidade é {probabilidade * 100} %. \n")
    else:
        print(f"\n A frase está incorreta: {probabilidade * 100}% não é uma probabilidade válida. \n")

# Testa a frase com uma probabilidade inválida (150%)
verificar_frase_probabilidade(0.3)
