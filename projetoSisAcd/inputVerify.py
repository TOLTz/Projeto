import phonenumbers


def getInput(prompt, validation=None, errorMensage='Entrada invalida, por favor tente novamente'):
    while True:
        userInput = input(prompt)
        if not validation or validation(userInput):
            return userInput
        print(errorMensage)

def digit(args):
    return args.isdigit()

def noneWord(args):
    return bool(args.strip())

def isEmail(args):
    return '@' in args and '.com' in args


def celVerify(args, zipCode='+55'):
    try:
        celphone = phonenumbers.parse(zipCode + args, None)
        if not phonenumbers.is_valid_number(celphone):
            print('numero invalido')
            return False
        return True
    except phonenumbers.NumberParseException as e:
        print('erro ao tentar validar o numero \n pode haver numeros faltando, ou caracteres invalidos.')
        return False


