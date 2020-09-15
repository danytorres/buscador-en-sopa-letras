from textwrap import wrap
import make
import barrido

def wordSearch(letters, words):
    
    makeWords = make.makeWords(words)
    grind = make.makeGrind(letters)

    grind.append(["","","","","","","","",""])

    resultado = make.makeRes(words)

    for x in range(8):
        for y in range(8):
            for z in range(len(makeWords)):
                if grind[x][y] == makeWords[z][0] and grind[x-1][y] == makeWords[z][1] and barrido.up(grind,x,y,makeWords[z]):
                    resultado[z] = True
                elif grind[x][y] == makeWords[z][0] and grind[x+1][y] == makeWords[z][1] and barrido.down(grind,x,y,makeWords[z]):
                    resultado[z] = True
                elif grind[x][y] == makeWords[z][0] and grind[x][y-1] == makeWords[z][1] and barrido.left(grind,x,y,makeWords[z]):
                    resultado[z] = True
                elif grind[x][y] == makeWords[z][0] and grind[x][y+1] == makeWords[z][1] and barrido.rigth(grind,x,y,makeWords[z]):
                    resultado[z] = True
                elif grind[x][y] == makeWords[z][0] and grind[x-1][y+1] == makeWords[z][1] and barrido.upRigth(grind, x, y, makeWords[z]):
                    resultado[z] = True
                elif grind[x][y] == makeWords[z][0] and grind[x-1][y-1] == makeWords[z][1] and barrido.upLeft(grind,x,y,makeWords[z]):
                    resultado[z] = True
                elif grind[x][y] == makeWords[z][0] and grind[x+1][y-1] == makeWords[z][1] and barrido.downLeft(grind,x,y,makeWords[z]):
                    resultado[z] = True
                elif grind[x][y] == makeWords[z][0] and grind[x+1][y+1] == makeWords[z][1] and barrido.downRigth(grind,x,y,makeWords[z]):
                    resultado[z] = True

    if barrido.resultado(resultado):
        return True
    else: 
        return False