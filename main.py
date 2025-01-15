import tkinter as tk
from tkinter import *

import asyncio
import os
import pickle
import random as rng

import Tamagotchi as Tamgo
import Shop

# Create an instance of the Tamagotchi class

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
        
        try:
            file = open("./Saves/save1.dat", "br")
            self.Tamamochi = pickle.load(file)
            print("Tamamochi loaded from file ", self.Tamamochi.stats)

            self.statsDict = [StringVar(self.root, self.Tamamochi.stats[i]) for i in range(4)]   # Stats Display
        except:
            self.Tamamochi = Tamgo.Tamagotchi()
            self.statsDict = [StringVar(self.root, self.Tamamochi.stats[i]) for i in range(4)]   # Stats Display

        self.storeDictNames = [StringVar(self.root, Store.inventory[i].Name) for i in range(len(Store.inventory))]  # Store Display names
        self.storeDictEffect = [StringVar(self.root, Store.inventory[i].Effect) for i in range(len(Store.inventory))]  # Store Display effect
        self.storeDictDesc = [StringVar(self.root, Store.inventory[i].Description) for i in range(len(Store.inventory))]
        self.storeDictPrice = [StringVar(self.root, Store.inventory[i].Price) for i in range(len(Store.inventory))]


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

        # Save Button
        self.saveButton = tk.Button(text="Save", command=self.save)

        # Label and Button grids
        self.healthLabel.grid(column=0, row=0)
        self.hungerLabel.grid(column=1, row=0)
        self.energyLabel.grid(column=2, row=0)
        self.funLabel.grid(column=3, row=0)

        self.healthStat.grid(column=0, row=6)
        self.hungerStat.grid(column=1, row=6)
        self.energyStat.grid(column=2, row=6)
        self.funStat.grid(column=3, row=6)

        self.healthButton.grid(column=0, row=7)
        self.hungerButton.grid(column=1, row=7)
        self.energyButton.grid(column=2, row=7)
        self.funButton.grid(column=3, row=7)

        self.saveButton.grid(column=4, row=0)

        self.storeButton = tk.Button(text="Store", command=self.open_store).grid(column=4, row=1)

        print("Screen succesfully initialized")

        

    async def display(self):
        """
        This method is the main loop for the Tamagotchi program.
        """
        tick = 0
        while True:
            tick += 1
            if tick % 60 == 0:
                if await self.const_mod_stats(rng.randint(-6, 0), rng.randint(-6, 0), rng.randint(-6, 0), rng.randint(-6, 0)):
                    break
                tick = 0
            self.root.update()
            await asyncio.sleep(.1)



    def save(self):
        file = open("./Saves/save1.dat", "bw")
        pickle.dump(self.Tamamochi, file)
        print("It's save now")



    def open_store(self):
        lenStore = len(Store.inventory)
        self.storeDispName = []
        self.storeDispPrice = []
        self.storeDispEffect = []
        self.storeDispDesc = []

        self.storeButton = []
        for y in range(lenStore):
            self.storeDispName.append(tk.Label(textvariable=self.storeDictNames[y]).grid(column = 5, row=y+y))
            self.storeDispPrice.append(tk.Button(textvariable=self.storeDictPrice[y]).grid(column=5, row=y+y+1))
            self.storeDispEffect.append(tk.Label(textvariable=self.storeDictEffect[y]).grid(column = 6, row=y+y))
            self.storeDispDesc.append(tk.Label(textvariable=self.storeDictDesc[y]).grid(column=6, row=y+y+1))

            self.storeButton.append(tk.Button(text="BUY!", command=lambda: self.storeButton.pop(y)).grid(column=7, row=y+y+1))



    async def const_mod_stats(self, Health, Hunger, Energy, Fun):
        """
        This method modifies the stats of the Tamagotchi by a constant amount.
        """
        self.Tamamochi.mod(Health,Hunger,Energy,Fun)
        if self.death():
            return True
        for i in range(len(self.statsDict)):
            self.statsDict[i].set(self.Tamamochi.stats[i])
            if self.death():
                return True
    
    def mod_stats(self, Health, Hunger, Energy, Fun):
        """
        This method modifies the stats of the Tamagotchi by a given amount.
        """
        self.Tamamochi.mod(Health,Hunger,Energy,Fun)
        for i in range(len(self.statsDict)):
            self.statsDict[i].set(self.Tamamochi.stats[i])
        self.death()



    def death(self):
        """This method is called when the Tamagotchi dies."""
        for stat in self.Tamamochi.stats:
            if stat == 0:
                self.healthButton.destroy()
                self.hungerButton.destroy()
                self.energyButton.destroy()
                self.funButton.destroy()
                
                tk.Label(self.root, text="Your Tamamochi is dead!").grid(columnspan=2, column=1, row=1)
                print("It ded")
                try:
                    os.remove("./Saves/save1.dat")
                except:
                    pass
                return True

     

if __name__ == "__main__":
    asyncio.run(main_loop().start())