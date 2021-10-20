
def citire():
    '''
    Functie care citeste o lista
    :return: O lista de numere float
    '''
    lista = []
    dimensiune = int(input("Dimensiune lista: "))
    while dimensiune:
        element = float(input())
        lista.append(element)
        dimensiune = dimensiune - 1
    return lista

def afisare_parte_intreaga(lista):
    '''
    Functie care returneaza partea intreaga a numerelor din lista
    :param lista: Lista de float uri
    :return: Partea intreaga a fiecarui numar
    '''
    result = []
    for numar in lista:
        result.append(int(numar))

    return result


def afisare_interval(lista):
    '''
    Functie care afiseaza numerele intr-un inverval dat
    :param lista: Lista de float uri
    :return: Numerele care se afla in intervalul respectiv
    '''
    lista = []






def extract_fractionar(numar):
    return str(numar).split('.')[1]


def parte_intreaga_divizor(lista):
    result = []
    for numar in lista:
        n=int(numar)
        m=extract_fractionar(numar)
        if n % m == 0 :
            result.append(numar)
    return result

def meniu():
    '''
    Functie care afiseaza meniul
    '''
    print("Meniu \n ")
    print("1.Citirea unei liste de numere float.")
    print("2.Afișarea părții întregi a tuturor numerelor din listă.")
    print("3.Afisarea tuturor numerelor care apartin unui interval")
    print("4.Afișarea tuturor numerelor a căror parte întreagă este divizor al părții fracționare.")
    print("5.Afișarea listei obținute din lista inițială în care numerele sunt înlocuite cu un string format din cuvinte care le descriu caracter cu caracter.")
    print("6.Iesire.")

def main():
    meniu()
    optiune = 0
    lst = []
    while optiune != 6 :
        optiune = int(input("Alegeti o optiune: "))
        if optiune == 1 :
            lst = citire()
        elif optiune == 2 :
            secv1 = afisare_parte_intreaga(lst)
            print (secv1)
        elif optiune == 3 :
            secv2 = (lst)
            print (secv2)
        elif optiune == 4 :
            secv3 = parte_intreaga_divizor(lst)
            print (secv3)
        elif optiune == 5 :
            secv4 = (lst)
            print (secv4)
        elif optiune == 6 :
            break

main()