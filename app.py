from entities import Inventory  # Importing necessary entities
from user_interface import CustomerMode, ManagerMode  # Importing user interfaces


class Application:
    """
    Represents the main application entry point.
    """

    def __init__(self) -> None:
        """
        Initializes the Application instance.
        """
        self.__inventory_file_path: str = 'inventory.json'  # File path to the inventory JSON file

    def run(self) -> None:
        """
        Runs the application.
        """
        inventory_manager: Inventory = Inventory(self.__inventory_file_path)  # Creating an Inventory instance
        print("Welcome to the Online Shopping System!")
        user_type: str = input("Are you a customer or store manager? (customer/manager): ").lower()

        if user_type == "customer":
            customer_name: str = input("Please enter your name: ").capitalize()  # Asking for customer's name
            CustomerMode(customer_name, inventory_manager).run()  # Running customer mode
        elif user_type == "manager":
            ManagerMode(inventory_manager).run()  # Running manager mode
        else:
            print("Invalid user type.")


# Main function
if __name__ == "__main__":
    Application().run()
