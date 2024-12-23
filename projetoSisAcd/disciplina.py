import string
from os import system
import random 
from bd import addData
from tinydb import TinyDB


def cadSupplies():
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
            return {'Disciplina': name,'Codigo': idSupplies, 'Carga Horaria': workLoad, 'Professor': ''}
        
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
            retry = input('quer tentar novamente? \n[S] [N]: ')
            if retry.upper() == 'N':
                return print('Ok, até mais!')
            else:
                continue

# confirmSup()

supplies = TinyDB('disciplinas.json')


supplies.update({'Professor': 'Joao'}, doc_ids=[1])
