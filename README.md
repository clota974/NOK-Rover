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

La classe Voiture sera le lien entre toutes les classes. Il permettra d'allumer la **LED**, coordonner les **deux moteurs**, **klaxonner**...

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
	def bouger(self, x, y):
		# Faire bouger les moteurs
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTEzMTkzOTk2OSw0MDg4OTY4NjNdfQ==
-->