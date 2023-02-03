
import secrets

caracterem = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
chiffre2 = ['1','2', '3', '4', '5', '6', '7', '8', '9']
caracterespé = ['@', '#', '&', 'é', 'à', 'ç', '!', ')', '-', '/','%', '*','$','^','`','+','=', '.','<', '>']
binaire = [1,2]
caractereM = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
L = []




def selectRandom(caractere):
  return secrets.choice(caractere)

def mdp() :

    print("Vous êtes ici pour obtenir un mot de passe. Vous pouvez choisir la longueur, et certains options.")
    long = int(input("Choisissez la longueur du mot de passe : "))
    majuscule = str(input("Voulez-vous des majuscules ? Y/N : "))
    chiffre = str(input("Voulez-vous des chiffres ? Y/N : "))
    caractere = str(input("Voulez-vous des caracteres speciaux ? Y/N : "))
# y / n

    if majuscule == 'N' and chiffre == 'N' and caractere == 'N':
            for i in range(long) :
                a = secrets.choice(caracterem)
                L.append(a)
                motdepasse = ''.join(L)
            print("Voici donc votre mot de passe : ", motdepasse)
            return motdepasse

    elif majuscule == 'Y' and chiffre == 'N' :
        for i in range(long) :
                a = secrets.choice(caracterem)
                b = secrets.choice(caractereM)
                r2 = secrets.choice(binaire)

                if r2 == 1 :
                    L.append(a)
                else :
                    L.append(b)
                motdepasse = ''.join(L)
        print("Voici donc votre mot de passe : ", motdepasse)
        return motdepasse

    elif majuscule == 'Y' and chiffre == 'Y' and caractere == 'N':
        for i in range(long) :
            a = secrets.choice(caracterem)
            b = secrets.choice(caractereM)
            c = secrets.choice(chiffre2)

            r1 = secrets.choice(binaire)
            r2 = secrets.choice(binaire)

            if r1 == 1 :
                L.append(c)
            elif r2 == 1 :
                L.append(a)
            else :
                L.append(b)
            motdepasse = ''.join(L)
        print("Voici donc votre mot de passe : ", motdepasse)
        return motdepasse

    elif majuscule == 'Y' and chiffre == 'Y' and caractere == 'Y':
        for i in range(long) :
            a = secrets.choice(caracterem)
            b = secrets.choice(caractereM)
            c = secrets.choice(chiffre2)
            d = secrets.choice(caracterespé)

            r1 = secrets.choice(binaire)
            r2 = secrets.choice(binaire)
            r4 = secrets.choice(binaire)

            if r1 == 1 :
                L.append(c)
            elif r2 == 1 :
                L.append(a)
            elif r4 == 1 :
                L.append(d)
            else :
                L.append(b)
            motdepasse = ''.join(L)
        print("Voici donc votre mot de passe : ", motdepasse)
        return motdepasse
        
mdp()
