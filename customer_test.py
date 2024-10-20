import re
import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class CustomerTest(unittest.TestCase):
	""" Tests of the Customer class"""

	def setUp(self):
		"""Test fixture contains:

		c = a customer
		movies = list of some movies
		"""
		self.c = Customer("Movie Mogul")
		self.new_movie = Movie("Dune: Part Two", 2024, {"Sci-Fi"})
		self.regular_movie = Movie("Air", 2023, {"Drama"})
		self.childrens_movie = Movie("Frozen", 2013, {"Children"})

	@unittest.skip("No convenient way to test")
	def test_billing():
		# no convenient way to test billing since its buried in the statement() method.
		pass

	def test_statement(self):
		stmt = self.c.statement()
		# get total charges from statement using a regex
		pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
		matches = re.match(pattern, stmt, flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("0.00", matches[1])
		# add a rental
		self.c.add_rental(Rental(self.new_movie, 4))  # days
		stmt = self.c.statement()
		matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("12.00", matches[1])

	def test_get_total_charge(self):
		"""test the get_total_charge method"""
		# initially, there are no rentals, so total charge should be 0
		self.assertEqual(self.c.get_total_charge(), 0.00)

		# add rentals
		self.c.add_rental(Rental(self.new_movie, 3))
		self.assertEqual(self.c.get_total_charge(), 9.00)

		self.c.add_rental(Rental(self.regular_movie, 5))
		self.assertEqual(self.c.get_total_charge(), 15.50)

		self.c.add_rental(Rental(self.childrens_movie, 4))
		self.assertEqual(self.c.get_total_charge(), 18.50)

	def test_get_rental_points(self):
		"""test the get_rental_points method"""
		# initially, there are no rentals, so rental points should be 0
		self.assertEqual(self.c.get_rental_points(), 0)

		# add rentals
		self.c.add_rental(Rental(self.new_movie, 1))
		self.assertEqual(self.c.get_rental_points(), 1)
		self.c.add_rental(Rental(self.new_movie, 3))
		self.assertEqual(self.c.get_rental_points(), 4)

		self.c.add_rental(Rental(self.regular_movie, 5))
		self.assertEqual(self.c.get_rental_points(), 5)

		self.c.add_rental(Rental(self.childrens_movie, 2))
		self.assertEqual(self.c.get_rental_points(), 6)
