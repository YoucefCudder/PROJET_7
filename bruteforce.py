#!/usr/bin/python3
# coding: utf8


""" enumerer toutes les combinaisons possibles
 trier les combinaisons possibles par rapport au maximum
 choisir la  meilleure combinaison"""

import csv
from itertools import combinations

MAX_INVEST = 500


def read_shares():
    """

    :return:
    """
    with open("test_shares.csv") as csv_file:
        shares_file = csv.reader(csv_file, delimiter=",")
        shares_list = []
        for share_row in shares_file:
            shares_list.append((share_row[0], float(share_row[1]), float(share_row[2])))
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
                    save.append(
                        {
                            "combi": elements,
                            "price": cost_of_combinaison,
                            "gain": gain_of_combinaison,
                        }
                    )

    shares_selected = sorted(save, key=lambda k: (k["gain"]), reverse=True)
    print(f"Pour une limite de {MAX_INVEST}, il est préférable d' acheter : \n")

    print(
        f'{shares_selected[0]["combi"]}, pour un coût total de {round(shares_selected[0]["price"], 2)}€'
        f'et un gain de {round(shares_selected[0]["gain"], 2)}€'
    )


if __name__ == "__main__":
    read_shares()
