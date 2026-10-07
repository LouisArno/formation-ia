#print("Bonjour, je démarre ma formation IA")

def Moyenne(L):
    moy = 0
    for i in range(len(L)):
        moy += L[i]
    moy = moy/len(L)
    return(moy)

def CompterMots(phrase):
    compte = {}

    for mot in phrase.lower().split():
        mot = mot.strip(".,!?;:")
        if mot:
            compte[mot] = compte.get(mot, 0) + 1

    return compte


carres_pairs = [nombre ** 2 for nombre in range(1, 21) if nombre % 2 == 0]


class Machine:
    def __init__(self, nom):
        self.nom = nom
        self.etat = "arrêt"

    def demarrer(self):
        self.etat = "en marche"

    def arreter(self):
        self.etat = "arrêt"


def CompterLignes(nom_fichier):
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            nombre_lignes = 0
            for ligne in fichier:
                nombre_lignes += 1
            return nombre_lignes
    except FileNotFoundError:
        print(f"Le fichier '{nom_fichier}' n'existe pas.")
        return None

