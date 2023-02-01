#%% Import des bibliothèques

import matplotlib.pyplot as plt
import numpy as np

#%% Assignation des variables
image_lena = plt.imread( '../images/hand.JPG') # Emplacement de l'image

#%% Traçage de l'image
plt.imshow(image_lena) # Permet d'afficher l'image
plt.show()