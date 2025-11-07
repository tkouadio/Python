# Ce programme calcule l'age d'une personne 

from datetime import date, datetime

def age():

    today = date.today()
    
    try:
        DateNaissance = input("Veuillez saisir votre date de naissance (JJ-MM-AAAA): ")
        DateNaissanceNormaliser = datetime.strptime(DateNaissance.replace("-",""), "%d%m%Y").date()
        DateDiff = today - DateNaissanceNormaliser
        CalculAge = int(DateDiff.days / 365)
        
        print("Vous avez "+ str(CalculAge) + " ans.")
   
    except ValueError: 
        print("Format de date invalide.")

age()