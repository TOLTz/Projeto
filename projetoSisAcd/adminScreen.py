from cadAluno import registration, searchStudent
from cadProfessor import registrationTeacher, searchTeacher
from turmas import registrationClass, searchClass
from disciplina import confirmSup, searchSupplies
from os import system
from tinydb import TinyDB, Query


def mainReg():
    """
    Funcao para realizar o registro de dados no banco de dados
    """
    todo = input('O que deseja registrar? \nAluno (A), Professor (P), Turma (T) ou Disciplina (D)? ')
    if  todo.lower() == 'a':
        registration()
    elif todo.lower() == 'p':
        registrationTeacher()
    elif todo.lower() == 't':
        registrationClass()
    elif todo.lower() == 'd':
        confirmSup()
    else:
        print('opção invalida')
        return mainReg()


def mainSearch():
    """
        funcao exclusiva para executar a busca de dados
    
    """
    wish = input('deseja buscar por Aluno (A), Professor (P), Turma (T) ou Disciplina (D)? ')
    if wish.lower() == 'a':
        searchStudent()
    elif wish.lower() == 'p':
        searchTeacher()
    elif wish.lower() == 't':   
        searchClass()
    elif wish.lower() == 'd':
        searchSupplies()
    else:
        print('opção invalida')
        return mainSearch()

def verify(name):
    """Verifica se o estudante ja esta cadastrado no sistema 

    Args:
        name (str): Nome do aluno que ira verificar a existencia

    Returns:
       bool: True or False
    """
    studentQuery = Query()
    dbStudent = TinyDB('Aluno.json')
    dbTeam = TinyDB('Turmas.json')
    inStudent = dbStudent.contains(studentQuery.Nome == name)
    inTeam = dbTeam.contains(lambda turma: name in turma['Alunos'])
    return inStudent and inTeam

def allocation():
    """A funcao serve para alocar alunos em turmas, disciplinas em professores e disciplina em turmas
    """
    choiceAllo = input('Deseja alocar um professor (P), um aluno (A) ou uma disciplinas (D)? ')
    query = Query()
    if choiceAllo.lower() == 'p':
        teacher = TinyDB('Teacher.json')
        supplies = TinyDB('disciplinas.json')
        choiceTea = input('Qual professor deseja alocar? ')
        choiceTea = choiceTea.title().replace(' ', '_')
        choiceSupp = input('Qual disciplina deseja alocar? ')
        supplies.update({'Professor': choiceTea}, query.Disciplina == choiceSupp)
        recordt = teacher.get(query.Nome == choiceTea)
        if recordt:
            teaSupp = recordt['disciplina']
            teaSupp.append(choiceSupp)
            teacher.update({'disciplina': teaSupp}, query.Nome == choiceTea)
        
    elif choiceAllo.lower() == 'a':
        team = TinyDB('Turmas.json')
        choiceTeam = input('qual turma deseja alocar o(s) aluno(s)? ')
        record = team.get(query.nomeDaTurma == choiceTeam)
        _ = True
        while _:
            student = input("Digite o nome do aluno: ").replace(' ', '_')
            student = student.title()
            if record:
                stud = record['Alunos']
                stud.append(student)
                team.update({'Alunos': stud}, query.nomeDaTurma == choiceTeam)
                _verify = verify(student)
                if _verify:
                    db = TinyDB('Aluno.json')
                    db.update({'Status':'Matriculado'}, query.Nome == student)
                    db.update({'Turma': choiceTeam}, query.Nome == student)           
            confirm = input("Deseja adicionar mais um aluno? (s/n): ")
            if confirm.lower() == 'n':
                _ = False
                system('cls')
            else:
                continue
           
    elif choiceAllo.lower() == 'd':
        teacherOrClass = input('Deseja alocar uma disciplina a uma turma (T) ou a um professor(P)? ')
        if teacherOrClass.lower() == 'p':
            teacher = TinyDB('Teacher.json')
            supplies = TinyDB('disciplinas.json')
            choiceSupp = input('Qual disciplina deseja alocar? ')
            choiceTea = input('Qual professor deseja alocar? ')
            choiceTea = choiceTea.replace(' ', '_').title()
            supplies.update({'Professor': choiceTea}, query.Disciplina == choiceSupp)
            recordt = teacher.get(query.Nome == choiceTea)
        if recordt:
            teaSupp = recordt['disciplina']
            teaSupp.append(choiceSupp)
            teacher.update({'disciplina': teaSupp}, query.Nome == choiceTea)
        
        elif teacherOrClass.lower() == 't':
            team = TinyDB('Turmas.json')
            choiceTeam = input('qual turma deseja alocar a disciplina? ')
            record = team.get(query.nomeDaTurma == choiceTeam)
            _ = True
            while _:
                discipline = input("Digite o nome da disciplina: ")
                if record:
                    dis = record['Disciplinas']
                    dis.append(discipline)
                    team.update({'Disciplinas': dis}, query.nomeDaTurma == choiceTeam)
                    confirm = input("Deseja adicionar mais uma disciplina? (s/n): ")
                    if confirm.lower() == 'n':
                        _ = False
                        system('cls')
                    else:
                        continue

def delete(args):
    """A funcao delete é responsavel por deletar uma disciplina ou uma turma 

    Args:
        args (str): Seleciona Turma ou disciplina, para acessar o banco de dados correto

    Returns:
    """
    query = Query()
    bd = TinyDB(f'{args}.json')
    
    if args == 'Turmas':
        choiceName = input('Qual voce deseja excluir? ')
        record = bd.get(query.nomeDaTurma == choiceName)
        if record:
            print(record)
            confirm = input('Tem certeza? (s/n): ')
        if confirm.lower() == 's':
            bd.remove(query.nomeDaTurma == choiceName)
        else:
            retry = input('quer deletar mais algo?')
            if retry.lower() == 's':
                return delete(args)
            else:
                system('cls')
    elif args.lower() == 'disciplinas':
        choiceName = input('Qual voce deseja excluir? ').capitalize()
        record = bd.get(query.Disciplina == choiceName)
        if record:
            print(record)
            confirm = input('Tem certeza? (s/n): ')
            if confirm.lower() == 's':
                bd.remove(query.Disciplina == choiceName)
            else:
                retry = input('quer deletar mais algo?')
                if retry.lower() == 's':
                    return delete(args)
                else:
                    system('cls')
