from os import system
import string
import random
from bd import addData
from tinydb import TinyDB, Query
import inputVerify

def cadTeacher():
    """ Cadastra um novo professor

    Returns:
        dict: Retorna um dicionario
    """
    _ = True
    idReg = registrationNum()
    while _:
            name = inputVerify.getInput('Digite o nome: ', inputVerify.noneWord, 'Voce nao digitou um nome')
            birthday = inputVerify.getInput('Digite a data de nascimento: ', inputVerify.digit, 'Voce nao digitou uma data de nascimento')
            email = inputVerify.getInput('Digite o email: ', inputVerify.isEmail, 'Voce nao digitou um email valido')
            gender = inputVerify.getInput('Digite o genero (M/F): ', inputVerify.noneWord, 'Voce nao digitou um genero')
            address = inputVerify.getInput('Digite o endereco: ', inputVerify.noneWord, 'Voce nao digitou um endereco')
            cel = inputVerify.getInput('Digite o celular: ', inputVerify.celVerify, 'Voce nao digitou um numero decelular')
    return {'Nome': name.replace(' ', '_').title(), 'Matricula': idReg, 'DataAniversario': birthday, 'genero': gender, 'Endereco': address, 'Telefone': cel, 'Email': email.lower(), 'disciplina': []}


def registrationNum():
    """Gera uma sequencia de 6 numeros e uma letra aleatoria para a matricula.

    Returns:
        Str: retorna uma string com a matricula.
    """
    # gera uma sequencia de 6 numreos aleatorios (a quantidade de numeros e definida pelo 'k')
    # e o os numeros sao definidos pelo 'string.digits')
    num = ''.join(random.choices(string.digits, k= 6))
    letterUpper = random.choice(string.ascii_uppercase) # ascii_uppercase gera letras maiusculas
    registrationId = letterUpper + num 
    return registrationId

def registrationTeacher():
    """Adiciona um novo professor ao sistema, com os dados fornecidos pela funcao
    cadStudent(). Alem de fazer a verificacao se o professor esta com os dados corretos.
    """
    _ = True
    _teacher = cadTeacher()
    while _:
        print(_teacher)
        confirm = input('confirmar? (S/N): ')
        if confirm.upper() == 'S':
            system('cls')
            addData('Teacher.json', _teacher)
            retry = input('quer registrar outro professor? ')
            if retry.upper() == 'N':
                _ = False
                system('cls')
                print('ok, até mais!')
            else:
                system('cls')
                return registrationTeacher()
        elif confirm.upper() == 'N':
            system('cls')
            _ = False
            print('cancelado!')
            retry = input('quer tentar dnv? ')
            if retry.upper() == 'N':
                system('cls')
                print('ok, até mais!')
            else:
                system('cls')
                return registrationTeacher()
        else:
            print('opcao invalida')
            continue
        
def searchTeacher():
    """Funcao que busca o professor pelo nome, matricula ou pela disciplina

    Returns:
        List : lista com os dados do professor
    """
    query = Query()
    teacher = TinyDB('Teacher.json')
    chooseItem = input('deseja pesquisar por: \nNome (N), Matricula (M) ou Disciplina (D)? ')
    if chooseItem.upper() == 'N':
        searchName = input('digite o nome do Professor: ')
        searchName = searchName.title()
        searchName = searchName.replace(' ', '_')
        searched = teacher.search(query.Nome.search(searchName))
        if searched == []:
            print('Professor nao encontrado')
            retry = input('quer tentar dnv? (s/n)')
            if retry.upper() == 'S':
                system('cls')
                return searchTeacher()
            else:
                return print('Ok, até mais!')
        else:
            for i in searched:
                print(i)
                print()
    elif chooseItem.upper() == 'M':
        searchRegistration = input('digite a matricula do Professor: ')
        searchRegistration = searchRegistration.upper()
        searched = teacher.search(query.Matricula.search(searchRegistration))
        if searched == []:
            print('Professor nao encontrado')
            retry = input('quer tentar dnv? (s/n)')
            if retry.upper() == 'S':
                system('cls')
                return searchTeacher()
            else:
                return print('Ok, até mais!')
        else:
            for i in searched:
                print(i)
                print()
    elif chooseItem.upper() == 'D':
        searchSupplies = input('digite a Disciplina do Professor: ')
        searchSupplies = searchSupplies.capitalize()
        searched = teacher.search(query.disciplina.search(searchSupplies))
        if searched == []:
            print('Professor nao encontrado')
            return searchTeacher()
        else:
            for i in searched:
                print(i)
                print()
    else:
        print('opcao invalida')
        return searchTeacher()

