import csv
import datetime

MAX_COST = 500


class Stock:
    def __init__(self, name, cost, rate):
        self.name = name
        self.cost = float(cost)
        self.rate = float(rate)
        self.profit = self.cost * self.rate / 100


def parse_csv(file_path):
    parsed_dataset = []
    with open(file_path) as file:
        for row in csv.DictReader(file):
            if float(row['price']) > 0 and float(row['profit']) > 0 and not row['price'].startswith("-"):
                parsed_dataset.append(Stock(row['name'], row['price'], row['profit']))
    return parsed_dataset


def greedy(stocks):
    stocks.sort(key=lambda x: x.rate, reverse=True)
    cost, profit = 0, 0
    selected_stocks = []
    for stock in stocks:
        if cost + stock.cost <= MAX_COST:
            cost += stock.cost
            profit += stock.profit
            selected_stocks.append(stock.name)
    return {
        'total_cost': cost,
        'total_profit': profit,
        'selected_stocks': selected_stocks
    }


def print_results(results, time):
    print("Voici les actions à acheter: ")
    for stock in results['selected_stocks']:
        print(" - " + stock)
    print("Coût: " + str(round(results['total_cost'], 2)))
    print("Profit: " + str(round(results['total_profit'], 2)))
    print("Temps d'éxecution: " + str(time))


if __name__ == "__main__":
    start_date = datetime.datetime.now()
    dataset = parse_csv("dataset2_P7.csv")
    print_results(greedy(dataset), datetime.datetime.now() - start_date)