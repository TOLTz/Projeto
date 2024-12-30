from os import system
import string
import random
from bd import addData
from tinydb import Query, TinyDB


def cadStudent():
    """ Cadastra um novo aluno

    Returns:
        dict: Retorna um dicionario
    """
    _ = True
    idReg = registrationNum()
    while _:
        try:
            name = input('Digite o nome: ')
            noneWord(name)
            print(f'Matricula: {idReg}')
            birthday = input('Digite a data de nascimento: ')
            noneWord(birthday)
            gender = input('Digite o genero: ')
            noneWord(gender)
            address = input('Digite o Endereco: ')
            noneWord(address)
            cel = input('Digite o telefone (apenas numeros): ')
            noneWord(cel)
            email = input('Digite o Email: ')
            noneWord(email)
        except:
            system('cls')
            # print(TypeError())
            print('Digite uma palavra')
            continue
        else:
            _ = False
    return {'Nome': name, 'Matricula': idReg, 'DataAniversario': birthday, 'genero': gender, 'Endereco': address, 'Telefone': cel, 'Email': email}


def noneWord(args):
    if args == '':
        raise

def registrationNum():
    """Gera uma sequencia de 8 numeros e uma letra aleatoria para a matricula do aluno.

    Returns:
        Str: retorna uma string com a matricula.
    """
    # gera uma sequencia de 8 numreos aleatorios (a quantidade de numeros e definida pelo 'k')
    # e o os numeros sao definidos pelo 'string.digits')
    num = ''.join(random.choices(string.digits, k= 8))
    letterUpper = random.choice(string.ascii_uppercase) # ascii_uppercase gera letras maiusculas
    registrationId = num + '-' + letterUpper 
    return registrationId
    

def registration():
    """Adiciona um novo aluno ao sistema, com os dados fornecidos pela funcao
    cadStudent(). Alem de fazer a verificacao se o aluno esta com os dados corretos.
    """
    _ = True
    _student = cadStudent()
    while _:
        system('cls')
        print(_student)
        confirm = input('confirmar? (S/N): ')
        if confirm.upper() == 'S':
            system('cls')
            addData('Aluno.json', _student)
            print('salvo com sucesso')
            retry = input('quer tentar novament? ')
        elif confirm.upper() == 'N':
            system('cls')
            _ = False
            print('cancelado!')
            retry = input('quer tentar novament? ')
            if retry.upper() == 'N':
                _ = False
                system('cls')
                print('ok, até mais!')
            else:
                system('cls')
                continue
        else:
            print('opcao invalida')
            continue

def searchStudent():
    query = Query()
    student = TinyDB('Aluno.json')
    chooseItem = input('deseja pesquisar por: \nNome (N), Matricula (M) ou Turma (T)? ')
    if chooseItem.upper() == 'N':
        searchName = input('digite o nome do aluno: ')
        searchName = searchName.capitalize()
        searched = student.search(query.Nome.search(searchName))
        if searched == []:
            print('aluno nao encontrado')
            return searchStudent()
        else:
            print(searched)
    elif chooseItem.upper() == 'M':
        searchRegistration = input('digite a matricula do aluno: ')
        searchRegistration = searchRegistration.upper()
        searched = student.search(query.Matricula.search(searchRegistration))
        if searched == []:
            print('aluno nao encontrado')
            retry = input('quer tentar dnv? (s/n)')
            if retry.upper() == 'S':
                system('cls')
                return searchStudent()
            else:
                return print('Ok, até mais!')
        else:
            print(searched)
    elif chooseItem.upper() == 'T':
        searchteam = input('digite a turma do aluno: ')
        searchteam = searchteam.upper()
        searched = student.search(query.Turma.search(searchteam))
        if searched == []:
            print('aluno nao encontrado')
            retry = input('quer tentar dnv? (s/n)')
            if retry.upper() == 'S':
                system('cls')
                return searchStudent()
            else:
                return print('Ok, até mais!')
        else:
            print(searched)
    else:
        print('opcao invalida')
        return searchStudent()
