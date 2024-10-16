import struct
from decimal import Decimal, getcontext

# Définir la précision des calculs décimaux
getcontext().prec = 50

# Fonction pour convertir un flottant en sa représentation binaire IEEE 754
def float_to_bin(num):
    """ Convert a float to its binary representation according to IEEE 754. """
    return ''.join(f'{c:08b}' for c in struct.pack('!d', float(num)))  # Conversion en float pour struct

# Fonction pour réaliser des calculs et imprimer les résultats
def calculate(bj_value, l_value, bi_value, diff_value, i, j):
    prod_value = l_value*bi_value
    calculated_diff = bj_value - prod_value
    print(f"Valeur décimale de b_av = B[{j}]: {bj_value:.21f}")
    print(f"Représentation binaire de b_av = B[{j}]: {float_to_bin(bj_value)}")
    print(f"Valeur décimale de L[{j}][{i}]: {l_value:.21f}")
    print(f"Représentation binaire de L[{j}][{i}]: {float_to_bin(l_value)}")
    print(f"Valeur décimale de B[{i}]: {bi_value:.21f}")
    print(f"Représentation binaire de B[{i}]: {float_to_bin(bi_value)}")
    print(f"Valeur décimale de L[{j}][{i}]*B[{i}]: {l_value:.21f}")
    print(f"Représentation binaire de L[{j}][{i}]*B[{i}]: {float_to_bin(l_value)}")
    print(f"Valeur décimale de B[{j}] - L[{j}][{i}]*B[{i}] avec gdb: {diff_value:.21f}")
    print(f"Représentation binaire de B[{j}] - L[{j}][{i}]*B[{i}] avec gdb: {float_to_bin(diff_value)}")
    print("__________________________________________________________________________________________________")
    return calculated_diff

# Fonction pour calculer et imprimer les erreurs
def calculate_errors(calculated_diff, diff_value, i, j):
    err_abs = abs(diff_value - calculated_diff)
    err_rel = err_abs / abs(calculated_diff) if calculated_diff != Decimal('0') else Decimal('inf')
    print(f"Erreur absolue de B[{j}] - L[{j}][{i}]*B[{i}]: {err_abs:.2e}")
    print(f"Erreur relative de B[{j}] - L[{j}][{i}]*B[{i}]: {err_rel:.2e}")
    print("__________________________________________________________________________________________________\n")
    
    
#valeurs
#i=1
bav1 = Decimal('32.000000000000000000000')

bav2 = Decimal('23.000000000000000000000')
bav3 = Decimal('33.000000000000000000000')
bav4 = Decimal('31.000000000000000000000')


l21 = Decimal('0.699999999999999955591')
l31 = Decimal('0.800000000000000044409')
l41 = Decimal('0.699999999999999955591')

l32 = Decimal('3.999999999999973354647')
l42 = Decimal('1.000000000000000000000')

l43 = Decimal('1.499999999999993338662')

res2 = Decimal('0.600000000000001421085')
res3 = Decimal('7.399999999999998578915')
res4 = Decimal('8.600000000000001421085')


calculated_diff_2 = calculate(bav2, l21, bav1, res2, 1,2)
calculated_diff_3 = calculate(bav3, l31, bav1, res3, 1,3)
calculated_diff_4 = calculate(bav4, l41, bav1, res4, 1,4)

calculate_errors(calculated_diff_2, res2, 1,2)
calculate_errors(calculated_diff_3, res3, 1,3)
calculate_errors(calculated_diff_4, res4, 1,4)


#valeurs
#i=2
bav2 = Decimal('0.600000000000001421085')

bav3 = Decimal('7.399999999999998578915')
bav4 = Decimal('8.600000000000001421085')

l32 = Decimal('3.999999999999973354647')
l42 = Decimal('1.000000000000000000000')

l43 = Decimal('1.499999999999993338662')

res3 = Decimal('5.000000000000008881784')
res4 = Decimal('8.000000000000000000000')

calculated_diff_3 = calculate(bav3, l32, bav2, res3, 2,3)
calculated_diff_4 = calculate(bav4, l42, bav2, res4,2,4)

calculate_errors(calculated_diff_3, res3, 2,3)
calculate_errors(calculated_diff_4, res4, 2,4)

#valeurs
#i=3
bav3 = Decimal('5.000000000000008881784')

bav4 = Decimal('8.000000000000000000000')

l43 = Decimal('1.499999999999993338662')

res4 = Decimal('0.500000000000020428104')

calculated_diff_4 = calculate(bav4, l43, bav3, res4,3,4)

calculate_errors(calculated_diff_4, res4, 3,4)
