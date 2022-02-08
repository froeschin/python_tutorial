spielfeld = ["_" for i in range(9)]

def spielfeld_anzeigen():
    for i in range(3):
        print(spielfeld[3*i], spielfeld[3*i+1], spielfeld[3*i+2])

def spiel_gewonnen():
    for i in range(3):
        if spielfeld[3*i] == spielfeld[3*i+1] == spielfeld[3*i+2] and spielfeld[3*i] != "_":
            return True
        if spielfeld[i] == spielfeld[i+3] == spielfeld[i+6] and spielfeld[i] != "_":
            return True
    if spielfeld[0] == spielfeld[4] == spielfeld[8] and spielfeld[0] != "_":
        return True
    if spielfeld[2] == spielfeld[4] == spielfeld[6] and spielfeld[2] != "_":
        return True
    return False

spielfeld_anzeigen()

for runde in range(9):
    zelle = input("In welche Zelle möchtest du dein Zeichen setzen? ")
    
    if runde % 2 == 0:
        spielfeld[int(zelle)] = "x"
    if runde % 2 != 0:
        spielfeld[int(zelle)] = "o"
    
    spielfeld_anzeigen()
    
    if spiel_gewonnen():
        print("Gewonnen!")
        break

