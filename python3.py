try:
    num=int(input("escribe un número: "))
    if num<0:
        raise "Error número negativo"
    for i in range(0,num,2):
        print(i,end=" ")
except ValueError as e:
    print("fError debe ser un número: {e}")
except KeyboardInterrupt as e2:
    print(e2)
except:
    print("Excepción genérica")

