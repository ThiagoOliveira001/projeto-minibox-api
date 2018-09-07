class Cliente():
    def __init__(self, nome, cep, logradouro, bairro, municipio, estado, cpf, dtnascimento, telefone):
        self.__nome = nome
        self.__cep = cep
        self.__logradouro = logradouro
        self.__bairro = bairro
        self.__municipio = municipio
        self.__estado = estado
        self.__cpf = cpf
        self.__dtnascimento = dtnascimento
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cep(self):
        return self.__cep
    
    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @property
    def logradouro(self):
        return self.__logradouro

    @logradouro.setter
    def logradouro(self, logradouro):
        self.__logradouro = logradouro
    
    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @property
    def municipio(self):
        return self.__municipio
    
    @municipio.setter
    def municipio(self, municipio):
        self.__municipio = municipio

    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def dtnascimento(self):
        return self.__dtnascimento

    @dtnascimento.setter
    def dtnascimento(self, dtnascimento):
        self.__dtnascimento = dtnascimento

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone