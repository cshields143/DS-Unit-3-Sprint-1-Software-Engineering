import random
from acme import Product

def generate_products(x=30):
  bucket = []
  for _ in range(x):
    pt1 = random.choice(['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved'])
    pt2 = random.choice(['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???'])
    name = f'{pt1} {pt2}'
    price = random.randint(5, 100)
    weight = random.randint(5, 100)
    flam = random.uniform(0.0, 2.5)
    bucket.append(Product(name, price, weight, flam))
  return bucket

def inventory_report(stuuf):
  list_o_names = [prod.name for prod in stuuf]
  num_o_names = len(list(set(list_o_names)))
  list_o_prices = [prod.price for prod in stuuf]
  avg_price = sum(list_o_prices) / len(list_o_prices)
  list_o_weights = [prod.weight for prod in stuuf]
  avg_weight = sum(list_o_weights) / len(list_o_weights)
  list_o_flams = [prod.flammability for prod in stuuf]
  avg_flam = sum(list_o_flams) / len(list_o_flams)
  print(f'UNIQUE PRODUCTS {num_o_names}')
  print(f'AVG PRICE {avg_price}')
  print(f'AVG WEIGHT {avg_weight}')
  print(f'AVG FLAM {avg_flam}')

if __name__ == '__main__':
  inventory_report(generate_products())