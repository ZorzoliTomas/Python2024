import random

# Lista de palabras posibles
words = ["python", "programacion", "computadora", "codigo", "desarrollo", "inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número maximo de fallos
max_failures = 5

# Número de fallos
failures = 0

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")

# Elige la dificultad

print("""Elije una dificultad:
      1. Facil
      2. Normal
      3. Dificil""")
dificulty = int(input())

if dificulty == 1:
    word_displayed = ""
    for letra in secret_word:
        if letra in "a,e,i,o,u":
            word_displayed += letra
        else:
            word_displayed += "_"   
elif dificulty == 2:
    word_displayed = secret_word[0] + "_" * (len(secret_word)-2) + secret_word[-1]
else:
    word_displayed = "_" * len(secret_word)

print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

# Mostrar la palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

while (failures < max_failures):
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    
    # Si el usuario no escribe nada le tira un error y cuenta como un intento
    if letter == "":
        print("ERROR No pusiste nada")
        failures += 1
        continue
    
    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        failures += 1
        continue
    
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        failures += 1
    
    # Mostrar palabra dependiendo que dificultad se eligio
    
    match dificulty: 
        case 3:
            letters = []
            for letter in secret_word:
                if letter in guessed_letters:
                    letters.append(letter)
                else:
                    letters.append("_")
            word_displayed = "".join(letters)
            print(f"Palabra: {word_displayed}")
        case 2:
            letters = []
            word_displayed = secret_word[0]
            for letter in secret_word[1:-1]:
                if letter in guessed_letters:
                    letters.append(letter)
                else:
                    letters.append("_")
            word_displayed += "".join(letters)
            word_displayed += secret_word[-1]
            print(f"Palabra: {word_displayed}")
        case 1:
            letters = []
            guessed_letters += "a", "e", "i", "o", "u"
            for letter in secret_word:
                if letter in guessed_letters:
                    letters.append(letter)
                else:
                    letters.append("_")
            word_displayed = "".join(letters)
            print(f"Palabra: {word_displayed}")
            
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has fallado {max_failures} veces.")
    print(f"La palabra secreta era: {secret_word}")