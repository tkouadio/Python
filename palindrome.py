# Cette fonction Écris une fonction qui détermine si une phrase est 
# un palindrome (ignorer espaces et accents).

from unidecode import unidecode
import re
def palindrome():
  
    phrase = input("Veuillez saisir une phrase...")

    # Suppresion des accents
    txt = unidecode(phrase)
     
    # Supprimer tout sauf lettres et chiffres
    clean = re.sub(r'[^a-zA-Z0-9]', '', txt).lower()
    
    reverseclean = clean[::-1]

    if clean == reverseclean:
        print("La phrase "+ clean + " est un palindrome.")
    else:
        print("La phrase "+ clean + " n'est pas un palindrome.")


palindrome()