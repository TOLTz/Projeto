from os import system

student = []


def cadStudent():
    """ Cadastra um novo aluno

    Returns:
        dict: Retorna um dicionario
    """
    name = input('Digite o nome: ')
    registration = input('Digite o numero de matricula: ')
    birthday = input('Digite a data de nascimento: ')
    gender = input('Digite o genero: ')
    address = input('Digite o Endereco: ')
    cel = input('Digite o telefone (apenas numeros): ')
    email = input('Digite o Email: ')
    return {'Nome': name, 'Matricula': registration, 'DataAniversario': birthday, 'genero': gender, 'Endereco': address, 'Telefone': cel, 'Email': email}


def registration():
    """Adiciona um novo aluno ao sistema, com os dados fornecidos pela funcao
    cadStudent(). Alem de fazer a verificacao se o aluno esta com os dados corretos.
    """
    _ = True
    _student = cadStudent()
    print(_student)
    confirm = input('confirmar? (S/N): ')
    while _:
        if confirm.upper() == 'S':
            system('cls')
            student.append(_student)
            _ = False
            return print('salvo com sucesso')
        elif confirm.upper() == 'N':
            system('cls')
            _ = False
            return print('cancelado!')
        else:
            print('opcao invalida')
            continue
            
            
registration()
        
    
