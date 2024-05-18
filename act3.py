import os, time

os.system("cls")

nombres = []

banderanombre= True
while banderanombre:
  nombre1= input("ingrese un nombre: \n")
  nombres.append(nombre1)
  opcion = input("desea agregar otro nombre? si/no \n")
  opcionminus = opcion.lower()
  #print(opcionminus)
  if opcionminus == "no":
     print(nombres)
     banderanombre = False
