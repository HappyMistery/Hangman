from Objectes import paraula
from Objectes import llista_paraules
import random
import time

#Hangman
def Hangman():
    global count
    global name
    global pick
    global word
    global spaces
    global total
    ok = False
    guess = input(f"La paraula a endevinar és {spaces}. Quina lletra vols probar?\n")
    if guess in pick:
        for lletra in spaces:
            if guess in pick:
                spaces = spaces[:pick.index(guess)] + guess + spaces[pick.index(guess) + 1:]
                pick = pick[:pick.index(guess)] + "_" + pick[pick.index(guess) + 1:]
                total-=1
                if total <= 0:
                    print(f"Has guanyat! La paraula correcte era {word}\n")
                    play_again()

        Hangman()
    else:
        count+=1
        if count==1:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("La lletra no forma part de la paraula. Et queden 6 intents\n")
            Hangman()
        elif count ==2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |   (;-;)\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("La lletra no forma part de la paraula. Et queden 5 intents\n")
            Hangman()
        elif count ==3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |   (;-;)\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("La lletra no forma part de la paraula. Et queden 4 intents\n")
            Hangman()
        elif count ==4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |   (;-;)\n"
                  "  |    /| \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("La lletra no forma part de la paraula. Et queden 3 intents\n")
            Hangman()
        elif count ==5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |   (;-;)\n"
                  "  |    /|\ \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("La lletra no forma part de la paraula. Et queden 2 intents\n")
            Hangman()
        elif count ==6:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |   (;-;)\n"
                  "  |    /|\ \n"
                  "  |    /\n"
                  "  |      \n"
                  "__|__\n")
            print("La lletra no forma part de la paraula. Et queden 1 intent\n")
            Hangman()
        else:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |   (x-x)\n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "  |      \n"
                  "__|__\n")
            print(f"Has perdut. La paraula correcte era {word}\n")
            play_again()


#Play again
def play_again():
    ans = input("Vols tornar a jugar? s = Sí, n = No\n")
    if ans in "sS":
        main()
    else:
        print("Que tinguis un bon dia!")
        exit()
#Main
def main():
    global count
    global name
    global pick
    global word
    global spaces
    global total
    count = 0
    name = ""
    pick = paraula().word_picking(llista_paraules)
    word = pick
    spaces = paraula().n_char(pick)
    total = paraula().num_lletres(pick)
    name = input("Nom del jugador: ")
    time.sleep(1)
    print("Benvingut/da al joc del penjat, " + name)
    time.sleep(1)
    print("El joc està a punt de començar...\n"+("="*59 ))
    Hangman()


main()