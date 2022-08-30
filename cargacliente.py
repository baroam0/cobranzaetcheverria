
from clientes.models import Cliente

archivo = open("clientes.txt", "r", encoding="utf8")

clientes = archivo.readlines()

print("Grabando...")

for cliente in clientes:
    if cliente != "":
        grabar = Cliente(apellido=str(cliente), nombre=" ")
        grabar.save()
