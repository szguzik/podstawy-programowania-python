# Funkcja do dodawania
def dodawanie(a, b):
    return a + b

# Funkcja do odejmowania
def odejmowanie(a, b):
    return a - b

# Funkcja do mnożenia
def mnozenie(a, b):
    return a * b

# Funkcja do dzielenia
def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return "Błąd: Nie można dzielić przez zero."

# Funkcja do obliczania reszty z dzielenia (modulo)
def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return ("Błąd: Nie można obliczyć reszty "
                "z dzielenia przez zero.")

# Funkcja do potęgowania
def potegowanie(a, b):
    return a ** b

# Funkcja do sprawdzenia, czy podany ciąg jest liczbą zmiennoprzecinkową
def czy_liczba(ciag):
    try:
        float(ciag)
        return True
    except ValueError:
        return False

# Wybór działania
print("Wybierz działanie:")
print("a. Dodawanie")
print("b. Odejmowanie")
print("c. Mnożenie")
print("d. Dzielenie")
print("e. Modulo")
print("f. Potęgowanie")

wybor = input("Twój wybór (a/b/c/d/e/f): ")

# Wprowadzenie dwóch liczb zmiennoprzecinkowych
while True:
    a = input("Podaj pierwszą liczbę: ")
    b = input("Podaj drugą liczbę: ")

    # Sprawdzenie, czy podane wartości są liczbami
    if not czy_liczba(a) or not czy_liczba(b):
        print("Błąd: Podane wartości nie są liczbami"
              " zmiennoprzecinkowymi.")
    else:
        a = float(a)
        b = float(b)
        break

# Słownik z funkcjami
operacje = {
    'a': dodawanie,
    'b': odejmowanie,
    'c': mnozenie,
    'd': dzielenie,
    'e': modulo,
    'f': potegowanie
}

# Wykonanie wybranego działania
if wybor in operacje:
    wynik = operacje[wybor](a, b)
    print(f"Wynik {wybor}: {wynik}")
else:
    print("Błąd: Niepoprawny wybór działania.")
