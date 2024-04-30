from typing import List

from entities import Product, CartItem

class Cart:
    """
    Represents a shopping cart.
    """

    def __init__(self, cart_items: List[CartItem]=[]):
        """
        Initializes a Cart instance.
        """
        self.__items: List[CartItem] = cart_items  # List of cart items

    def add_item(self, product: Product, quantity: int) -> None:
        """
        Add an item to the cart.

        Args:
            product (Product): The product to add to the cart.
            quantity (int): The quantity of the product to add.
        """
        self.__items.append(CartItem(product, quantity))

    def remove_item(self, index: int) -> None:
        """
        Remove an item from the cart.

        Args:
            index (int): The index of the item to remove from the cart.
        """
        del self.__items[index]

    def update_item_quantity(self, index: int, new_quantity: int) -> None:
        """
        Update the quantity of an item in the cart.

        Args:
            index (int): The index of the item to update.
            new_quantity (int): The new quantity of the item.
        """
        if new_quantity <= self.__items[index].product.stock:
            self.__items[index].quantity = new_quantity
        else:
            self.__items[index].quantity = self.__items[index].product.stock
            print(f"Not enough of this product in stock. The new quantity has been set to the max available stock: {self.__items[index].quantity} units.")

    def get_cart_items(self) -> List[CartItem]:
        """
        Get all items in the cart.

        Returns:
            List[CartItem]: A list of all items in the cart.
        """
        return self.__items

    def display_cart(self) -> None:
        """
        Display the contents of the cart.
        """
        if self.__items:
            print("{:<10} {:<20} {:<10} {:<10}".format("Index", "Name", "Quantity", "Total"))
            for i, item in enumerate(self.__items):
                print("{:<10} {:<20} {:<10} {:<4} EGP".format(i+1, item.product.name, item.quantity, item.calculate_item_total()))
        else:
            print("Your cart is empty.")
