# 27/02/2019

## Objectifs

| To do | In progress | Done
|--|--|--|
| Rien | Voiture | LED, Buzzer

## Notes

Le `led.class.py` est à revoir. Des commentaires ont été ajoutés pour que vous corrigiez les erreurs.

Les commentaires commençant par :
-  `#`  : commentaires que vous avez écrits.
- `##` : Notes de correction (à enlever une fois la correction effectuée)
- `####` : Commentaire pour le correcteur Python

## Nouveautés

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
- L'écran LCD (plus tard)
- Les adresses

Il faut donc créer des fonctions pour :

- Klaxonner (array: intervalles, booléen: repeter)  :
*C'est un peu compliqué mais tu peux le faire. Programmer c'est chercher des solutions (par soi-même ou sur internet)*
Exemple : `klaxonner([2,3,4,5], true)`. 
La voiture klaxonnera 2s puis attendra 3s avant de klaxonner 4s puis attendra 5s avant de recommencer en klaxonnant 2s et attendre 3s....

Pour cela, il faut stocker le temps auquel on instancie la fonction pour la première fois, puis on calcule 

- Bouger la voiture `(vitesse_x, vitesse_y)`

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU4MzEzOTEyMCwxMTMxOTM5OTY5LDQwOD
g5Njg2M119
-->