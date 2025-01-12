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

# create Screen
class Screen:
    def __init__(self, loop):
        self.loop = loop
        self.root = tk.Tk()
        mainframe = 
        # Give Window a Name
        self.root.title("Tamamochi")

        # Set Tamamochi Stat var1
        self.Health = IntVar(Tamamochi.stats[0])
        self.Hunger = IntVar(Tamamochi.stats[1])
        self.Energy = IntVar(Tamamochi.stats[2])
        self.Fun = IntVar(Tamamochi.stats[3])
        
        self.label

if __name__ == "__main__":
    asyncio.run(TamamochiLoop().start())