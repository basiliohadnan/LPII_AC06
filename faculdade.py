# Linguagem de Programação II
# AC06 ADS2D - Faculdade
# alunos: guilherme.dalbuquerque@aluno.faculdadeimpacta.com.br
#         hadnan.basilio@aluno.faculdadeimpacta.com.br


class Disciplina:
    '''
    Abstração de uma disciplinai, possui os atributos Nome e carga Horária
    '''
    def __init__(self, nome: str, carga_horaria: int) -> None:
        self.nome = nome
        self.carga_horaria = carga_horaria

    def get_nome(self) -> str:
        '''
        Acessor do atributo nome
        '''
        return self.nome

    def get_carga_horaria(self) -> int:
        '''
        Acessor do atributo cargar horaria
        '''
        return self.carga_horaria


class Pessoa:
    '''
    Abstração de uma pessoa no Modelo, classe base para Aluno e Professor
    que contém dados pertencentes a ambos.
    '''
    def __init__(self, nome: str, telefone: int, email: float) -> None:
        self._nome = nome
        self._telefone = telefone
        self._email = email

    def get_nome(self) -> str:
        '''
        Acessor do atributo Nome
        '''
        return self._nome

    def get_telefone(self) -> int:
        '''
        Acessor do atributo telefone
        '''
        return self._telefone

    def set_telefone(self, novo_telefone: int) -> None:
        '''
        Mutador do atributo telefone deve checar se é um número inteiro e,
        caso contrário devolver um TypeError
        '''
        if type(novo_telefone) != int:
            raise TypeError('Formato de telefone inválido!')
        self._telefone = novo_telefone

    def get_email(self) -> str:
        '''
        Acessor do atributo email
        '''
        return self._email

    def set_email(self, novo_email) -> None:
        '''
        Mutador do atributo eail, deve checar se éum email válido
        (se possuir o caractere '@') e caso contrário devolver
        um ValueError
        '''
        if "@" not in list(novo_email):
            raise ValueError('Este e-mail não pode ser válidado')
        self._email = novo_email


class Aluno(Pessoa):

    def __init__(self, nome: str, telefone: int,
                 email: str, n_matricula: int) -> None:
        self._nome = nome
        self._telefone = telefone
        self._email = email
        self._n_matricula = n_matricula
        self._disciplinas_matriculadas = []

    def get_matricula(self) -> int:
        '''
        Acessor do atributo matricula
        '''
        return self._n_matricula

    def matricular(self, disciplina: Disciplina) -> None:
        '''
        Realiza matrícula do Aluno na disciplina
        '''
        self._disciplinas_matriculadas.append(disciplina)

    def lista_disciplinas(self) -> list:
        '''
        Devolve a lista de disciplinas em que o aluno esta matriculado
        '''
        return self._disciplinas_matriculadas


class Professor(Pessoa):
    '''
    Entidade professor do Modelo
    '''
    def __init__(self, nome, telefone, email):
        self._nome = nome
        self._telefone = telefone
        self._email = email
        self.horas_aula = 0
        self.limite_horas_aula = 200
        self.disciplinas_ministradas = []

    def ministra(self, disciplina: Disciplina) -> None:
        '''
        Atribui o professor como ministrante da disiciplina
        Um professor não pode dar mais de 200 horas de aula,
        Caso um professor tente atribuir mais de 200h devolve
        ValueError
        '''
        d = disciplina
        if self.horas_aula + d.carga_horaria >= self.limite_horas_aula:
            raise ValueError('Vá curtir a vida, está trabalhando demais.')
        self.horas_aula += d.carga_horaria
        self.disciplinas_ministradas.append(d)

    def lista_disciplinas(self) -> list:
        '''
        lista as disciplinas ministradas pelo professor
        '''
        return self.disciplinas_ministradas
