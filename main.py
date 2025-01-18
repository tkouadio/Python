
# Ce fonction demande le nom et l'âge d'une personne et lui renvoi son statut(Enfant, Majeur)
def demander_informations(nom, age):
    while nom == "":
          nom = input("Quel est votre nom : ")

    age_prochain = 0
    while age == 0:
        try:
            age = input("Quel est votre age : ")
            age_prochain = int(age) + 1
        except:
            print(" ERREUR - Veuillez entrer votre age : ")
            return

    print()
    print("Vous vous appellez " + nom + " et vous avez " + str(age) + " ans.")
    print("L'an prochain vous aurez " + str(age_prochain) + " ans.")

    age_int = int(age)
    if age_int < 10:
        print("Vous êtes enfant.")
    elif age_int == 17:
        print("Vous êtes presque majeur.")
    elif age_int == 18:
        print("Tout juste majeur : Félicitation.")
    elif age_int > 60:
        print("Vous êtes sénior.")
    elif age_int >= 18:
        print("Vous êtes majeur.")
    else:
        print("Vous êtes mineur.")


# Appel de la fonction: demander_informations

demander_informations("", 0)
