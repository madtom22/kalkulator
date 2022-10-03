import logging
logging.basicConfig(level=logging.INFO)

def addition(c):
    e = 0
    f = []
    for i in range(1,c+1):
        d = float(input(f'Podaj składnik {i}: '))
        e = e + d
        f.append(d)
    logging.info(f'Składnik które zostały dodane do siebie: {f}')
    print('Wynik z dokładnością do dwóch miejsc po przecinku to: ', round(e,2))

def subtraction(c):
    a = float(input('Podaj składnik 1: '))
    b = float(input('Podaj składnik 2: '))
    logging.info(f'Odejmuję {a} - {b}')
    print('Wynik z dokładnością do dwóch miejsc po przecinku to: ', round(a - b,2))

def multiplication(c):
    e = 1
    f = []
    for i in range(1,c+1):
        d = float(input(f'Podaj składnik {i}: '))
        e = e * d
        f.append(d)
    logging.info(f'Składnik które zostały pomnożone przez siebie to: {f}')
    print('Wynik z dokładnością do dwóch miejsc po przecinku to: ', round(e,2))

def division(c):
    a = float(input('Podaj składnik 1: '))
    b = float(input('Podaj składnik 2: '))
    try:
        logging.info(f'Dzielę {a} / {b}')
        print('Wynik z dokładnością do dwóch miejsc po przecinku to: ', round(a / b,2))
    except ZeroDivisionError:
        print('Pamiętaj, kolego: nie dziel przez 0!')

if __name__ == "__main__":

    x = int(input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: '))
    c = 2

    if x == 1:
        c = int(input('Podaj ile składników chcesz dodać do siebie: '))
        if c < 2:
            print('Nie można dodać mniej niż dwóch składników.')
        elif c >= 2:
            addition(c)

    if x == 2:
        subtraction(c)

    if x == 3:
        c = int(input('Podaj ile składników chcesz pomnożyć przez siebie: '))
        if c < 2:
            print('Nie można mnożyć mniej niż dwóch składników.')
        elif c >= 2:
            multiplication(c)

    if x == 4:
        division(c)

    elif x < 1 or x > 4:
        print('Podano błędny numer.')