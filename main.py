import tkinter as tk
from tkinter import *

import asyncio

import Tamagotchi as Tamgo
import Shop

# Create an instance of the Tamagotchi class
Tamamochi = Tamgo.Tamagotchi()

from tkinter import *
# Create an instance of the shop class
Store = Shop.shop()

# Start the Loop
class TamamochiLoop:
    """
    This class is the main loop for the Tamagotchi program.
    """
    async def start(self):
        """
        This method starts the main loop.
        """
        self.Window = Screen(asyncio.get_event_loop())
        await self.Window.display()

# create Screen
class Screen:
    """
    This class creates the main screen for the Tamagotchi program.
    """
    def __init__(self, loop):
        """
        This method initializes the screen.
        """
        self.loop = loop
        self.root = tk.Tk()

        # Give Window a Name
        self.root.title("Tamamochi")
        
        # Stats Display
        self.statsDict = [StringVar(self.root, Tamamochi.stats[i]) for i in range(4)]
        
        # Stats Labels
        self.healthLabel = tk.Label(text="Health")
        self.hungerLabel = tk.Label(text="Hunger")
        self.energyLabel = tk.Label(text="Energy")
        self.funLabel = tk.Label(text="Fun") 

        # Stats State
        self.healthStat = tk.Label(textvariable=self.statsDict[0])
        self.hungerStat = tk.Label(textvariable=self.statsDict[1])
        self.energyStat = tk.Label(textvariable=self.statsDict[2])
        self.funStat = tk.Label(textvariable=self.statsDict[3])

        # Stats Buttons
        self.healthButton = tk.Button(text="Heal", command=self.heal)
        self.hungerButton = tk.Button(text="Feed", command=self.feed)
        self.energyButton = tk.Button(text="Sleep", command=self.sleep)
        self.funButton = tk.Button(text="Play", command=self.play)

        # Label and Button grids
        self.healthLabel.grid(column=0, row=0)
        self.hungerLabel.grid(column=1, row=0)
        self.energyLabel.grid(column=2, row=0)
        self.funLabel.grid(column=3, row=0)

        self.healthStat.grid(column=0, row=2)
        self.hungerStat.grid(column=1, row=2)
        self.energyStat.grid(column=2, row=2)
        self.funStat.grid(column=3, row=2)

        self.healthButton.grid(column=0, row=3)
        self.hungerButton.grid(column=1, row=3)
        self.energyButton.grid(column=2, row=3)
        self.funButton.grid(column=3, row=3)

        print("Screen succesfully initialized")

    # 'Tis be the loop for reducing stats
    async def display(self):
        """
        This method is the main loop for the Tamagotchi program.
        """
        tick = 0
        print("Ticks succesfully initialized")
        while True:
            if tick % 300 == 0:
                await self.const_mod_stats()
                tick = 0
            self.root.update()
            await asyncio.sleep(.1)
            tick += 1

    async def const_mod_stats(self, Health=-3, Hunger=-2, Energy=-1, Fun=-15):
        """
        This method modifies the stats of the Tamagotchi by a constant amount.
        """
        Tamamochi.mod(Health,Hunger,Energy,Fun)
        for i in range(len(self.statsDict)):
            self.statsDict[i].set(Tamamochi.stats[i])
        self.death()
    
    def mod_stats(self, Health=-6, Hunger=-4, Energy=-3, Fun=-12):
        """
        This method modifies the stats of the Tamagotchi by a given amount.
        """
        Tamamochi.mod(Health,Hunger,Energy,Fun)
        for i in range(len(self.statsDict)):
            self.statsDict[i].set(Tamamochi.stats[i])
        self.death()

    def heal(self):
        """
        This method increases the health of the Tamagotchi by 24.
        """
        self.mod_stats(Health=24)
    def feed(self):
        """
        This method increases the hunger of the Tamagotchi by 23.
        """
        self.mod_stats(Hunger=23)
    def sleep(self):
        """
        This method increases the energy of the Tamagotchi by 8.
        """
        self.mod_stats(Energy=32)
    def play(self):
        """
        This method increases the fun of the Tamagotchi by 46.
        """
        self.mod_stats(Fun=46)

    def death(self):
        """This method is called when the Tamagotchi dies."""
        for stat in Tamamochi.stats:
            if stat == 0:
                self.healthButton.grid_forget()
                self.hungerButton.grid_forget()
                self.energyButton.grid_forget()
                self.funButton.grid_forget()
                
                tk.Label(self.root, text="Your Tamamochi is dead!").grid(columnspan=2, column=1, row=1)
                print("It ded")

if __name__ == "__main__":
    asyncio.run(TamamochiLoop().start())



