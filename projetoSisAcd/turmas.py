import string
from os import system
import random 
from bd import addData
from tinydb import TinyDB, Query

def team():
    """ Essa função serve para criar uma turma, ainda sem os alunos

    Returns:
        _type_: dict
    """
    team = input("Digite o nome da turma: ")
    idTeam = code()
    time = input('Qual periodo? (Matutino/Vespertino/Noturno) ')
    return {'nomeDaTurma': team, 'idDaTurma': idTeam, 'Periodo': time, 'Alunos': [], 'Disciplinas': []}

 
    
def code():
    """Gera uma sequencia de 4 numeros e uma letra aleatoria para o código de turma.

    Returns:
        Str: retorna uma string com o codigo.
    """
    # gera uma sequencia de 4 numreos aleatorios (a quantidade de numeros e definida pelo 'k')
    # e o os numeros sao definidos pelo 'string.digits')
    num = ''.join(random.choices(string.digits, k= 4))
    letterUpper = random.choice(string.ascii_uppercase) # ascii_uppercase gera letras maiusculas
    registrationId = letterUpper + num 
    return registrationId
    
    
def registrationClass():
    """Esta função adiciona as informações da turma e alunos ao Banco de Dados.
    
    """
    _ = True
    while _:
        _team = team()
        system('cls')
        print(_team)
        confirm = input('Deseja confirmar? \n[S] [N]: ')
        if confirm.upper() == 'S':
            addData('Turmas.json', _team)
            print('Cadastro realizado com sucesso')
            retry = input('quer realizar outro? \n[S] [N]: ')
            if retry.upper() == 'N':
                return print('Ok, até mais!')
            else:
                return registrationClass()
        else:
            print('Cadastro cancelado!')
            retry = input('quer tentar novamente? \n[S] [N]: ')
            if retry.upper() == 'N':
                return print('Ok, até mais!')
            else:
                return registrationClass()

            
def searchClass():
    """Funcao que busca as turmas no Banco de Dados.

    Returns:
        List : Retorna uma lista com as Turmas
    """
    query = Query()
    team = TinyDB('Turmas.json')
    chooseItem = input('deseja pesquisar por: \nNome/Curso (N), código de turma (C), aluno (A) ou Disciplina (D)? ')
    if chooseItem.upper() == 'N':
        searchName = input('digite o nome da turma: ')
        searched = team.search(query.nomeDaTurma.search(searchName))
        if searched == []:
            print('Turma nao encontrada')
            retry = input('quer tentar dnv? (s/n)')
            if retry.upper() == 'S':
                system('cls')
                return searchClass()
            else:
                return print('Ok, até mais!')
        else:
            for i in searched:
                print(i)
                print()
    elif chooseItem.upper() == 'C':
        searchRegistration = input('digite o código da turma: ')
        searchRegistration = searchRegistration.upper()
        searched = team.search(query.Matricula.search(searchRegistration))
        if searched == []:
            print('Turma nao encontrada')
            retry = input('quer tentar dnv? (s/n)')
            if retry.upper() == 'S':
                system('cls')
                return searchClass()
            else:
                return print('Ok, até mais!')
        else:
            for i in searched:
                print(i)
                print()
    elif chooseItem.upper() == 'D':
        searchSupplies = input('digite a Disciplina da turma: ')
        searchSupplies = searchSupplies.capitalize()
        searched = team.search(query.Disciplinas.any(searchSupplies))
        if searched == []:
            print('Turma nao encontrada')
            retry = input('quer tentar dnv? (s/n)')
            if retry.upper() == 'S':
                system('cls')
                return searchClass()
            else:
                return print('Ok, até mais!')
        else:
            for i in searched:
                print(i)
                print()
    elif chooseItem.upper() == 'A':
        searchStudent = input('digite o nome do aluno: ')
        searchStudent = searchStudent.title().replace(' ', '_')
        searched = team.search(query.Alunos.any(searchStudent))
        if searched == []:
            print('Turma nao encontrada')
            retry = input('quer tentar dnv? (s/n)')
            if retry.upper() == 'S':
                system('cls')
                return searchClass()
            else:
                return print('Ok, até mais!')
        else:
            for i in searched:
                print(i)
                print()
    else:
        print('opcao invalida')
        return searchClass()
