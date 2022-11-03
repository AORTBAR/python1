"""para comentar
varias lineas"""
while True:
    nombre=input("como te llamas? ")
    if nombre == "":
        print("No has \n escrito nada",end="\n")
    else:
        print(f"Hola {nombre} encantado",end=" ---")
        print("Adios")
        break;