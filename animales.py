# animales.py
# Ejemplo simple para practicar pull requests en GitHub
# Cada colaborador puede agregar un nuevo animal a la lista

def mostrar_animales():
    animales = [
        "Perro",
        "Gato",
        "Loro"
    ]
    for a in animales:
        print("Animal:", a)

if __name__ == "__main__":
    print("Bienvenido al zoológico colaborativo 🐾")
    mostrar_animales()
