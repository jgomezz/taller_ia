
def resta(a, b):
    '''
        Resta dos números
    '''
    return a - b


def suma(a, b):
    '''
        Suma dos números
    '''
    return a + b

''' Funcion to multiply two numbers '''
def multiply(a, b):
    '''
        Multiply two numbers
    '''
    return a * b

''' Funcion to divide two numbers '''
def divide(a, b):
    '''
        Divide two numbers
    '''
    return a / b

''' Funcion para elevar a la potencia un numero '''
def power(a, b):
    '''
        Power of a number
    '''
    return a ** b

# Funcion para obtener la raiz cuadrada de un numero
def square_root(a):
    '''
        Square root of a number
    '''
    return a ** 0.5


''' Main function '''
if __name__ == '__main__':

    a = 3
    b = 2
    print(suma(a, b))
    print(resta(a, b))
    print(multiply(a, b))
    print(divide(a, b))        
    print(power(a, b))
    print(square_root(a))
    