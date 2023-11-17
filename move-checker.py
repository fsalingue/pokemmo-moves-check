import os
import json

def find_pokemon_with_moves(directory, moves_to_check):
    pokemon_with_moves = []

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), "r") as file:
                data = json.load(file)
                moves = [move["name"] for move in data.get("moves", [])]

                if all(move in moves for move in moves_to_check):
                    pokemon_with_moves.append(data["name"])

    return pokemon_with_moves

if __name__ == "__main__":
    folder_path = "pokemons/"  # Replace this with the path to your folder

    moves_input = input("What moves the poke should have (comma-separated): ")
    moves_to_check = [move.strip() for move in moves_input.split(",")]

    pokemon_list = find_pokemon_with_moves(folder_path, moves_to_check)

    if pokemon_list:
        print(f"Pokémon with {', '.join(moves_to_check)} moves:")
        for pokemon in pokemon_list:
            print("- {}".format(pokemon))
    else:
        print(f"No Pokémon found with {', '.join(moves_to_check)} moves.")
