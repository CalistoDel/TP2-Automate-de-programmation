#fait par Calisto DEL AGUILA le 23/09/2024
#Objectif: création d'un automate de programmation ayant pour but de vérifier si la syntaxe d'une phrase qui lui est donnée est juste ou non


dictionnaire ={"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,
"mange" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1,
"bleu" : 1, "verte" : 1, "dort" : 3,"julie" : 4, "jean" : 4, "." : 5}


def conversion(phrase):
#fonction qui prend en argument une phrase et la transforme en une suite de caractere selon la classe des mots la formant
    sequence=[]
    caractere_speciaux=['_','-','!','?',':',',','.']
    phrase_decouper=phrase.split()
    for mot in phrase_decouper:
        motcorrect=''
        for lettre in mot:
            if lettre not in caractere_speciaux:    
                motcorrect+= lettre                 #retire les caractères spéciaux d'un mot
            if lettre in dictionnaire.keys():
                sequence.append(dictionnaire[lettre])
        sequence.append(dictionnaire[motcorrect])
    return sequence




def automate(phrase):
#fonction qui avec prend en argument d'entrée une phrase et qui renvoie si elle est corect syntaxiquement ou non
    sequence=conversion(phrase)
    etat=0                      #initialisation de l'état
    matriceEE=[[1,8,8,5,8,8,8,8,8,8],[8,1,2,8,8,5,6,8,8,8],[8,2,8,8,8,6,8,8,8,8],[8,8,3,8,3,8,8,8,8,8],[4,8,8,7,8,8,8,8,8,8],[8,8,8,9,8,8,9,9,8,9]]
    matriceES=[0,0,0,0,0,0,0,0,0,1]
    for entree in sequence:
        etat=matriceEE[entree][etat]
    s=matriceES[etat]
    if s==1:
        print("La phrase est correcte")
    else:
        print("La phrase est incorrecte")
