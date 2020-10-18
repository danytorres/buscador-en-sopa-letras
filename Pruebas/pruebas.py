# Archivo de pruebas de el logaritmo que desarrollaba 


from textwrap import wrap
import barrido
import make


words = ["stick", "most", "key", "vein", "yes", "package", "tube", "target", "elm", "spy"]

# find = []
# for columnas in words:
#     makeColumnas = wrap(columnas, 1)
#     find.append(makeColumnas)

# x=0
# print(find[True])

letters = "PSUWHATSLPACKAGENYOLRDVLFINGEZBMIREHQNJOATBVGYESJDUWUESTPSTICKEY"
#letters = letters.lower()
# print(letters)
# resultado = make.makeRes(words)
# print(resultado)
grind = make.makeGrind(letters)
print(grind)

words[1] = False
print(words)

# makeWords = make.makeWords(words)
# grind = [
#   ["P", "S", "U", "W", "H", "A", "T", "S"],
#   ["L", "P", "A", "C", "K", "A", "G", "E"],
#   ["N", "Y", "O", "L", "R", "D", "V", "L"],
#   ["F", "I", "N", "G", "E", "Z", "B", "M"],
#   ["I", "R", "E", "H", "Q", "N", "J", "O"],
#   ["A", "T", "B", "V", "G", "Y", "E", "S"],
#   ["J", "D", "U", "W", "U", "E", "S", "T"],
#   ["P", "S", "T", "I", "C", "K", "E", "Y"]
# ]

pruebas = ["EBEGLAER",
           "OZPOSTVL",
           "KYEEONEO",
           "CUTETEIS",
           "IBUYRCHT",
           "RMYGSBCN",
           "TCERIDAP",
           "RDIKOMAN"]


# grind.append(["","","","","","","",""])
# x=1
# y=1
# #print(grind[-1])
# print(grind[x][y])
# print(makeWords[5][0])
# fr = grind[x][y]
# fe = makeWords[5][0]
# print(grind[x][y] == makeWords[5][0])
# print(fr == fe)
# for z in range(len(makeWords)):
#     print(x)
#     print(y)
#     print(z)
#     print(grind[x][y] == makeWords[z][0])
#     print(grind[x-1][y] == makeWords[z][1])
#     print(barrido.up(grind,x,y,makeWords[z]))
#     if grind[x][y] == makeWords[z][0] and grind[x-1][y] == makeWords[z][1] and barrido.up(grind,x,y,makeWords[z]):
#         print("entro1")
#         makeWords.pop(z)
#     elif grind[x][y] == makeWords[z][0] and grind[x+1][y] == makeWords[z][1] and barrido.down(grind,x,y,makeWords[z]):
#         print("entro2")
#         makeWords.pop(z)
#     elif grind[x][y] == makeWords[z][0] and grind[x][y-1] == makeWords[z][1] and barrido.left(grind,x,y,makeWords[z]):
#         print("entro3")
#         makeWords.pop(z)
#     elif grind[x][y] == makeWords[z][0] and grind[x][y+1] == makeWords[z][1] and barrido.rigth(grind,x,y,makeWords[z]):
#         print("entro4")
#         makeWords.pop(z)
#     elif grind[x][y] == makeWords[z][0] and grind[x-1][y+1] == makeWords[z][1] and barrido.upRigth(grind, x, y, makeWords[z]):
#         print("entro5")
#         makeWords.pop(z)
#     elif grind[x][y] == makeWords[z][0] and grind[x-1][y-1] == makeWords[z][1] and barrido.upLeft(grind,x,y,makeWords[z]):
#         print("entro6")
#         makeWords.pop(z)
#     elif grind[x][y] == makeWords[z][0] and grind[x+1][y-1] == makeWords[z][1] and barrido.downLeft(grind,x,y,makeWords[z]):
#         print("entro7")
#         makeWords.pop(z)
#     elif grind[x][y] == makeWords[z][0] and grind[x+1][y+1] == makeWords[z][1] and barrido.downRigth(grind,x,y,makeWords[z]):
#         print("entro8")
#         makeWords.pop(z)

# vacio = []

# print(makeWords)

# if makeWords != vacio:
#     print("true")
# else: 
#     print("false")