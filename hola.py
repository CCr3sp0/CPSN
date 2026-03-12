>>> print(edad)
16
>>> print(alive)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'alive' is not defined. Did you mean: 'slice'?
>>> alive = True 
>>> print(alive)
True
>>> print(nombre, edad, estatura, alive)
cristobal 16 1.83 True
>>> print(nombre, edad, estatura, alive)
cristobal 16 1.83 True
>>> saludar = "Hola" 
>>> pregunta = "Como estas?"
>>> print(saludar,nombre)
Hola cristobal
>>> print(saludar, pregunta)
Hola Como estas?
>>> frase = "We arec charlie kirk"
>>> print(Frase)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Frase' is not defined. Did you mean: 'frase'?
>>> nombre = "we are charlie kirk"
>>> print(Nombre)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Nombre' is not defined. Did you mean: 'nombre'?