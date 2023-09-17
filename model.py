"""Danou-se Sistemas - Clínica Sorriso"""

class Pessoas:
    """Pessoas cadastradas no sistema"""
    def __init__(self, nome, cpf, telefone, rua, cidade, estado, classe):
        self.nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__rua = rua
        self.__cidade = cidade
        self.__estado = estado
        self.__classe = classe

    @classmethod
    def cadastrar(cls):
        """Dados para cadastro geral"""
        nome = input('Digite seu nome: ')
        cpf = input('Digite seu cpf: ')
        telefone = int(input('Digite seu telefone: '))
        rua = input('Digite sua rua: ')
        cidade = input('Digite sua cidade: ')
        estado = input('Digite seu estado: ')
        return nome, cpf, telefone, rua, cidade, estado

    def __str__(self):
        return f'Nome: {self.nome} \nTelefone: {self.__telefone} \nClasse: {self.__classe}'

class Funcionarios(Pessoas):
    """Funcionários da clínica"""
    lista_func = []

    def __init__(self, nome, cpf, telefone, rua, cidade, estado, salario, funcao, classe = 'Funcionário'):
        super().__init__(nome, cpf, telefone, rua, cidade, estado, classe)
        self.__salario = salario
        self.__funcao = funcao
        Funcionarios.lista_func.append(self)

    @classmethod
    def cadastrar_funcionario(cls):
        """Cadastramento de funcionário"""
        dados = super().cadastrar()
        salario = input('Digite seu salario: ')
        funcao = input('Digite sua função: ')
        return cls.lista_func.append(Funcionarios(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], salario, funcao))

class Pacientes(Pessoas):
    """Pacientes da clínica"""
    lista_pac = []
    def __init__(self, nome, cpf, telefone, rua, cidade, estado, indicacao, classe = 'Paciente'):
        super().__init__(nome, cpf, telefone, rua, cidade, estado, classe)
        self.__indicacao = indicacao
        Pacientes.lista_pac.append(self)

    @classmethod
    def cadastrar_paciente(cls):
        """Cadastramento de pacientes"""
        dados = super().cadastrar()
        indicacao = input('Como você chegou até nossa clínica?: ')
        return cls.lista_pac.append(Pacientes(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], indicacao))


class Usuarios:
    """Usuários do sistema"""
    lista_usuarios = []
    def __init__(self, login, senha):
        self.__login = login
        self.__senha = senha

    @classmethod
    def cadastrar_usuario(cls):
        """Cadastramento de usuário"""
        login = input('Digite seu login: ')
        senha = input('Digite sua senha: ')
        return cls.lista_usuarios.append(Usuarios(login, senha))
