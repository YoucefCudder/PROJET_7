#!/usr/bin/python3
# coding: utf8


# enumerer toutes les combinaisons possibles
# trier les combinaisons possibles par rapport au maximum
# choisir la  meilleure combinaison

import csv
from itertools import combinations


def read_shares(max_cost=500):
    with open("test_shares.csv") as csv_file:
        shares_file = csv.reader(csv_file, delimiter=",")
        shares_list = []
        for share_row in shares_file:
            shares_list.append((share_row[0], float(share_row[1]), float(share_row[2])))
            # print(float(share_row[1]), float(share_row[2]))

    return shares_list


def find_the_profit(shares_list):
    gains = []
    for shares in shares_list:
        profit = shares[1] * shares[2] / 100
        gains.append(profit)
    return (sum(gains))



def make_combinations(shares_list):
    for i in range(len(shares_list)):
        possibilities = combinations(shares_list, i+1)
        for element in possibilities:
            print(element)

def find_the_cost(shares_list):
    pass


if __name__ == "__main__":
    shares = read_shares()
    # read_shares()
    # find_the_profit(shares)
    make_combinations(shares)
