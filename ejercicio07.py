class Cuenta:

    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
        
    def ingresos(self, cantidad):
        if cantidad < 0:
            return
        else:
            self.cantidad = self.cantidad + cantidad
        
    def egresos(self, cantidad):
        self.cantidad = self.cantidad - cantidad
        
    def mostrar_cantidad(self, cantidad):
        return self.cantidad
        
        
    def imprimir(self):
        print(f'Apellido y Nombre Titular: {self.titular}','-',
              '$ {self.cantidad}')
        
    def __str__(self):
        return f'{self.titular}\t $ {self.cantidad}'
        
    # Programa Principal
    #Crea el objeto
  
    cuenta1 = Cuenta('Maria', 10000)
    cuenta2 = Cuenta('Pedro', 15000)
    
    cuenta1.ingresar(5000)
    cuenta1.egresos(3000)
    cuenta1.mostrar_cantidad()
    cuenta1.imprimir()
    
        