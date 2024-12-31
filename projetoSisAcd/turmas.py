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
    return {'nomeDaTurma': team, 'idDaTurma': idTeam, 'Periodo': time, 'alunos': [], 'Disciplina': []}

 
    
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

    Returns:
        _type_: _description_
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
                continue
        else:
            print('Cadastro cancelado!')
            retry = input('quer tentar novamente? \n[S] [N]: ')
            if retry.upper() == 'N':
                return print('Ok, até mais!')
            else:
                continue

            
def searchClass():
    query = Query()
    teacher = TinyDB('disciplinas.json')
    chooseItem = input('deseja pesquisar por: \nNome/Curso (N), código de turma (C) ou Disciplina (D)? ')
    if chooseItem.upper() == 'N':
        searchName = input('digite o nome da turma: ')
        searchName = searchName.capitalize()
        searched = teacher.search(query.nomeDaTurma.search(searchName))
        if searched == []:
            print('Turma nao encontrada')
            retry = input('quer tentar dnv? (s/n)')
            if retry.upper() == 'S':
                system('cls')
                return searchClass()
            else:
                return print('Ok, até mais!')
        else:
            print(searched)
    elif chooseItem.upper() == 'C':
        searchRegistration = input('digite o código da turma: ')
        searchRegistration = searchRegistration.upper()
        searched = teacher.search(query.Matricula.search(searchRegistration))
        if searched == []:
            print('Turma nao encontrada')
            retry = input('quer tentar dnv? (s/n)')
            if retry.upper() == 'S':
                system('cls')
                return searchClass()
            else:
                return print('Ok, até mais!')
        else:
            print(searched)
    elif chooseItem.upper() == 'D':
        searchSupplies = input('digite a Disciplina da turma: ')
        searchSupplies = searchSupplies.upper()
        searched = teacher.search(query.disciplina.search(searchSupplies))
        if searched == []:
            print('Turma nao encontrada')
            retry = input('quer tentar dnv? (s/n)')
            if retry.upper() == 'S':
                system('cls')
                return searchClass()
            else:
                return print('Ok, até mais!')
        else:
            print(searched)
    else:
        print('opcao invalida')
        return searchClass()

