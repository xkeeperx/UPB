ckprint("-------------------------------------------------------------\n")
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
print("\n-------------------------------------------------------------\n")

usuario = input("Digite el nombre de usuario:")
if(len(usuario) > 0  and len(usuario)<6):
    clave = input("Digite la contraseña:")
    claveBD = usuario[::-1]
    if(claveBD == clave):
        print("Usuario Valido")
    else:
        print("clave invalida")
    print("datos",claveBD)
    print("nombre lleno")
else:
    print("Error")