from textwrap import wrap

# Recibe el arreglo de letras y empieza a generar el grind de 8x8
def makeGrind(letters):
    grind = []
    letters = letters.lower() # Pasa a minusculas las letras para poder compararlas y todas esten en minusculas
    makeFilas = wrap(letters, 8)

    for columnas in makeFilas:
        makeColumnas = wrap(columnas, 1)
        makeColumnas.append("") # Agrega una columna extra vacia, esto para evitar el error de numeros negativos en el barrido de palabras
        grind.append(makeColumnas)
    
    grind.append(["","","","","","","","",""]) # Agrega una fila extra vacia para evitar el error de numeros negativos 

    return grind

# Separa cada una de las letras de cada palabra del arreglo de palabras
def makeWords(words):
    find = []
    for columnas in words:
        makeColumnas = wrap(columnas, 1)
        find.append(makeColumnas)

    return find

# Genera un arreglo con valores False con la misma cantindad de palabras a buscar
def makeRes(words):
    res = []
    for x in range(len(words)):
        res.append(False) 

    return res