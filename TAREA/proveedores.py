class proveedor:
    producto = []
    def __init__(self):
        pass

    def AgregarProveedor(self, apellidos, nombre, telefono):
        self.__apellidos = apellidos 
        self.__nombre = nombre
        self.__telefono = telefono

    def AgregarProductos(self,producto):
        self.producto.append(producto)

    
