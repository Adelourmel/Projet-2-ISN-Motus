#coding : utf-8
import unidecode
def menu():
    quitter = True
    while quitter:
        print("Jouer à MOTUS :\n1. Jouer seul =(\n2. Jouer à deux =)\n3. Règles du jeu\n4. Quitter")
        choice = int(input("Votre choix : "))
        if choice == 1:
            solo()
        elif choice == 2:
            dual()
        elif choice == 3:
            print("On demande au joueur 1 de saisir un mot de 7 lettres.")
            print("Le programme affiche la réponse alors de la manière suivante :")
            print("\t Les lettres bien placée sont écrites en MAJUSCULES.")
            print("\tLes lettres mal placée sont écrites en minuscules.")
            print("\tLes autres sont remplacées par des points.\n")
        elif choice == 4:
            quitter = False
        else:
            print("Erreur")

def dual():
    i = True
    trouve = False
    while i:
        mot = input("Entrez un mot de 7 caractères :")
        if len(mot) == 7:
            while trouve == False:
                trouve = game(mot)
            i = False
        else:
            print("Votre mot ne fais pas 7 caractères !")

def game(word):
    word = deleteAccent(word)
    player = " "
    reponse = ["*"]*7
    while len(player) != 7:
        player = input("Entrez votre réponse : ")
        if len(player) != 7:
            print("La réponse comporte 7 caractères")

    player = deleteAccent(player)
    if player == word:
        print("Bravo vous avez trouvé le mot caché : " + word)
        return True
    else:
        for i in range(7):
            if player.find(word[i]) != -1:
                if player[i] == word[i]:
                    reponse[i] = word[i]
                else:
                    reponse[player.find(word[i])] = word[i].lower()
        for i in range(7):
            if word.find(player[i]) != -1:
                if player[i] == word[i]:
                    reponse[i] = word[i]
                else:
                    reponse[i] = player[i].lower()

    print("".join(reponse))
    return False

def deleteAccent(word):              
    word = word.lower()
    word = word.replace("à", "a")
    word = word.replace("é", "e")
    word = word.replace("è", "e")
    word = word.replace("ç", "c")
    word = word.upper()
    return word

def solo():
    print("Le mode solo n'est pas fonctionnel pour le moment !")
menu()