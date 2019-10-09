# Linguagem de Programação II
# AC06 ADS2D - Faculdade
# alunos: aluno1.sobrenome@aluno.faculdadeimpacta.com.br
#         aluno2.sobrenome@aluno.faculdadeimpacta.com.br


class Disciplina:
    '''
    Abstração de uma disciplinai, possui os atributos Nome e carga Horária
    '''
    def __init__(self, nome: str, carga_horaria: int) -> None:
        pass

    def get_nome(self) -> str:
        '''
        Acessor do atributo nome
        '''
        pass

    def get_carga_horaria(self) -> int:
        '''
        Acessor do atributo cargar horaria
        '''
        pass


class Pessoa:
    '''
    Abstração de uma pessoa no Modelo, classe base para Aluno e Professor
    que contém dados pertencentes a ambos.
    '''
    def __init__(self, nome: str, telefone: int, email: float) -> None:
        pass

    def get_nome(self) -> str:
        '''
        Acessor do atributo Nome
        '''
        pass

    def get_telefone(self) -> int:
        '''
        Acessor do atributo telefone
        '''
        pass

    def set_telefone(self, novo_telefone: int) -> None:
        '''
        Mutador do atributo telefone deve checar se é um número inteiro e,
        caso contrário devolver um TypeError
        '''
        pass

    def get_email(self) -> str:
        '''
        Acessor do atributo email
        '''
        pass

    def set_email(self, novo_email) -> None:
        '''
        Mutador do atributo eail, deve checar se éum email válido
        (se possuir o caractere '@') e caso contrário devolver
        um ValueError
        '''
        pass


class Aluno(Pessoa):

    def __init__(self, nome: str, telefone: int,
                 email: str, n_matricula: int) -> None:
        pass

    def get_matricula(self) -> int:
        '''
        Acessor do atributo matricula
        '''
        pass

    def matricular(self, disciplina: Disciplina) -> None:
        '''
        Realiza matrícula do Aluno na disciplina
        '''
        pass

    def lista_disciplinas(self) -> list:
        '''
        Devolve a lista de disciplinas em que o aluno esta matriculado
        '''
        pass


class Professor(Pessoa):
    '''
    Entidade professor do Modelo
    '''
    def __init__(self, nome, telefone, email):
        pass

    def ministra(self, disciplina: Disciplina) -> None:
        '''
        Atribui o professor como ministrante da disiciplina
        Um professor não pode dar mais de 200 horas de aula,
        Caso um professor tente atribuir mais de 200h devolve
        ValueError
        '''
        pass

    def lista_disciplinas(self) -> list:
        '''
        lista as disciplinas ministradas pelo professor
        '''
        pass
