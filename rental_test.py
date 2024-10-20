import unittest
from rental import Rental
from movie import Movie
from pricing import NEW_RELEASE, REGULAR, CHILDRENS


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", 2024, {"Sci-Fi"})
        self.regular_movie = Movie("Air", 2023, {"Drama"})
        self.childrens_movie = Movie("Frozen", 2013, {"Children"})

    def test_movie_attributes(self):
        self.assertEqual("Dune: Part Two", self.new_movie.title)
        self.assertEqual(NEW_RELEASE, self.new_movie.price_code_for_movie())
        self.assertEqual("Air", self.regular_movie.title)
        self.assertEqual(REGULAR, self.regular_movie.price_code_for_movie())
        self.assertEqual("Frozen", self.childrens_movie.title)
        self.assertEqual(CHILDRENS, self.childrens_movie.price_code_for_movie())

    def test_rental_price(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)

        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 4)
        self.assertEqual(rental.get_price(), 5.0)

        rental = Rental(self.childrens_movie, 3)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.get_price(), 4.5)

    def test_rental_points(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(self.new_movie, 4)
        self.assertEqual(rental.rental_points(), 4)

        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(self.regular_movie, 4)
        self.assertEqual(rental.rental_points(), 1)

        rental = Rental(self.childrens_movie, 1)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(self.childrens_movie, 4)
        self.assertEqual(rental.rental_points(), 1)


if __name__ == '__main__':
    unittest.main()
