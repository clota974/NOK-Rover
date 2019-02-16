
# NOK Rover - Cahier des Charges

# I) Introduction 

## a) Objectif du projet 

La NOK-Rover est une voiture motorisée contrôlée par une manette sans fil.

## b) Spécifications / Fiche technique

- Processeur de la voiture : Raspberry Pi 3B+
- Alimentation : Batterie externe
- Manette sans fil : Dualshock 4 (Manette de PS4)
- Connexion : Bluetooth 4.0
- Langage de programmation : Python 3

## c) Détails électroniques

- Roues motorisées : 2 (individuelles)
- LEDs : 2 (à l'avant)
- Couleur LED : Blanc
- Buzzer : 1 (1024 kHz)
- Ecran LCD : 1 RGB
- Boutons (Pushbutton) : 2

## d) Détails logiciels 

- Numérotation (GPIO/BCM) : BCM (On notera le numéro des pins avec le préfixe `a_`)
- PWM moteurs : 980Hz 

Le PWM des moteurs a été choisi d'après la fréquence PWM des cartes Arduino.

Le logiciel utilisé afin de modéliser le schéma éléectronique sera Fritzing.

## e) Annexes

[[Schéma Fritzing]]


## f) Pourquoi cela nous intéresse-t-il ?

Nous aimerions dépasser l'aspect logiciel de la programmation et d'avoir un rendu concret et physique de notre travail.

# II) Cahier des charges

Nous utiliserons la programmation orientée objet afin de rendre le code plus clair.

Nous définirons les objets suivants : 

- `Voiture` :
    - `List moteurs : [moteur1, moteur2]`
    - `List onBuzz1_: [...Fonctions...]`
    - `List onBuzz2_: [...Fonctions...]`
    - `List onManetteConnecte_: [...Fonctions...]`
    - `List onManetteDeconnecte: [...Fonctions...]`
    - `Object lcd` (défini par un module)
    - `Object buzzer`:
        
        - `Function klaxonner(List intervalsInMs)`
    - `Object led`:
        - `Function allumer(Bool onOff)`
        - `Function flasher(Int intervalMs)`
    - `Function bouger(Int vitesseX, vitesseY)` (droite/gauche ; avancer/reculer)
    - `Function afficher(Str texte, Int hexCodeRGB)`
    - `Function onBuzz1()`


## Notations


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA0OTM5MTg2NCw0MDg4OTY4NjNdfQ==
-->