#!/usr/bin/python3
# coding: utf8

import csv

MAX_COST = 500


def read_shares(csv_doc):
    """ """
    with open(csv_doc) as csv_file:
        data_list = list(csv.reader(csv_file))
    selection = []
    take = []
    for row in data_list[1:]:
        if round(float(row[1])) != 0 and float(row[2]) >= 0 and not row[1].startswith("-"):
            benefit = round(float(row[1]) * float(row[2]) / 100, 2)
            ratio = round(float(row[2])) / round(float(row[1]))
            selection.append(
                {
                    "action": row[0],
                    "price": float(row[1]),
                    "value": float(row[2]),
                    "benefit": benefit,
                    "ratio": ratio,
                }
            )

    sorted_selection = sorted(selection, key=lambda x: x["ratio"], reverse=True)

    total_cost, total_gain = 0, 0
    left_space = MAX_COST
    print(f'Pour une limite de {MAX_COST}, il est préférable d\' acheter : \n')
    for share in sorted_selection:
        if share["price"] < left_space and share not in take:
            total_gain += share["benefit"]
            total_cost += share["price"]
            left_space -= share["price"]
            take.append(share)
        # if take.count(share) > 1:
        #     take.remove(share)
        print(f'{share["action"]}', end=' ')
        # print()

    print(f'\n Pour un coût total de : {round(total_cost, 2)}\n')
    print(f'\n Avec un gain total de : {round(total_gain, 2)}')


if __name__ == "__main__":
    read_shares("dataset1_P7.csv")
    read_shares("dataset2_P7.csv")
    # read_shares( "dataset2_P7.csv")
    # read_shares("test_shares.csv")
