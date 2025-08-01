import requests
import random

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name_or_id):
    url = f"{base_url}/pokemon/{name_or_id}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data ({response.status_code})")
        return None

def user_info():
    user = input("Enter a Pokémon name or Dex no. (1-1025): ").strip().lower()
    return get_pokemon_info(user)

print("Welcome to pokemon survival game.\nYou are stranded in a frozen cave by game master.Try to guess the pokemon of game master to escape ")
count=0

# Generate target Pokémon
comp = random.randint(1, 1025)
comp_poke_info = get_pokemon_info(comp)

# Get user's first guess
user_poke_info = user_info()

while True:
    if not user_poke_info:
        print("Invalid input! Try again.")
        user_poke_info = user_info()
        continue

    user_id = user_poke_info["id"]
    diff = abs(user_id - comp)

    if diff == 0:
        print(f"\n🎉 You guessed correctly!\nThe Pokémon was {comp_poke_info['name'].capitalize()}. You took {count} turns.")
        break
    elif diff <= 5:
        print(f"\n🔥 You're really warm and comfortable.\nYou guessed {user_poke_info['name'].capitalize()}.\nYou're within 10!\n")
        count+=1
    elif diff <= 10:
        print(f"\n🔥 You're very warm.\nYou guessed {user_poke_info['name'].capitalize()}.\nYou're within 20!\n")
        count+=1
    elif diff <= 50:
        print(f"\n🪔 You're warm.\nYou guessed {user_poke_info['name'].capitalize()}.\nYou're within 100!\n")
        count+=1
    elif diff <= 200:
        print(f"\n🙂 You're starting to feel warm.\nYou guessed {user_poke_info['name'].capitalize()}.\nYou're within 400!\n")
        count+=1
    elif diff <= 250:
        print(f"\n😐 You're cold.\nYou guessed {user_poke_info['name'].capitalize()}.\nYou're within 500!\n")
        count+=1
    elif diff <= 300:
        print(f"\n🥶 You're very cold.\nYou guessed {user_poke_info['name'].capitalize()}.\nYou're within 600!\n")
        count+=1
    elif diff <= 350:
        print(f"\n⛄ You're frostbitten in cold.\nYou guessed {user_poke_info['name'].capitalize()}.\nYou're within 700!\n")
        count+=1
    else:
        print(f"\n🧊 You're in an icy cave... far away from the target!\nYou guessed {user_poke_info['name'].capitalize()}.\n")
        count+=1

    user_poke_info = user_info()
