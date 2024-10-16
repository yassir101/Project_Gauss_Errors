Dans le dossier, vous trouverez les dossiers suivants:

-Le rapport écrit en Latex nommé Projet_MMSN_Erreurs_Gauss.

-Le dossier codeGauss contenant le fichier gaussCode.c qui est le code utilisé tout le long du projet, qui correspond à l'implémentation de la méthode de Gauss en double precision.

-Le dossier Resultats: Le dossier Resultats contient lui même différents dossiers:

	.Verif_donnees : Vous retrouverez la verification de l'affection des valeurs de A[i][j] et b[i] en gdb, avec différentes captures d'écran notées Aij_donnees_gdb ou bi_donnees_gdb. Vous retrouverez aussi les fichiers se terminant par _command qui correspondent à la commande utilisée sur gdb pour l'affichage.

	.Triangularisation : Dans ce dossier, vous retrouverez toutes les opérations élémentaires liées à la phase de triangularisation, soit le fichier aji_aii_div (la division aji/aii), le fichier ajk_LjiAik_diff (qui correspond à ajk - Lji * Aik) et enfin lji_aik_mult (qui correspond à lji * aik). Dans chacun de ces fichiers, vous retrouverez le code Python/Sage utilisé pour les calculs, ainsi que la commande GDB (même nom que le fichier mère seulement avec _command à la fin), mais surtout vous retrouverez des sous dossiers permettant de séparer les valeurs selon les valeurs de i=1..3, et dans chacun de ces fichiers vous retrouverez un fichier _codage (session GDB), _calcul (calcul exact avec Python/Sage), _erreurs (calcul des erreurs absolues et relatives).

	.Descente : Dans ce dossier vous retrouverez l'opération élémentaire liée à la modification du second membre. Il contient un dossier bj_LjiBi_diff (soit l'opération bj - Lji * Bi), dans ce dossier vous retrouverez le code Python/Sage utilisé pour les calculs, ainsi que la commande GDB (même nom que le fichier mère seulement avec _command à la fin), mais surtout vous retrouverez des sous dossiers permettant de séparer les valeurs selon les valeurs de i=1..3, et dans chacun de ces fichiers vous retrouverez un fichier _codage (session GDB), _calcul (calcul exact avec Python/Sage), _erreurs (calcul des erreurs absolues et relatives).

	.Remontée : Dans ce dossier, vous retrouverez les opérations élémentaires liées au calcul de X[i], il y a donc un sous fichier aij_xj_mult (correspondant à l'opération aij * xj) et le sous fichier calcul_xi qui correspond au calcul de xi selon la formule du cours.
Dans ces dossiers vous retrouverez le code Python/Sage utilisé pour les calculs, ainsi que la commande GDB (même nom que le fichier mère seulement avec _command à la fin), mais surtout vous retrouverez des sous dossiers permettant de séparer les valeurs selon les valeurs de i=1..3, et dans chacun de ces fichiers vous retrouverez un fichier _codage (session GDB), _calcul (calcul exact avec Python/Sage), _erreurs (calcul des erreurs absolues et relatives).

___________________________________________________________________________________________

Tout les résultats ont été obtenus avec l'ordinateur qui a les propriétés suivantes:

Modèle	HP Laptop 15-dw2xxx	
Type	PC à base de x64		
Processeur	Intel(R) Core(TM) i7-1065G7 CPU @ 1.30GHz, 1498 MHz, 4 cœur(s), 8 processeur(s) logique(s)
Fabricant de la carte de base	HP	
Produit de la carte de base	85F4	
Version de la carte de base	40.19	

Mémoire physique (RAM) installée	16,0 Go	
Mémoire physique totale	15,8 Go		
Mémoire virtuelle totale	19,0 Go	

Capacité du disque	475.23 Go
SO : Windows 10
Interface de programmation :
- C : VSCode
- Python : Jupyter Notebook
- SageMath : Cocalc
	