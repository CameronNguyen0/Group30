from pokemon_base import PokemonBase
"""
"""
class Charizard(PokemonBase):
    def __init__(self, non_evolved_pokemon: PokemonBase) -> None:
        self.hp = non_evolved_pokemon.hp
        self.status_effect = non_evolved_pokemon.status_effect
        PokemonBase.__init__(self, self.hp, "fire")
        self.level = 3
        
    def level_up(self) -> None:
        # adjust hp to match that of the pokemon's level
        lost_hp = (12 + 1 * self.level) - self.hp
        self.level += 1
        self.hp = (12 + 1 * self.level) - lost_hp

    def get_speed(self) -> int:
        if self.status_effect == 'paralysis':
            return (9 + 1 * self.level)//2
        return 9 + 1 * self.level 

    def get_attack_damage(self) -> int:
        return 10 + 2 * self.level

    def get_defence(self) -> int:
        return 4

    def defend(self, damage: int) -> None:
        if get_defence(self) < damage:
            lose_hp(self, 2*damage)
        else: 
            lose_hp(self, damage)

    def get_poke_name(self) -> str:
        return 'Charizard'

    def should_evolve(self) -> bool:
        return False

    def can_evolve(self) -> bool:
        return False

    def get_evolved_version(self):
        pass

    
class Charmander(PokemonBase):
    def __init__(self)
        PokemonBase.__init__(self, 9, "fire")
        
    def level_up(self) -> None:
        # adjust hp to match that of the pokemon's level
        lost_hp = (8 + 1 * self.level) - self.hp
        self.level += 1
        self.hp = (8 + 1 * self.level) - lost_hp

    def get_speed(self) -> int:
        if self.status_effect == 'paralysis':
            return (7 + 1 * self.level)//2
        return 7 + 1 * self.level 

    def get_attack_damage(self) -> int:
        return 6 + 1 * self.level

    def get_defence(self) -> int:
        return 4

    def defend(self, damage: int) -> None:
        if get_defence(self) < damage:
            lose_hp(self, damage)
        else: 
            lose_hp(self, damage//2)

    def get_poke_name(self) -> str:
        return 'Charmander'

    def should_evolve(self) -> bool:
        if self.level == 3:
            return True
        return False

    def can_evolve(self) -> bool:
        return True

    ########## IDK IF CORRECT ########################
    def get_evolved_version(self) -> PokemonBase:
        return Charizard(self)

class Venusaur(PokemonBase):
        def __init__(self, non_evolved_pokemon: PokemonBase) -> None:
        self.hp = non_evolved_pokemon.hp
        self.status_effect = non_evolved_pokemon.status_effect
        PokemonBase.__init__(self, self.hp, "grass")
        self.level = 2
        
        def level_up(self) -> None:
        # adjust hp to match that of the pokemon's level
        lost_hp = (20 + self.level//2) - self.hp
        self.level += 1
        self.hp = (20 + self.level//2) - lost_hp

    def get_speed(self) -> int:
        if self.status_effect == 'paralysis':
            return (3 + self.level//2)//2
        return 3 + self.level//2

    def get_attack_damage(self) -> int:
        return 5

    def get_defence(self) -> int:
        return 10

    def defend(self, damage: int) -> None:
        if (get_defence(self) + 5) < damage:
            lose_hp(self, damage)
        else: 
            lose_hp(self, damage//2)

    def get_poke_name(self) -> str:
        return 'Venusaur'

    def should_evolve(self) -> bool:
        return False

    def can_evolve(self) -> bool:
        return False

    def get_evolved_version(self):
        pass

class Bulbasaur(PokemonBase):
    def __init__(self)
        PokemonBase.__init__(self, 13, "grass")
        
    def level_up(self) -> None:
        # adjust hp to match that of the pokemon's level
        lost_hp = (12 + 1 * self.level) - self.hp
        self.level += 1
        self.hp = (12 + 1 * self.level) - lost_hp

    def get_speed(self) -> int:
        if self.status_effect == 'paralysis':
            return (7 + self.level//2)//2
        return 7 + self.level //2

    def get_attack_damage(self) -> int:
        return 5

    def get_defence(self) -> int:
        return 5

    def defend(self, damage: int) -> None:
        if (get_defence(self) + 5) < damage:
            lose_hp(self, damage)
        else: 
            lose_hp(self, damage//2)

    def get_poke_name(self) -> str:
        return 'Bulbasaur'

    def should_evolve(self) -> bool:
        if self.level == 2:
            return True
        return False

    def can_evolve(self) -> bool:
        return True

    ########## IDK IF CORRECT ########################
    def get_evolved_version(self) -> PokemonBase:
        return Venusaur(self)


class Blastoise(PokemonBase):
    def __init__(self, non_evolved_pokemon: PokemonBase) -> None:
        self.hp = non_evolved_pokemon.hp
        self.status_effect = non_evolved_pokemon.status_effect
        PokemonBase.__init__(self, self.hp, "water")
        self.level = 3

        def level_up(self) -> None:
        # adjust hp to match that of the pokemon's level
        lost_hp = (15 + 2 * self.level) - self.hp 
        self.level += 1
        self.hp = (15 + 2 * self.level) - lost_hp

    def get_speed(self) -> int:
        if self.status_effect == 'paralysis':
            return 10//2
        return 10

    def get_attack_damage(self) -> int:
        return 8 + (self.level//2)

    def get_defence(self) -> int:
        return 8 + 1 * self.level
    
    def defend(self, damage: int) -> None:
        if (get_defence(self)*2) < damage:
            lose_hp(self, damage)
        else: 
            lose_hp(self, damage//2)

    def get_poke_name(self) -> str:
        return 'Blastoise'

    def should_evolve(self) -> bool:
        return False

    def can_evolve(self) -> bool:
        return False

    def get_evolved_version(self):
        pass


class Squirtle(PokemonBase):
    def __init__(self)
        PokemonBase.__init__(self, 11, "water")
        
    def level_up(self) -> None:
        # adjust hp to match that of the pokemon's level
        lost_hp = (9 + 2 * self.level) - self.hp
        self.level += 1
        self.hp = (9 + 2 * self.level) - lost_hp

    def get_speed(self) -> int:
        if self.status_effect == 'paralysis':
            return 7//2
        return 7

    def get_attack_damage(self) -> int:
        return 4 + (self.level//2)

    def get_defence(self) -> int:
        return 6 + self.level

    def defend(self, damage: int) -> None:
        if (get_defence(self)*2) < damage:
            lose_hp(self, damage)
        else: 
            lose_hp(self, damage//2)

    def get_poke_name(self) -> str:
        return 'Squirtle'

    def should_evolve(self) -> bool:
        if self.level == 3:
            return True
        return False

    def can_evolve(self) -> bool:
        return True

    ########## IDK IF CORRECT ########################
    def get_evolved_version(self) -> PokemonBase:
        return Blastoise(self)


class Gengar:
    def __init__(self, non_evolved_pokemon: PokemonBase) -> None:
        self.hp = non_evolved_pokemon.hp
        self.status_effect = non_evolved_pokemon.status_effect
        PokemonBase.__init__(self, self.hp, "ghost")
        self.level = 3
        
        def level_up(self) -> None:
        # adjust hp to match that of the pokemon's level
        lost_hp = (12 + self.level//2) - self.hp
        self.level += 1
        self.hp = (12 + self.level//2) - lost_hp

    def get_speed(self) -> int:
        if self.status_effect == 'paralysis':
            return 12//2
        return 12 

    def get_attack_damage(self) -> int:
        return 18

    def get_defence(self) -> int:
        return 3

    def defend(self, damage: int) -> None:
        lose_hp(self, damage)

    def get_poke_name(self) -> str:
        return 'Gengar'

    def should_evolve(self) -> bool:
        return False

    def can_evolve(self) -> bool:
        return False

    def get_evolved_version(self):
        pass

class Haunter(PokemonBase):
    def __init__(self, non_evolved_pokemon: PokemonBase) -> None:
        self.hp = non_evolved_pokemon.hp
        self.status_effect = non_evolved_pokemon.status_effect
        PokemonBase.__init__(self, self.hp, "ghost")
        self.level = 1
        
        def level_up(self) -> None:
        # adjust hp to match that of the pokemon's level
        lost_hp = (9 + self.level//2) - self.hp
        self.level += 1
        self.hp = (9 + self.level//2) - lost_hp

    def get_speed(self) -> int:
        if self.status_effect == 'paralysis':
            return 6//2
        return 6

    def get_attack_damage(self) -> int:
        return 8

    def get_defence(self) -> int:
        return 6

    def defend(self, damage: int) -> None:
        lose_hp(self, damage)

    def get_poke_name(self) -> str:
        return 'Haunter'

    def should_evolve(self) -> bool:
        if self.level == 3:
            return True
        return False

    def can_evolve(self) -> bool:
        return True

    ########## IDK IF CORRECT ########################
    def get_evolved_version(self) -> PokemonBase:
        return Gengar(self)

class Gastly:
    def __init__(self)
        PokemonBase.__init__(self, 6, "ghost")
        
    def level_up(self) -> None:
        # adjust hp to match that of the pokemon's level
        lost_hp = (6 + self.level//2) - self.hp
        self.level += 1
        self.hp = (6 + self.level//2) - lost_hp

    def get_speed(self) -> int:
        if self.status_effect == 'paralysis':
            return 2//2
        return 2 

    def get_attack_damage(self) -> int:
        return 4

    def get_defence(self) -> int:
        return 8

    def defend(self, damage: int) -> None:
        lose_hp(self, damage)

    def get_poke_name(self) -> str:
        return 'Gastly'

    def should_evolve(self) -> bool:
        return True

    def can_evolve(self) -> bool:
        return True

    ########## IDK IF CORRECT ########################
    def get_evolved_version(self) -> PokemonBase:
        return Haunter(self)


class Eevee:
    def __init__(self)
        PokemonBase.__init__(self, 10, "normal")
        
    def level_up(self) -> None:
        self.level += 1

    def get_speed(self) -> int:
        if self.status_effect == 'paralysis':
            return (7 + self.level)//2
        return 7 + self.level 

    def get_attack_damage(self) -> int:
        return 6 + self.level

    def get_defence(self) -> int:
        return 4 + self.level

    def defend(self, damage: int) -> None:
        if get_defence(self) < damage:
            lose_hp(self, damage)

    def get_poke_name(self) -> str:
        return 'Eevee'

    def should_evolve(self) -> bool:
        return False

    def can_evolve(self) -> bool:
        return False

    def get_evolved_version(self) -> PokemonBase:
        pass