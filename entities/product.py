class Product:
    """
    Represents a product with an ID, name, price, and quantity.
    """

    def __init__(self, id: int, name: str, price: float, stock: int):
        """
        Initializes a Product instance.

        Args:
            id (int): The ID of the product.
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product available.
        """
        self.id: int = id  # ID of the product
        self.name: str = name  # Name of the product
        self.price: float = price  # Price of the product
        self.stock: int = stock  # Quantity of the product available

    def to_dict(self) -> dict:
        """
        Converts the Product instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Product instance.
        """
        return {
            "id": self.id,  # ID of the product
            "name": self.name,  # Name of the product
            "price": self.price,  # Price of the product
            "stock": self.stock  # Quantity of the product
        }
