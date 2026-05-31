class Personagem_principal:
    def __init__(self, nome, idade, sexo, raça):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.raça = raça

    def arqueiro(self):
        print(f"Personagem: {self.nome}, Idade: {self.idade}, Sexo: {self.sexo}, Raça: {self.raça}, Classe: Arqueiro")
        vida = 70
        ataque = 80
        defesa = 70
        agilidade = 90
        forca = 70
        magia = 60
        print(f"Vida: {vida}, Ataque: {ataque}, Defesa: {defesa}, Agilidade: {agilidade}, Força: {forca}")

    def guerreiro(self):
        print(f"Personagem: {self.nome}, Idade: {self.idade}, Sexo: {self.sexo}, Raça: {self.raça}, Classe: Guerreiro")
        vida = 100
        ataque = 90
        defesa = 80
        agilidade = 50
        forca = 90
        magia = 30
        print(f"Vida: {vida}, Ataque: {ataque}, Defesa: {defesa}, Agilidade: {agilidade}, Força: {forca}")

    def mago(self):
        print(f"Personagem: {self.nome}, Idade: {self.idade}, Sexo: {self.sexo}, Raça: {self.raça}, Classe: Mago")
        vida = 60
        ataque = 100
        defesa = 50
        agilidade = 70
        forca = 60
        magia = 100
        print(f"Vida: {vida}, Ataque: {ataque}, Defesa: {defesa}, Agilidade: {agilidade}, Força: {forca}")

    def assassino(self):
        print(f"Personagem: {self.nome}, Idade: {self.idade}, Sexo: {self.sexo}, Raça: {self.raça}, Classe: Assassino")
        vida = 60
        ataque = 95
        defesa = 55
        agilidade = 100
        forca = 80
        magia = 50
        print(f"Vida: {vida}, Ataque: {ataque}, Defesa: {defesa}, Agilidade: {agilidade}, Força: {forca}, Magia: {magia}")

    
    def paladino(self):
        print(f"Personagem: {self.nome}, Idade: {self.idade}, Sexo: {self.sexo}, Raça: {self.raça}, Classe: Paladino")
        vida = 90
        ataque = 80
        defesa = 90
        agilidade = 50
        forca = 70
        magia = 60
        print(f"Vida: {vida}, Ataque: {ataque}, Defesa: {defesa}, Agilidade: {agilidade}, Força: {forca}, Magia: {magia}")

    