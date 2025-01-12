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

    def heal(self):
        """
        Increases the health of the Tamagotchi by 50.
        This method ensures that the health does not exceed 100.
        Returns the updated health value.
        """
        self.health += 50       # Increase health by 50
        if self.health > 100:   # Ensure health does not exceed 100
            self.health = 100
        return self.health      # Return the updated health value

    def feed(self):
        """
        Increases the hunger of the Tamagotchi by 25.
        This method ensures that the hunger does not exceed 100.
        Returns the updated hunger value.
        """
        self.hunger += 25       # Increase hunger by 25
        if self.hunger > 100:   # Ensure hunger does not exceed 100
            self.hunger = 100
        return self.hunger      # Return the updated hunger value

    def play(self):
        """
        Increases the fun of the Tamagotchi by 10.
        This method ensures that the fun does not exceed 100.
        Returns the updated fun value.
        """
        self.fun += 10      # Increase fun by 10
        if self.fun > 100:  # Ensure fun does not exceed 100
            self.fun = 100
        return self.fun     # Return the updated fun value

    def sleep(self):
        """
        Increases the energy of the Tamagotchi by 20.
        This method ensures that the energy does not exceed 100.
        Returns the updated energy value.
        """
        self.energy += 20       # Increase energy by 20
        if self.energy > 100:   # Ensure energy does not exceed 100
            self.energy = 100
        return self.energy      # Return the updated energy value

    def loseHealth(self, value=10):
        """
        Decreases the health of the Tamagotchi by the given value.
        If no value is provided, defaults to subtracting 10.
        Returns the updated health value.
        """
        self.health -= value    # Decrease health by the specified value
        if self.health <= 0:    # Ensure health does not drop below 0
            self.health = 0
        return self.health      # Return the updated health value

    def loseHunger(self, value=5):
        """
        Decreases the hunger of the Tamagotchi by the given value.
        If no value is provided, defaults to subtracting 5.
        Returns the updated hunger value.
        """
        self.hunger -= value    # Decrease hunger by the specified value
        if self.hunger <= 0:    # Ensure hunger does not drop below 0
            self.hunger = 0
        return self.hunger      # Return the updated hunger value

    def loseFun(self, value=2):
        """
        Decreases the fun of the Tamagotchi by the given value.
        If no value is provided, defaults to subtracting 2.
        Returns the updated fun value.
        """
        self.fun -= value   # Decrease fun by the specified value
        if self.fun <= 0:   # Ensure fun does not drop below 0
            self.fun = 0
        return self.fun     # Return the updated fun value

    def loseEnergy(self, value=30):
        """
        Decreases the energy of the Tamagotchi by the given value.
        If no value is provided, defaults to subtracting 30.
        Returns the updated energy value.
        """
        self.energy -= value    # Decrease energy by the specified value
        if self.energy <= 0:    # Ensure energy does not drop below 0
            self.energy = 0
        return self.energy      # Return the updated energy value

