class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def display_list(self):
        print("Shopping List:")
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item}")
        print()

class ShoppingCart:
    def __init__(self, shopping_list):
        self.shopping_list = shopping_list

    def add_item_to_cart(self, item):
        self.shopping_list.add_item(item)
        print(f"Added {item} to the shopping list.")

    def remove_item_from_cart(self, item):
        self.shopping_list.remove_item(item)
        print(f"Removed {item} from the shopping list.")

    def display_cart(self):
        self.shopping_list.display_list()

if __name__ == "__main__":
    shared_shopping_list = ShoppingList()

    user1_cart = ShoppingCart(shared_shopping_list)
    user2_cart = ShoppingCart(shared_shopping_list)

    # User 1 adds items to the shopping list
    user1_cart.add_item_to_cart("Apples")
    user1_cart.add_item_to_cart("Milk")
    user1_cart.display_cart()

    # User 2 removes an item from the shopping list
    user2_cart.remove_item_from_cart("Apples")
    user2_cart.display_cart()

    # User 1 adds more items
    user1_cart.add_item_to_cart("Eggs")
    user1_cart.add_item_to_cart("Bread")
    user1_cart.display_cart()

    # Display the final shopping list
    shared_shopping_list.display_list()
