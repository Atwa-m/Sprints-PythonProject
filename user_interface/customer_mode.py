from typing import List, Optional
from entities import Product, Inventory, Cart, Order, OrderProcessing, sms


class CustomerMode:
    """
    Represents the customer mode for browsing and managing the shopping cart.
    """

    def __init__(self, customer_name: str, inventory_manager: Inventory):
        """
        Initializes a CustomerMode instance.

        Args:
            customer_name (str): The name of the customer.
            inventory_manager (Inventory): An instance of the Inventory class.
        """
        self.__customer_name: str = customer_name  # Customer name
        self.__inventory_manager: Inventory = inventory_manager  # Inventory manager instance
        self.__cart: Cart = Cart()  # Cart instance
    
    def run(self) -> None:
        """
        Runs the customer mode to browse and manage the shopping cart.
        """
        print(f"Welcome, {self.__customer_name}!")
        while True:
            choice: str = self.__ask_for_an_operation()
            if choice == '1':
                print("\n\t\tAvailable Products:")
                self.__inventory_manager.display_inventory()
            elif choice == '2':
                self.__add_to_cart_adapter()
            elif choice == '3':
                print('\n\n\t\tYOUR CART')
                self.__cart.display_cart()
            elif choice == '4':
                self.__update_cart_item_adapter()
            elif choice == '5':
                self.__remove_item_from_cart_adapter()
            elif choice == '6':
                self.__checkout_adapter()
            elif choice == '7':
                break
            else:
                print("Invalid choice.")

    def __ask_for_an_operation(self) -> str:
        """
        Asks the user to choose an operation.

        Returns:
            str: The chosen operation ID.
        """
        print("\nCustomer Operations:")
        print("1. Browse all products in-stock")
        print("2. Add item to cart")
        print("3. View cart")
        print("4. Update the quantity of a cart item")
        print("5. Remove item from cart")
        print("6. Checkout")
        print("7. Exit")
        return input("\nEnter the id of the operation you want to perform: ")
    
    def __add_to_cart_adapter(self) -> None:
        """
        Adapter method to add a product to the cart.
        """
        try:
            product_id: int = int(input("Enter product ID to add to cart: "))
            quantity: int = int(input("Enter quantity: "))
            product: Optional[Product] = self.__inventory_manager.get_product_by_id(product_id)
            if product:
                self.__cart.add_item(product, quantity)
            else:
                print("Product not found.")
        except:
            print("Please enter a number.")
        

    def __update_cart_item_adapter(self) -> None:
        """
        Adapter method to update the quantity of a cart item.
        """
        while True:
            try:
                cart_item_index: int = int(input("Enter index of item to update: ")) - 1
                new_quantity: int = int(input("Enter new quantity: "))
                if 0 <= cart_item_index < len(self.__cart.get_cart_items()):
                    self.__cart.update_item_quantity(cart_item_index, new_quantity)
                    break
                else:
                    print("Invalid item index.")
            except:
                print("Please enter a number.")

    def __remove_item_from_cart_adapter(self) -> None:
        """
        Adapter method to remove an item from the cart.
        """
        while True:
            try:
                cart_item_index: int = int(input("Enter index of item to remove: ")) - 1
                if 0 <= cart_item_index < len(self.__cart.get_cart_items()):
                    self.__cart.remove_item(cart_item_index)
                    break
                else:
                    print("Invalid item index.")

            except:
                print("Please enter a number.")
            
    def __checkout_adapter(self) -> None:
        """
        Adapter method to process checkout and place an order.
        """
        order: Order = Order(self.__customer_name, self.__cart)
        order.display_order_summary()
        purchase_confirmation = input("\nAre you sure you want to confirm order? (yes/no): ").lower()
        if purchase_confirmation == 'yes':
            order_status: bool = OrderProcessing(order, self.__inventory_manager).place_order()
            if order_status:
                print(f"\nYour order has been placed successfully! Thank you for shopping with us, {self.__customer_name} :).")
            try:
                sms.send_sms("Your Order is on the way")
            except:
                pass
                
