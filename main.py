from tkinter import *
from tkinter import ttk
import Tamagotchi as Tg
import Shop
import asyncio

# Create an instance of the Tamagotchi class
Tamamochi = Tg.Tamagotchi()
# Create an instance of the shop class
Store = Shop.shop()

class screen:
    """Creates the main window for the Tamagotchi game."""

    mainframe = None

    def __init__(self, root):
        """
        Initializes the main window.

        :param root: The root window.
        """
        # Set the title of the root window
        root.title("Tamamochi")

        # Create the main frame with padding and place it in the root window
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Initialize the StringVar variables to track Tamamochi's attributes
        self.health = StringVar(value=Tamamochi.stats[0])
        self.hunger = StringVar(value=Tamamochi.stats[1])
        self.fun = StringVar(value=Tamamochi.stats[2])
        self.energy = StringVar(value=Tamamochi.stats[3])
        
        # Create labels for each attribute
        ttk.Label(self.mainframe, text="Health").grid(column=0, row=0, sticky=(N))
        ttk.Label(self.mainframe, text="Hunger").grid(column=1, row=0, sticky=(N))
        ttk.Label(self.mainframe, text="Fun").grid(column=2, row=0, sticky=(N))
        ttk.Label(self.mainframe, text="Energy").grid(column=3, row=0, sticky=(N))

        # Create labels bound to each StringVar to display the current values
        ttk.Label(self.mainframe, textvariable=self.health).grid(column=0, row=1)
        ttk.Label(self.mainframe, textvariable=self.hunger).grid(column=1, row=1)
        ttk.Label(self.mainframe, textvariable=self.fun).grid(column=2, row=1)
        ttk.Label(self.mainframe, textvariable=self.energy).grid(column=3, row=1)

        # Create buttons to interact with Tamamochi's attributes
        ttk.Button(self.mainframe, text="Bandage", command=self.setHealth).grid(column=0, row=4, sticky=(S, W))
        ttk.Button(self.mainframe, text="Feed", command=self.setHunger).grid(column=1, row=4, sticky=(S))
        ttk.Button(self.mainframe, text="Play", command=self.setFun).grid(column=2, row=4, sticky=(S))
        ttk.Button(self.mainframe, text="Sleep", command=self.setEnergy).grid(column=3, row=4, sticky=(S, E))

        # Create Button to open shop
        ttk.Button(self.mainframe, text="Shop", command=self.openShop).grid(column=4, row=2, sticky=(E))

    def openShop(self, *args):
        """Opens the shop to buy items."""
        for nr in range(len(Store.inventory)):
            print(Store.inventory[nr].Name)
            print(Store.inventory[nr].Effect)
            print(Store.inventory[nr].Description)
            print(Store.inventory[nr].Price)
            print("\n'TIS BE THE END!\n")

    async def modStats(self, health=-5, hunger=-10, energy=-4, fun=-15):
        """
        Modifies the stats of Tamamochi.

        :param health: Health modification amount.
        :param hunger: Hunger modification amount.
        :param energy: Energy modification amount.
        :param fun: Fun modification amount.
        """
        Tamamochi.mod(health, hunger, energy, fun)
        self.health.set(Tamamochi.stats[0])
        self.hunger.set(Tamamochi.stats[1])
        self.fun.set(Tamamochi.stats[2])
        self.energy.set(Tamamochi.stats[3])
        
        self.death()

    def setHealth(self, *args):
        """Increases the health of the Tamamochi."""
        asyncio.run(self.modStats(health=10))

    def setHunger(self, *args):
        """Increases the hunger of the Tamamochi."""
        asyncio.run(self.modStats(hunger=20))
        
    def setFun(self, *args):
        """Increases the fun of the Tamamochi."""
        asyncio.run(self.modStats(energy=8))

    def setEnergy(self, *args):
        """Increases the energy of the Tamamochi."""
        asyncio.run(self.modStats(fun=30))
    
    def death(self, *args):
        """Checks if the Tamamochi is dead."""
        if Tamamochi.stats[0] <= 0:
            # Destroy all children of the mainframe and display death message
            for child in self.mainframe.winfo_children():
                child.master.destroy()
            ttk.Label(master=None, text="Your Tamamochi is dead").grid(column=1, row=1, sticky=(N, E, S, W))
        if Tamamochi.stats[1] <= 0:
            # Destroy all children of the mainframe and display starvation message
            for child in self.mainframe.winfo_children():
                child.master.destroy()
            ttk.Label(master=None, text="Your Tamamochi starved!").grid(column=1, row=1, sticky=(N, E, S, W))

# Create the Tkinter application window
root = Tk()
# Initialize the screen class
screen(root)

# Start the main loop of the Tkinter application
root.mainloop()