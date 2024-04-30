from typing import List, Optional
from entities import Product, Inventory, CartItem, Order

class OrderProcessing:
    """
    Represents a system for processing orders and updating inventory.
    """

    def __init__(self, order: Order, inventory_manager: Inventory):
        """
        Initializes an OrderProcessing instance.

        Args:
            order (Order): The order to be processed.
            inventory (Inventory): The inventory system.
        """
        self.__order: Order = order  # The order to be processed
        self.__inventory_manager: Inventory = inventory_manager  # The inventory system

    def place_order(self) -> bool:
        """
        Place the order and update inventory.

        Raises:
            ValueError: If there is not enough stock for any item in the order.

        Returns:
            bool: The status of the operation.
        """
        # Copy order items to avoid modifying the original order
        order_items: List[CartItem] = self.__order.items.copy()

        for item in order_items:
            inventory_product: Optional[Product] = self.__inventory_manager.get_product_by_id(item.product.id)
            if inventory_product: 
                if item.quantity > inventory_product.stock:
                    print(f"Failed to place order. Not enough stock for {item.product.name}. Please update the quantity in your cart.")
                    return False
                # Deduct the ordered quantity from the inventory
                inventory_product.stock -= item.quantity
                # Update the inventory with the new product quantity
                self.__inventory_manager.update_product(inventory_product.id, inventory_product)

        return True  # Return the processed order