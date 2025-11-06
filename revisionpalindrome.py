from unidecode import unidecode
import re

def palindrome():

    phrase = input("Veuillez saisir une phrase..:")

    # Nettoya de la phrase : Suppresion d"accent, d'espace, ponctuation et apostrope
    phrase_sans_accent = unidecode(phrase)
    clean_phrase = re.sub(r'[^a-zA-Z0-9]','',phrase_sans_accent).lower()
    
    # Inversion de la phrase
    inverse_clean_phrase = clean_phrase[::-1]

    if clean_phrase == inverse_clean_phrase:
        print("La phrase "+ phrase + " est un palindrome.")
    else:
        print("La phrase " + phrase + " n'est un palindrome.")


palindrome()