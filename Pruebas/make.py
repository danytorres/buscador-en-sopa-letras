from textwrap import wrap

def makeGrind(letters):
    grind = []
    letters = letters.lower()
    makeFilas = wrap(letters, 8)

    for columnas in makeFilas:
        makeColumnas = wrap(columnas, 1)
        makeColumnas.append("")
        grind.append(makeColumnas)
    return grind

def makeWords(words):
    find = []
    for columnas in words:
        makeColumnas = wrap(columnas, 1)
        find.append(makeColumnas)

    return find

def makeRes(words):
    res = []
    for x in range(len(words)):
        res.append(False) 

    return res