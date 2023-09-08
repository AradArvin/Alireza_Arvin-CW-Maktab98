# Question3 code snippet
class ShoppingCart:     
    def __init__(self) -> None:         
        self.items = []         
        self.total_price = 0   

    def add_items(self, item):         
        self.items.append(item)         
        self.total_price += item.price  

    def remove_item(self, item):         
        self.items.remove(item)         
        self.total_price -= item.price 

    def calculate_discount(self):         
        if self.total_price > 100:             
            return self.total_price * 0.1         
        else:             
            return 0   
                    
    def checkout(self):         
        final_price = self.total_price - self.calculate_discount()         
        print(f"Total price: {self.total_price}")         
        print(f"Discount applied: {self.calculate_discount()}")         
        print(f"Final price after discount: {final_price}")


'''
1) The design pattern issues in the given code snippet are:
   - Lack of separation of concerns: The `ShoppingCart` class is responsible for managing the items in the cart, calculating discounts, 
     and handling the checkout process. This violates the Single Responsibility Principle.

   - Tight coupling: The `ShoppingCart` class directly depends on the `Item` class, as it accesses the `price` attribute of an item. 
     This creates a tight coupling between the two classes.

   - Lack of flexibility and extensibility: The code does not provide an easy way to add new types of discounts or modify the discount 
     calculation logic.

2) The chosen design pattern that can improve the code is the Strategy Pattern.

3) Here's the refactored code implementing the Strategy Pattern:
'''


from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, total_price):
        pass

class FixedDiscount(DiscountStrategy):
    def calculate_discount(self, total_price):
        return 10 if total_price > 100 else 0

class PercentDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def calculate_discount(self, total_price):
        return total_price * self.percentage

class ShoppingCart:
    def __init__(self, discount_strategy=None):
        self.items = []
        self.total_price = 0
        self.discount_strategy = discount_strategy or DiscountStrategy()

    def add_items(self, item):
        self.items.append(item)
        self.total_price += item.price

    def remove_item(self, item):
        self.items.remove(item)
        self.total_price -= item.price

    def calculate_discount(self):
        return self.discount_strategy.calculate_discount(self.total_price)

    def checkout(self):
        final_price = self.total_price - self.calculate_discount()
        print(f"Total price: {self.total_price}")
        print(f"Discount applied: {self.calculate_discount()}")
        print(f"Final price after discount: {final_price}")


'''
4) Explanation of the Strategy Pattern and its benefits in addressing the design issues:

The Strategy Pattern is a behavioral design pattern that defines a family of algorithms, encapsulates each one, and makes them interchangeable. 
It allows the algorithm to vary independently from clients that use it.

In the original code, the discount calculation logic was tightly coupled with the `ShoppingCart` class, violating the Single Responsibility 
Principle. By applying the Strategy Pattern, we separate the discount calculation into different strategies, each encapsulating a specific 
discount algorithm. The `DiscountStrategy` interface provides a common method `calculate_discount()` that all discount strategies must implement.

The refactored `ShoppingCart` class now takes a `discount_strategy` parameter in its constructor, allowing clients to choose a specific discount 
strategy or use the default strategy (`FixedDiscount` in this case). This enhances the flexibility and extensibility of the code as new discount 
strategies can be easily added by implementing the `DiscountStrategy` interface.

The use of the Strategy Pattern promotes loose coupling as the `ShoppingCart` class no longer needs to know the specific details of how discounts 
are calculated. It only depends on the abstract `DiscountStrategy` interface, which can be easily substituted with different concrete 
implementations at runtime.

5) Here is the refactored code again for your reference:
'''


from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, total_price):
        pass

class FixedDiscount(DiscountStrategy):
    def calculate_discount(self, total_price):
        return 10 if total_price > 100 else 0

class PercentDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def calculate_discount(self, total_price):
        return total_price * self.percentage

class ShoppingCart:
    def __init__(self, discount_strategy=None):
        self.items = []
        self.total_price = 0
        self.discount_strategy = discount_strategy or DiscountStrategy()

    def add_items(self, item):
        self.items.append(item)
        self.total_price += item.price

    def remove_item(self, item):
        self.items.remove(item)
        self.total_price -= item.price

    def calculate_discount(self):
        return self.discount_strategy.calculate_discount(self.total_price)

    def checkout(self):
        final_price = self.total_price - self.calculate_discount()
        print(f"Total price: {self.total_price}")
        print(f"Discount applied: {self.calculate_discount()}")
        print(f"Final price after discount: {final_price}")



# Sina's example Code

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class DiscountStrategy:
    def calculate_discount(self, items):
        pass


class NoDiscount(DiscountStrategy):
    def calculate_discount(self, items):
        return 0


class TenPercentDiscount(DiscountStrategy):
    def calculate_discount(self, items):
        total_price = sum(item.price for item in items)
        if total_price > 100:
            return total_price * 0.1
        else:
            return 0


class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def calculate_discount(self, items):
        return self.discount_amount


class ShoppingCart:
    def __init__(self, discount_strategy):
        self.items = []
        self.discount_strategy = discount_strategy

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_discount(self):
        return self.discount_strategy.calculate_discount(self.items)

    def calculate_total_price(self):
        return sum(item.price for item in self.items)

    def checkout(self):
        total_price = self.calculate_total_price()
        discount = self.calculate_discount()
        final_price = total_price - discount
        print(f"Total price: {total_price}")
        print(f"Discount applied: {discount}")
        print(f"Final price after discount: {final_price}")


if __name__ == "__main__":
    cart = ShoppingCart(FixedAmountDiscount(20))

    item1 = Item("Item 1", 50)
    item2 = Item("Item 2", 75)
    cart.add_item(item1)
    cart.add_item(item2)

    cart.checkout()