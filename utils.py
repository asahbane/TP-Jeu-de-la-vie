import numpy as np
import matplotlib.pylab as plt
from matplotlib import pyplot as plt
from matplotlib import animation

def calcul_nb_voisins(Z):
    forme = len(Z), len(Z[0])
    N  =[[0,]*(forme[0])for i in range(forme[1])]
    for x in range (1, forme[0] -1) :
        for y in range (1, forme[1] -1) :
            N[x][y] = Z[x-1][y-1] + Z[x][y-1]+Z[x+1][y-1] \
            +Z[x-1][y] + 0   +Z[x+1][y] \
            + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return  N

def iteration_jeu(Z):
    """
    Returns the next generation of the matrix Z following the rules of Conway's Game of Life.
    alive cells are represented with ones, while dead ones are represented with zeroes. Therfore, 
    Z has only zeros and ones.
    Args:
        Z : list of lists or 2d array (zeros and ones only). 
        
    returns:
        Z: list of lists or 2d array.

    Examples:
        >>> Z = [[0,0,0,0,0],
                 [0,0,0,1,0],
                 [0,1,0,1,0],
                 [0,0,1,1,0],
                 [0,0,0,0,0]]
                     
        >>> print(iteration_jeu(Z))
        >>> [[0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0],
             [0, 0, 0, 1, 0],
             [0, 0, 1, 1, 0],
             [0, 0, 0, 0, 0]]
         
    """
    forme  = len(Z),len(Z[0])
    N = calcul_nb_voisins(Z)
    for  x in range(1,forme[0]-1):
        for y in range(1,forme[1]-1):
            if Z[x][y]   ==  1  and (N[x][y]< 2 or N[x][y] > 3):
                Z[x][y] = 0 
            elif Z[x][y] == 0 and N[x][y] == 3 : 
                Z[x][y] = 1 
    return Z

## fonction d'affichage de 10 premières itérations 
## quand on initialise avec la matrice M
def mat_show(M):
    #création de la figure 
    fig=plt.figure(figsize=(10, 10))
    for i in range (10):
        fig.add_subplot(2, 5, i+1)
        plt.axis('off')
        plt.title('Itération '+ str(i))
        plt.imshow(M, origin = 'upper', interpolation="nearest")
        M = iteration_jeu(M)
    plt.show()  
    
