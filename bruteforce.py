#!/usr/bin/python3
# coding: utf8
# enumerer toutes les combinaisons possibles
# trier les combinaisons possibles par rapport au maximum
# choisir la  meilleure combinaison

import csv
from itertools import combinations

MAX_INVEST = 500


def read_shares():
    with open("test_shares.csv") as csv_file:
        shares_file = csv.reader(csv_file, delimiter=",")
        shares_list = []
        for share_row in shares_file:
            shares_list.append((share_row[0], float(share_row[1]), float(share_row[2])))
        shares_selected = []
        save = []
    for i in range(len(shares_list)):
        possibilities = combinations(shares_list, i + 1)
        for elements in possibilities:
            cost_of_combinaison = 0
            gain_of_combinaison = 0
            for actions in elements:
                cost = []
                gains = []
                benefit = round((float(actions[1]) * float(actions[2])) / 100, 2)
                cost_of_combinaison += float(actions[1])
                gain_of_combinaison += float(benefit)
                cost.append(actions[1])
                gains.append(benefit)
                if cost_of_combinaison <= float(MAX_INVEST):
                    save.append({"combi": elements, "price": cost_of_combinaison, "gain": gain_of_combinaison})

    shares_selected = sorted(save, key=lambda k: (k["gain"]), reverse=True)
    print(shares_selected[0])

    # if sum(cost) < 500 and max(gains) :
    #    print(sum(cost), max(gains))

    # if sum(cost) < MAX_INVEST:
    # save.append(cost)

    # print(sum(cost))
    # sum(range(int(elements[i][1]))
    # gains_of_combinaison = sum(range(int(elements[i][2])))


# cost_of_combinaison += j[1]


"""all_costs = 0
                all_gains = 0
                costs = []
                gains = []
                MAX_INVEST = 500

                for actions in elements:
                    costs.append(actions[1])
                    gains.append(actions[2])

                    for cost in costs:
                        all_costs += cost
                    for gain in gains:
                        all_gains += gain

                    if all_costs <= MAX_INVEST:

                        shares_selected.append(
                            (round(all_gains), (round(all_costs)), elements)
                        )  # actions ou elements????????

    shares_selected = sorted(shares_selected, key=lambda x: -x[0])
    # print(all_costs, all_gains)
    print(len(shares_selected))
    print(shares_selected[0])

"""
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

if __name__ == "__main__":
    read_shares()
