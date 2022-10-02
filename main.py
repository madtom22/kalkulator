import logging
logging.basicConfig(level=logging.INFO)

def addition(a,b):
    logging.info(f'Dodaję {a} + {b}')
    print('Wynik z dokładnością do dwóch miejsc po przecinku to: ',round(a + b,2))

def subtraction(a,b):
    logging.info(f'Odejmuję {a} - {b}')
    print('Wynik z dokładnością do dwóch miejsc po przecinku to: ',round(a - b,2))

def multiplication(a,b):
    logging.info(f'Mnożę {a} * {b}')
    print('Wynik z dokładnością do dwóch miejsc po przecinku to: ',round(a * b,2))

def division(a,b):
    logging.info(f'Dzielę {a} / {b}')
    print('Wynik z dokładnością do dwóch miejsc po przecinku to: ',round(a / b,2))

if __name__ == "__main__":

    x = int(input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: '))

    if x == 1:
        c = int(input('Podaj ile składników chcesz dodać do siebie: '))
        if c < 2:
            print('Nie można dodać mniej niż dwóch składników.')
        if c == 2:
            a = float(input('Podaj składnik 1: '))
            b = float(input('Podaj składnik 2: '))
            addition(a ,b)
        elif c >2:
            addition_more_than_2(c)

    if x == 2:
        a = float(input('Podaj składnik 1: '))
        b = float(input('Podaj składnik 2: '))
        subtraction(a, b)

    if x == 3:
        c = int(input('Podaj ile składników chcesz pomnożyć przez siebie: '))
        if c < 2:
            print('Nie można mnożyć mniej niż dwóch składników.')
        if c == 2:
            a = float(input('Podaj składnik 1: '))
            b = float(input('Podaj składnik 2: '))
            multiplication(a,b)
        elif c > 2:
            multiplication_more_than_2(c)

    if x == 4:
        a = float(input('Podaj składnik 1: '))
        b = float(input('Podaj składnik 2: '))
        division(a, b)

    elif x <1 or x > 4:
        print('Podano błędny numer.')