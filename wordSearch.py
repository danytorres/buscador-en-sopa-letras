from textwrap import wrap
import make, barrido


def wordSearch(letters, words):
    
    makeWords = make.makeWords(words) # Separa cada letra del arreglo de palabras 
    grind = make.makeGrind(letters) # Genera el arreglo 8x8 y pone en minusculas todas las palabras
    resultado = make.makeRes(words) # Genera un arreglo con valores False con la misma cantindad de palabras a buscar

    for x in range(8):
        for y in range(8): # Recorre el grind generando sus indices x y
            for z in range(len(makeWords)): # Recorre las palabras y genera su indice z
                if grind[x][y] == makeWords[z][0]: # Determina si la letra de grind es alguna inicial de alguna palabra
                    # Realiza barrido de la palabra con indice z en cada una de las direcciones
                    # Si encuentra toda la palabra cambia a True en el arreglo resultado en la misma posicion que 
                    # en el arreglo original de palabras 
                    if barrido.up(grind, x, y, makeWords[z]): resultado[z] = True 
                    elif barrido.down(grind, x, y, makeWords[z]): resultado[z] = True
                    elif barrido.left(grind, x, y, makeWords[z]): resultado[z] = True
                    elif barrido.rigth(grind, x, y, makeWords[z]): resultado[z] = True
                    elif barrido.upRigth(grind, x, y, makeWords[z]): resultado[z] = True
                    elif barrido.upLeft(grind, x, y, makeWords[z]): resultado[z] = True
                    elif barrido.downLeft(grind, x, y, makeWords[z]): resultado[z] = True
                    elif barrido.downRigth(grind, x, y, makeWords[z]): resultado[z] = True

    return barrido.resultado(resultado) # Revisa si el arreglo de resultado se encontraron todas las palabras 