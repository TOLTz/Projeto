from adminScreen import mainSearch, mainReg, allocation, delete
from os import system


print('olá, bem vindo ao sistema academico!')
studentOrTeacher = input('Você é um professor (P) ou um aluno (A)? ')
_ = True
if studentOrTeacher == 'professor' or 'P':
    while _:
        print('ok, você está logado como professor')
        choice = input('Qual operação deseja fazer? \nPesquisa (P), Registrar (R), Alocar (A), Deletar (D) ou Sair (S)? ')
        if choice.lower() == 'p':
            mainSearch()
            retry = input('Quer fazer mais uma ação?(s/n) ')
            if retry.lower() == 'n':
                _ = False
                print('Ok, Até mais ver!')
            else:
                continue
        elif choice.lower() == 'r':
            mainReg()
            retry = input('Quer fazer mais uma ação?(s/n) ')
            if retry.lower() == 'n':
                _ = False
                print('Ok, Até mais ver!')
            else:
                continue
        elif choice.lower() == 'a':
            allocation()
            retry = input('Quer fazer mais uma ação?(s/n) ')
            if retry.lower() == 'n':
                _ = False
                print('Ok, Até mais ver!')
            else:
                continue
        elif choice.lower() == 'd': 
            while _:
                choice = input('deseja uma disciplina ou uma turma?')
                if choice.lower() == 'disciplina' or 'd':
                    delete('disciplinas')
                elif choice.lower() == 'turma' or 't':
                    delete('turmas')
                else:
                    print('operação invalida')
                    continue
            retry = input('Quer fazer mais uma ação?(s/n) ')
            if retry.lower() == 'n':
                _ = False
                print('Ok, Até mais ver!')
            else:
                continue
        elif choice.lower() == 's':
            system('cls')
            print('até logo!')
            _ = False
           
        else:
            print('operação inválida')
            continue
elif studentOrTeacher == 'aluno' or 'A':
    print('bem vindo!')
    while _:
        choice = input('Deseja pesquisar algo? (s/n)')
        if choice == 's':
            mainSearch()
            retry = input('Quer fazer mais uma ação?(s/n) ')
            if retry.lower() == 'n':
                _ = False
                print('Ok, Até mais ver!')
            else:
                continue    
        else:
            print('ok, até mais ver!')
            _ = False