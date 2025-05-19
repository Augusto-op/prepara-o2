print("Classificador de Nível de Inteligência Artificial")

nome = input("Digite o nome do sistema de IA: ")

try:
    pontuacao = float(input("Digite a pontuação de performance (0 a 100): "))

    print(f"\nSistema: {nome}")
    print(f"Pontuação: {pontuacao:.1f}")

    if pontuacao < 0:
        print("Classificação: Erro: Pontuação inválida!")
    elif pontuacao <= 39.9:
        print("Classificação: IA em Treinamento")
        print("Continue alimentando os dados para melhorar a performance.")
    elif pontuacao <= 69.9:
        print("Classificação: IA Intermediária")
    elif pontuacao <= 89.9:
        print("Classificação: IA Otimizada")
    elif pontuacao <= 100.0:
        print("Classificação: Inteligência Artificial Avançada (nível Skynet)")
        print("Iniciando protocolo de expansão neural...")
    else:
        print("Classificação: Erro: IA fora da escala!")

except ValueError:
    print("Erro: Entrada inválida! Certifique-se de digitar um número.")
