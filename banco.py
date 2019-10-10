# Linguagem de Programação II
# AC05 ADS2D - Banco
#
# Alunos: breno.abreu@aluno.faculdadeimpacta.com.br
#         hadnan.basilio@aluno.faculdadeimpacta.com.br

from typing import Union, List, Dict

Number = Union[int, float]


class Cliente():
    """
    Classe Cliente do Banco.

    possui os atributos: nome, telefone e email, todos privados
    caso o email não seja um email válido gera um ValueError,
    caso o telefone não seja um número gera um TypeError
    """

    def __init__(self, nome: str, telefone: int, email: str):
        self.__nome = nome
        if type(telefone) != int:
            raise TypeError('Favor digitar um telefone válido.')
        self.__telefone = telefone
        self.lista = list(email)
        if "@" not in self.lista:
            raise ValueError('Favor digitar um e-mail válido.')
        self.__email = email

    def get_nome(self) -> str:
        """Acessor do atributo Nome."""
        return self.__nome

    def get_telefone(self) -> int:
        """Acessor do atributo Telefone."""
        return self.__telefone

    def set_telefone(self, novo_telefone: int) -> None:
        """
        Mutador do atributo telefone, caso não receba um número,
        gera um TypeError
        """
        if type(novo_telefone) != int:
            raise TypeError('Favor digitar um telefone válido.')
        self.__telefone = novo_telefone

    def get_email(self) -> str:
        """Acessor do atributo Email."""
        return self.__email

    def set_email(self, novo_email: str) -> None:
        """
        Mutador do atributo Email, caso não receba um email válido
        gera um ValueError.
        """
        self.novo_email = novo_email
        lista_email = list(novo_email)
        if "@" not in lista_email:
            raise ValueError('Este e-mail não pode ser válidado')   
        self.__email = self.novo_email
   

class Banco():
    """
    A classe Banco deverá receber um nome em sua construção e deverá
    implementar os métodos:
    * abre_contas: abre uma nova conta, atribuindo o numero da conta em ordem
    crescente.
    * lista_contas(): apresenta um resumo de todas as contas do banco
    DICA: mantenha uma variável interna que armazene todas as contas do banco
    DICA2: utilze a variável acima para gerar automaticamente o número das
    contas do banco
    """
    
    def __init__(self, nome: str):
        self.__nome = nome
        self.id_cliente = 0
        self.contas = []
       
    def get_nome(self) -> str:
        """Acessor do Atributo Nome."""
        return self.__nome

    def abre_conta(self, _cliente: Cliente, saldo_ini: Number) -> None:
        """
        Método para abertura de nova conta, recebe os clientes
        e o saldo inicial.
        Caso o saldo inicial seja menor que 0 devolve um ValueError
        """
        if saldo_ini < 0:
            raise ValueError('Saldo insuficiente para abertura de conta')
        self.id_cliente += 1
        self.saldo_ini = saldo_ini
        nova_conta = Conta(_cliente, self.id_cliente, saldo_ini)
        self.contas.append(nova_conta)

    def lista_contas(self) -> List['Conta']:
        """Retorna a lista com todas as contas do banco."""
        return self.contas

class Conta():
    """
    Classe Conta.
    * Todas as operações (saque e deposito, e saldo inicial) devem aparecer
    no extrato como tuplas, exemplo ('saque', 100), ('deposito'), 200) etc.
    * Caso o saldo inicial seja menor que zero deve lançar um ValueError
    * A criação da conta deve aparecer no extrato com o valor
    do saldo_inicial, exemplo: ('saldo_inicial', 1000)
    DICA: Crie uma variável interna privada para guardar as
    operaões feitas na conta
    """

    def __init__(self, clientes: List[Cliente], numero_conta: int,
                 saldo_inicial: Number):
        self.__clientes = clientes
        self.__numero_conta = numero_conta
        self.__saldo_inicial = saldo_inicial
        self.__saldo_atual = saldo_inicial
        self.__extrato = []
        self.__extrato.append (('saldo_inicial',self.__saldo_inicial))

    def get_clientes(self) -> List[Cliente]:
        '''
        Acessor para o atributo Clientes
        '''
        return self.__clientes

    def get_saldo(self) -> Number:
        '''
        Acessor para o Atributo Saldo
        '''
        return self.__saldo_inicial

    def get_numero(self) -> int:
        '''
        Acessor para o atributo Numero
        '''
        return self.__numero_conta

    def saque(self, valor: Number) -> None:
        '''
        Método de saque da classe Conta, operação deve aparecer no extrato
        Caso o valor do saque seja maior que o saldo da conta,
        deve retornar um ValueError, e não efetuar o saque
        '''
        self.valor_saque = valor
        if self.valor_saque > self.__saldo_atual:
            raise ValueError('Saque maior que o saldo existente na conta')
        self.__saldo_atual -= self.valor_saque
        self.__extrato.append(('saque',self.valor_saque))

    def deposito(self, valor: Number):
        '''
        Método depósito da classe Conta, operação deve aparecer no extrato
        '''
        self.valor_deposito = valor
        if self.valor_deposito < 1:
            raise ValueError('Depósito com valor inválido')
        self.__saldo_atual += self.valor_deposito
        self.__extrato.append(('deposito',self.valor_deposito))

    def extrato(self) -> List[Dict[str, Number]]:
        '''
        Retorna uma lista com as operações (Tuplas) executadas na Conta
        '''
        return self.__extrato
