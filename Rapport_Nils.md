*La lecture est aussi possible depuis le répertoire GitHub suivant : [https://github.com/clota974/NOK-Rover](https://github.com/clota974/NOK-Rover)*

# Rapport - NOK-Rover

*En route vers 127.0.0.1 à bord du NOK-Rover piloté par les capitaines Nils, Olivia et Killian.*

---
**rover**  [\ʁɔ.vœʁ\] _masculin_
1.  _(Astronautique)_  Robot  mobile conçu pour se déplacer effectuer des prélèvements, analyses ou photographies à la  surface d’astres éloignés de la Terre et du système solaire.
---


# I) Introduction

## a) Objectif du projet :
    
Notre projet a pour objectif le pilotage d'un mini Rover piloté par un Raspberry Pi
  

## b) Pourquoi ce projet nous intéresse-t-il ?

  

Suite au mini-projet, durant lequel nous avons programmé avec une interface CLI. Nous souhaitions réaliser un projet qui était en interaction avec le réel. Pouvoir toucher notre projet de nos propres mains. De plus, mettre en oeuvre un tel projet nous a permis de “tester” nos capacités dans un domaine de découverte.
  

# II) Cahier des charges

## Mapping des touches

| **Touche** |**Action**  |
|--|--|
| Croix | Klaxon |
| Carré | LED |
| Gâchette R2 | Avancer |
| Gâchette L2 | Reculer |
| Joystick gauche (Axe X) | Lacet |
| Flèche Haut | Vitesse supérieure |
| Flèche Bas | Vitesse inférieure |
| Flèche Gauche | Diminuer le contraste |
| Flèche Droite | Augmenter le contraste |
| Options | Test LED |
| Share | Arrêter le programme |

## Terminologie

 - Le moteur supporte 3 multiples de vitesse différents. Ces multiples sont appelés **Gear**, soit le terme anglais pour parler des différentes vitesses dans les voitures
 - Le **lacet** désigne l'axe selon lequel la voiture pivote
 - L'anglicisme **PWM** pourra être utilisé pour désigner la modulation de largeur d'impulsions (MLI)
 - L'anglicisme **Duty Cycle** se rapporte au rapport cyclique de la modulation de largeur d'impulsions
 - Le terme `pin` pourra être utilisé afin de désigner les GPIO

## Conventions

Les pourcentages se basent sur des nombres supérieurs à 0. 
L'utilisation des pourcentages en tant que tel a été fixé en accord avec les notations de la fréquence de `RPi.GPIO.PWM` . 

## Matériel utilisé
Voici la liste du matériel utilisé par le NOK-Rover : [https://www.sparkfun.com/orders/4429576](https://www.sparkfun.com/orders/4429576)
Bien que tous les éléments commandés furent destinés au NOK-Rover, certains n'ont pas été utilisé.

## Logiciels utilisés

Le code sera stocké sur GitHub au répertoire suivant : [https://github.com/clota974/NOK-Rover](https://github.com/clota974/NOK-Rover)

# III) Réalisation

Le programme est séparé en de nombreuses classes, chacune définissant une partie de la voiture. Par exemple, la classe LED détermine l’allumage de celles-ci.


## Interaction avec la manette et interface HID
La manette utilisée est une Dualshock 4 *(manette de PS4)* via Bluetooth.
L'interface utilisée est une interface HID. La communication des données se fait en hexadécimal (sur 2 octets généralement). Afin de récupérer les données HID, nous utilisons le programme `ds4drv`.
  

Le processus du NOK-Rover se divise en ces classes suivantes :

## Classe Moteur

Une même classe pour les 2 moteurs qui permettra d'actionner les moteurs.

Elle programme leur sens ainsi que leur vitesse.

La méthode de modulation de largeur d'impulsions (PWM en anglais) sera utilisée. Nous avons défini la fréquence à 980 Hz, ce qui se réfère à la fréquence des pins PWM des cartes Arduino Uno.


*Nota Bene* : La coordination entre les deux moteurs sera gérée par la Classe Voiture

## Classe Buzzer

Cette classe permettra de "klaxonner" en maintenant une touche sur la manette.
La méthode de modulation de largeur d'impulsions est utilisée à une fréquence de 2048 Hz, soit la fréquence donnée sur la feuille de renseignement du Buzzer Piezo.

## Classe LED

La méthode de modulation de largeur d'impulsions est utilisée à une fréquence basse de 1 Hz afin de pouvoir faire clignoter la LED aisément.

La méthode principale de cette classe est `start(clignotement)` qui va définir le rapport cyclique, soit le clignotement de la LED.

La fonction `inverse()` permet d'allumer la LED si elle est éteinte, et inversement.

## L’écran LCD

La bibliothèque `Adafruit_CharLCD` d’Adafruit est utilisée afin d'interagir avec l’écran LCD (Mode 4 bits).

L’écran LCD affiche les informations suivantes :

-   `V` : Gear de 1 à 3
    
-   `L` : LED, 1 ou 0
    
-   `C` : Pourcentage de tension du contraste de l’écran. ⚠ Plus la tension est haute, plus le pourcentage est haut, moins les caractères seront visibles
    
-   `D` et `G` : Rapport cyclique (Duty Cycle) des pins PWM des moteurs. Par convention, si la valeur est négative, le moteur tourne dans le sens inverse.
    
![enter image description here](https://lh3.googleusercontent.com/NfXo9AKnpuvXgd7b3c7qwrL6dTxU54VgG4cNZWtnFlE2v_cR0GxetnJLnsKZYFsOMq-Gx0kDWkVW "LCD")

## Classe Event

La classe `Event` est invoquée à chaque fois que des données sont reçues par le Main.

La classe `Event` se charge d’analyser les données, et de les classer.

Nous pouvons noter la méthode `base16_vers_pourcent` qui permet de convertir les données HID hexadécimales en pourcentage. Un des défis qui se posait portait sur le boutisme c'est-à-dire l'ordre des octets lors de la conversion. En effet, alors que les données étaient représentées sous forme petit-boutiste dans l'interface HID, l'ordre des données étaient en réalité grand-boutiste.
Afin d'achever cette conversion de boutisme, le code suivant a été instauré : 
```py
valeur = (bit2<<2*4)+bit1 # Arrange les bits selon l'ordre correct (Petit-boutiste --> Grand-boutiste)
        
 if valeur & 0x8000 > 0: # Si la valeur est négative
     valeur -= 0x10000

 max16 = 0x7FFF

 pourcentage = valeur/max16*100

 return int(pourcentage)
```


Deux propriétés importantes se distinguent de la classe :

- `data` qui correspond aux valeurs réelles des capteurs de la manette. 
- `changement` qui correspond aux changements de valeur par rapport au précédent *Event*
  

## Classe Voiture

La classe Voiture a pour propriétés les objets des classes précédentes. 

### Coordination des moteurs
La classe Voiture a pour objectif la coordination avec la méthode `bouger(vitesse, lacet)`.

```py
default = 5 if vitesse>0 else -5
if(lacet != 0): # Tourner à droite
    vD = (50+lacet/2)/100*vitesse or default
    vG = (50-lacet/2)/100*vitesse or default
else:
    vD = vG = vitesse# IV) Planification
```
La vitesse du moteur est donc défini par la formule `(50±lacet/2)/100*vitesse`. 
La vitesse ne peut être nulle, sa valeur par défaut est 5. Ceci permet d'empêcher le blocage des roues, lors du pivot.
  

# Répartition du travail 

La répartition des tâches prévue au début du projet était la suivante :
- Killian devait s'occuper du traitement des données de la manette et donc de la classe `Event`. De plus, il s'occupait de donner les tâches à éxécuter par Nils via la partie "Projets" de GitHub.
- Nils devait s'occuper de la création des classes qui intéragissent directement avec les GPIO.

Olivia est arrivée en cours de projet et donc n'a pas pu participer à toute la programmation. 

L'organisation et la répartition des tâches furent modifiées au cours des séances.
Killian a réalisé la majeure partie du code, mais aussi du traitement des données de la manette.
Nils et Olivia, quant à eux, ont réalisé une partie de la programmation ainsi que les diaporamas d'explications.

Nous avons tous participé à la rédaction du rapport

# V) Réalisation

Les pièces de la voiture nous ont été livrées mi-janvier, l’assemblage de la voiture fut également réalisé en janvier par Killian. Le code quant à lui, fut réalisé en 18 semaines, du 30 janvier jusqu’au 20 mai. Avec une fréquence de travail de l’ordre d’une fois par semaine, le projet...
  

# VI) Fonctionnement

  
  

# VII) Amélioration

  
  

# VIII) Conclusion

  
  
  
  

Bilan personnel Nils:

  
  

Bilan personnel Olivia:

  
  

Bilan personnel Killian:
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExODc0MzI2NjBdfQ==
-->