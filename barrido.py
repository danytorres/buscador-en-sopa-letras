from textwrap import wrap
import make

# Resive los valores del grind y la posicion (x, y) de la letra donde hubo coincidencia con alguna palabra
# y la palabra que coincidio, realiza el barrido en cada una de las direcciones y devuelve True si encuentra la palabra, si no 
# devuelve False
def up(grind, x, y, word):
    for letter in word:
        if letter == grind[x][y]:
            x -= 1
        else: 
            return False
    return True

def down(grind, x, y, word):
    for letter in word:
        if letter == grind[x][y]:
            x += 1
        else: 
            return False
    return True

def left(grind, x, y, word):
    for letter in word:
        if letter == grind[x][y]:
            y -= 1
        else: 
            return False
    return True

def rigth(grind, x, y, word):
    for letter in word:
        if letter == grind[x][y]:
            y += 1
        else: 
            return False
    return True

def upLeft(grind, x, y, word):
    for letter in word:
        if letter == grind[x][y]:
            x -= 1
            y -= 1
        else: 
            return False
    return True

def upRigth(grind, x, y, word):
    for letter in word:
        if letter == grind[x][y]:
            x -= 1
            y += 1
        else: 
            return False
    return True

def downLeft(grind, x, y, word):
    for letter in word:
        if letter == grind[x][y]:
            x += 1
            y -= 1
        else: 
            return False
    return True

def downRigth(grind, x, y, word):
    for letter in word:
        if letter == grind[x][y]:
            x += 1
            y += 1
        else: 
            return False
    return True

# Resive el arreglo de resultado y determina si se encontraron todos los valores 
def resultado(resultado):
    for x in resultado:
        if x:
            continue
        else:
            return False
    return True