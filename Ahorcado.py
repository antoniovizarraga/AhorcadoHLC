from typing import Final
from random import choice

class Ahorcado:
    palabras = ("humanidad", "persona", "hombre", "mujer", "individuo", "cuerpo", "pierna", "cabeza", "brazo", "familia")

    # Esto es una constante. Aunque en Python no existe el concepto de: "Constantes", a partir de Python 3.8 en adelante
    # implementaron el Final. Funciona igual que el Final de Java. Aunque sólo sirve para indicar a herramientas como
    # mypy que una variable no debería cambiar de valor. Aún así, en Python se puede cambiar el valor de la variable
    # en cualquier momento.
    NUMINTENTOS: Final[int] = 7

    def __init__(self):
        
        self.palabraSecreta = ""
        self.palabraPista = ""

        # Declaro esto como variable ya que las letras tienen que tener espacios de por medio y
        # porque realmente no nos hace falta recorrer las distintas letras que se vayan
        # insertando. Simplemente ir añadiendo las letras que no coincidan con las
        # letras de la palabra.
        self.noAcertadas = ""

    def generaPalabra(self):
        self.palabraSecreta = choice(Ahorcado.palabras)

        # La función ljust rellena una cadena tantas veces como se le
        # indique en el primer parámetro y rellena la cadena con el
        # carácter o cadena especificado en el segundo parámetro.
        self.palabraPista = self.palabraSecreta.ljust(len(self.palabraSecreta), "_")
    

    # No me ha dado tiempo a hacerla. Mi idea era recorrer la cadena y si encontraba la letra,
    # sustituir el guión bajo de palabraPista.
    def compruebaLetra(self, letra):

        letraTemp = letra.lower()

        if letraTemp in self.palabraSecreta:
            for letra in self.palabraSecreta:
                #if letra
                pass


