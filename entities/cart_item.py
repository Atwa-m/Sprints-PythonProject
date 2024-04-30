from entities import Product

class CartItem:
    """
    Represents an item in a shopping cart.
    """

    def __init__(self, product: Product, quantity: int):
        """
        Initializes a CartItem instance.

        Args:
            product (Product): The product associated with this cart item.
            quantity (int): The quantity of the product in this cart item.
        """
        self.product: Product = product  # Product associated with this cart item

        # Ensure that the quantity does not exceed the available stock
        if quantity <= self.product.stock:
            self.quantity = quantity
        else:
            self.quantity = self.product.stock
            print(f"Not enough of this product in stock. The quantity has been set to the max available stock: {self.quantity} units.")

    def calculate_item_total(self) -> float:
        """
        Calculate the total cost of this cart item.

        Returns:
            float: The total cost of this cart item.
        """
        return self.product.price * self.quantity
