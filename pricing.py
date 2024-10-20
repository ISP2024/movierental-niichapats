from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PriceStrategy, cls).__new__(cls)
        return cls._instance

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass


class NewRelease(PriceStrategy):
    """Pricing rules for New Release movies."""
    def get_price(self, days: int) -> float:
        return days * 3

    def get_rental_points(self, days: int) -> int:
        return days


class RegularPrice(PriceStrategy):
    """Pricing rules for Regular movies."""
    def get_price(self, days: int) -> float:
        price = 2.0
        if days > 2:
            price += (days - 2) * 1.5
        return price

    def get_rental_points(self, days: int) -> int:
        return 1


class ChildrensPrice(PriceStrategy):
    """Pricing rules for Children's movies."""
    def get_price(self, days: int) -> float:
        price = 1.5
        if days > 3:
            price += (days - 3) * 1.5
        return price

    def get_rental_points(self, days: int) -> int:
        return 1


NEW_RELEASE = NewRelease()
REGULAR = RegularPrice()
CHILDRENS = ChildrensPrice()
