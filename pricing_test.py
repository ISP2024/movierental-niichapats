import unittest
from movie import Movie
from datetime import datetime
from pricing import NEW_RELEASE, REGULAR, CHILDRENS


class TestMoviePricing(unittest.TestCase):

    def test_new_release_movie(self):
        movie = Movie("New Release Movie", datetime.now().year, {"Drama"})
        self.assertIs(movie.price_code_for_movie(), NEW_RELEASE)

    def test_childrens_movie(self):
        movie = Movie("Children's Movie", 2020, {"Children"})
        self.assertIs(movie.price_code_for_movie(), CHILDRENS)

    def test_regular_movie(self):
        movie = Movie("Regular Movie", 2020, {"Action"})
        self.assertIs(movie.price_code_for_movie(), REGULAR)

if __name__ == '__main__':
    unittest.main()
