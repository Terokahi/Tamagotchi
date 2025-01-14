class Tamagotchi:
    """
    A Tamagotchi is a digital pet that you must take care of.
    The Tamagotchi has four attributes: health, hunger, energy, and fun.
    """
    def __init__(self):
        # The self's attributes start at 100 by default, representing full levels.
        self.health = 100  # The health of the self, starts at 100
        self.hunger = 100  # The hunger level of the self, starts at 100
        self.energy = 100  # The energy level of the self, starts at 100
        self.fun = 100     # The fun level of the self, starts at 100
        self.stats = [self.health, self.hunger, self.energy, self.fun]


    def mod(self, modHealth, modHunger, modEnergy, modFun):
        """
        Modifies the stats of the Tamagotchi by the given values.

        :param modHealth: The amount to modify the health by.
        :param modHunger: The amount to modify the hunger by.
        :param modEnergy: The amount to modify the energy by.
        :param modFun: The amount to modify the fun by.
        """
        modStats =[modHealth, modHunger, modEnergy, modFun]
        for i in range(len(self.stats)):
            if self.stats[i] + modStats[i] <= 0:
                self.stats[i] = 0
            elif self.stats[i] + modStats[i] >= 100:
                self.stats[i] = 100
            else:
                self.stats[i] += modStats[i]