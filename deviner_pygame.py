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
import pygame
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

def affiche_orig(cards, n):
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

def affiche(surf, cards, n):
    '''
    fenetre pygame, lst -> None
    affiche la grille du morpion sur la fenetre surf avec les coups joués a partir du tableau g
    '''

    carte = cards[n]
    #display a four by four grid with the numbers in the list carte put lines in the middle
    #include the numbers between the lines
    #print(carte)
    pygame.draw.line(surf, (0, 0, 0), (200, 0), (200, 600), 5)
    pygame.draw.line(surf, (0, 0, 0), (400, 0), (400, 600), 5)
    pygame.draw.line(surf, (0, 0, 0), (0, 200), (600, 200), 5)
    pygame.draw.line(surf, (0, 0, 0), (0, 400), (600, 400), 5)


    
    pygame.display.update()

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
        print(affiche(cartes, i))
        reponse = input("Y\'a t-il votre date de naissance sur cette carte? (y/n): ")
        if reponse == "y":
            date_binaire[i] = "1"
        #print(date_binaire)
  
    date = "".join(date_binaire)
    print("Votre jour de naissance est le ", dec(date))

def check_pos(pos):
	'''
	(int, int) -> (int, int)
	renvoie col, lig correspondant a la case cliqué
	'''
	if pos[0] < 200:
		col = 0
	elif pos[0] < 400:
		col = 1
	else:
		col = 2
	if pos[1] < 200:
		lig = 0
	elif pos[1] < 400:
		lig = 1
	else:
		lig = 2
	return lig, col

def render_text(surf, text, x, y, color=(0, 0, 0,), size=32, border=False):
	'''
	fenetre pygame, str, int, int -> None
	options: color=(int,int,int), size=int, border=bool
	affiche du texte sur la fenetre surf a la position x, y de taille size et de couleur color
	'''
	font = pygame.font.Font('freesansbold.ttf', size)
	text = font.render(text, True, color, (255, 255, 255))
	textRect = text.get_rect(center=(x,y))
	#draw a box around text if the border arg is set to True
	if border:
		pygame.draw.rect(surf, (0, 0, 0), (textRect.x-5, textRect.y-5, textRect.width+10, textRect.height+10), 5)
	surf.blit(text, textRect)
	pygame.display.update()

def main():
    WIDTH = 800
    HEIGHT = 600
    surf = pygame.display.set_mode((WIDTH, HEIGHT))
    surf.fill((255, 255, 255))
    pygame.font.init() #necessary for text rendering
    while True:
        pygame.display.update()
        affiche(surf, generate_cards(5), 0)

main()


    #generer_date_de_naissance(generate_cards(5))

