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
        await asyncio.sleep(.5)

# create Screen
class Screen:
    def __init__(self, loop):
        self.loop = loop
        self.root = tk.Tk()
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        
        # Give Window a Name
        self.root.title("Tamamochi")

        # Stats Display
        self.Health = Tamamochi.stats[0]
        self.Hunger = Tamamochi.stats[1]
        self.Energy = Tamamochi.stats[2]
        self.Fun = Tamamochi.stats[3]
        
        # Stats Labels
        self.healthLabel = tk.Label(self.mainframe, text="Health").grid(column=0, row=0),
        self.hungerLabel = tk.Label(self.mainframe, text="Hunger").grid(column=0, row=1),
        self.energyLabel = tk.Label(self.mainframe, text="Energy").grid(column=0, row=2),
        self.funLabel = tk.Label(self.mainframe, text="Fun").grid(column=0, row=3)

        # Stats State
        self.healthStat = tk.Label(self.mainframe, textvariable=self.Health).grid(column=1, row=0)
        self.hungerStat = tk.Label(self.mainframe, textvariable=self.Hunger).grid(column=1, row=1)
        self.energyStat = tk.Label(self.mainframe, textvariable=self.Energy).grid(column=1, row=2)
        self.funStat = tk.Label(self.mainframe, textvariable=self.Fun).grid(column=1, row=3)

        # Stats Buttons
        self.healthButton = tk.Button(self.mainframe, text="Bandage", command=modStats())
    
    async def modStats(Health = -10, Hunger = -5, Energy = -4, Fun = -14):
        Tamamochi.mod(Health, Hunger, Energy, Fun)
        
    
    async def display(self):
        pass

if __name__ == "__main__":
    asyncio.run(TamamochiLoop().start())