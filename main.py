from classes.classes_personagem import Personagem_principal


def inicio():
    print("Bem vindo ao jogo de RPG!")
    nome = input("Digite o nome do seu personagem: ")
    idade = input("Digite a idade do seu personagem: ")
    sexo = input("Digite o sexo do seu personagem: ")
    raça = input("Digite a raça do seu personagem: ")
    personagem = Personagem_principal(nome, idade, sexo, raça)


    classe_escolhida = False
    while classe_escolhida == False:
        print("Escolha a classe do seu personagem:")
        print("1 - Arqueiro")
        print("2 - Guerreiro")
        print("3 - Mago")
        print("4 - Assassino")
        print("5 - Paladino")
        classe = input("Digite o número da classe escolhida: ")
        if classe == "1":
            personagem.arqueiro()
            classe_escolhida = True
        elif classe == "2":
            personagem.guerreiro()
            classe_escolhida = True
        elif classe == "3":
            personagem.mago()
            classe_escolhida = True 
        elif classe == "4":
            personagem.assassino()
            classe_escolhida = True
        elif classe == "5":
            personagem.paladino()
            classe_escolhida = True
        else:
            print("Classe inválida. Por favor, escolha uma classe válida.") 