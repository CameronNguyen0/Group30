
# Importing modules required.
from __future__ import annotations      # Module used for getting functionalities within the newer version of Python.
from abc import ABC, abstractmethod     # Module used for defining abstract methods.
from random_gen import RandomGen                      # Module used for generating random values.

"""
File Description:
This file contains the implementation of Task 1 of Assignment 2 for the unit FIT1008 of Monash University. The
file implements the class PokemonBase whose purpose is to create a template that can be used to implement future
Pokemons in the subsequent task.

Date Last Modified: Wednesday, 14th of September, 2022
Contributions: Khanh Gia (Ryan) Nguyen, Amy Dang
"""

# The original author that established this file.
__author__ = "Scaffold by Jackson Goerner, Code by Amy Dang"


# Implementation of PokemonBase class.
class PokemonBase(ABC):
    # Initialiser method or constructor for creating a PokemonBase for a certain Pokemon.
    def __init__(self, hp: int, poke_type: str) -> None:



        """ Constructor for the PokemonBase of a Pokemon and set the initialised values into that PokemonBase.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: The best and worst case is O(1), because we are just defining variables.
        """

        # Table of multipliers for each Pokemon attack (refer to Page 3 of the Assignment 2 Specification Sheet for more detail).
        self.multiplier = [[1, 2, 0.5, 1, 1], [0.5, 1, 2, 1, 1], [2, 0.5, 1, 1, 1], [1.25, 1.25, 1.25, 2, 0], [1.25, 1.25, 1.25, 0, 1]]

        # Array of status effects to be used (as specified in the Assignment Specification). # Pretty sure can't have this.
        self.status_things = ['burn', 'poison', 'paralysis', 'sleep', 'confusion']

        # A dictionary of the order of the position of the Pokemon types. # Only allowed list for calculations.
        self.list_position_dict = {'fire': 0, 'grass': 1, 'water': 2, 'ghost': 3, 'normal': 4}

        self.hp = hp                                                    # Defines the HP of the Pokemon.       
        self.poke_type = poke_type                                      # Defines the type of the Pokemon.
        self.level = 1                                                  # Defines the level of the Pokemon (initialised to level 1).
        self.status_effect = None                                       # Defines if the Pokemon is currently being affected by any status effect.
        self.list_position = self.list_position_dict[self.poke_type]         # Defines the position of that Pokemon types for the Pokemon given its type.
        self.attack_multiplier = self.multiplier[self.list_position]         # Defines the attack multiplier of the Pokemon given it's position in Pokemon types.
        self.status_inflict = self.status_things[self.list_position]         # Define the status effect of the Pokemon's attack given it's position in Pokemon types.
        self.attack_self = False

    def get_hp(self) -> int:
        return self.hp
    
    def get_level(self) -> int:
        return self.level

    # Method to determine if the Pokemon has fainted.
    def is_fainted(self) -> bool:
        """ Pokemon health equalling 0 will result in fainting, and this method implements it.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: The best and worst case is O(1), because there is one comparison of integer values and then just return.
        """
        return (self.hp <= 0)

    # Abstract method to level up a Pokemon.
    @abstractmethod
    def level_up(self) -> None:
        """ This abstract method acts as a template to level up a Pokemon; its implementation is abstract because changing 
        the level of a Pokemon affects the HP of that Pokemon, which requires changing with each Pokemon, and it is unique
        to that Pokemon.
        :pre: <not >implemented
        :post: <not implemented>
        :complexity: 
        """
        pass

    # Abstract method to return the speed of a Pokemon.
    @abstractmethod
    def get_speed(self) -> int:
        """ This abstract method acts as a template to return the speed of the Pokemon; it is abstract because each Pokemon
        has a unique definition of what their speed is, which is implemented in the next task.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity:
        """
        pass

    # Abstract method to return the attack damage of a Pokemon.
    @abstractmethod
    def get_attack_damage(self) -> int:
        """ This abstract method acts a template to return the attack damage of the Pokemon; it is abstract because each Pokemon
        has a unique definition of what their attack damage is (implemented in the next task and its formula is in assignment
        specifications).
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: <not implemented>
        """
        pass

    # Abstract method to return the defence value of a Pokemon.
    @abstractmethod
    def get_defence(self) -> int:
        """ This abstract method acts a template to return the defence value of the Pokemon; it is abstract because each Pokemon
        has a unique definition of what their defence value is (implemented in the next task and its formula is in assignment
        specifications).
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: <not implemented>
        """
        pass

    # Method to decrease the HP from what is lost.
    def lose_hp(self, lost_hp: int) -> None:
        """ This method takes in an integer value, representing the amount HP lost, then it decrease the Pokemon's HP from the 
        input HP.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best = Worst = O(1)
       
        """
        self.hp -= lost_hp

    # Abstract method to perform the defence calculation of the Pokemon.
    @abstractmethod
    def defend(self, damage: int) -> None:
        """ This abstract method acts as a template to perform the defence calculation required by the specification; it is 
        abstract because each Pokemon has unique defence calculations and thus requires implementation in the following task. 
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: <not implemented>
        """
        pass

    # Method to perform the attack towards Pokemon.
    def attack(self, other: PokemonBase) -> None:
        """ Given the other Pokemon's base, this method implements the attack procedure as stated in the specification.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best = Worst = O(1)
        """
        # Step 1: Status effects on attack damage / redirecting attacks.
        # If the attacking Pokemon is asleep, stop the attack.
        if self.status_effect == 'sleep':
            return None


        # Step 2: Do the attack.
        # Calculates the effective attack that the attacking Pokemon would do on the defending Pokemon with the multiplier.
        # self.attack_multiplier is an array, other.list_position determines which multiplier.
        effective_attack = self.get_attack_damage() * self.attack_multiplier[other.list_position]     

        # If status effect is burn, then half the effective_attack.
        if self.status_effect == 'burn':
            effective_attack = effective_attack//2

        # If status effect is confusion, then you have 50% chance to attack yourself.
        if self.status_effect == 'confusion':
            if RandomGen.random_chance(0.5) == True:    # Checking (with 50% chance) whether or not to not attack yourself.
                self.attack_self = True    
                # When attacking yourself, multiply your current attacking damage with the multiplier for your type.
                self.defend(self.get_attack_damage() * self.multiplier[self.list_position][self.list_position])
            else:
                self.attack_self = False   

        # Call defend for the defending Pokemon to calculate how much HP is lost from the attack to them.
        if self.attack_self == False:
            other.defend(effective_attack)
        elif self.attack_self == True:
            effective_attack = self.get_attack_damage() * self.attack_multiplier[self.list_position]
            self.defend(effective_attack)
        
        # Step 3: Losing hp to status effects + applying status effects
        # Check if infliction of status effect occurs.
        if self.attack_self == False and RandomGen.random_chance(0.2) == True:
            other.status_effect = self.status_things[self.list_position]
            if self.status_inflict == 'burn':
                other.lose_hp(1)
            if self.status_inflict == 'poison':
                other.lose_hp(3)
        # Check if infliction of status effect occurs to self.
        if self.attack_self == True and RandomGen.random_chance(0.2) == True:
            self.status_effect = self.status_things[self.list_position]
            if self.status_inflict == 'burn':
                self.lose_hp(1)             
            if self.status_inflict == 'poison':
                self.lose_hp(3)

    # Abstract method to retrive the Pokemon's name.
    @abstractmethod
    def get_poke_name(self) -> str:
        """ <not implemented>
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: <not implemented>
        """
        pass

    # ??? What is this function for?
    #CLARIFY (is abstraction needed if get_poke_name is abstract?)
    def __str__(self) -> str:
        return f"LV. {self.level} {self.get_poke_name()}: {self.hp} HP"

    # Abstract method to determine if the Pokemon should evolve.  
    @abstractmethod
    def should_evolve(self) -> bool:
        """ <not implemented>
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: <not implemented>
        """
        pass
    
    # Abstract method to determine whether or not the Pokemon can evolve anymore.
    @abstractmethod
    def can_evolve(self) -> bool:
        """ <not implemented>
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: <not implemented>
        """
        pass

    # Abstract method to get the evolved version of the Pokemon.
    @abstractmethod
    def get_evolved_version(self) -> PokemonBase:
        """ <not implemented>
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: <not implemented>
        """
        pass
