'''
TODO

generer les cartes
  - generer toutes les possibilités pour chaque bit en binaire
      - recursion (?)
      - boucle puis sort reverse (?)
  - convertir chaque byte en decimal

fonction conversion binaires <> decimal

game loop
  - inputs
  - affichage des cartes
  - generation de la date de naissance binaire
  - affichage du resultat

Difficultés:
- générer les cartes, particulierement les nombres binaires de 0 - 31
- générer la date de naissance, problemes avec des indexs décalés

'''
from random import shuffle

def dec(num):
  '''
  str --> int
  fonction qui convertie un nombre binaire en décimale 
  '''
  decimalNum = 0
  for i in range(len(num)):
    decimalNum += 2 **(len(num) - i - 1) * int(num[i])
  return decimalNum

def generate_cards(n):
    '''
    int, int -> lst[int]
    renvoie la liste de tout les nombres binaires de longeur n avec un 1 a la position p
    '''

    binary_numbers = []
    for i in range(2**n):

        binary = '' #nombre binaire sous forme de strings
        while i > 0:
            binary =  str(i % 2) + binary
            i = i // 2
        binary = '0' * (n - len(binary)) + binary # complete pour que le nombre soit sur n bits
        binary_numbers.append(binary)

    print(binary_numbers)
    cartes = {i:[dec(binary_numbers[j]) for j in range(2**n) if binary_numbers[j][i] == '1'] for i in range(5)}

    return cartes

#print(generate_cards(5))

def affiche(cards, n):
    '''
    dict{int:lst}, int -> None
    affiche la carte n dans un ordre aleatoire
    '''
    
    carte = cards[n]
    #print(carte)
    shuffle(carte)

    print('      |      |      |      ')
    for i in range(4):
        for j in range(4):
            print(f'  {carte.pop(0):<2}  ' ,end='')
            if j<3:
                print('|',end='')
        print()
        if i<3:
            print('______|______|______|______')
            print('      |      |      |      ')
        else:
            print('      |      |      |      ')
    print()
    return None

def generer_date_de_naissance(cartes):
    '''
    dict{int:lst} --> None
    fonction qui genere le jour de naissance de l'utilisateur en binaire en fonction des cartes auxquelles il répond oui
    '''
    #print(cartes)
    date_binaire = ["0", "0", "0", "0", "0"]
    ordre = [i for i in range(5)]
    shuffle(ordre)
    for i in ordre:
        affiche(cartes, i)
        reponse = input("Y\'a t-il votre date de naissance sur cette carte? (y/n): ")
        if reponse == "y":
            date_binaire[i] = "1"
        #print(date_binaire)
  
    date = "".join(date_binaire)
    print("Votre jour de naissance est le ", dec(date))

generer_date_de_naissance(generate_cards(5))

'''
le projet est terminé, j'ai merge la fonction generate_cards et generate_binary_numbers afin de gagner en complexité algorithmique (- 5n)
j'ai changer la fonction dec car elle donnait des resultat faux
pour generer_date_de_naissance, la fonction faisait un randint entre 1 et 5 a chaque fois donc appelait parfois 2 fois la meme carte, puisque je pop les elements de la liste (detruisant les cartes), 
j'ai du changer la fonction pour qu'elle ne fasse pas de randint mais un shuffle d'une liste des nombres de 0 a 4'
j'ai aussi delete la fonction bin que je pense etait inutilisée et pas completée

autres changement pas tres important en relation avec l'ordre des cartes et de la completation de la liste pour la date de naissance
il me reste plus qu'a faire la version avec une interface pygames si j'ai le temps, sinon au pire cette interface est deja correcte
'''
