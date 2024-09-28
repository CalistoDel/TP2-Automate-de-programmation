#fait par Calisto DEL AGUILA le 23/09/2024
#Objectif: création d'un automate de programmation ayant pour but de vérifier si la syntaxe d'une phrase qui lui est donnée est juste ou non
#ToDo: - Programmation de l'automate et test par saise de phrase (FAIT)
# - Saisie possible par utilisateur pour test de l'automate (FAIT)
# - Création d'un jeu de test vérifiant la validité de l'automate (FAIT) 


from fonctions_TP2 import conversion
from fonctions_TP2 import automate

# Saisie de phrase par l'utilisateur

phrase_test=input("Ecrivez une phrase:")
test=automate(phrase_test)
print(test)


#Jeu de test - Permet de tester la validité de l'automate de programmation  

phrase_test_mange='le joli chat mange.'
phrase_test_dort="le ,joli chat ; dort."
phrase_test_souris="la grosse souris verte mange le joli petite chat blanc."
phrase_test_verte="la grosse souris verte mange jean"
phrase_test_Jean= "Jean dort."
phrase_test_Martin="Jean mange Martin."
phrase_test_chat="Jean mange le chat."
phrase_test_petite= "la verte souris grosse petit mange le bleu verte chat petite."
phrase_test_faux="le joli chat joue."

automate(phrase_test_dort)