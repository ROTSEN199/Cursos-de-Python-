secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

number = int(input('ingrese un numero entero'))
while not(number != secret_number):
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!" )

    print("""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
number = int(input('ingrese un numero entero'))

while number == secret_number:
    print ("¡Bien hecho, muggle! Eres libre ahora")