from trajet import *
import re

#Jeux de test
assert distanceRestante(100,600) == 500
assert vitesseMoyenne ( 150 , 1.2 )   == 125
assert vitesseMoyenne ( 30 , 0.5 )   == 60
assert tempsRestant ( 150 , 80 )  == 1.875
assert round(tempsRestant ( 20 , 110 ), 4)  == 0.1818
assert round(coutTrajet (22 , 5.6 , 1.41 ), 5)  == 1.73712
assert round(coutTrajet ( 545 , 8.2 , 1.53 ), 4)  == 68.3757
assert afficheTemps  ( 1.5 )  == "1 heure⋅s 30"
assert afficheTemps ( 5.2 ) == "5 heure⋅s 12"

print(vehiculeParser())