# Importing modules required.
# from pokemon import Venusaur
#from base_test import BaseTest      # Module for testing the functionalities.  
from pokemon_base import PokemonBase      # Module for access to the base class in Task 1.

"""
File Description:
This file contains the implementation of Task 2 of Assignment 2 for the unit FIT1008 of Monash University. The
file implements the class Pokemon whose purpose is to create various types of Pokemon for future implementation 
in Pokemon battles.

Date Last Modified: Wednesday, 17th of September, 2022
Contributions: Khanh Gia (Ryan) Nguyen, Amy Dang, Cameron Nguyen
"""

# The original author that established this file.
__author__ = "Scaffold by Jackson Goerner, Code by Amy Dang and Vonara"

# Implementing the Pokemon Charizard, child class of PokemonBase.AssertionError
class Charizard(PokemonBase):

    # Initialiser method for Charizard HPs and other attributes.
    def __init__(self, non_evolved_pokemon: PokemonBase) -> None:
        """ This method initialises Charizard to its base attributes.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case is O(1).
        """  
        self.hp = non_evolved_pokemon.hp
        self.status_effect = non_evolved_pokemon.status_effect
        PokemonBase.__init__(self, self.hp, "fire")
        self.level = 3

    
    def reset_hp(self) -> None:
        """  This method resets HP when heal action is taken.
        :pre:
        :post:
        :complexity: Best case and worst case if O(1).
        """
        self.hp = (12 + 1 * self.level)
        
    def level_up(self) -> None:
        """ This method level up Charizard to the parameters set within the specification and also
        adjust its HP to match its corresponding level.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case is O(1).
        """
        # Adjust HP to match that of the pokemon's level.
        lost_hp = (12 + 1 * self.level) - self.hp
        self.level += 1     # Level up Charizard.
        self.hp = (12 + 1 * self.level) - lost_hp

    def get_speed(self) -> int:
        """ This method gets the speed of Charizard base on the level and parameters set out by the
        specification.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case is O(1).
        """
        if self.status_effect == 'paralysis':
            return (9 + 1 * self.level)//2
        return 9 + 1 * self.level 

    def get_attack_damage(self) -> int:
        """ This method gets the attacking damage Charizard base on its level.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case is O(1).
        """
        return 10 + 2 * self.level

    def get_defence(self) -> int:
        """ This method gets the defence points of Charizard.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case is O(1).
        """
        return 4

    def defend(self, damage: int) -> None:
        """ This method calculate how Charizard will defend against an attack as shown in the
        specification.
        :pre: get_defence must return an integer
              damage must be an integer
        :post: <not implemented>
        :complexity: Best case and worst case is O(1).
        """
        if get_defence(self) < damage:
            lose_hp(self, 2*damage)
        else: 
            lose_hp(self, damage)

    def get_poke_name(self) -> str:
        """ This method retrieves the name of the Pokemon which is Charizard.
        :pre: <not implemented>
        :post:  <not implemented>
        :complexity: Best case and worst case is O(1).
        """
        return 'Charizard'

    def should_evolve(self) -> bool:
        """ This method determines is the Pokemon should evolve, and as Charizard is at the last
        stage of its evolution, it cannot and should not evolve.
        :pre:
        :post:
        :complexity: Best case and worst case is O(1).
        """
        return False

    def can_evolve(self) -> bool:
        """ This method determines is the Pokemon can evolve, and as Charizard is at the last
        stage of its evolution, it cannot and should not evolve.
        :pre:
        :post:
        :complexity: Best case and worst case is O(1).
        """
        return False

    def get_evolved_version(self) -> None:
        """ This method finds the evolved version of Charizard, and since it is at its last stage
        it has no evolved version.
        :pre:
        :post:
        :complexity: Best case and worst case if O(1).
        """
        pass
"""all following functions have similar"""
    
class Charmander(PokemonBase):
    def __init__(self) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        PokemonBase.__init__(self, 9, "fire")

    def reset_hp(self) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        self.hp = (8 + 1 * self.level)
        
    def level_up(self) -> None:
        """ This method adjusts hp to match that of the pokemon's level.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        lost_hp = (8 + 1 * self.level) - self.hp
        self.level += 1
        self.hp = (8 + 1 * self.level) - lost_hp

    def get_speed(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        if self.status_effect == 'paralysis':
            return (7 + 1 * self.level)//2
        return 7 + 1 * self.level 

    def get_attack_damage(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 6 + 1 * self.level

    def get_defence(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 4

    def defend(self, damage: int) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        if get_defence(self) < damage:
            lose_hp(self, damage)
        else: 
            lose_hp(self, damage//2)

    def get_poke_name(self) -> str:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 'Charmander'

    def should_evolve(self) -> bool:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        if self.level >= 3:
            return True
        return False

    def can_evolve(self) -> bool:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return True

    ########## IDK IF CORRECT ########################
    def get_evolved_version(self) -> PokemonBase:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return Charizard(self)

class Venusaur(PokemonBase):
    def __init__(self, non_evolved_pokemon: PokemonBase) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        self.hp = non_evolved_pokemon.hp
        self.status_effect = non_evolved_pokemon.status_effect
        PokemonBase.__init__(self, self.hp, "grass")
        self.level = 2
        
    def reset_hp(self) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        self.hp = (20 + self.level//2)

    def level_up(self) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        lost_hp = (20 + self.level//2) - self.hp
        self.level += 1
        self.hp = (20 + self.level//2) - lost_hp

    def get_speed(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        if self.status_effect == 'paralysis':
            return (3 + self.level//2)//2
        return 3 + self.level//2

    def get_attack_damage(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 5

    def get_defence(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 10

    def defend(self, damage: int) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        if (get_defence(self) + 5) < damage:
            lose_hp(self, damage)
        else: 
            lose_hp(self, damage//2)

    def get_poke_name(self) -> str:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 'Venusaur'

    def should_evolve(self) -> bool:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return False

    def can_evolve(self) -> bool:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return False

    def get_evolved_version(self):
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        pass

class Bulbasaur(PokemonBase):
    def __init__(self):
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        PokemonBase.__init__(self, 13, "grass")

    def reset_hp(self) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        self.hp = (12 + 1 * self.level)
        
    def level_up(self) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        lost_hp = (12 + 1 * self.level) - self.hp
        self.level += 1
        self.hp = (12 + 1 * self.level) - lost_hp

    def get_speed(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        if self.status_effect == 'paralysis':
            return (7 + self.level//2)//2
        return 7 + self.level //2

    def get_attack_damage(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 5

    def get_defence(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 5

    def defend(self, damage: int) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        if (get_defence(self) + 5) < damage:
            lose_hp(self, damage)
        else: 
            lose_hp(self, damage//2)

    def get_poke_name(self) -> str:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 'Bulbasaur'

    def should_evolve(self) -> bool:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        if self.level >= 2:
            return True
        return False

    def can_evolve(self) -> bool:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return True

    ########## IDK IF CORRECT ########################
    def get_evolved_version(self) -> PokemonBase:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return Venusaur(self)


class Blastoise(PokemonBase):
    def __init__(self, non_evolved_pokemon: PokemonBase) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        self.hp = non_evolved_pokemon.hp
        self.status_effect = non_evolved_pokemon.status_effect
        PokemonBase.__init__(self, self.hp, "water")
        self.level = 3

    def reset_hp(self) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        self.hp = (15 + 2 * self.level)

    def level_up(self) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        lost_hp = (15 + 2 * self.level) - self.hp 
        self.level += 1
        self.hp = (15 + 2 * self.level) - lost_hp

    def get_speed(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        if self.status_effect == 'paralysis':
            return 10//2
        return 10

    def get_attack_damage(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 8 + (self.level//2)

    def get_defence(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 8 + 1 * self.level
    
    def defend(self, damage: int) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        if (get_defence(self)*2) < damage:
            lose_hp(self, damage)
        else: 
            lose_hp(self, damage//2)

    def get_poke_name(self) -> str:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 'Blastoise'

    def should_evolve(self) -> bool:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return False

    def can_evolve(self) -> bool:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return False

    def get_evolved_version(self):
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        pass


class Squirtle(PokemonBase):
    def __init__(self):
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        PokemonBase.__init__(self, 11, "water")

    def reset_hp(self) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        self.hp = (9 + 2 * self.level)
        
    def level_up(self) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        lost_hp = (9 + 2 * self.level) - self.hp
        self.level += 1
        self.hp = (9 + 2 * self.level) - lost_hp

    def get_speed(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        if self.status_effect == 'paralysis':
            return 7//2
        return 7

    def get_attack_damage(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 4 + (self.level//2)

    def get_defence(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 6 + self.level

    def defend(self, damage: int) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        if (get_defence(self)*2) < damage:
            lose_hp(self, damage)
        else: 
            lose_hp(self, damage//2)

    def get_poke_name(self) -> str:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 'Squirtle'

    def should_evolve(self) -> bool:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        if self.level == 3:
            return True
        return False

    def can_evolve(self) -> bool:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return True

    ########## IDK IF CORRECT ########################
    def get_evolved_version(self) -> PokemonBase:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return Blastoise(self)


class Gengar:
    def __init__(self, non_evolved_pokemon: PokemonBase) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        self.hp = non_evolved_pokemon.hp
        self.status_effect = non_evolved_pokemon.status_effect
        PokemonBase.__init__(self, self.hp, "ghost")
        self.level = 3

    def reset_hp(self) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        self.hp = (12 + self.level//2)
        
    def level_up(self) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        # adjust hp to match that of the pokemon's level
        lost_hp = (12 + self.level//2) - self.hp
        self.level += 1
        self.hp = (12 + self.level//2) - lost_hp

    def get_speed(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        if self.status_effect == 'paralysis':
            return 12//2
        return 12 

    def get_attack_damage(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 18

    def get_defence(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 3

    def defend(self, damage: int) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        lose_hp(self, damage)

    def get_poke_name(self) -> str:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 'Gengar'

    def should_evolve(self) -> bool:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return False

    def can_evolve(self) -> bool:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return False

    def get_evolved_version(self):
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        pass

class Haunter(PokemonBase):
    def __init__(self, non_evolved_pokemon: PokemonBase) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        self.hp = non_evolved_pokemon.hp
        self.status_effect = non_evolved_pokemon.status_effect
        PokemonBase.__init__(self, self.hp, "ghost")
        self.level = 1

    def reset_hp(self) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        self.hp = (9 + self.level//2)
        
    def level_up(self) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        lost_hp = (9 + self.level//2) - self.hp
        self.level += 1
        self.hp = (9 + self.level//2) - lost_hp

    def get_speed(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        if self.status_effect == 'paralysis':
            return 6//2
        return 6

    def get_attack_damage(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 8

    def get_defence(self) -> int:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 6

    def defend(self, damage: int) -> None:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        lose_hp(self, damage)

    def get_poke_name(self) -> str:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return 'Haunter'

    def should_evolve(self) -> bool:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        if self.level == 3:
            return True
        return False

    def can_evolve(self) -> bool:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return True


    def get_evolved_version(self) -> PokemonBase:
        """
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case if O(1).
        """
        return Gengar(self)

class Gastly:
    def __init__(self):
        """ This method initialises Gastly to its base attributes.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case is O(1).
        """
        PokemonBase.__init__(self, 6, "ghost")

    def reset_hp(self) -> None:
        self.hp = (6 + self.level//2)
        
    def level_up(self) -> None:
        """ This method level up Gastly to the parameters set within the specification and also
        adjust its HP to match its corresponding level.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case is O(1).
        """
        # adjust hp to match that of the pokemon's level
        lost_hp = (6 + self.level//2) - self.hp
        self.level += 1
        self.hp = (6 + self.level//2) - lost_hp

    def get_speed(self) -> int:
        """ This method gets the speed of Gastly base on the parameters set out by the
        specification.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case is O(1).
        """
        if self.status_effect == 'paralysis':
            return 2//2 
        return 2 

    def get_attack_damage(self) -> int:
        """ This method gets the attacking damage Gastly base on the parameters set out by the
        specification.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case is O(1).
        """
        return 4

    def get_defence(self) -> int:
        """ This method gets the defence points of Gastly.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case is O(1).
        """
        return 8

    def defend(self, damage: int) -> None:
        """ This method calculate how Gastly will defend against an attack as shown in the
        specification.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case is O(1).
        """
        lose_hp(self, damage)

    def get_poke_name(self) -> str:
        """ This method retrieves the name of the Pokemon which is Gastly.
        :pre: <not implemented>
        :post:  <not implemented>
        :complexity: Best case and worst case is O(1).
        """
        return 'Gastly'

    def should_evolve(self) -> bool:
        """ This method determines is the Pokemon should evolve, and as Gastly can evolve to Haunter,
         it should evolve
        :pre:
        :post:
        :complexity: Best case and worst case is O(1).
        """
        return True

    def can_evolve(self) -> bool:
        """ This method determines is the Pokemon should evolve, and as Gastly can evolve to Haunter,
         it should evolve
        :pre:
        :post:
        :complexity: Best case and worst case is O(1).
        """
        return True


    def get_evolved_version(self) -> PokemonBase:
        """ This method finds the evolved version of Gastly, which is Haunter and return the pokemon
        as its evolved version
        :pre:
        :post:
        :complexity: Best case and worst case if O(1).
        """
        return Haunter(self)


class Eevee:
    def __init__(self, non_evolved_pokemon: PokemonBase) -> None:
        """ This method initialises Eevee to its base attributes.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case is O(1).
        """
        self.hp = non_evolved_pokemon.hp
        self.status_effect = non_evolved_pokemon.status_effect
        PokemonBase.__init__(self, 10, "normal")
        self.level = 1
        
    def reset_hp(self) -> None:
        self.hp = 10
        
    def level_up(self) -> None:
        """ This method level up Eevee to the parameters set within the specification
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case is O(1).
        """
        self.level += 1

    def get_speed(self) -> int:
        """ This method gets the speed of Eevee base on the level and parameters set out by the
        specification.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case is O(1).
        """
        if self.status_effect == 'paralysis':
            return (7 + self.level)//2
        return 7 + self.level 

    def get_attack_damage(self) -> int:
        """ This method gets the attacking damage Eevee base on its level.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case is O(1).
        """
        return 6 + self.level

    def get_defence(self) -> int:
        """ This method gets the defence points of Eevee.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case is O(1).
        """
        return 4 + self.level

    def defend(self, damage: int) -> None:
        """ This method calculate how Eevee will defend against an attack as shown in the
        specification.
        :pre: <not implemented>
        :post: <not implemented>
        :complexity: Best case and worst case is O(1).
        """
        if get_defence(self) < damage:
            lose_hp(self, damage)

    def get_poke_name(self) -> str:
        """ This method retrieves the name of the Pokemon which is Eevee.
        :pre: <not implemented>
        :post:  <not implemented>
        :complexity: Best case and worst case is O(1).
        """
        return 'Eevee'

    def should_evolve(self) -> bool:
        """ This method determines is the Pokemon should evolve, and as Eevee is at the last
        stage of its evolution, it cannot and should not evolve.
        :pre:
        :post:
        :complexity: Best case and worst case is O(1).
        """
        return False

    def can_evolve(self) -> bool:
        """ This method determines is the Pokemon can evolve, and as Eevee is at the last
        stage of its evolution, it cannot and should not evolve.
        :pre:
        :post:
        :complexity: Best case and worst case is O(1).
        """
        return False

    def get_evolved_version(self) -> PokemonBase:
        """ This method finds the evolved version of Eevee, and since it is at its last stage
        it has no evolved version.
        :pre:
        :post:
        :complexity: Best case and worst case if O(1).
        """
        pass
