nombres_usuario={}
sexos={}
contraseñas={}
opcion="0"

def validadorDeContraseña(contraseña):
    contador_numeros = 0
    contador_letras = 0
    for letra in str(contraseña): 
        if letra.isnumeric(): 
            contador_numeros += 1
        if letra.isupper():
            contador_letras += 1

    if len(contraseña) < 8:
        print("La contraseña debe tener minimo 8 caracteres.")
        return False
    if contador_numeros < 1:
        print("La contraseña debe tener minimo 1 número.")
        return False
    if contador_letras != 1:
        print("La contraseña debe tener minimo 1 letra.")
        return False
    return True
    


while opcion != "4":
    print("----Menu Principal----")
    print("1._Ingresar usuario")
    print("2._Buscar usuario")
    print("3._Eliminar usuario")
    print("4._Salir")
    opcion = input("Ingrese la opcion que desea (1-4): ") 
    if opcion == "":
        print("la opcion no puede estar vacia")
        continue
    elif opcion >= "5":
        print("opcion invalida")

    match opcion:
        case "1":
            while True:
                usuario = input("Ingrese su nombre de usuario: ")
                if usuario in nombres_usuario:
                    print("El nombre de usuario ya existe, intente con otro")
                    continue
                else:
                    nombres_usuario[usuario] = None
                    
                    sexo = input("Ingrese su sexo (M/F): ").upper()
                    if sexo in ["M", "F"]:
                      print

                      contraseña = input("Ingrse su contraseña(Debe tener almenos 1 letra y 1 numero): ")
                    if validadorDeContraseña(contraseña):
                        nombres_usuario[usuario] = {'sexo': sexo, 'contraseña': contraseña}
                        break
                    else:
                        ("Contraseña invalida") 
                    
        case "2":
            buscadeusuario = input("Ingrese el usuario a buscar: ")
            if buscadeusuario in nombres_usuario:
                print(f"El sexo del usuario es {nombres_usuario[buscadeusuario]['sexo']} y su contraseña es {nombres_usuario[buscadeusuario]['contraseña']}")
            else:
                 print("Usuario no encontrado")
        case "3": 
            usuario= input("Ingrese el nombre de el usuario a eliminar: ")
            if usuario in nombres_usuario:
                nombres_usuario.pop(usuario)
                print(f"El usuario '{usuario}' fue eliminado exitosamente")
            else:
                print("El usuario no fue enconrado") 

print("Programa Terminado")