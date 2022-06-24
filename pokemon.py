"""
Author: Kvin2K
Date: 04/22/2022
pokemon sussy
"""
def read_csv(file_name):
    """read from csv file
    
    Args:
        file_name(str): The name of the csv file.
    
    Returns:
        ([[str]]): the data from the csv.
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        data = []
        #read the csv line by line
        for line in f.readlines():
            parsed_line = line.strip().split(',')
            data.append(parsed_line)
        
        return data

def get_type1_from_name(poke_data, name):
    """Returns type
    
    Args:
        poke_data ([[str]]): the pokemon data
        name (str): the name of the pokemon to look up
        
    Returns:
        (str): The type1 of the specified pokemon.   
    
    """
    # linear
    name_index = 1 
    type1_index = 2
    # loop through every pokemon
    # all data for z pokemon
    pokemon_index = -1
    #Loop through every pokemon
    for pokemon_data in poke_data:
        if pokemon_data[name_index] == name:
            pokemon_index = int(pokemon_data[0])

    type1 = poke_data[pokemon_index][type1_index] if pokemon_index != -1 : else 'not found'
    return type1 

def main():
    poke_data = read_csv('pokemon.csv')
    
    pokemon = input ("Enter the name of a pokemon").title()

    type1 = get_type1_from_name(poke_data, pokemon)
    print(f"{pokemon} is a {type1} ")
if __name__ == '__main__':
    main()
