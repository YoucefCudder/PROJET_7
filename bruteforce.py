#!/usr/bin/python3
# coding: utf8
# enumerer toutes les combinaisons possibles
# trier les combinaisons possibles par rapport au maximum

# choisir la  meilleure combinaison

import csv
from itertools import combinations


# Solution force brute - Recherche de toutes les solutions
def sac_a_dos_force_brute(elements, capacite, elements_selection=None):
    if elements_selection is None:
        elements_selection = []
    if elements:
        val1, lst_val1 = sac_a_dos_force_brute(capacite, elements[1:], elements_selection)
        val = elements[0]
        if val[1] <= capacite:
            val2, lst_val2 = sac_a_dos_force_brute(capacite - val[1], elements[1:], elements_selection + [val])
            if val1 < val2:
                return val2, lst_val2

        return val1, lst_val1
    else:
        return sum([i[2] for i in elements_selection]), elements_selection


def read_shares():
    with open('test_shares.csv') as csv_file:
        shares_file = csv.reader(csv_file, delimiter=',')
        shares_list = []
        for share_row in shares_file:
             shares_list.append(
                (share_row[0], float(share_row[1]), float(share_row[2]))
            )

        for i in range(len(shares_list) + 1):
            for element in combinations(shares_list, i):
                for info in element:
                    print(info[0])
            return shares_list


# info[0] = nom de l'action
# info[1] = coût de l'action
# info[2] = bénéfice (après 2ans)
# Nom
# poids
# Valeur


# ele = read_shares()
"""[('Montre à gousset', 2, 6),
       ('Boule de bowling', 3, 10),
       ('Portrait de tata Germaine', 4, 12)]
"""


# print('Algo force', sac_a_dos_force_brute(ele, capacite=500))


def knapsack(w, wt, val, n):
    """
    :param w: capacity of knapsack
    :param wt: list containing weights
    :param val: list containing corresponding values
    :param n: size of lists
    :return: Integer
    """
    # code here
    print(read_shares)
    if n == 0 or w == 0:
        return 0
    if wt[n - 1] <= w:
        return max(val[n - 1] + knapsack(w - wt[n - 1], wt, val, n - 1), knapsack(w, wt, val, n - 1))
    else:
        return knapsack(w, wt, val, n - 1)


if __name__ == '__main__':
    read_shares()
