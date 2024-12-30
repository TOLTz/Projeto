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
    return {'nomeDaTurma': team, 'idDaTurma': idTeam, 'Periodo': time, 'alunos': []}

 
    
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