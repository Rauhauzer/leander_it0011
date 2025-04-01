class Item:
    """
    Class to represent an Item with id, name, description, and price.
    """
    def __init__(self, item_id, name, description, price):
        # Validating the inputs for item creation
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("Item ID must be a positive integer.")
        if not name or len(name) == 0:
            raise ValueError("Item name cannot be empty.")
        if not isinstance(description, str) or len(description) == 0:
            raise ValueError("Item description cannot be empty.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Item price must be a non-negative number.")

        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: {self.price}"


class ItemManager:
    """
    Class to handle CRUD operations for Items.
    """
    def __init__(self):
        # Dictionary to store items with item_id as the key
        self.items = {}

    def create_item(self, item_id, name, description, price):
        # Create an item and add it to the items dictionary
        try:
            item = Item(item_id, name, description, price)
            self.items[item_id] = item
            print("Item created successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def read_item(self, item_id):
        # Retrieve an item based on item_id
        item = self.items.get(item_id)
        if item:
            print(item)
        else:
            print("Item not found.")

    def update_item(self, item_id, name=None, description=None, price=None):
        # Update an existing item
        item = self.items.get(item_id)
        if item:
            if name:
                item.name = name
            if description:
                item.description = description
            if price is not None:
                item.price = price
            print("Item updated successfully!")
        else:
            print("Item not found.")

    def delete_item(self, item_id):
        # Delete an item based on item_id
        if item_id in self.items:
            del self.items[item_id]
            print("Item deleted successfully!")
        else:
            print("Item not found.")


# Sample usage:
def main():
    manager = ItemManager()

    # Creating items
    manager.create_item(1, "Laptop", "A high-performance laptop", 1500.00)
    manager.create_item(2, "Phone", "A smartphone with a great camera", 800.00)
    manager.create_item(3, "Mouse", "Wireless mouse", 25.99)

    # Reading an item
    manager.read_item(1)

    # Updating an item
    manager.update_item(2, price=750.00)

    # Deleting an item
    manager.delete_item(3)

    # Trying to read a deleted item
    manager.read_item(3)

if __name__ == "__main__":
    main()
