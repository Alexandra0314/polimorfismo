class Trabajo:
    pass

    def __init__(self, Profesion):
        self.Profesion = Profesion

Trabajo1 = Trabajo("Maestro")
Trabajo2 = Trabajo("Ingeniero")

class Diego(Trabajo):
    pass

    def __init__(self, Nombre):
        self.Nombre = Nombre
    
    def Descripcion(self):
        return'{} compro {}'.format(self.Nombre,Trabajo1)
    
Diego = Diego("Diego")

class Alexa(Trabajo):
    pass

    def __init__(self, Nombre):
        self.Nombre = Nombre
    
    def Descripcion(self):
        return'{} Trabaja como {}'.format(self.Nombre,Trabajo2)
    
Alexa = Alexa("Alexa")

print(Diego.Descripcion())
print(Alexa.Descripcion())


