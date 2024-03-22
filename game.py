import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de fallos permitidos
max_fails = 10
# Contador de errores
fails = 0
# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")

while True:
    difficulties=input("Elige la dificultad del juego (Facil - Media - Dificil):").lower()
    match difficulties:
        case "facil":
            word_displayed = "".join(letter if letter in "aeiouáéíóú" else "_" for letter in secret_word)
            break
        case "media":
            word_displayed = secret_word[0] + "_" * (len(secret_word) - 2) + secret_word[-1]
            break
        case "dificil":
            word_displayed = "_" * len(secret_word)
            break
        case _:
            print("Opcion no valida. Intenta de nuevo")


# Mostrarla palabra parcialmente adivinada
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
print(f"Palabra: {word_displayed}")


while fails < max_fails:
     # Pedir al jugador que ingrese una letra
     letter = input("Ingresa una letra: ").lower()
     
     # Verifica que el caracter sea valido (NO CUENTA COMO ERROR, CUENTA COMO NO VALIDO)
     if len(letter) != 1 or not letter.isalpha():
        print("Entrada no valida")
        continue     
     
     # Verificar si la letra ya ha sido adivinada (SI LA LETRA YA SE USO, CUENTA COMO ERROR)
     if letter in guessed_letters:
         print("Ya has intentado con esa letra. Intenta con otra.")
         fails += 1
         continue
     
     # Agregar la letra a la lista de letras adivinadas
     guessed_letters.append(letter)
     
     # Verificar si la letra está en la palabra secreta
     if letter in secret_word:
         print("¡Bien hecho! La letra está en la palabra.")
     else:
         print("Lo siento, la letra no está en la palabra.")
         fails += 1
    
     # Mostrar la palabra parcialmente adivinada
     letters = []
     for letter in secret_word:
         if letter in guessed_letters:
             letters.append(letter)
         else:
             letters.append("_")
     word_displayed = "".join(letters)
     print(f"Palabra: {word_displayed}")
     
     # Verificar si se ha adivinado la palabra completa
     if word_displayed == secret_word:
         print(f"¡Felicidades! Has adivinado la palabra secreta:  {secret_word}")
         break
else:
     print(f"¡Oh no! Has alcanzado el maximo de fallos que era {max_fails}.")
     print(f"La palabra secreta era: {secret_word}")
     
input() # Para poder ver las cosas sin que se cierre la terminal