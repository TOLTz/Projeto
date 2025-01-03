from cadAluno import registration, searchStudent
from cadProfessor import registrationTeacher, searchTeacher
from turmas import registrationClass, searchClass
from disciplina import confirmSup, searchSupplies
from os import system
from tinydb import TinyDB, Query


def mainReg():
    todo = input('O que deseja registrar? \nAluno, Professor, Turma ou Disciplina? ')
    if  todo.lower() == 'a':
        registration()
    elif todo.lower() == 'p':
        registrationTeacher()
        retry = input('quer tentar dnv?')
        if retry.upper() == 'N':
            system('cls')
            print('ok, até mais!')
        else:
            system('cls')
            return mainReg()
    elif todo.lower == 't':
        registrationClass()
        retry = input('quer tentar dnv?')
        if retry.upper() == 'N':            
            system('cls')
            print('ok, até mais!')
        else:
            system('cls')
            return mainReg()
    elif todo.lower() == 'd':
        confirmSup()
        retry = input('quer tentar dnv?')
        if retry.upper() == 'N':
            system('cls')
            print('ok, até mais!')
        else:
            system('cls')
            return mainReg()
    else:
        print('opção invalida')
        return mainReg()


def mainSearch():
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
    studentQuery = Query()
    dbStudent = TinyDB('Aluno.json')
    dbTeam = TinyDB('Turmas.json')
    inStudent = dbStudent.contains(studentQuery.Nome == name)
    inTeam = dbTeam.contains(lambda turma: name in turma['Alunos'])
    return inStudent and inTeam

def allocation():
    choiceAllo = input('Deseja alocar um professor (P), um aluno (A) ou uma disciplinas (D)? ')
    query = Query()
    if choiceAllo.lower() == 'p':
        supplies = TinyDB('disciplinas.json')
        choiceTea = input('Qual professor deseja alocar? ')
        choiceSupp = input('Qual disciplina deseja alocar? ')
        supplies.update({'Professor': choiceTea}, query.Disciplina == choiceSupp)
        
    elif choiceAllo.lower() == 'a':
        team = TinyDB('Turmas.json')
        choiceTeam = input('qual turma deseja alocar o(s) aluno(s)? ')
        record = team.get(query.nomeDaTurma == choiceTeam)
        _ = True
        while _:
            student = input("Digite o nome do aluno: ").replace(' ', '_')
            if record:
                stu = record['Alunos']
                stu.append(student)
                team.update({'Alunos': stu}, query.nomeDaTurma == choiceTeam)
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
            supplies = TinyDB('disciplinas.json')
            choiceTea = input('Qual professor deseja alocar? ')
            choiceSupp = input('Qual disciplina deseja alocar? ')
            supplies.update({'Professor': choiceTea}, query.Disciplina == choiceSupp)
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
    query = Query()
    bd = TinyDB(f'{args}.json')
    
    if args.lower() == 'turmas':
        choiceName = input('Qual voce deseja excluir? ')
        record = bd.get(query.nomeDaTurma == choiceName)
        if record:
            print(record)
            confirm = input('Tem certeza? (s/n): ')
        if confirm.lower() == 's':
            bd.remove(query.nomeDaTurma == choiceName)
        else:
            return delete(args)
    elif args.lower() == 'disciplinas':
        choiceName = input('Qual voce deseja excluir? ').capitalize()
        record = bd.get(query.Disciplina == choiceName)
        if record:
            print(record)
            confirm = input('Tem certeza? (s/n): ')
            if confirm.lower() == 's':
                bd.remove(query.Disciplina == choiceName)
            else:
                return delete(args)
