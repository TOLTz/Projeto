import string
from os import system
import random 
from bd import addData
from tinydb import TinyDB, Query


def cadSupplies():
    """ Funcao que cadastra uma nova disciplina
    Returns:
       Dict : Dicionario com as informações da disciplina
    """
    idSupplies = disciplineCode()
    _ = True
    while _:
        try:
            name = input('Qual o nome da disciplina? ')
            workLoad = input('Qual a carga horaria? ')
            
        except:
            system('cls')
            print('Digite uma palavra')
        
        else:
            return {'Disciplina': name.replace(' ', '_'),'Codigo': idSupplies, 'Carga Horaria': workLoad, 'Professor': ''}
        
def disciplineCode():
    """Gera uma sequencia de 5 numeros e uma letra aleatoria para a matricula.

    Returns:
        Str: retorna uma string com o codigo.
    """
    # gera uma sequencia de 5 numreos aleatorios (a quantidade de numeros e definida pelo 'k')
    # e o os numeros sao definidos pelo 'string.digits')
    num = ''.join(random.choices(string.digits, k= 5))
    letterUpper = random.choice(string.ascii_uppercase) # ascii_uppercase gera letras maiusculas
    registrationId = letterUpper + num 
    return registrationId

def confirmSup():
    """ Funcao que confirma a disciplina, caso a disciplina seja confirmada,
    sera adicionada ao banco de dados.

    """
    _ = True
    while _:
        _supplies = cadSupplies()
        system('cls')
        print(_supplies)
        confirm = input('Deseja confirmar? \n[S] [N]: ')
        if confirm.upper() == 'S':
            addData('disciplinas.json', _supplies)
            print('Cadastro realizado com sucesso')
            retry = input('quer realizar outro? \n[S] [N]: ')
            if retry.upper() == 'N':
                return print('Ok, até mais!')
            else:
                continue
        else:
            print('Cadastro cancelado!')
            
            if retry.upper() == 'N':
                return print('Ok, até mais!')
            else:
                continue


def searchSupplies():
    """Funcao que pesquisa as disciplinas no banco de dados.

    Returns:
        List : retorna uma lista com as disciplinas.
    """
    query = Query()
    Supplies = TinyDB('disciplinas.json')
    chooseItem = input('deseja pesquisar por: \nNome (N), Código (C) ou Professor (P)? ')
    if chooseItem.upper() == 'N':
        searchName = input('digite o nome da disciplina: ')
        searchName = searchName.capitalize()
        searched = Supplies.search(query.Disciplina.search(searchName))
        if searched == []:
            print('Disciplina nao encontrada')
            retry = input('quer tentar dnv? (s/n)')
            if retry.upper() == 'S':
                system('cls')
                return searchSupplies()
            else:
                return print('Ok, até mais!')
        else:
            print(searched)
    elif chooseItem.upper() == 'C':
        searchCode = input('digite o código da disciplina: ')
        searchCode = searchCode.upper()
        searched = Supplies.search(query.Codigo.search(searchCode))
        if searched == []:
            print('Disciplina nao encontrada')
            retry = input('quer tentar dnv? (s/n)')
            if retry.upper() == 'S':
                system('cls')
                return searchSupplies()
            else:
                return print('Ok, até mais!')
        else:
            print(searched)
    elif chooseItem.upper() == 'P':
        searchTeacher = input('digite o nome do Professor: ')
        searchTeacher = searchTeacher.capitalize()
        searched = Supplies.search(query.Professor.search(searchTeacher))
        if searched == []:
            print('Disciplina nao encontrada')
            retry = input('quer tentar dnv? (s/n)')
            if retry.upper() == 'S':
                system('cls')
                return searchSupplies()
            else:
                return print('Ok, até mais!')
        else:
            print(searched)
    else:
        print('opcao invalida')
        return searchSupplies()
    