import unittest
import random
from acme import Product
readout = __import__('acme-report')

class AcmeProductTests(unittest.TestCase):
  def test_default_product_price(self):
    prod = Product('Test Product')
    self.assertEqual(prod.price, 10)
  def test_default_flam(self):
    prod = Product('Test Product')
    self.assertEqual(prod.flammability, 0.5)
  def test_steal_explode(self):
    price = random.randint(5, 100)
    weight = random.randint(5, 100)
    flam = random.uniform(0.0, 2.5)
    prod = Product('Test Product', price, weight, flam)
    if price / weight < 0.5:
      self.assertEqual(prod.stealability(), 'Not so stealable...')
    elif price / weight < 1.0:
      self.assertEqual(prod.stealability(), 'Kinda stealable.')
    else:
      self.assertEqual(prod.stealability(), 'Very stealable!')
    if weight * flam < 10.0:
      self.assertEqual(prod.explode(), '...fizzle.')
    elif weight * flam < 50.0:
      self.assertEqual(prod.explode(), '...boom!')
    else:
      self.assertEqual(prod.explode(), '...BABOOM!!')

class AcmeReportTests(unittest.TestCase):
  def test_default_num_products(self):
    prods = readout.generate_products()
    self.assertEqual(len(prods), 30)
  def test_legal_names(self):
    prods = readout.generate_products()
    for p in prods:
      parts = p.name.split(' ')
      self.assertEqual(len(parts), 2)
      self.assertIn(parts[0], ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved'])
      self.assertIn(parts[1], ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???'])

if __name__ == '__main__':
  unittest.main()