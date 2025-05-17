from proveedores import proveedor
from producto import producto
global prov1, prod1
Opcion = ""
prov1 = proveedor()
prod1 = producto()

while(Opcion!=5):

    print("1. Agregar Proveedor ")
    print("2. Crear Producto ")
    print("3. Agregar producto a proveedor ")
    print("4. Listar Producto ")
    print("5. salir ")
    Opcion = int(input())

    if Opcion == 1:
        
        apellidos = input("Ingrese Apellidos ")
        nombre = input("Ingrese nombre ")
        telefono = input("Ingrese telefono ")
        prov1.AgregarProveedor(apellidos,nombre,telefono)


    elif Opcion == 2:
        prod1 = producto()
        codigo = int(input("Ingrese el codigo del producto "))
        nomproducto = input("Ingrese el nombre del producto ")
        precio = input("Ingrese el precio del producto ")

        prod1.CrearProducto(codigo, nomproducto, precio)

    elif Opcion == 3:
        prov1.AgregarProductos(prod1)

    elif Opcion == 4:
        prod1.ListaProductos(producto)
        
