# TP-Jeu-de-la-vie
Ce TP a pour but de programmer le "Jeu de la vie" sur python. Nous allons représenter le jeu par une matrice composée de deux valeurs 0 et 1, où 0 désigne une cellule morte, et 1 désigne une cellule vivante.  

Dans un premier temps, nous allons considérer que ce jeu est joué sur une grille carrée, on ne se s'intéresse donc pas aux bords de la matrice. Nous allons commencer par créer des fonctions qui permettent d'appliquer les règles du jeu de la vie sur une matrice que nous allons proposer, avant de se servire de la fonction `imshow` de `matplotlib` pour afficher les résultats de ces fonctions. Ensuite, nous allons faire appel à la commande `animation.FuncAnimation` de `matplotlib` pour afficher un film qui représente les itérations du jeu de la vie quand on initialise avec des matrices que nous allons proposer.

Dans un deuxième temps, nous allons considérer que ce jeu est joué sur un tore, et donc les bords de la matrice seront prise en compte.
