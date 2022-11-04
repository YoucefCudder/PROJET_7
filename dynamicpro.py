import csv


def read_shares(csv_doc):
    """ """
    with open(csv_doc) as csv_file:
        data_list = list(csv.reader(csv_file))
    selection = []
    for row in data_list[1:]:
        if round(float(row[1])) != 0 and float(row[2]) >= 0 and not row[1].startswith("-"):
            benefit = round(float(row[1]) * float(row[2]) / 100, 2)
            ratio = round(float(row[2])) / round(float(row[1]))

            selection.append(
                {
                    "action": row[0],
                    "price": row[1],
                    "value": row[2],
                    "benefit": benefit,
                    "ratio": ratio,
                }
            )

    return selection


def knapsack(value, price):
    n = len(shares)
    MAX_INVEST = 500 * 100

    K = [[0 for x in range(MAX_INVEST + 1)] for x in range(n + 1)]
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(MAX_INVEST + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif price[i - 1] <= w:
                K[i][w] = max(value[i - 1]
                              + K[i - 1][w - price[i - 1]],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][MAX_INVEST] / 100


shares = read_shares("dataset1_P7.csv")
value = []
price = []
for j in shares:
    value.append(round(float(j['value'])))
    price.append(round(float(j['price'])))
print(knapsack(value, price))
# n = len(shares)
# MAX_INVEST = 500
# benefit = shares['benefit']
# ratio = shares['price']
# print(knapsack(MAX_INVEST, benefit=shares('benefit'), ratio, selection))


# if n == 0 or MAX_INVEST == 0:
#     return 0
# if (price[n - 1] > MAX_INVEST):
#     return knapsack(MAX_INVEST, value, price, n - 1)
# else:
#     return max(
#         value[n - 1] + knapsack(
#             MAX_INVEST - price[n - 1], price, value, n - 1),
#         knapsack(MAX_INVEST, price, value, n - 1))
