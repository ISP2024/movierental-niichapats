import csv
import logging
from typing import Optional


class Movie:
    """A movie available for rent."""

    def __init__(self, title: str, year: int, genres: set[str]):
        self.title = title
        self.year = year
        self.genres = genres

    def __str__(self):
        return f"{self.title} ({self.year})"

    def is_genre(self, genre: str) -> bool:
        return genre.lower() in (g.lower() for g in self.genres)


class MovieCatalog:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'movies'):
            self.movies = []
            self.load_data('movies.csv')

    def load_data(self, file_path: str):
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for line_number, row in enumerate(reader, start=1):
                if line_number == 1:
                    continue
                if len(row) < 4 or len(row) > 5:
                    logging.error(f"Line {line_number}: Unrecognized format {','.join(row)}")
                    continue

                movie_id, title, year, *genres = row

                if not movie_id.isdigit() or not year.isdigit():
                    logging.error(f"Line {line_number}: Unrecognized format {','.join(row)}")
                    continue
                year = int(year)
                genres = set(genre.strip() for genre in genres[0].split('|')) if genres else set()
                self.movies.append(Movie(title, year, genres))

    def get_movie(self, title: str, year: Optional[int] = None) -> Optional[Movie]:
        """Return the first movie with the matching title and optional year."""
        for movie in self.movies:
            if movie.title.lower() == title.lower() and (year is None or movie.year == year):
                return movie
        return None
