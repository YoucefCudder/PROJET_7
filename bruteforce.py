#!/usr/bin/python3
# coding: utf8
# enumerer toutes les combinaisons possibles
# trier les combinaisons possibles par rapport au maximum
# choisir la  meilleure combinaison

import csv
from itertools import combinations


def read_shares():
    with open('test_shares.csv') as csv_file:
        shares_file = csv.reader(csv_file, delimiter=',')
        shares_list = []
        MAX_INVEST = 500
        for share_row in shares_file:
            shares_list.append((share_row[0], float(share_row[1]), float(share_row[2])))
        selected_elements = []

    for i in range(len(shares_list)):
        possibilities = combinations(shares_list, i+1)
        for elements in possibilities:
            for actions in elements:
                costs = []
                gains = []
                all_costs = 0
                all_gains = 0
                costs.append(actions[1])
                gains.append(actions[2])
                for cost in costs:
                    all_costs += cost
                for gain in gains:
                    all_gains += gain

                if all_costs <= MAX_INVEST:

                    selected_elements.append((round(all_gains, 2), actions))

        selected_elements = sorted(selected_elements, key=lambda x: -x[0])


    print(selected_elements[0])


def calc_brute(shares_list, MAX_INVEST=500, bag=None):

        if bag is None:
            bag = []
        if shares_list:
            shares_list[0][1], shares_list[0][2] = calc_brute(shares_list[-1:], MAX_INVEST, bag)
            val = shares_list[0][1]
            if val <= MAX_INVEST:
                shares_list[1][1], shares_list[1][2] = calc_brute(MAX_INVEST - shares_list[0][1], shares_list[:1], bag + [val])
                if shares_list[0][1] < shares_list[1][1]:
                    return shares_list[1][1], shares_list[1][2]

            return shares_list[0][1], shares_list[0][2]

        else:
            return sum([i[2] for i in bag]), bag

# print(f'{info[0]}, {info[1]}, {info[2]}')


"""
N denotes the number of items.
W denotes the weight of the item.
C denotes the cost of the item.
    if elements_selection is None:
        elements_selection = []
        if elements:
            val1, lst_val1 = read_shares(capacite, elements[1:], elements_selection)
            val = elements[0]
            if val[1] <= capacite:
                val2, lst_val2 = read_shares(capacite - val[1], elements[1:], elements_selection + [val])
                if val1 < val2:
                    return val2, lst_val2

                return val1, lst_val1
            else:
                return sum([i[2] for i in elements_selection]), elements_selection
"""


if __name__ == '__main__':
    read_shares()

