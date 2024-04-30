from typing import List
import uuid

from entities import CartItem, Cart


class Order:
    """
    Represents an order containing items from a shopping cart.
    """

    def __init__(self, owner_name: str, cart: Cart):
        """
        Initializes an Order instance.

        Args:
            owner_name (str): The name of the owner placing the order.
            cart (Cart): The cart containing items to be ordered.
        """
        self.order_id: str = str(uuid.uuid4())[:8]  # Unique order ID
        self.owner_name: str = owner_name  # Name of the owner placing the order
        self.items: List[CartItem] = cart.get_cart_items()  # Items in the order

    def __calculate_order_total(self) -> float:
        """
        Calculate the total cost of the order.

        Returns:
            float: The total cost of the order.
        """
        total: float = 0
        for item in self.items:
            total += item.calculate_item_total()
        return total

    def display_order_summary(self) -> None:
        """
        Display the order summary.
        """
        print("\nOrder Summary:")
        print(f"Order ID: {self.order_id}")
        for item in self.items:
            print(f"{item.product.name}: {item.product.price} EGP x {item.quantity} = {item.calculate_item_total()} EGP")
        print(f"Order Total: {self.__calculate_order_total()} EGP")