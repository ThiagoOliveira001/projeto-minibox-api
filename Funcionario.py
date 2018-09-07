from Cliente import Cliente

class Funcionario(Cliente):
    def __init__(self, cargo, salario, nome, cep, logradouro, bairro, municipio, estado, cpf, dtnascimento, telefone):
            self.__cargo = cargo
            self.__salario = salario
            return super().__init__(nome, cep, logradouro, bairro, municipio, estado, cpf, dtnascimento, telefone)
    
    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        self.__salario = salario