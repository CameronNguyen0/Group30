# Importing modules required.
from __future__ import annotations              # Module used for getting functionalities within the newer version of Python.
import random                                   # Module used for generating random values.
from array_list import ArrayList                # Module for accessing ArrayList properties.
from referential_array import ArrayR            # Module for accessing ArrayR properties.
from sorted_list import SortedList, ListItem    # Module for accessing SortedList properties.
from enum import Enum, auto                     # Module for Enum properties.
from task_1 import PokemonBase                  # Module for PokemonBase access.
from random_gen import RandomGen                # Another module used for generating random values.
from array_sorted_list import ArraySortedList
"""
File Description:
This file contains the implementation of Task 3 of Assignment 2 for the unit FIT1008 of Monash University. The
file implement various classes to create various battle modes for the future implementation of Pokemon battles.

Date Last Modified: Wednesday, 17th of September, 2022
Contributions: Khanh Gia (Ryan) Nguyen, Amy Dang, Cameron, Vonara Subasinghe
"""

# The original author that established this file.
__author__ = "Scaffold by Jackson Goerner, Code by Khanh Gia (Ryan) Nguyen, Cameron and Vonara Subasinghe"

# This class lists the option of moves possible to perform during battle.
class Action(Enum):
    ATTACK = 4
    SWAP = 1
    HEAL = 3
    SPECIAL = 2
    
# This class list the different criterions that can be used during the battle mode.
class Criterion(Enum):
    SPD = auto()
    HP = auto()
    LV = auto()
    DEF = auto()

# This is the main PokeTeam class where the team of Pokemon is built, with corresponding methods to retrive and 
# return Pokemon for battle.
class PokeTeam:

    # Pokemon limit is the number of Pokemon allowed in a team.
    pokemon_limit = 6
    # A list of the PokedexOrder.
    pokedex_order = ArraySortedList()
    pokedex_order.add("Charmander", 1) 
    pokedex_order.add("Charizard", 2)
    pokedex_order.add("Bulbasaur", 3)
    pokedex_order.add("Venusaur", 4)
    pokedex_order.add("Squirtle", 5)
    pokedex_order.add("Blastoise", 6)
    pokedex_order.add("Gastly", 7)
    pokedex_order.add("Haunter", 8)
    pokedex_order.add("Gengar", 9)

    # The class list the different AI mode that can be used when initialise a Pokemon team.
    class AI(Enum):
        ALWAYS_ATTACK = auto()
        SWAP_ON_SUPER_EFFECTIVE = auto()
        RANDOM = auto()
        USER_INPUT = auto()

    # Initialiser for a PokeTeam.
    def __init__(self, team_name: str, team_numbers: list[int], battle_mode: int, ai_type: PokeTeam.AI, criterion=None) -> None:
        """ This method initialises the PokeTeam using variables inputted, to create team of Pokemon for battle.
        :pre: The Pokemon HP is always an integer.
        :post: <not implemented>
        :complexity: <not implemented> 
        """
        # Define attributes of a PokeTeam.
        self.team_name = team_name
        self.team_numbers = team_numbers
        self.battle_mode = battle_mode
        self.ai_type = ai_type
        self.criterion = criterion
        self.current_battling_pokemon = None   
        self.heal_count = 0
        self.fainted_pokemon_list = ArrayStack(team_numbers[5])
        self.action = None
        self.win = None
        self.fire_present = False
        self.grass_present = False
        self.water_present = False
        self.ghost_present = False
        self.normal_present = False
        self.has_battled = LinkedList()
        for i in range(5):
            self.has_battled.insert(i, 0)

        

        # Creating conditions for battle mode 0.
        if battle_mode == 0:
            # Create a stack to store pokemon in a team as method in battle mode 0 revolves around method that is appliable using a stack ADT.
            self.team_pokemon = ArrayStack(pokemon_limit)
            for _ in self.team_numbers[5]-self.team_numbers[4]:
                self.team_pokemon.push(Eevee())
            for _ in self.team_numbers[4]-self.team_numbers[3]:
                self.team_pokemon.push(Gastly())
            for _ in self.team_numbers[3]-self.team_numbers[2]:
                self.team_pokemon.push(Squirtle())
            for _ in self.team_numbers[2]-self.team_numbers[1]:
                self.team_pokemon.push(Bulbasaur())
            for _ in self.team_numbers[1]-self.team_numbers[0]:
                self.team_pokemon.push(Charmander())
            
        # Creating conditions for battle mode 1.
        elif battle_mode == 1:
            # Create a queue to store the pokemon in the team. 
            Q = CircularQueue(pokemon_limit)
            
            # team_numbers = [0,2,2,4,5,6]
            # Create a queue to see how many of each Pokemon is needed to add into the final team.

            for _ in self.team_numbers[1]-self.team_numbers[0]:
                Q.append(Charmander())
            for _ in self.team_numbers[2]-self.team_numbers[1]:
                Q.append(Bulbasaur())
            for _ in self.team_numbers[3]-self.team_numbers[2]:
                Q.append(Squirtle())
            for _ in self.team_numbers[4]-self.team_numbers[3]:
                Q.append(Gastly())
            for _ in self.team_numbers[5]-self.team_numbers[4]:
                Q.append(Eevee())

            # The collection of Pokemon in the team.
            self.team_pokemon = Q
            
        # Creating conditions for battle mode 2.
        elif battle_mode == 2:
            # Creates an ArraySortedList.
            criterion_sorted_poke = ArraySortedList(team_numbers[5])

            # Makes new pokemon and places them in their correct positions in a ArraySortedList (according to criterion, not Pokedex Order).
            for _ in self.team_numbers[1]-self.team_numbers[0]:
                temporary_object = Charmander()
                criterion_sorted_poke.add(ListItem(temporary_object,criterion_find(temporary_object)))
            for _ in self.team_numbers[2]-self.team_numbers[1]:
                temporary_object = Bulbasaur()
                criterion_sorted_poke.add(ListItem(temporary_object,criterion_find(temporary_object)))
            for _ in self.team_numbers[3]-self.team_numbers[2]:
                temporary_object = Squirtle()
                criterion_sorted_poke.add(ListItem(temporary_object,criterion_find(temporary_object)))
            for _ in self.team_numbers[4]-self.team_numbers[3]:
                temporary_object = Gastly()
                criterion_sorted_poke.add(ListItem(temporary_object,criterion_find(temporary_object)))
            for _ in self.team_numbers[5]-self.team_numbers[4]:
                temporary_object = Eevee()
                criterion_sorted_poke.add(ListItem(temporary_object,criterion_find(temporary_object)))

            ####
            pokedex_sorted_poke = ArraySortedList(pokemon_limit)
            for i in criterion_sorted_poke:
                pokedex_sorted_poke.add(ListItem(i, pokedex_order.index(i)))
            ####
    
            self.team_pokemon = ArrayStack(team_numbers[5])
            for i in criterion_sorted_poke:
                self.team_pokemon.push(criterion_sorted_poke[i])

            #Stack with hp LOWEST at top to HIGHEST at bottom pokemon order
            self.special()
            #Stack with hp HIGHEST at top to LOWEST at bottom pokemon order

    def criterion_find(pokemon: PokemonBase): #-> value of criterion for the pokemon
        if criterion == Criterion.HP:
            return pokemon.hp()
        if criterion == Criterion.SPD:
            return pokemon.get_speed()
        if criterion == Criterion.DEF:
            return pokemon.get_defence()
        if criterion == Criterion.LV:
            return pokemon.level

        
    
    @classmethod
    def random_team(cls, team_name: str, battle_mode: int, team_size=None, ai_mode=None, **kwargs) -> None:
        """ Create a random team given the rules shown in specification.
        :pre: The input of any other additional element must of type within the class Criterion.
        :post:
        :complexity:
        """
        # When no team size is specified, generate a team size from half pokemon_limit to pokemon_limit.
        if team_size == None:
            team_size = RandomGen.randint(pokemon_limit/2, pokemon_limit)

        # Created sorted list and add the values 0 and team size.
        list_of_numbers = ArraySortedList(SortedList[T])
        list_of_numbers.add(0)
        list_of_numbers.add(team_size)

        # Generate 4 random numbers from 0 to team size and insert into sorted list.
        i = 0
        while i != 4:
            rand_num = RandomGen.randint(0, team_size)
            list_of_numbers.add(rand_num)
            i += 1
        
        # Call the main constructor method to contruct the PokeTeam, after receiving the random team list of numbers.
        cls(team_name, list_of_numbers, battle_mode, ai_mode, kwargs = None)
    
    # return a pokemon to the team
    def return_pokemon(self, poke: PokemonBase) -> None:
        """
        :pre: The team_pokemon is always a sorted list.
        :post:
        :complexity:
        """
         ###
        #if evolved change key to -0.1
         

        # depending on the battle mode, position of pokemon in a team is arranged accordingly
        if self.battle_mode == 0:
            self.team_pokemon.push(self.current_battling_pokemon)   # Returns the Pokemon to the front of the team.
        elif self.battle_mode == 1:
            self.team_pokemon.append(self.current_battling_pokemon) # Returns the Pokemon to the end of the team.
        elif self.battle_mode == 2:
            flip_status = False
    
            # Check if the stack is in ascending order, if yes then we will directly convert the stack into a sorted list.
            # To do so, check the values of the first (using peek()) and last elements in the stack.
            first_pokemon = self.team_pokemon.peek()
            last_pokemon = self.team_pokemon.pop()

            # If descending order, then reverse the stack and turn flip stack status to true.
            if find_criterion(first_pokemon) > find_criterion(last_pokemon):
                self.team_pokemon.push(last_pokemon)            # Place the value of the last pokemon back into the stack.
                poke_stack = reverse_stack(self.team_pokemon)                
                flip_status = True
                
                # Turn stack into sorted list and add new value.
                sorted_list = stack_to_sorted_list(poke_stack, self.current_battling_pokemon)
                
                # Put all values back into stack and if flip stack status is on then flip the stack back.
                poke_stack = sorted_list_to_stack(sorted_list)
                self.pokemon_team = reverse_stack(poke_stack)
                return None

            # Place the value of the last pokemon back into the stack.
            self.team_pokemon.push(last_pokemon)
            sorted_list = stack_to_sorted_list(self.team_pokemon, self.current_battling_pokemon)
            self.pokemon_team = sorted_list_to_stack(sorted_list)
             
            # Determine if stack is in ascending order of descending order.
            # If descending order, then reverse the stack and turn flip stack status to true.
                
            # Put all values back into stack and if flip stack status is on then flip the stack back.

    def sorted_list_to_stack(sorted_list: ArraySortedList) -> ArrayStack:
        temp = ArrayStack(pokemon_limit)
        for i in sorted_list:
            temp.push(sorted_list[i])
        return temp
        
    ####################
    # Method to convert a stack into a one to one sorted list with criterion considered.
    def stack_to_sorted_list(poke_stack: ArrayStack, pokemon: PokemonBase) -> ArraySortedList: 
        criterion_sorted_list = ArraySortedList(pokemon_limit)
        for _ in range(len(poke_stack)):
            curr_pokemon = poke_stack.pop()
            criterion_sorted_poke.add(ListItem(curr_pokemon, criterion_find(curr_pokemon)))
        criterion_sorted_poke.add(ListItem(pokemon, criterion_find(pokemon)))


        pokedex_sorted_poke = ArraySortedList(pokemon_limit)
        for i in criterion_sorted_poke:
            pokedex_sorted_poke.add(ListItem(i, pokedex_order.index(i)))
        return pokedex_sorted_poke

    # Method to reverse a stack.
    def reverse_stack(poke_stack: ArrayStack) -> ArrayStack:
        """
        """
        temp = ArrayStack(len(poke_stack))
        for i in poke_stack:
            curr_poke = poke_stack.pop()
            temp.push(curr_poke)
        return temp

    ############################
        





        

    def retrieve_pokemon(self) -> PokemonBase | None:
        """
        :pre:
        :post:
        :complexity:
        """
        if self.battle_mode == 0 or self.battle_mode == 2:
            self.current_battling_pokemon = self.team_pokemon.pop()
        elif self.battle_mode == 1:
            self.current_battling_pokemon = self.team_pokemon.serve()
            


    def special(self):
        """ This method implements all the special that is unique to each battle mode as shown in the assignment specification.
        :pre:
        :post:
        :complexity:
        """
        # Battle mode 0 special is to swap the last and the first Pokemon's position.
        if self.battle_mode == 0:
            temp = ArrayStack(len(self.team_pokemon))            # Tempoary stack to rearrange the order of the team.
            first_pokemon = self.team_pokemon.pop()     # Take the first element of the stack.
            for _ in self.team_pokemon:                 # Push all elements of the team into the temp stack.
                curr_pokemon = self.team_pokemon.pop()
                temp.push(curr_pokemon)
            last_pokemon = temp.pop()                   # The last Pokemon from the team is the first element in temp stack.
            self.team_pokemon.push(first_pokemon)       # The first Pokemon in the original stack is now the last Pokemon.
            for _ in temp:                              # Start putting all the Pokemon in the middle back to its places.
                curr_pokemon = temp.pop()               
                self.team_pokemon.push(curr_pokemon)
            self.team_pokemon.push(last_pokemon)        # The last Pokemon in the original stack is now the first Pokemon (on top of the stack).

        # Battle mode 1 special is to swap the first and second halves of the team (the second half includes the middle of the Pokemon for odd
        # team numbers) and reverse the order of the previously front half of the team.
        elif self.battle_mode == 1:
            temp = ArrayStack(len(self.team_pokemon))
            # Iterate over the whole queue and add front half to stack (not including the middle if odd length).
            for _ in range(len(self.pokemon_team)//2): 
                curr_pokemon = self.pokemon_team.serve()                            
                temp.push(curr_pokemon)
            # Using stack we can automatically reverse the Pokemon order of front half by adding it back into the queue.
            for _ in temp:
                curr_pokemon = temp.pop()
                self.team_pokemon.append(curr_pokemon)

        elif self.battle_mode == 2:
            # new_position = len(self.team_pokemon) - 1
            # temp = ArraySortedList(len(self.team_pokemon))
            # for i in range(len(self.team_pokemon)):
            #     temp[new_position] = self.team_pokemon[i]
            #     new_position -= 1
            
            temp = ArrayStack(len(self.team_pokemon))
            for i in range(len(self.team_pokemon)):
                temp.push(self.team_pokemon.pop())
            self.team_pokemon = temp
                

    def regenerate_team(self):
        self.__init__(self.team_name, self.team_numbers, self.battle_mode, self.ai_type, self.criterion)

    def __str__(self):
        if self.battle_mode == 0 or self.battle_mode == 2:
            temp_storage = ArrayStack(len(self.team_pokemon))
            string = ""
            for i in range(len(self.team_pokemon)):
                analysing = self.team_pokemon.pop()
                temp_storage.push(analysing)
                string_segment = f"LV. {analysing.level} {analysing.get_poke_name}: {analysing.hp} HP,"
                string == string + string_segment
            for i in range(len(temp_storage)):
                self.team_pokemon.push(temp_storage.pop())
        if self.battle_mode == 1:
            temp_storage = CircularQueue(len(self.team_pokemon))
            for _ in range(len(self.team_pokemon)):
                analysing = self.team_pokemon.serve()
                temp_storage.append(analysing)
                string_segment = f"LV. {analysing.level} {analysing.get_poke_name}: {analysing.hp} HP,"
                string == string + string_segment
            self.team_pokemon = temp_storage
        string = string[:-1]
            
        return f"{self.team_name} ({self.battle_mode}): [{string}]"

    # Checks to see if team is empty Boolean expression, returns Boolean value (true or false)
    def is_empty(self) -> bool: 
        return len(self.team_pokemon) == 0
        

    def choose_battle_option(self, my_pokemon: PokemonBase, their_pokemon: PokemonBase) -> Action:
        if self.ai_type == PokeTeam.AI.ALWAYS_ATTACK:
            return Action.ATTACK
        elif self.ai_type == PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE:
            if my_pokemon.poke_type == 'fire':
                if their_pokemon.poke_type == 'grass':
                    return Action.SWAP
            if my_pokemon.poke_type == 'grass':
                if their_pokemon.poke_type == 'water':
                    return Action.SWAP
            if my_pokemon.poke_type == 'water':
                if their_pokemon.poke_type == 'fire':
                    return Action.SWAP
            if my_pokemon.poke_type == 'ghost':
                if their_pokemon.poke_type == 'ghost':
                    return Action.SWAP
        elif self.ai_type == PokeTeam.AI.USER_INPUT:
            user_input = input("Enter number: \n1. ATTACK \n2. SWAP \n3. HEAL \n4. SPECIAL")
            if user_input == 1:
                return Action.ATTACK
            elif user_input == 2:
                return Action.SWAP
            elif user_input == 3:
                return Action.HEAL
            elif user_input == 4:
                return Action.SPECIAL
        elif self.ai_type == PokeTeam.AI.RANDOM:
            random = RandomGen.randint(1,4)
            if self.heal_count == 3:
                random = RandomGen.randint(1,3)
            if random == 1:
                return Action.ATTACK
            elif random == 2:
                return Action.SWAP
            elif random == 3:
                return Action.SPECIAL
            elif random == 4:
                self.heal_count += 1
                return Action.HEAL
            
        
        # if no swap occurs with SWAP_ON_SUPER_EFFECTIVE, take random action
        random = RandomGen.randint(1,3)
        if random == 1:
            return Action.ATTACK
        elif random == 2:
            return Action.SPECIAL
        elif random == 3:
            return Action.HEAL

