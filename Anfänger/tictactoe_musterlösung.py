spielfeld = ["_" for i in range(9)]

for i in range(3):
    print(spielfeld[3*i], spielfeld[3*i+1], spielfeld[3*i+2])

for runde in range(9):
    zelle = input("In welche Zelle möchtest du dein Zeichen setzen? ")
    
    if runde % 2 == 0:
        spielfeld[int(zelle)] = "x"
    if runde % 2 != 0:
        spielfeld[int(zelle)] = "o"
    
    for i in range(3):
        print(spielfeld[3*i], spielfeld[3*i+1], spielfeld[3*i+2])
    
    for i in range(3):
        if spielfeld[3*i] == spielfeld[3*i+1] == spielfeld[3*i+2] and spielfeld[3*i] != "_":
            print("Gewonnen!")
            break
        if spielfeld[i] == spielfeld[i+3] == spielfeld[i+6] and spielfeld[i] != "_":
            print("Gewonnen!")
            break
    if spielfeld[0] == spielfeld[4] == spielfeld[8] and spielfeld[0] != "_":
        print("Gewonnen!")
        break
    if spielfeld[2] == spielfeld[4] == spielfeld[6] and spielfeld[2] != "_":
        print("Gewonnen!")
        break
