import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    print("🎲 Bem-vindo ao jogo: Adivinha o Número!")
    print("Estou pensando em um número entre 1 e 100... Tente adivinhar!")

    while not acertou:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < 1 or palpite > 100:
                print("❗ O número deve estar entre 1 e 100.")
            elif palpite < numero_secreto:
                print("🔻 Muito baixo. Tente novamente.")
            elif palpite > numero_secreto:
                print("🔺 Muito alto. Tente novamente.")
            else:
                print(f"🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
                acertou = True
        except ValueError:
            print("⚠️ Por favor, digite um número válido.")

if __name__ == "__main__":
    jogo_adivinhacao()
