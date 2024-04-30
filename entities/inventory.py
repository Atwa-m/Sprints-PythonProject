import json
import os
from typing import List

from entities import Product

class Inventory:
    """
    Represents an inventory of products.
    """

    def __init__(self, inventory_file_path: str):
        """
        Initializes an Inventory instance.

        Args:
            inventory_file_path (str): The file path to the inventory JSON file.
        """
        self.__inventory_file_path: str = inventory_file_path  # File path to the inventory JSON file
        self.__products: List[Product] = self.__load_inventory()  # List of products in the inventory

    def __load_inventory(self) -> List[Product]:
        """
        Load products from the inventory JSON file.

        Returns:
            List[Product]: A list of Product instances loaded from the inventory file.
        """
        if not os.path.exists(self.__inventory_file_path):
            return []
        with open(self.__inventory_file_path, 'r') as file:
            products_data = json.load(file)
            products = []
            for product_data in products_data:
                products.append(Product(**product_data))
            return products
        
    def __save_products(self) -> None:
        """
        Save products to the inventory JSON file.
        """
        products_data = [product.to_dict() for product in self.__products]
        with open(self.__inventory_file_path, 'w') as file:
            json.dump(products_data, file, indent=4)

    def get_all_products(self) -> List[Product]:
        """
        Get all products in the inventory.

        Returns:
            List[Product]: A list of all products in the inventory.
        """
        return self.__products
    
    def get_product_by_id(self, product_id: int) -> Product | None:
        """
        Retrieve a product from the inventory by its ID.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            Product | None: The product with the specified ID if found, otherwise None.
        """
        for product in self.__products:
            if product.id == product_id:
                return product
        return None 
        

    def add_product(self, product: Product) -> Product:
        """
        Add a new product to the inventory.

        Args:
            product (Product): The product to add to the inventory.

        Returns:
            Product: The added product.
        """
        self.__products.append(product)
        self.__save_products()
        return product

    def update_product(self, product_id: int, updated_product: Product) -> Product | None:
        """
        Update an existing product in the inventory.

        Args:
            product_id (int): The ID of the product to update.
            updated_product (Product): The updated product information.

        Returns:
            Product | None: The updated product if it exists, otherwise None.
        """
        for product in self.__products:
            if product.id == product_id:
                product.name = updated_product.name
                product.price = updated_product.price
                product.stock = updated_product.stock
                self.__save_products()
                return updated_product
        print("This product doesn't exist.")
        return None


    def remove_product(self, product_id: int) -> None:
        """
        Remove a product from the inventory.

        Args:
            product_id (int): The ID of the product to be removed.
        """
        self.__products = [product for product in self.__products if product.id != product_id]
        self.__save_products()

    def display_inventory(self) -> None:
        """
        Display all products in the inventory.
        """
        print("{:<5} {:<20} {:<15} {:<10}".format("ID", "Name", "Price", "Quantity"))
        for product in self.__products:
            print("{:<5} {:<20} {:<4} {:<10} {:<10}".format(product.id, product.name, product.price, 'EGP', product.stock))
