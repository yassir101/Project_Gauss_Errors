import struct
from decimal import Decimal, getcontext

# Définir la précision des calculs décimaux
getcontext().prec = 50

# Fonction pour convertir un nombre flottant en sa représentation binaire IEEE 754
def float_to_bin(num):
    """ Convertir un flottant en représentation binaire selon IEEE 754. """
    return ''.join(f'{c:08b}' for c in struct.pack('!d', float(num)))  # Assurez-vous que num est un float

# Fonction simplifiée pour les calculs des produits
def calculprod(l_value, a_value):
    calculated_product = l_value * a_value
    return calculated_product

# Fonction pour réaliser des calculs et imprimer les résultats
def calculate(a_value, prod_value, diff_value, i, j, k):
    calculated_diff = a_value - prod_value
    print(f"Valeur décimale de A[{j}][{k}]: {a_value:.21f}")
    print(f"Représentation binaire de A[{j}][{k}]: {float_to_bin(a_value)}")
    print(f"Valeur décimale de A[{j}][{k}] - L[{j}][{i}]*A[{i}][{k}] avec gdb: {diff_value:.21f}")
    print(f"Représentation binaire de A[{j}][{k}] - L[{j}][{i}]*A[{i}][{k}] avec gdb: {float_to_bin(diff_value)}")
    print("__________________________________________________________________________________________________")
    return calculated_diff

# Fonction pour calculer et imprimer les erreurs
def calculate_errors(calculated_diff, diff_value, i, j, k):
    err_abs = abs(diff_value - calculated_diff)
    err_rel = err_abs / abs(calculated_diff) if calculated_diff != Decimal('0') else Decimal('inf')
    print(f"Erreur absolue de A[{j}][{k}] - L[{j}][{i}]*A[{i}][{k}]: {err_abs:.2e}")
    print(f"Erreur relative de A[{j}][{k}] - L[{j}][{i}]*A[{i}][{k}]: {err_rel:.2e}")
    print("__________________________________________________________________________________________________\n")


########################################################################################################################  
#i=1
# valeurs initialisation
a11 = Decimal('10.00000000000000000000')
a21 = Decimal('7.000000000000000000000')
a31 = Decimal('8.000000000000000000000')
a41 = Decimal('7.000000000000000000000')

l21 = Decimal('0.699999999999999955591')
l31 = Decimal('0.800000000000000044409')
l41 = Decimal('0.699999999999999955591')

a22 = Decimal('0.100000000000000532907')
a32 = Decimal('0.399999999999999467093')
a42 = Decimal('0.100000000000000532907')

l32 = Decimal('3.999999999999973354647')
l42 = Decimal('1.000000000000000000000')

a33 = Decimal('2.000000000000008881784')
a43 = Decimal('3.000000000000000000000')

l43 = Decimal('1.499999999999993338662')

calculated_product_22 = calculprod(l21, a21)
calculated_product_23 = calculprod(l21, a31)
calculated_product_24 = calculprod(l21, a41)

calculated_product_31 = calculprod(l31, a11)
calculated_product_32 = calculprod(l31, a21)
calculated_product_33 = calculprod(l31, a31)
calculated_product_34 = calculprod(l31, a41)

calculated_product_41 = calculprod(l41, a11)
calculated_product_42 = calculprod(l41, a21)
calculated_product_43 = calculprod(l41, a31)
calculated_product_44 = calculprod(l41, a41)

#valeurs pour execution
prod21 = calculated_product_21
prod22 = calculated_product_22
prod23 = calculated_product_23
prod24 = calculated_product_24

prod31 = calculated_product_31
prod32 = calculated_product_32
prod33 = calculated_product_33
prod34 = calculated_product_34

prod41 = calculated_product_41
prod42 = calculated_product_42
prod43 = calculated_product_43
prod44 = calculated_product_44

# Variables pour la matrice A
a21 = Decimal('7.000000000000000000000')
a22 = Decimal('5.000000000000000000000')
a23 = Decimal('6.000000000000000000000')
a24 = Decimal('5.000000000000000000000')

a31 = Decimal('8.000000000000000000000')
a32 = Decimal('6.000000000000000000000')
a33 = Decimal('10.000000000000000000000')
a34 = Decimal('9.000000000000000000000')

a41 = Decimal('7.000000000000000000000')
a42 = Decimal('5.000000000000000000000')
a43 = Decimal('9.000000000000000000000')
a44 = Decimal('10.000000000000000000000')

# Variables pour les résultats attendus
res21 = Decimal('0.000000000000000000000')
res22 = Decimal('0.100000000000000532907')
res23 = Decimal('0.400000000000000355271')
res24 = Decimal('0.100000000000000532907')

res31 = Decimal('0.000000000000000000000')
res32 = Decimal('0.399999999999999467093')
res33 = Decimal('3.599999999999999644729')
res34 = Decimal('3.399999999999999467093')

res41 = Decimal('0.000000000000000000000')
res42 = Decimal('0.100000000000000532907')
res43 = Decimal('3.400000000000000355271')
res44 = Decimal('5.100000000000000532907')
    
# Exécution des calculs pour différentes valeurs de A, produit et résultat (les noms des variables doivent correspondre à ceux définis)
calculated_diff_21 = calculate(a21, prod21, res21, 1,2,1)
calculated_diff_22 = calculate(a22, prod22, res22, 1,2,2)
calculated_diff_23 = calculate(a23, prod23, res23, 1,2,3)
calculated_diff_24 = calculate(a24, prod24, res24, 1,2,4)

calculate_errors(calculated_diff_21, res21, 1,2,1)
calculate_errors(calculated_diff_22, res22, 1,2,2)
calculate_errors(calculated_diff_23, res23, 1,2,3)
calculate_errors(calculated_diff_24, res24, 1,2,4)

calculated_diff_31 = calculate(a31, prod31, res31, 1,3,1)
calculated_diff_32 = calculate(a32, prod32, res32, 1,3,2)
calculated_diff_33 = calculate(a33, prod33, res33, 1,3,3)
calculated_diff_34 = calculate(a34, prod34, res34, 1,3,4)

calculate_errors(calculated_diff_31, res31, 1,3,1)
calculate_errors(calculated_diff_32, res32, 1,3,2)
calculate_errors(calculated_diff_33, res33, 1,3,3)
calculate_errors(calculated_diff_34, res34, 1,3,4)

calculated_diff_41 = calculate(a41, prod41, res41, 1,4,1)
calculated_diff_42 = calculate(a42, prod42, res42, 1,4,2)
calculated_diff_43 = calculate(a43, prod43, res43, 1,4,3)
calculated_diff_44 = calculate(a44, prod44, res44, 1,4,4)

calculate_errors(calculated_diff_41, res41, 1,4,1)
calculate_errors(calculated_diff_42, res42, 1,4,2)
calculate_errors(calculated_diff_43, res43, 1,4,3)
calculate_errors(calculated_diff_44, res44, 1,4,4)


########################################################################################################################  
#i=2
# valeurs initialisation
a22 = Decimal('0.100000000000000532907')
a32 = Decimal('0.400000000000000355271')
a42 = Decimal('0.100000000000000532907')

l32 = Decimal('3.999999999999973354647')
l42 = Decimal('1.000000000000000000000')

a33 = Decimal('2.000000000000008881784')
a43 = Decimal('3.000000000000000000000')

l43 = Decimal('1.499999999999993338662')

calculated_product_32 = calculprod(l32, a22)
calculated_product_33 = calculprod(l32, a32)
calculated_product_34 = calculprod(l32, a42)

calculated_product_42 = calculprod(l42, a22)
calculated_product_43 = calculprod(l42, a32)
calculated_product_44 = calculprod(l42, a42)

prod32 = calculated_product_32
prod33 = calculated_product_33
prod34 = calculated_product_34

prod42 = calculated_product_42
prod43 = calculated_product_43
prod44 = calculated_product_44

# Variables pour les résultats attendus
a32 = Decimal('0.399999999999999467093')
a33 = Decimal('3.599999999999999644729')
a34 = Decimal('3.399999999999999467093')

a42 = Decimal('0.100000000000000532907')
a43 = Decimal('3.400000000000000355271')
a44 = Decimal('5.100000000000000532907')

res32 = Decimal('0.000000000000000000000')
res33 = Decimal('2.000000000000008881784')
res34 = Decimal('3.000000000000000000000')

res42 = Decimal('0.000000000000000000000')
res43 = Decimal('3.000000000000000000000')
res44 = Decimal('5.000000000000000000000')
    
# Exécution des calculs pour différentes valeurs de A, produit et résultat (les noms des variables doivent correspondre à ceux définis)
calculated_diff_32 = calculate(a32, prod32, res32, 2,3,2)
calculated_diff_33 = calculate(a33, prod33, res33, 2,3,3)
calculated_diff_34 = calculate(a34, prod34, res34, 2,3,4)

calculate_errors(calculated_diff_32, res32, 2,3,2)
calculate_errors(calculated_diff_33, res33, 2,3,3)
calculate_errors(calculated_diff_34, res34, 2,3,4)

calculated_diff_42 = calculate(a42, prod42, res42, 2,4,2)
calculated_diff_43 = calculate(a43, prod43, res43, 2,4,3)
calculated_diff_44 = calculate(a44, prod44, res44, 2,4,4)

calculate_errors(calculated_diff_42, res42, 2,4,2)
calculate_errors(calculated_diff_43, res43, 2,4,3)
calculate_errors(calculated_diff_44, res44, 2,4,4)

########################################################################################################################  
#i=3
# valeurs initialisation
a33 = Decimal('2.000000000000008881784')
a43 = Decimal('3.000000000000000000000')

l43 = Decimal('1.499999999999993338662')

prod43 = Decimal(' 3.000000000000000000000')
prod44 = Decimal(' 4.499999999999980460075')

calculated_product_43 = calculprod(l43, a33)
calculated_product_44 = calculprod(l43, a43)

prod43 = calculated_product_43
prod44 = calculated_product_44

# Variables pour les résultats attendus
a43 = Decimal('3.000000000000000000000')
a44 = Decimal('5.000000000000000000000')

res43 = Decimal('0.000000000000000000000')
res44 = Decimal('0.500000000000019539925')
    
# Exécution des calculs pour différentes valeurs de A, produit et résultat (les noms des variables doivent correspondre à ceux définis)
calculated_diff_43 = calculate(a43, prod43, res43, 3,4,3)
calculated_diff_44 = calculate(a44, prod44, res44, 3,4,4)

calculate_errors(calculated_diff_43, res43, 3,4,3)
calculate_errors(calculated_diff_44, res44, 3,4,4)
