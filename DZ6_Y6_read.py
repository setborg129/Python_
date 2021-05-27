import sys


def read_price(price_market):
    with open(price_market, 'r', encoding='utf-8') as price_f:
        for item in price_f:
            print(item)


if __name__ == "__main__":
    _script_name, price_file = sys.argv
    read_price(price_file)
