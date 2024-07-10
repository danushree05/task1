import unittest
<<<<<<< HEAD
from client3 import getDataPoint,getRatio
=======
from client3 import getDataPoint
>>>>>>> b73b46ec53fb33428054e16ec90040fa6bcb2065

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
<<<<<<< HEAD
    expected = [
            ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2),
            ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
        ]
    for i, quote in enumerate(quotes):
            self.assertEqual(getDataPoint(quote), expected[i])
=======
>>>>>>> b73b46ec53fb33428054e16ec90040fa6bcb2065
    """ ------------ Add the assertion below ------------ """

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
<<<<<<< HEAD
    expected = [
            ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2),
            ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
        ]
    for i, quote in enumerate(quotes):
            self.assertEqual(getDataPoint(quote), expected[i])

    
  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatio(self):
        price_a = 121.68
        price_b = 117.87
        expected = price_a / price_b
        self.assertEqual(getRatio(price_a, price_b), expected)

  def test_getRatio_priceBZero(self):
        price_a = 121.68
        price_b = 0
        self.assertIsNone(getRatio(price_a, price_b))

  def test_getRatio_priceAZero(self):
        price_a = 0
        price_b = 117.87
        expected = 0.0
        self.assertEqual(getRatio(price_a, price_b), expected)
=======


  """ ------------ Add more unit tests ------------ """

>>>>>>> b73b46ec53fb33428054e16ec90040fa6bcb2065


if __name__ == '__main__':
    unittest.main()
