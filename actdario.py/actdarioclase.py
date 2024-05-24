import os

os.system("cls")

usuarios = []

for x in range(2):
    
    nombre = input("ingrese nombre\n")
    while nombre == "":
        nombre = input("ingrese nombre\n")
    
    banderauser= True
    while banderauser:    
        try:
            idusuario = int(input("ingrese codigo\n"))
            while idusuario < 2 :
                idusuario = int(input("ingrese codigo\n"))
                
            banderauser = False
        except:
            print("id ususario no valida, deben ser solo numeros")
            
        
    correo = input("ingrese correo\n")
    while "@correo.cl" not in correo:
        correo = input("ingrese correo\n")
    
    usuario = {
        "nombre" : nombre,
        "idusuario" : idusuario,
        "correo" : correo
    }

    usuarios.append(usuario)

# for x in usuarios:
#     print(x)
    
print(usuarios)