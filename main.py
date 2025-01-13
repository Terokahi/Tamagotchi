import tkinter as tk
from tkinter import *
from tkinter import ttk
import Tamagotchi as Tg
import Shop
import asyncio

# Create an instance of the Tamagotchi class
Tamamochi = Tg.Tamagotchi()
# Create an instance of the shop class
Store = Shop.shop()

# Start the Loop
class TamamochiLoop:
    async def start(self):
        self.Window = Screen(asyncio.get_event_loop())
        await self.Window.display()

# create Screen
class Screen:
    def __init__(self, loop):
        self.loop = loop
        self.root = tk.Tk()
        
        # Give Window a Name
        self.root.title("Tamamochi")
        
        # Stats Display
        self.Health = IntVar(Tamamochi.stats[0])
        self.Hunger = IntVar(Tamamochi.stats[1])
        self.Energy = IntVar(Tamamochi.stats[2])
        self.Fun = IntVar(Tamamochi.stats[3])
        
        # Stats Labels
        self.healthLabel = tk.Label(text="Health").grid(column=0, row=0)
        
        self.hungerLabel = tk.Label(text="Hunger").grid(column=0, row=1)
        
        self.energyLabel = tk.Label(text="Energy").grid(column=0, row=2)

        self.funLabel = tk.Label(text="Fun").grid(column=0, row=3) 

        # Stats State
        self.healthStat = tk.Label(textvariable=self.Health).grid(column=1, row=0)
        self.hungerStat = tk.Label(textvariable=self.Hunger).grid(column=1, row=1)
        self.energyStat = tk.Label(textvariable=self.Energy).grid(column=1, row=2)
        self.funStat = tk.Label(textvariable=self.Fun).grid(column=1, row=3)

        # Stats Buttons

        print("Screen succesfully init")

    # 'Tis be the loop for reducing stats
    async def display(self):
        while True:        
            self.root.update()
            await asyncio.sleep(.5)
    
if __name__ == "__main__":
    asyncio.run(TamamochiLoop().start())