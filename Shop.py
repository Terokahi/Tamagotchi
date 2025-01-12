import Items

class shop:
    """
    A class representing a shop that holds an inventory of items. The items are
    loaded from a text file upon initialization.
    """
    inventory = []  # Class attribute to hold the list of items available in the shop

    def __init__(self):
        """
        Initializes the shop by loading items from a text file and populating
        the inventory. Each item's attributes are extracted from the file.
        """
        # Create a new item instance
        Item = Items.Items()

        # Open and read the items list file line by line
        with open("ItemsList.txt") as f:
            alist = [line.rstrip() for line in f]

        # Process each line to extract item attributes and populate the inventory
        for line in alist:
            if "Name" in line:
                Item.Name = line[5:]  # Extract the item name
            elif "Effect" in line:
                Item.Effect = line[7:]  # Extract the item effect
            elif "Description" in line:
                Item.Description = line[12:]  # Extract the item description
            elif "Price" in line:
                Item.Price = line[6:]  # Extract the item price
                self.inventory.append(Item)  # Add the item to the inventory
                Item = Items.Items()  # Create a new item instance for the next item
