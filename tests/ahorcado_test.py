from Ahorcado import Ahorcado

def test_palabras():
    listaPalabras = ["humanidad", "persona", "hombre", "mujer", "individuo", "cuerpo", "pierna", "cabeza", "brazo", "familia"]
    res = True

    for x in listaPalabras:
        if x not in Ahorcado.palabras:
            res = False
    assert res

def test_declaracionAtributos():
    juego = Ahorcado()
    assert juego.palabraSecreta == ""
    assert juego.palabraPista == ""
    assert juego.noAcertadas == ""

def test_generaPalabra():
    juego = Ahorcado()
    juego.generaPalabra()

    assert juego.palabraSecreta in Ahorcado.palabras
    assert juego.palabraPista == juego.palabraSecreta.ljust(len(juego.palabraSecreta), "_")

def test_compruebaLetra2():
    juego = Ahorcado()
    juego.palabraSecreta = "humanidad"
    letra = "D"

    juego.compruebaLetra(letra)
    

    assert juego.palabraPista == "______d_d"
    assert letra not in juego.noAcertadas

def test_compruebaLetra2():
    juego = Ahorcado()
    juego.palabraSecreta = "humanidad"
    letra = "d"

    juego.compruebaLetra(letra)
    

    assert juego.palabraPista == "______d_d"
    assert letra not in juego.noAcertadas
    

