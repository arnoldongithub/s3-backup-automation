# Funktion, die eine andere Funktion zurückgibt
def create_adder(x):
    # innere Funktion, die zwei Werte addiert
    def adder(y):
        return x + y
    # gibt die innere Funktion zurück
    return adder  # type: ignore

# Erstellt eine neue Funktion add_15, die 15 zu jeder Zahl addiert
add_15 = create_adder(15)

# Verwendet add_15, um 10 zu addieren, was 15 + 10 ergibt
print(add_15(10))  # Ausgabe: 25

def create_adder(x):
    def adder(y):
        return x + y
    return adder  # type: ignore

add_15 = create_adder(15)
print(add_15(10))  # Expected output: 25
