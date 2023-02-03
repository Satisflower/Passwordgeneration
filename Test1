import random
import secrets

caracterem = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
chiffre = ['1','2', '3', '4', '5', '6', '7', '8', '9']
binaire = [1,2]
caractereM = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
L = []

def selectRandom(caractere):
  return secrets.choice(caractere)


def mdp() :

    print("Vous êtes ici pour obtenir un mot de passe. Vous pouvez choisir la longueur, et certains options.")
    print("Conseil : Si vous voulez un mot de passe sécurisé, choisie")
    long = int(input("Choisissez la longueur du mot de passe : "))
    majuscule = str(input("Voulez-vous des majuscules ? Oui/Non : "))
    chiffre = str(input("Voulez-vous des chiffres ? Oui/Non : "))


    if majuscule == 'Non' and chiffre == 'Non' :
            for i in range(long) :
                a = secrets.choice(caracterem)
                L.append(a)
                motdepasse = ''.join(L)
    print(motdepasse)
    return a

    if majuscule == 'Oui' and chiffre == 'Non' :
        for i in range(long) :
            a = secrets.choice(caracterem)
            b = secrets.choice(caractereM)

            r1 = secrets.choice(binaire)
            r2 = secrets.choice(binaire)

            if r2 == 1 :
                L.append(a)
            if r1 == 1 :
                L.append(a)
                motdepasse = ''.join(L)
    print(motdepasse)
    return a
