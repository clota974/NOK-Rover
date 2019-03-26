# 28/03/2019

J'ai mis ici ce que tu peux faire pour avancer un peu. 
(Tu peux aussi penser à la fonction `bouger` de la classe voiture)


## Commencer la rédaction du Cahier des charges

Oublie pas l'exemple que M. Et

## 


### Classe `Voiture`

La classe Voiture sera le lien entre toutes les classes. Il permettra d'allumer la **LED**, coordonner les **deux moteurs**, **klaxonner**... ⇒ 

Il faudra créer un dictionnaire avec les adresses de chaque PIN d'après pinout.pdf dans le dossier `notes`

Exemple du code : 
```py
class Voiture:
	adresses = {
		PWMA: 27,
		AIN2: 18,
		...
	}
	led = Led(adresses.led) # ⇒ C'est la classe qu'on a cree nous-mêmes
	moteur1 = Moteur(adresses.AIN1, adresses.AIN2, adresses.PWMA)
	# .....
	# .....
	# .....
	def bouger(self, vitesse_x, vitesse_y):
		# Faire bouger les moteurs
```

Les propriétés (variables) de la classe sont : 

- La LED
- Le Buzzer
- Les DEUX moteurs [⇒ Revoir la classe que tu as faite] :
Ex *(à vérifier/confirmer)* : 
```py
import classes.Moteur 

moteur_gauche = Moteur(...à remplir selon la classe...)
```
- L'écran LCD (plus tard)
- Les adresses

Il faut donc créer des fonctions pour :

- Klaxonner (list: intervalles, entier: repeter_nbr_fois)  :
*C'est un peu compliqué mais tu peux le faire. Programmer c'est chercher des solutions (par soi-même ou sur internet)*
Exemple : `klaxonner([2,3,4,5], 5)`. 
La voiture klaxonnera 2s puis attendra 3s avant de klaxonner 4s puis attendra 5s avant de recommencer en klaxonnant 2s et attendre 3s.... Il répétera en 5 fois

Plusieurs manières de faire, je te laisse y réfléchir. Le plus facile serait de stocker la position dans la liste des intervalles, stocker l'heure de départ, calculer la différence de temps avec l'heure actuelle (tout ça dans une boucle *while*). Si la différence correspond à la valeur dans l'array (selon la position) (càd le nombre de secondes à attendre ou à klaxonner) alors passer à la position suivante dans la liste et changer l'état du buzzer.

- Bouger la voiture  :

Petit exercice : Réfléchis à comment on pourrait faire pour coordonner les deux moteurs. C'est-à-dire, je veux faire bouger la voiture avec la fonction qui s'appelle **par exemple** `bouger` :

Quels paramètres/arguments j'utilise (ce qu'il y a entre parenthèses après le nom de la fonction)? 

Quel est le type, le format, l'unité de chaque paramètre? 

Comment est-ce que je fais avancer physiquement la voiture? --> En activant les moteurs --> Comment? A quelle vitesse? Dans quel sens?

A toi d'y réfléchir... Ecrire du code python si tu le sens, sinon juste réfléchir à la méthode, et écrire du pseudo-code (en français).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA1MjI4NTkzMywxMTMxOTM5OTY5LDQwOD
g5Njg2M119
-->