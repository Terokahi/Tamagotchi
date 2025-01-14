import tkinter as tk
from tkinter import *

import asyncio
import random as rng

import Tamagotchi as Tamgo
import Shop

# Create an instance of the Tamagotchi class
Tamamochi = Tamgo.Tamagotchi()

from tkinter import *
# Create an instance of the shop class
Store = Shop.shop()

# Start the Loop
class main_loop:
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
        self.healthButton = tk.Button(text="Heal", command=lambda: 
                                      self.mod_stats(rng.randint(20, 40), rng.randint(-12, 0), rng.randint(-12, 0), rng.randint(-12, 0)))
        
        self.hungerButton = tk.Button(text="Feed", command=lambda: 
                                      self.mod_stats(rng.randint(-12, 0), rng.randint(20, 40), rng.randint(-12, 0), rng.randint(-12, 0)))
        
        self.energyButton = tk.Button(text="Sleep", command=lambda: 
                                      self.mod_stats(rng.randint(-12, 0), rng.randint(-12, 0), rng.randint(20, 40), rng.randint(-12, 0)))
        
        self.funButton = tk.Button(text="Play", command=lambda: 
                                      self.mod_stats(rng.randint(-12, 0), rng.randint(-12, 0), rng.randint(-12, 0), rng.randint(20,40)))

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
        while True:
            tick += 1
            if tick % 30 == 0:
                if await self.const_mod_stats(rng.randint(-12, 0), rng.randint(-12, 0), rng.randint(-12, 0), rng.randint(-12, 0)):
                    break
                tick = 0
            self.root.update()
            await asyncio.sleep(.1)

    async def const_mod_stats(self, Health, Hunger, Energy, Fun):
        """
        This method modifies the stats of the Tamagotchi by a constant amount.
        """
        Tamamochi.mod(Health,Hunger,Energy,Fun)
        if self.death():
            return True
        for i in range(len(self.statsDict)):
            self.statsDict[i].set(Tamamochi.stats[i])
            if self.death():
                return True
    
    def mod_stats(self, Health, Hunger, Energy, Fun):
        """
        This method modifies the stats of the Tamagotchi by a given amount.
        """
        Tamamochi.mod(Health,Hunger,Energy,Fun)
        for i in range(len(self.statsDict)):
            self.statsDict[i].set(Tamamochi.stats[i])
        self.death()

    def death(self):
        """This method is called when the Tamagotchi dies."""
        for stat in Tamamochi.stats:
            if stat == 0:
                self.healthButton.destroy()
                self.hungerButton.destroy()
                self.energyButton.destroy()
                self.funButton.destroy()
                
                tk.Label(self.root, text="Your Tamamochi is dead!").grid(columnspan=2, column=1, row=1)
                print("It ded")
                return True
        

if __name__ == "__main__":
    asyncio.run(main_loop().start())



