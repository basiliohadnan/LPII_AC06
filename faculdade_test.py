from faculdade import Disciplina, Pessoa, Aluno, Professor


def test_disciplina():
    dis = Disciplina('Linguagem de Programação II', 80)
    assert dis.get_nome() == 'Linguagem de Programação II'
    assert dis.get_carga_horaria() == 80


def test_pessoa():
    pes = Pessoa('Fulano da Silva', 999999, 'fulano@mail.com')
    assert pes.get_nome() == 'Fulano da Silva'
    assert pes.get_email() == 'fulano@mail.com'
    assert pes.get_telefone() == 999999


def test_pessoa_set_tel():
    pes = Pessoa('Fulano da Silva', 999999, 'fulano@mail.com')
    pes.set_telefone(888888)
    assert pes.get_telefone() == 888888


def test_pessoa_set_tel_errado():
    pes = Pessoa('Fulano da Silva', 999999, 'fulano@mail.com')
    try:
        pes.set_telefone('não é um telefone')
    except TypeError:
        pass
    else:
        assert pes.get_telefone() == 999999


def test_pessoa_set_mail():
    pes = Pessoa('Fulano da Silva', 999999, 'fulano@mail.com')
    pes.set_email('fulano@othermail.com')
    assert pes.get_email() == 'fulano@othermail.com'


def test_pessoa_set_mail_errado():
    pes = Pessoa('Fulano da Silva', 999999, 'fulano@mail.com')
    try:
        pes.set_email('não é um email')
    except ValueError:
        pass
    else:
        assert pes.get_email() == 'fulano@mail.com'


def test_aluno():
    al = Aluno('Cicrano Souza', 999999, 'cicrano@mail.com', 123456)
    assert al.get_matricula() == 123456
    assert al.get_nome() == 'Cicrano Souza'
    assert al.get_email() == 'cicrano@mail.com'
    assert al.get_telefone() == 999999


def test_aluno_matricula():
    dis = Disciplina('Linguagem de Programação II', 80)
    al = Aluno('Cicrano Souza', 999999, 'cicrano@mail.com', 123456)
    al.matricular(dis)
    assert dis in al.lista_disciplinas()


def test_professor():
    prof = Professor('Cicrano Souza', 999999, 'cicrano@mail.com')
    assert prof.get_nome() == 'Cicrano Souza'
    assert prof.get_email() == 'cicrano@mail.com'
    assert prof.get_telefone() == 999999


def test_prof_ministra():
    dis1 = Disciplina('Linguagem de Programação II', 80)
    dis2 = Disciplina('Tecnologias Web', 80)
    prof = Professor('Cicrano Souza', 999999, 'cicrano@mail.com')
    prof.ministra(dis1)
    prof.ministra(dis2)
    assert len(prof.lista_disciplinas()) == 2
    assert dis1 in prof.lista_disciplinas()
    assert dis2 in prof.lista_disciplinas()


def test_prof_ministra_erro():
    dis1 = Disciplina('Linguagem de Programação II', 80)
    dis2 = Disciplina('Tecnologias Web', 80)
    dis3 = Disciplina('Linguagem SQL', 80)
    prof = Professor('Cicrano Souza', 999999, 'cicrano@mail.com')
    try:
        prof.ministra(dis1)
        prof.ministra(dis2)
        prof.ministra(dis3)
    except ValueError:
        pass
    else:
        assert len(prof.lista_disciplinas()) == 2
        assert dis1 in prof.lista_disciplinas()
        assert dis2 in prof.lista_disciplinas()
