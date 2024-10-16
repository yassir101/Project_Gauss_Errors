import struct
from decimal import Decimal, getcontext

# Définir la précision des calculs décimaux
getcontext().prec = 50

# Fonction pour convertir un flottant en sa représentation binaire IEEE 754
def float_to_bin(num):
    """ Convert a float to its binary representation according to IEEE 754. """
    return ''.join(f'{c:08b}' for c in struct.pack('!d', float(num)))  # Conversion en float pour struct

# Fonction pour effectuer les calculs et imprimer les résultats
def calculate(b_value, somme, a_value,x_value, i):
    calculated_x = (b_value - somme)/a_value
    print(f"Valeur décimale de A[{i}][{i}]: {a_value:.21f}")
    print(f"Représentation binaire de A[{i}][{i}]: {float_to_bin(a_value)} \n")
    print(f"Valeur décimale de B[{i}]: {b_value:.21f}")
    print(f"Représentation binaire de B[{i}]: {float_to_bin(b_value)} \n")
    print(f"Calcul exact de (B[{i}] - somme) / A[{i}][{i}] : {calculated_x:.21f}")
    print(f"Représentation binaire du calcul exact: {float_to_bin(calculated_x)} \n")
    print(f"Valeur décimale de (B[{i}] - somme) / A[{i}][{i}] avec gdb: {x_value:.21f}")
    print(f"Représentation binaire de (B[{i}] - somme) / A[{i}][{i}] avec gdb: {float_to_bin(x_value)} \n")
    print(f"__________________________________________________________________________________________________")
    return calculated_x

# Fonction pour calculer et imprimer les erreurs en format scientifique
def calculate_errors(calculated_x, x_value, i):
    err_abs = abs(x_value - calculated_x)
    err_rel = err_abs / calculated_x if calculated_x != Decimal('0') else Decimal('inf')
    print(f"Erreur absolue de (B[{i}] - somme) / A[{i}][{i}]: {err_abs:.2e}")
    print(f"Erreur relative de (B[{i}] - somme) / A[{i}][{i}]: {err_rel:.2e}\n")
    print(f"__________________________________________________________________________________________________")
    
    
#valeurs
a44 = Decimal('0.500000000000019539925')
a33 = Decimal('2.000000000000008881784')
a22 = Decimal('0.100000000000000532907')
a11 = Decimal('10.000000000000000000000')

b4 = Decimal('0.500000000000020428104')
b3 = Decimal('5.000000000000008881784')
b2 = Decimal('0.600000000000001421085')
b1 = Decimal('32.000000000000000000000')

somme4 = Decimal('0.000000000000000000000')
somme3 = Decimal('3.000000000000005329071')
somme2 = Decimal('0.500000000000000000000')
somme1 = Decimal('22.000000000000053290705')

x4 = Decimal('1.000000000000001776357')
x3 = Decimal('0.999999999999997335465')
x2 = Decimal('1.000000000000008881784')
x1 = Decimal('0.999999999999994670929')

calculated_x_4 = calculate(b4, somme4, a44, x4, 4)
calculated_x_3 = calculate(b3, somme3, a33, x3, 3)
calculated_x_2 = calculate(b2, somme2, a22, x2, 2)
calculated_x_1 = calculate(b1, somme1, a11, x1, 1)

calculate_errors(calculated_x_4, x4, 4)
calculate_errors(calculated_x_3, x3, 3)
calculate_errors(calculated_x_2, x2, 2)
calculate_errors(calculated_x_1, x1, 1)
