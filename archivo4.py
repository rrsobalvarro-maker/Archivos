#crea un programa que permita guardan n cantidad de 
# notas en un archivo, leer las notas, calcular el prmedio
#ls nota mas alta y mas baja

n = int(input("Ingrese la cantidad de notas: "))
total = 0
max = 0
min = 0

with open("notas.txt", "a", encoding = "utf-8") as archivo:
    for i in range(n):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        archivo.write(f"Nota {i+1}: {nota}\n")

        total += nota

        if i == 0:
            mayor = nota
            menor = nota
        else:
            if nota > mayor:
                mayor = nota

            if nota < menor:
                min = nota
    promedio = total / n

    archivo.write("\n--- RESULTADOS ---\n")
    archivo.write(f"Promedio: {promedio}\n")
    archivo.write(f"Nota más alta: {mayor}\n")
    archivo.write(f"Nota más baja: {menor}\n")
    archivo.write("\n")
    