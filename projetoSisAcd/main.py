from cadAluno import registration, searchStudent
from cadProfessor import registrationTeacher, searchTeacher
from turmas import registrationClass
from disciplina import confirmSup
from os import system
from tinydb import TinyDB, Query


choice = input('O que você deseja fazer? \nPesquisar (P) ou registrar (R) ou fazer uma alocação (A)? ')

def mainReg():
    if choice.upper() == 'R': 
        todo = input('O que deseja registrar? \nAluno, Professor, Turma ou Disciplina? ')
    if  todo.lower() == 'a':
        registration()
        retry = input('quer tentar novamente? \n[S] [N]: ')
        if retry.upper() == 'N':
            system('cls')
            print('ok, até mais!')
        else:
            system('cls')
            return mainReg()
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
    elif todo.lower == 'd':
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
        ...
    elif wish.lower() == 't':   
        ...
    elif wish.lower() == 'd':
        ...
    else:
        print('opção invalida')
        return mainSearch()

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
            student = input("Digite o nome do aluno: ")
            if record:
                stu = record['Alunos']
                stu.append(student)
                team.update({'Alunos': stu}, query.nomeDaTurma == choiceTeam)
            confirm = input("Deseja adicionar mais um aluno? (s/n): ")
            if confirm.lower() == 'n':
                _ = False
                system('cls')
            else:
                continue
            
    elif choiceAllo.lower() == 'd':
        teacher = TinyDB('Teacher.json')
        supplies = TinyDB('disciplinas.json')
        choiceTea = input('Qual professor deseja alocar? ')
        choiceSupp = input('Qual disciplina deseja alocar? ')
        supplies.update({'Professor': choiceTea}, query.Disciplina == choiceSupp)
    
allocation()
        
         