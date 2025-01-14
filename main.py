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
        tk.Label(text="Health").grid(column=0, row=0)
        tk.Label(text="Hunger").grid(column=1, row=0)
        tk.Label(text="Energy").grid(column=2, row=0)
        tk.Label(text="Fun").grid(column=3, row=0) 

        # Stats State
        tk.Label(textvariable=self.statsDict[0]).grid(column=0, row=2)
        tk.Label(textvariable=self.statsDict[1]).grid(column=1, row=2)
        tk.Label(textvariable=self.statsDict[2]).grid(column=2, row=2)
        tk.Label(textvariable=self.statsDict[3]).grid(column=3, row=2)

        # Stats Buttons
        tk.Button(text="Heal", command=self.heal).grid(column=0, row=3)
        tk.Button(text="Feed", command=self.feed).grid(column=1, row=3)
        tk.Button(text="Sleep", command=self.sleep).grid(column=2, row=3)
        tk.Button(text="Play", command=self.play).grid(column=3, row=3)

        print("Screen succesfully init")

    # 'Tis be the loop for reducing stats
    async def display(self):
        """
        This method is the main loop for the Tamagotchi program.
        """
        tick = 0
        print("Ticks succesfully started")
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
                self.root.children.clear()
                tk.Label(self.root, text="Your Tamamochi is dead!").grid(columnspan=2, column=1, row=1)
                    

if __name__ == "__main__":
    asyncio.run(TamamochiLoop().start())



