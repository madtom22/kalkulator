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
    