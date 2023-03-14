class Tienda:
    pass

    def __init__(self, Producto):
        self.Producto = Producto

Producto1 = Tienda("Manzana")
Producto2 = Tienda("Uva")

class Diego(Tienda):
    pass

    def __init__(self, Nombre):
        self.Nombre = Nombre
    
    def Comprar(self):
        return'{} compro {}'.format(self.Nombre,Producto1)
    
Diego = Diego("Diego")

class Alexa(Tienda):
    pass

    def __init__(self, Nombre):
        self.Nombre = Nombre
    
    def Comprar(self):
        return'{} compro {}'.format(self.Nombre,Producto2)
    
Alexa = Alexa("Alexa")

print(Diego.Comprar())
print(Alexa.Comprar())


       