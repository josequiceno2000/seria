# SERIA
## Setup
1. ~~Create virtual environment~~ ✔
2. ~~Set up project folder structure~~ ✔
3. ~~Create main.py~~ ✔

## game_data.py
1. ~~Create game_data.py~~ ✔
2. ~~Add data (list of dictionaries with name, follower_count, description, and country)~~ ✔
3. ~~Input real data~~ ✔

## Intro
0. ~~Create intro.py~~ ✔
1. ~~Get ASCII title art~~ ✔
### Intro Function
1. ~~Create intro function~~ ✔
2. ~~Display title art~~ ✔
3. ~~Display explanation of the game~~ ✔
4. ~~Let player choose between classic or beat the clock mode~~ ✔
5. ~~Set up game based on specifications~~ ✔
6. ~~Return appropriate value(s?)~~ ✔
7. ~~Add type hints and docstring~~ ✔
8. ~~Connect to main.py~~ ✔
### beat_the_clock_or_classic
1. ~~Create function to ask user to choose mode~~ ✔
2. ~~Set countdown time based on user choice~~ ✔ 

## User Class
1. ~~Create User class~~ ✔
2. ~~Add name and score and high_score fields~~ ✔
3. ~~Add method to record run~~ ✔
4. ~~Add method to increase score~~ ✔
5. ~~Connect to main.py~~ ✔

## Round
### clock
0. ~~Create round.py file~~ ✔
1. ~~Add default function for clock~~ ✔
2. ~~Connect to main.py~~ ✔
### play round
0. Get VS ASCII art
1. Define play_round function with default parameters
2. Select two random entries from data
3. Print out compare statement for A based on name, description and country
4. Print out VS ASCII art
5. Print out compare statement for A based on name, description and country
6. Ask user to select which has more followers
7. Incorporate the countdown
8. If user is right:
    a. increase score
    b. print right statement with their current score
    c. set the more popular one to be the A comparison
    d. play another round with A 
9. If user is wrong or runs out of time:
    a. record their score
    b. print out wrong statement with final score
    c. Allow user to play again, view high scores, or quit



