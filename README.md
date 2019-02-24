# 27/02/2019

## Objectifs

| To do | In progress | Done
|--|--|--|
| Rien | Voiture | LED, Buzzer

## Nouveautés

### Classe `Voiture`

La classe Voiture sera le lien entre toutes les classes. Il permettra d'allumer la LED, coordonner les deux moteurs, klaxonner...

Exemple du code : 
```py
class Voiture:
	adresses = {
		PWMA: 27,
		AIN1: 
	}
	led = Led(adresses.led) # ⇒ C'est la classe qu'on a cree nous-même
	moteur1 = Moteur(adresses.AIN1, adresses.AIN2, adresses.PWMA)
	# .....
	# .....
	# .....
	def bouger(self, x, y):
		# Faire bouger les moteurs
```

Il faudra 

<!--stackedit_data:
eyJoaXN0b3J5IjpbNTc3MzcxNDczLDQwODg5Njg2M119
-->