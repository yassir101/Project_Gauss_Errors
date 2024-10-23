#!/usr/bin/env python
# coding: utf-8

# In[9]:


import struct
from decimal import Decimal, getcontext

# Définir la précision des calculs décimaux
getcontext().prec = 50

# Fonction pour convertir un flottant en sa représentation binaire IEEE 754
def float_to_bin(num):
    """ Convert a float to its binary representation according to IEEE 754. """
    return ''.join(f'{c:08b}' for c in struct.pack('!d', float(num)))  # Conversion en float pour struct


# Fonction pour effectuer les calculs et imprimer les résultats
def calculate(l_value, a_value, prod_value, li, lj, ai, aj):
    calculated_product = l_value * a_value
    print(f"Valeur décimale de L[{li}][{lj}]: {l_value:.21f}")
    print(f"Représentation binaire de L[{li}][{lj}]: {float_to_bin(l_value)} \n")
    print(f"Valeur décimale de A[{ai}][{aj}]: {a_value:.21f}")
    print(f"Représentation binaire de A[{ai}][{aj}]: {float_to_bin(a_value)} \n")
    print(f"Calcul exact de L[{li}][{lj}]*A[{ai}][{aj}] : {calculated_product:.21f}")
    print(f"Représentation binaire du calcul exact: {float_to_bin(calculated_product)} \n")
    print(f"Valeur décimale de L[{li}][{lj}]*A[{ai}][{aj}] avec gdb: {prod_value:.21f}")
    print(f"Représentation binaire de L[{li}][{lj}]*A[{ai}][{aj}] avec gdb: {float_to_bin(prod_value)} \n")
    print(f"__________________________________________________________________________________________________")
    return calculated_product

# Fonction pour calculer et imprimer les erreurs en format scientifique
def calculate_errors(calculated_product, prod_value, li, lj, ai, aj):
    err_abs = abs(prod_value - calculated_product)
    err_rel = err_abs / calculated_product if calculated_product != Decimal('0') else Decimal('inf')
    print(f"Erreur absolue de L[{li}][{lj}]*A[{ai}][{aj}]: {err_abs:.2e}")
    print(f"Erreur relative de L[{li}][{lj}]*A[{ai}][{aj}]: {err_rel:.2e}\n")
    print(f"__________________________________________________________________________________________________")

    
#i = 0
# Définition des variables au format Decimal pour une précision maximale
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

prod21 = Decimal('7.000000000000000000000')
prod22 = Decimal('4.899999999999999467093')
prod23 = Decimal('5.599999999999999644729')
prod24 = Decimal('4.899999999999999467093')

prod31 = Decimal('8.000000000000000000000')
prod32 = Decimal('5.600000000000000532907')
prod33 = Decimal('6.400000000000000355271')
prod34 = Decimal('5.600000000000000532907')

prod41 = Decimal('7.000000000000000000000')
prod42 = Decimal('4.899999999999999467093')
prod43 = Decimal('5.599999999999999644729')
prod44 = Decimal('4.899999999999999467093')

calculated_product_21 = calculate(l21, a11, prod21, 2, 1,1,1)
calculated_product_22 = calculate(l21, a21, prod22, 2, 1,1,2)
calculated_product_23 = calculate(l21, a31, prod23, 2, 1,1,3)
calculated_product_24 = calculate(l21, a41, prod24, 2, 1,1,4)

calculate_errors(calculated_product_21, prod21, 2, 1,1,1)
calculate_errors(calculated_product_22, prod22, 2, 1,1,2)
calculate_errors(calculated_product_23, prod23, 2, 1,1,3)
calculate_errors(calculated_product_24, prod24, 2, 1,1,4)

calculated_product_31 = calculate(l31, a11, prod31, 3, 1,1,1)
calculated_product_32 = calculate(l31, a21, prod32, 3, 1,1,2)
calculated_product_33 = calculate(l31, a31, prod33, 3, 1,1,3)
calculated_product_34 = calculate(l31, a41, prod34, 3, 1,1,4)

calculate_errors(calculated_product_31, prod31, 3, 1,1,1)
calculate_errors(calculated_product_32, prod32, 3, 1,1,2)
calculate_errors(calculated_product_33, prod33, 3, 1,1,3)
calculate_errors(calculated_product_34, prod34, 3, 1,1,4)

calculated_product_41 = calculate(l41, a11, prod41, 4, 1,1,1)
calculated_product_42 = calculate(l41, a21, prod42, 4, 1,1,2)
calculated_product_43 = calculate(l41, a31, prod43, 4, 1,1,3)
calculated_product_44 = calculate(l41, a41, prod44, 4, 1,1,4)

calculate_errors(calculated_product_41, prod41, 4, 1,1,1)
calculate_errors(calculated_product_42, prod42, 4, 1,1,2)
calculate_errors(calculated_product_43, prod43, 4, 1,1,3)
calculate_errors(calculated_product_44, prod44, 4, 1,1,4)

######################################################################
#i=1
#valeurs
a22 = Decimal('0.100000000000000532907')
a32 = Decimal('0.400000000000000355271')
a42 = Decimal('0.100000000000000532907')

l32 = Decimal('3.999999999999973354647')
l42 = Decimal('1.000000000000000000000')

a33 = Decimal('2.000000000000008881784')
a43 = Decimal('3.000000000000000000000')

l43 = Decimal('1.499999999999993338662')

prod32 = Decimal('0.399999999999999467093')
prod33 = Decimal('1.599999999999990762944')
prod34 = Decimal('0.399999999999999467093')

prod42 = Decimal('0.100000000000000532907')
prod43 = Decimal('0.400000000000000355271')
prod44 = Decimal('0.100000000000000532907')



calculated_product_32 = calculate(l32, a22, prod32, 3, 2,2,2)
calculated_product_33 = calculate(l32, a32, prod33, 3, 2,2,3)
calculated_product_34 = calculate(l32, a42, prod34, 3, 2,2,4)

calculate_errors(calculated_product_32, prod32, 3, 2,2,2)
calculate_errors(calculated_product_33, prod33, 3, 2,2,3)
calculate_errors(calculated_product_34, prod34, 3, 2,2,4)

calculated_product_42 = calculate(l42, a22, prod42, 4, 2,2,2)
calculated_product_43 = calculate(l42, a32, prod43, 4, 2,2,3)
calculated_product_44 = calculate(l42, a42, prod44, 4, 2,2,4)

calculate_errors(calculated_product_42, prod42, 4, 2,2,2)
calculate_errors(calculated_product_43, prod43, 4, 2,2,3)
calculate_errors(calculated_product_44, prod44, 4, 2,2,4)



##############################################################################
#i=2
#valeurs
a33 = Decimal('2.000000000000008881784')
a43 = Decimal('3.000000000000000000000')

l43 = Decimal('1.499999999999993338662')

prod43 = Decimal(' 3.000000000000000000000')
prod44 = Decimal(' 4.499999999999980460075')


calculated_product_43 = calculate(l43, a33, prod43, 4, 3,3,3)
calculated_product_44 = calculate(l43, a43, prod44, 4, 3,3,4)

calculate_errors(calculated_product_43, prod43, 4, 3,3,3)
calculate_errors(calculated_product_44, prod44, 4, 3,3,4)


# In[ ]:




