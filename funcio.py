class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.__salario = salario 

   
    def obter_salario(self):
        return self.__salario

    
    def aumentar_salario(self, aumento):
        if aumento > 0:
            self.__salario += aumento
        else:
            print("Aumento deve ser positivo")

class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario, bonus):
        super().__init__(nome, cargo, salario)
        self.nome = nome
        self.cargo = cargo
        self.__salario = salario
        self.bonus = bonus


    def aumentar_salario(self, aumento):
        if aumento > 0:
            self.__salario = self.__salario + aumento
        else:
            print("Aumento deve ser positivo")  


if __name__ == "__main__":
   
   
    funcionario = Funcionario("Tae-hyung", "Analista", 3000)
    print(f"Salário inicial do {funcionario.nome}: R${funcionario.obter_salario()}")

    funcionario.aumentar_salario(500)
    print(f"Salário após aumento do {funcionario.nome}: R${funcionario.obter_salario()}")


    gerente = Gerente("jimin", "Gerente", 5000, 1000)
    print(f"\nSalário inicial da {gerente.nome}: R${gerente.obter_salario()}")

    gerente.aumentar_salario(1000)
    print(f"Salário após aumento da {gerente.nome}: R${gerente.obter_salario()}")
