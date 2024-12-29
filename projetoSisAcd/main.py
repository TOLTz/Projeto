from cadAluno import registration
from cadProfessor import registrationTeacher
from turmas import registrationClass
from disciplina import confirmSup
from os import system

print('olá, bem vindo ao sistema academico')
stuOrTea = input('Você é um professor ou aluno? ')


choice = input('O que você deseja fazer? \nPesquisar (P) ou registrar (R) ou fazer alocação (A)? ')
_ = True
while _:
    if choice.upper() == 'R': 
        todo = input('O que deseja registrar? \nAluno, Professor, Turma ou Disciplina? ')
    if  todo.lower() == 'a':
        registration()
        retry = input('quer tentar novamente? \n[S] [N]: ')
        if retry.upper() == 'N':
            _ = False
            system('cls')
            print('ok, até mais!')
        else:
            system('cls')
            continue
    elif todo.lower() == 'p':
        registrationTeacher()
        retry = input('quer tentar dnv?')
        if retry.upper() == 'N':
            _ = False
            system('cls')
            print('ok, até mais!')
        else:
            system('cls')
            continue
    elif todo.lower == 't':
        registrationClass()
        retry = input('quer tentar dnv?')
        if retry.upper() == 'N':
            _ = False
            system('cls')
            print('ok, até mais!')
        else:
            system('cls')
            continue
    elif todo.lower == 'd':
        confirmSup()
        retry = input('quer tentar dnv?')
        if retry.upper() == 'N':
            _ = False
            system('cls')
            print('ok, até mais!')
        else:
            system('cls')
            continue
    else:
        print('opção invalida')
        continue
        
    
    