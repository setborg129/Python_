import sys


def save_price(price_market, price):
    with open(price_market, 'a', encoding='utf-8') as price_f:
            price_f.write(f'{price}\n')




if __name__ == "__main__":
    _script_name, price_file, text_price,  = sys.argv
    save_price(price_file, text_price)