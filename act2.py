import os, time

os.system("cls")

nombre = []
apellido = []


for i in range(3):
  nombre1 = input(f"ingrese nombre {i+1}\n")
  apellido1 = input(f"ingrese apellido {i+1}\n")
  nombre.append(nombre1)
  apellido.append(apellido1)

nombreapellido = zip(nombre, apellido)
print(list(nombreapellido))