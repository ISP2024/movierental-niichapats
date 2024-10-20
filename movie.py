from dataclasses import dataclass, field


@dataclass(frozen=True)
class Movie:
    """A movie available for rent."""
    title: str
    year: int
    genre: set[str] = field(default_factory=set)

    def is_genre(self, genre_name: str) -> bool:
        """Check if the movie matches the specified genre."""
        return genre_name.lower() in (g.lower() for g in self.genre)

    def __str__(self) -> str:
        return f"{self.title} ({self.year})"
