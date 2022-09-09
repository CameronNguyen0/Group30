from __future__ import annotations

from abc import ABC, abstractmethod
import random_gen
"""
"""
__author__ = "Cry cry cry cry cry"

# Multipliers for each pokemon attack.
# The labeled pokemon type is the type of the pokemon attacking. E.g. fire_multiplier = fire pokemon attacking.
# Position 0 in list = fire pokemon defending
# Position 1 = grass
# Position 2 = water
# Position 3 = ghost
# Position 4 = normal

multiplier = [[1, 2, 0.5, 1, 1], [0.5, 1, 2, 1, 1], [2, 0.5, 1, 1, 1], [1.25, 1.25, 1.25, 2, 0], [1.25, 1.25, 1.25, 0, 1]]

status_things = ['burn', 'poison', 'paralysis', 'sleep', 'confusion']

list_position_dict = {'fire': 0, 'grass': 1, 'water': 2, 'ghost': 3, 'normal': 4}

class PokemonBase:

    def __init__(self, hp: int, poke_type: str) -> None:
        self.hp = hp
        self.poke_type = poke_type
        self.level = 1
        self.status_effect = None
        self.list_position = list_position_dict[self.poke_type]
        self.attack_multiplier = multiplier[self.list_position]
        self.status_inflict = status_things[self.list_position]
    
    def is_fainted(self) -> bool:
        if self.hp == 0:
            return True
        return False

    @abstractionmethod
    def level_up(self) -> None:
        pass

    @abstractionmethod
    def get_speed(self) -> int:
        pass

    @abstractionmethod
    def get_attack_damage(self) -> int:
        pass

    @abstractionmethod
    def get_defence(self) -> int:
        pass

    def lose_hp(self, lost_hp: int) -> None:
        self.hp -= lost_hp

    @abstractionmethod
    def defend(self, damage: int) -> None:
        pass

    def attack(self, other: PokemonBase):
        # Step 1: Status effects on attack damage / redirecting attacks
        if self.status_effect == 'sleep':
            return

        # Step 2: Do the attack
        effective_attack = self.get_attack_damage * self.attack_multiplier[other.list_position]

        if self.status_effect == 'burn':
            effective_attack = effective_attack//2

        other.defend(effective_attack)

        if self.status_effect == 'confusion':
            if RandomGen.random_chance(0.5) == True:
                attack_self = True
                if self.poke_type == 'ghost':
                    defend(self, self.get_attack_damage * 2)
                else:
                    defend(self, self.get_attack_damage)
            attack_self = False
        
        # Step 3: Losing hp to status effects + applying status effects
        # check if infliction of status effect occurs
        if attack_self == False and RandomGen.random_chance(0.2) == True:
            other.status_effect = status_things[list_position]
            if self.status_inflict == 'burn':
                other.lost_hp(1)
            if self.status_inflict == 'poison':
                other.lose_hp(3)

        if attack_self == True and RandomGen.random_chance(0.2) == True:
            self.status_effect = status_things[list_position]
            if self.status_inflict == 'burn':
                self.lost_hp(1)
            if self.status_inflict == 'poison':
                self.lose_hp(3)

    @abstractionmethod
    def get_poke_name(self) -> str:
        pass

    #CLARIFY (is abstraction needed if get_poke_name is abstract?)
    def __str__(self) -> str:
        return f"LV. {self.level} {self.get_poke_name()}: {self.hp} HP"
        
    @abstractionmethod
    def should_evolve(self) -> bool:
        pass

    @abstractionmethod
    def can_evolve(self) -> bool:
        pass

    @abstractionmethod
    def get_evolved_version(self) -> PokemonBase:
        pass
