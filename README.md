# Guess_the_pokemon
# ❄️ Pokémon Survival Game

Welcome to the **Pokémon Survival Game** — a fun and simple terminal-based Python guessing game powered by the [PokéAPI](https://pokeapi.co/)! You're trapped in a frozen cave by a mysterious game master. The only way to escape? **Guess the correct Pokémon!**

---

## 🎯 Game Objective

The game master has randomly selected a Pokémon (by its National Dex number between 1 and 1025).  
Your mission: **Guess the correct Pokémon by name or Pokédex number.**

After each guess, the game will tell you how "warm" or "cold" you are — based on how close your guess is to the target Pokémon's Dex number.

---

## 🔥 Closeness Feedback System

| Distance (Dex Difference) | Feedback                              |
|---------------------------|---------------------------------------|
| 0                         | 🎉 You guessed correctly!             |
| ≤ 5                       | 🔥 You're really warm and comfortable |
| ≤ 10                      | 🔥 You're very warm                   |
| ≤ 50                      | 🪔 You're warm                        |
| ≤ 200                     | 🙂 You're starting to feel warm       |
| ≤ 250                     | 😐 You're cold                        |
| ≤ 300                     | 🥶 You're very cold                   |
| ≤ 350                     | ⛄ You're frostbitten in cold         |
| > 350                     | 🧊 You're in an icy cave...           |

---

## 🚀 How to Run the Game

### 1. Make sure Python is installed

-----------------------------------------------------------------------------------------------------------------------------------
SAMPLE GAMEPLAY

Welcome to pokemon survival game.
You are stranded in a frozen cave by game master.
Try to guess the pokemon of game master to escape

Enter a Pokémon name or Dex no. (1-1025): bulbasaur

🪔 You're warm.
You guessed Bulbasaur.
You're within 100!

Enter a Pokémon name or Dex no. (1-1025): charmander

🔥 You're very warm.
You guessed Charmander.
You're within 20!

Enter a Pokémon name or Dex no. (1-1025): squirtle

🎉 You guessed correctly!
The Pokémon was Squirtle. You took 3 turns.
