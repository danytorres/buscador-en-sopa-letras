from textwrap import wrap
import make
import barrido

letters = "EBEGLAEROZPOSTVLKYEEONEOCUTETEISIBUYRCHTRMYGSBCNTCERIDAPRDIKOMAN"
words = ['buy', 'lost', 'real', 'breeze', 'direct', 'man', 'post', 'trick', 'degree', 'achieve', 'hola']


makeWords = make.makeWords(words)
grind = make.makeGrind(letters)

grind.append(["","","","","","","","",""])

resultado = make.makeRes(words)

for x in range(8):
    for y in range(8):
        for z in range(len(makeWords)):
            print(x)
            print(y)
            print(z)
            print("----------------------------------------------------------------------------")
            print(resultado)
            if grind[x][y] == makeWords[z][0] and grind[x-1][y] == makeWords[z][1] and barrido.up(grind,x,y,makeWords[z]):
                print("entro1")
                input("Press Enter to continue...")
                resultado[z] = True
            elif grind[x][y] == makeWords[z][0] and grind[x+1][y] == makeWords[z][1] and barrido.down(grind,x,y,makeWords[z]):
                print("entro2")
                input("Press Enter to continue...")
                resultado[z] = True
            elif grind[x][y] == makeWords[z][0] and grind[x][y-1] == makeWords[z][1] and barrido.left(grind,x,y,makeWords[z]):
                print("entro3")
                input("Press Enter to continue...")
                resultado[z] = True
            elif grind[x][y] == makeWords[z][0] and grind[x][y+1] == makeWords[z][1] and barrido.rigth(grind,x,y,makeWords[z]):
                print("entro4")
                input("Press Enter to continue...")
                resultado[z] = True
            elif grind[x][y] == makeWords[z][0] and grind[x-1][y+1] == makeWords[z][1] and barrido.upRigth(grind, x, y, makeWords[z]):
                print("entro5")
                input("Press Enter to continue...")
                resultado[z] = True
            elif grind[x][y] == makeWords[z][0] and grind[x-1][y-1] == makeWords[z][1] and barrido.upLeft(grind,x,y,makeWords[z]):
                print("entro6")
                input("Press Enter to continue...")
                resultado[z] = True
            elif grind[x][y] == makeWords[z][0] and grind[x+1][y-1] == makeWords[z][1] and barrido.downLeft(grind,x,y,makeWords[z]):
                print("entro7")
                input("Press Enter to continue...")
                resultado[z] = True
            elif grind[x][y] == makeWords[z][0] and grind[x+1][y+1] == makeWords[z][1] and barrido.downRigth(grind,x,y,makeWords[z]):
                print("entro8")
                input("Press Enter to continue...")
                resultado[z] = True

vacio = []

print(makeWords)
print(resultado)
print(barrido.resultado(resultado))

if barrido.resultado(resultado):
    print("true")
else: 
    print("false")