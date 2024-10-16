import struct
from decimal import Decimal, getcontext

# Définir la précision des calculs décimaux
getcontext().prec = 50

# Fonction pour convertir un flottant en sa représentation binaire IEEE 754
def float_to_bin(num):
    """ Convert a float to its binary representation according to IEEE 754. """
    return ''.join(f'{c:08b}' for c in struct.pack('!d', float(num)))  # Conversion en float pour struct

# Fonction pour effectuer les calculs et imprimer les résultats
def calculate(a_value, x_value, prod_value, i,j):
    calculated_product = a_value * x_value
    print(f"Valeur décimale de A[{i}][{j}]: {a_value:.21f}")
    print(f"Représentation binaire de A[{i}][{j}]: {float_to_bin(a_value)} \n")
    print(f"Valeur décimale de X[{j}]: {x_value:.21f}")
    print(f"Représentation binaire de X[{j}]: {float_to_bin(x_value)} \n")
    print(f"Calcul exact de A[{i}][{j}]*X[{j}] : {calculated_product:.21f}")
    print(f"Représentation binaire du calcul exact: {float_to_bin(calculated_product)} \n")
    print(f"Valeur décimale de A[{i}][{j}]*X[{j}] avec gdb: {prod_value:.21f}")
    print(f"Représentation binaire de A[{i}][{j}]*X[{j}] avec gdb: {float_to_bin(prod_value)} \n")
    print(f"__________________________________________________________________________________________________")
    return calculated_product

# Fonction pour calculer et imprimer les erreurs en format scientifique
def calculate_errors(calculated_product, prod_value, i,j):
    err_abs = abs(prod_value - calculated_product)
    err_rel = err_abs / calculated_product if calculated_product != Decimal('0') else Decimal('inf')
    print(f"Erreur absolue de A[{i}][{j}]*X[{j}]: {err_abs:.2e}")
    print(f"Erreur relative de A[{i}][{j}]*X[{j}]: {err_rel:.2e}\n")
    print(f"__________________________________________________________________________________________________")
    

#i=3
#valeurs
x4 = Decimal('1.000000000000001776357')

a34 = Decimal('3.000000000000000000000')

prod4 = Decimal('3.000000000000005329071')

calculated_product_4 = calculate(a34, x4, prod4, 3,4)

calculate_errors(calculated_product_4, prod4, 3,4)


#i=2
#valeurs
x3 = Decimal('0.999999999999997335465')
a23 = Decimal('0.400000000000000355271')
prod3 = Decimal('0.399999999999999300559')

x4 = Decimal('1.000000000000001776357')
a24 = Decimal('0.100000000000000532907')
prod4 = Decimal('0.100000000000000713318')

calculated_product_3 = calculate(a23, x3, prod3, 2,3)

calculated_product_4 = calculate(a24, x4, prod4, 2,4)
calculate_errors(calculated_product_3, prod3, 2,3)


calculate_errors(calculated_product_4, prod4, 2 ,4)


#i=3
#valeurs
x2 = Decimal('1.000000000000008881784')
a12 = Decimal('7.000000000000000000000')
prod2 = Decimal('7.000000000000062172489')

x3 = Decimal('0.999999999999997335465')
a13 = Decimal('8.000000000000000000000')
prod3 = Decimal('7.999999999999978683718')

x4 = Decimal('1.000000000000001776357')
a14 = Decimal('7.000000000000000000000')
prod4 = Decimal('7.000000000000012434498')

calculated_product_2 = calculate(a12, x2, prod2, 1,2)
calculated_product_3 = calculate(a13, x3, prod3, 1,3)
calculated_product_4 = calculate(a14, x4, prod4, 1,4)

calculate_errors(calculated_product_2, prod2, 1,2)


calculate_errors(calculated_product_3, prod3, 1,3)


calculate_errors(calculated_product_4, prod4, 1,4)
