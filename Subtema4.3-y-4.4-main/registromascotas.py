import os

nombre_mascotas = [""] * 3
edad_mascotas = [0] * 3


def insertar():
    for i in range(len(nombre_mascotas)):
        if nombre_mascotas[i] == "":
            nombre = input("Ingrese el nombre de la mascota: ").strip()

            if nombre == "":
                print("El nombre no puede estar vacío")
                continue

            while True:
                try:
                    edad = int(input("Ingrese edad de la mascota: "))
                    if edad < 0:
                        print("La edad no puede ser negativa")
                        continue
                    break
                except ValueError:
                    print("Ingrese una edad válida")

            nombre_mascotas[i] = nombre
            edad_mascotas[i] = edad

    print("Registro finalizado")


def mostrar():
    encontrado = False

    for i in range(len(nombre_mascotas)):
        if nombre_mascotas[i] != "":
            print(f"Nombre: {nombre_mascotas[i]} | Edad: {edad_mascotas[i]}")
            encontrado = True

    if not encontrado:
        print("No hay mascotas registradas")


def eliminar(nombreAborrar):
    for i in range(len(nombre_mascotas)):
        if nombre_mascotas[i].lower() == nombreAborrar.strip().lower() and nombre_mascotas[i] != "":

            mascota_eliminada = nombre_mascotas[i]

            for j in range(i, len(nombre_mascotas) - 1):
                nombre_mascotas[j] = nombre_mascotas[j + 1]
                edad_mascotas[j] = edad_mascotas[j + 1]

            nombre_mascotas[-1] = ""
            edad_mascotas[-1] = 0

            print(f"Mascota eliminada: {mascota_eliminada}")
            return

    print("Mascota no encontrada")


def ordenar_mascotas():
    for i in range(len(nombre_mascotas) - 1):
        for j in range(len(nombre_mascotas) - 1 - i):

            primero = nombre_mascotas[j]
            segundo = nombre_mascotas[j + 1]

            if (primero == "" and segundo != "") or (
                primero != "" and segundo != "" and
                primero.lower() > segundo.lower()
            ):
                aux = nombre_mascotas[j]
                nombre_mascotas[j] = nombre_mascotas[j + 1]
                nombre_mascotas[j + 1] = aux

                aux_edad = edad_mascotas[j]
                edad_mascotas[j] = edad_mascotas[j + 1]
                edad_mascotas[j + 1] = aux_edad

    print("Mascotas ordenadas alfabéticamente")


def main():
    global nombre_mascotas, edad_mascotas

    nombre_mascotas = [""] * 3
    edad_mascotas = [0] * 3

    opcion = 0

    while opcion != 5:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("[1] Insertar mascota (nombre | edad)")
        print("[2] Mostrar mascotas (nombre | edad)")
        print("[3] Eliminar mascotas por nombre (en ambos vectores)")
        print("[4] Ordenar mascotas alfabéticamente")
        print("[5] Salir")

        try:
            opcion = int(input("Elija una opción: "))
        except ValueError:
            print("Ingrese una opción numérica")
            input("Presione para continuar...")
            continue

        if opcion == 1:
            insertar()

        elif opcion == 2:
            mostrar()

        elif opcion == 3:
            nombreAborrar = input("Ingrese mascota a eliminar: ")
            eliminar(nombreAborrar)

        elif opcion == 4:
            ordenar_mascotas()

        elif opcion == 5:
            print("Saliendo...")

        else:
            print("Opción inválida")

        if opcion != 5:
            input("Presione para continuar...")


main()