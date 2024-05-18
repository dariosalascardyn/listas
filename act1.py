import os, time

os.system("cls")
nombrelargo = ""
nombres = []

for i in range(3):
  nombre1 = input(f"ingrese nombre {i+1}\n")
  nombres.append(nombre1)

for nombre1 in nombres:
  if len(nombre1) > len(nombrelargo):
    nombrelargo = nombre1

    
                   
print(f"el nombre mas largo es: {nombrelargo}")
