def calcular_idade(nome, ano_nascimento, ano_atual=2022):
    return ano_atual - ano_nascimento

def obter_dados_usuario():
    while True:
        try:
            nome = input("Digite seu nome completo: ")
            ano_nascimento = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))

            if 1922 <= ano_nascimento <= 2021:
                idade = calcular_idade(nome, ano_nascimento)
                print(f"\n{nome}, você completou ou completará {idade} anos em 2022.")
                break
            else:
                print("Erro: O ano de nascimento deve estar entre 1922 e 2021.")
        except ValueError:
            print("Erro: Por favor, insira um número válido para o ano de nascimento.")

if __name__ == "__main__":
    obter_dados_usuario()
