# Định nghĩa interface tính toán
from abc import ABC, abstractmethod


class CalculateStrategy(ABC):
    @abstractmethod
    def calculate(self, price: float) -> float:
        pass


# Các class triển khai CalculateStrategy
class RetailPriceStrategy(CalculateStrategy):
    def calculate(self, price: float) -> float:
        return price * 1.2


class WholesalePriceStrategy(CalculateStrategy):
    def calculate(self, price: float) -> float:
        return price * 1.1


class PromotionalPriceStrategy(CalculateStrategy):
    def calculate(self, price: float) -> float:
        return price * 0.8


# Class sử dụng Strategy Pattern
class Product:
    def __init__(self):
        self.calculate_strategy = None


    def set_calculate_strategy(self, strategy: CalculateStrategy):
        self.calculate_strategy = strategy


    def calculate_price(self, price: float) -> float:
        return self.calculate_strategy.calculate(price)


# Sử dụng 
product = Product()

product.set_calculate_strategy(RetailPriceStrategy())
print(product.calculate_price(100)) # Kết quả: 120.0

product.set_calculate_strategy(WholesalePriceStrategy())
print(product.calculate_price(100))# Kết quả: 110.0

product.set_calculate_strategy(PromotionalPriceStrategy())
print(product.calculate_price(100)) # Kết quả: 80.0