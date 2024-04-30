from entities import Product, Inventory
class ManagerMode:
    """
    Represents the manager mode for managing inventory operations.
    """

    def __init__(self, inventory_manager: Inventory):
        """
        Initializes a ManagerMode instance.

        Args:
            inventory_manager (Inventory): An instance of the Inventory class.
        """
        self.__inventory_manager: Inventory = inventory_manager  # Inventory manager instance
    
    def run(self) -> None:
        """
        Runs the manager mode to perform inventory operations.
        """
        print("Welcome, Store Manager!")
        while True:
            choice: str = self.__ask_for_an_operation()
            if choice == '1':
                print("\n\t\tAvailable Products:")
                self.__inventory_manager.display_inventory()
            elif choice == '2':
                self.__add_product_adapter()
            elif choice == '3':
                self.__update_product_adapter()
            elif choice == '4':
                self.__remove_product_adapter()
            elif choice == '5':
                break
            else:
                print("Invalid choice.")

    def __ask_for_an_operation(self) -> str:
        """
        Asks the user to choose an operation.

        Returns:
            str: The chosen operation ID.
        """
        print("\nInventory Management:")
        print("1. View inventory")
        print("2. Add product")
        print("3. Update product")
        print("4. Remove product")
        print("5. Exit")
        return input("\nEnter the id of the operation you want to perform: ")
    
    def __add_product_adapter(self) -> None:
        """
        Adapter method to add a product to the inventory.
        """
        while True:
            try:
                product_id: int = int(input("Enter product ID: "))
                name: str = input("Enter product name: ")
                price: float = float(input("Enter product price: "))
                quantity: int = int(input("Enter product quantity: "))

                product: Product = Product(product_id, name, price, quantity)
                if self.__inventory_manager.add_product(product):
                    print("Product added successfully.")
                break
            except:
                print("Please enter valid inputs")

    def __update_product_adapter(self) -> None:
        """
        Adapter method to update a product in the inventory.
        """
        while True:
            try:
                product_id: int = int(input("Enter product ID: "))
                name: str = input("Enter updated product name: ")
                price: float = float(input("Enter updated product price: "))
                quantity: int = int(input("Enter updated product quantity: "))

                updated_product: Product = Product(product_id, name, price, quantity)
                if self.__inventory_manager.update_product(product_id, updated_product):
                    print("Product updated successfully.")
                break
            except:
                print("Please enter valid inputs")

    def __remove_product_adapter(self) -> None:
        """
        Adapter method to remove a product from the inventory.
        """
        while True:
            try:
                product_id: int = int(input("Enter product ID: "))
                self.__inventory_manager.remove_product(product_id)
                print("Product removed successfully.")
                break
            except:
                print("Please enter valid inputs")
