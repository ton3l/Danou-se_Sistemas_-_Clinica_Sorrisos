"""Danou-se Sistemas - Clínica Sorriso"""

class Pessoas:
    """Pessoas cadastradas no sistema"""
    def __init__(self, nome, cpf, telefone, rua, cidade, estado, classe):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._rua = rua
        self._cidade = cidade
        self._estado = estado
        self._classe = classe
        self._dados = {}
        self._dados['nome'] = nome
        self._dados['cpf'] = cpf
        self._dados['telefone'] = telefone
        self._dados['rua'] = rua
        self._dados['cidade'] = cidade
        self._dados['estado'] = estado
        self._dados['classe'] = classe

    @property
    def _cpf(self):
        """Getter self.__cpf"""
        return self.__cpf

    @_cpf.setter
    def _cpf(self, cpf):
        """Setter self.__cpf"""
        cpf_str = []
        for caractere in cpf:
            cpf_str.append(caractere)
        for i, caractere in enumerate(cpf_str):
            if not caractere.isnumeric():
                cpf_str.pop(i)
        if len(cpf_str) != 11:
            self.__cpf = 'Erro, digite um cpf válido'
            return self.__cpf
        c = 0
        while c <= 9:
            if c == 9:
                cpf_str.insert(c + 3, '-')
                break
            elif c % 4 == 0:
                cpf_str.insert(c, '.')
                c+=1
            else:
                c+=1
        cpf_str.pop(0)
        cpf = ''.join(cpf_str)
        self.__cpf = cpf
        return self.__cpf

    def atualizar_dados(self):
        """Atualizando os atributos pelo dicionário"""
        self._nome = self._dados['nome']
        self._cpf = self._dados['cpf']
        self._telefone = self._dados['telefone']
        self._rua = self._dados['rua']
        self._cidade = self._dados['cidade']
        self._estado = self._dados['estado']
        self._classe = self._dados['classe']

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
        return f"""
Nome: {self._nome}
CPF: {self._cpf}
Telefone: {self._telefone} 
Rua: {self._rua}
Cidade: {self._cidade}
Estado: {self._estado}
Classe: {self._classe}
"""

class Funcionarios(Pessoas):
    """Funcionários da clínica"""
    lista_func = []

    def __init__(self, nome, cpf, telefone, rua, cidade, estado, salario, funcao, classe = 'Funcionário'):
        super().__init__(nome, cpf, telefone, rua, cidade, estado, classe)
        self._salario = salario
        self._funcao = funcao
        self._dados['salário'] = self._salario
        self._dados['função'] = self._funcao
        Funcionarios.lista_func.append(self)

    def  __str__(self):
        return f'{super().__str__()}Função: {self._funcao}\nSalário: {self._salario}'

    def atualizar_dadosf(self):
        """Atualizar dados do funcionário"""
        super().atualizar_dados()
        self._salario = self._dados['salário']
        self._funcao = self._dados['função']

    @classmethod
    def cadastrar_funcionario(cls):
        """Cadastramento de funcionário"""
        dados = super().cadastrar()
        salario = input('Digite seu salario: ')
        funcao = input('Digite sua função: ')
        return cls.lista_func.append(Funcionarios(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], salario, funcao))

    @classmethod
    def pesquisar_funcionario(cls):
        """Pesquisa e exibição de funcionário"""
        func = input('Digite o funcionário a ser exibido(Nome ou CPF): ')
        for objeto in cls.lista_func:
            if objeto._nome == func or objeto._cpf == func:
                return objeto

    @classmethod
    def editar_funcionario(cls):
        """Edição de dados do funcionário"""
        func = input('Digite o funcionário a ser editado(Nome ou CPF): ')
        for objeto in cls.lista_func:
            if objeto._nome == func or objeto._cpf == func:
                dado = (input('Digite o dado a ser alterado: ')).lower()
                new = input(f'Digite o novo valor para o/a {dado}: ')
                objeto._dados[dado] = new
                objeto.atualizar_dadosf()

    @classmethod
    def deletar_funcionario(cls):
        func = input('Digite o funcionário a ser deletado(Nome ou CPF): ')
        for objeto in cls.lista_func:
            if objeto._nome == func or objeto._cpf == func:
                resposta = input(f'Tem certeza de que quer deletar {objeto._nome} do sistema(S/N)?: ').lower()
                if resposta == 's' or resposta == 'sim':
                    cls.lista_func.remove(objeto)
                    return 'Funcionário deletado com sucesso'
                else:
                    return 'O funcionário não foi deletado'

    @classmethod
    def mostrar_todos(cls):
        """Exibe o nome e o telefone de todos os funcionários cadastrados"""
        for objeto in cls.lista_func:
            print(f'\nNome: {objeto._nome}\nTelefone: {objeto._telefone}\n')

class Pacientes(Pessoas):
    """Pacientes da clínica"""
    lista_pac = []
    def __init__(self, nome, cpf, telefone, rua, cidade, estado, indicacao, classe = 'Paciente'):
        super().__init__(nome, cpf, telefone, rua, cidade, estado, classe)
        self._indicacao = indicacao
        Pacientes.lista_pac.append(self)

    def __str__(self):
        return f'{super().__str__()}Indicação: {self._indicacao}'

    @classmethod
    def cadastrar_paciente(cls):
        """Cadastramento de pacientes"""
        dados = super().cadastrar()
        indicacao = input('Como você chegou até nossa clínica?: ')
        return cls.lista_pac.append(Pacientes(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], indicacao))

    @classmethod
    def pesquisar_paciente(cls):
        """Pesquisa e exibição de paciente"""
        func = input('Digite o paciente a ser exibido(Nome ou CPF): ')
        for objeto in cls.lista_pac:
            if objeto._nome == func or objeto._cpf == func:
                return objeto

    @classmethod
    def editar_paciente(cls):
        """Edição de dados do paciente"""
        func = input('Digite o paciente a ser editado(Nome ou CPF): ')
        for objeto in cls.lista_pac:
            if objeto._nome == func or objeto._cpf == func:
                dado = (input('Digite o dado a ser alterado: ')).lower()
                new = input(f'Digite o novo valor para o/a {dado}: ')
                objeto._dados[dado] = new
                objeto.atualizar_dadosf()

    @classmethod
    def deletar_paciente(cls):
        func = input('Digite o paciente a ser deletado(Nome ou CPF): ')
        for objeto in cls.lista_pac:
            if objeto._nome == func or objeto._cpf == func:
                resposta = input(f'Tem certeza de que quer deletar {objeto._nome} do sistema(S/N)?: ').lower()
                if resposta == 's' or resposta == 'sim':
                    cls.lista_pac.remove(objeto)
                    return 'Paciente deletado com sucesso'
                else:
                    return 'O paciente não foi deletado'

    @classmethod
    def mostrar_todos(cls):
        """Exibe o nome e o telefone de todos os paciente cadastrados"""
        for objeto in cls.lista_pac:
            print(f'\nNome: {objeto._nome}\nTelefone: {objeto._telefone}\n')


class Usuarios:
    """Usuários do sistema"""
    lista_usuarios = []
    def __init__(self, login, senha):
        self.__login = login
        self.__senha = senha

    def __str__(self):
        return f'Login: {self.__login}\nClasse: Usuário'

    @classmethod
    def cadastrar_usuario(cls):
        """Cadastramento de usuário"""
        login = input('Digite seu login: ')
        senha = input('Digite sua senha: ')
        return cls.lista_usuarios.append(Usuarios(login, senha))


class Program:
    """Classe"""
    def __init__(self) -> None:
        pass
    def __str__(self):
        CADASTRAR = '1'
        EXIBIR = '2'
        EDITAR = '3'
        DELETAR = '4'

        return f"""
            --------------------------    Clínica Sorrisos    --------------------------
            {CADASTRAR}
        """
