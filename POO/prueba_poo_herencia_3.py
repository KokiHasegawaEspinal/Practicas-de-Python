# video 31
class Persona():
    def __init__(self, nombre, edad, Lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=Lugar_residencia

    def descripcion(self):
        print("Nombre: ",self.nombre, "\nEdad: ",self.edad, "\nLugar de residencia: ",self.lugar_residencia)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        
        self.salario=salario
        self.antiguedad=antiguedad

    def descripcion(self):
        super().descripcion()

        print("Salario: ", self.salario, "\nAntiguedad: ",self.antiguedad)



# Koki=Persona("Koki", 42, "Peru")

# si cambio el tipo a persona en vez de empleado debo cambiar u obviar los dos primeros parametros 5000 y 15

# Koki=Persona("Koki",42,"Peru")



Koki=Empleado(5000,15, "Koki", 42, "Peru")
Koki.descripcion()

print("Koki es un empleado: ",isinstance(Koki, Empleado))
print("Koki es una persona: ",isinstance(Koki,Persona))