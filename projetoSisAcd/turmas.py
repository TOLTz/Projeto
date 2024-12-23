import string
from os import system
import random 
from bd import addData

def team():
    """ Essa função serve para criar uma turma, ainda sem os alunos

    Returns:
        _type_: dict
    """
    team = input("Digite o nome da turma: ")
    idTeam = code()
    time = input('Qual periodo? (Matutino/Vespertino/Noturno) ')
    return {'nome da turma': team, 'id da turma': idTeam, 'Periodo': time}

def addStudant():
    """Esta função cria uma lista com Alunos 

    Returns:
        _type_: list
    """
    studentList = []
    _ = True
    while _:
        system('cls')
        student = input("Digite o nome do aluno: ")
        studentList.append(student)
        confirm = input("Deseja adicionar mais um aluno? (s/n): ")
        if confirm.lower() == 'n':
            _ = False
            system('cls')
    return studentList    
    
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

def unite():
    """Esta função une as duas funções anteriores

    Returns:
        _type_: dict
    """
    teamdata = team()
    studant = addStudant()
    teamdata['Alunos'] = studant
    return teamdata
    
    
def registration():
    """Esta função adiciona as informações da turma e alunos ao Banco de Dados.

    Returns:
        _type_: _description_
    """
    _ = True
    while _:
        _team = unite()
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

registration()