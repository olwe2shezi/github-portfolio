import requests
import random
import time # *EXTENSION* 'time' module used to introduce a pause 'time.sleep()' between rounds

# *REQUIRED* 1. This function generates a random number
def get_random_planet_data():
    # Generate a random planet_id between 1 and 60. SWAPI has 60 planets
    planet_id = random.randint(1, 60)
    # *REQUIRED* 2. Construct the URL for the Star Wars API with the random planet_id
    url = "https://swapi.dev/api/planets/{}".format(planet_id)
    response = requests.get(url) # Make a GET request to the API
    return response.json() # Return the JSON data received from the API

# *REQUIRED* 3. Create a dictionary containing specific stats of the planet ('name' and 3 stats)
# *EXTENSION* stats - 'diameter', 'gravity', and 'surface_water'
def create_planet_dict(planet_data):
    return dict(
        name=planet_data['name'],
        rotation_period=planet_data['rotation_period'],
        orbital_period=planet_data['orbital_period'],
# If a value is 'unknown' in the planet data, it sets the corresponding dictionary value to None
        population=planet_data['population'] if planet_data['population'] != 'unknown' else None,
        diameter=planet_data['diameter'] if planet_data['diameter'] != 'unknown' else None,
        gravity=planet_data['gravity'] if planet_data['gravity'] != 'unknown' else None,
        surface_water=planet_data['surface_water'] if planet_data['surface_water'] != 'unknown' else None
    )

def star_wars():
    # Get random planet data and create a dictionary for the player's planet
    planet_data = get_random_planet_data()
    return create_planet_dict(planet_data)



def record_result(result_dict,player_score,opponent_score,ties): #declare function that takes on  Arg
    # Creates a text file  records that allows you to read/write and stores the results for each round

    nice_message = ["May The Force Be Wit You!..In The Next Round ",
                    "And the Result is ....",
                    "Aren't You A Little Short For A StormTrooper ",
                    "Great Game, Play Again Soon "]
    random_message = random.choice(nice_message) #randomly chooses a message from list
    with open("game_results.txt", "w") as file: #opens file as write file
        # file.write("\n")
        file.write("*****************************\n")
        file.write(f"***{random_message}***\n")
        file.write("*****************************\n")
        file.write(result_dict["Result"] + "\n") #writes result from result_dict dictionary to file

        result_lower= result_dict["Result"].lower() #result is in all lower case
    if "win" in result_lower: #checks if the result. If i win then my score goes up by 1
        player_score += 1
    elif "lose" in result_lower: #elsif i lose then obv my opponent won so his score goes up by 1
        opponent_score += 1
    elif "tie" in result_lower: #if there is a tie increment the 'ties' by 1.
        ties +=1
    with open("game_results.txt", "a") as file: #writes the updated player and opponent score to the file
        file.write(f"Player Score: {player_score}\n")
        file.write(f"Opponent Score: {opponent_score}\n")
        file.write(f"Draws: {ties}\n")


# round_number = 1

def run_game():
    # *REQUIRED* 4a. Get and print the player's planet information
    # placeholders in record_result() that are passed in this function  to get the updated score based on result
    player_score = 0
    opponent_score = 0
    ties = 0

    player_planet = star_wars() #getting a random planet data for me
    player_dict = create_planet_dict(player_planet) #returning it with attributes of my planet data in DIc=\C format

    # ANSI escape codes to change the color of text and background(\33[97m\33[1m\33[45m). UNICODE characters(★★★») to add decorative elements
    print(
        "                   ★★★» \33[97m\33[1m\33[45mCK23INTP10 - CODING KICKSTARTER, INTRODUCTION TO PYTHON & APPS \33[0m »★★★\n  ")
    print("                    ★★★ \33[97m\33[45m  WELCOME TO STARWARS TOP TRUMPS GAME  \33[0m ★★★\n")

    print("\33[97m\33[46m\33[1m--- First Round ---\33[0m\n")
    time.sleep(1)
    print('\33[32m\33[1mYOU WERE GIVEN: "{}"\33[0m'.format(player_dict['name']))
    print('»»\33[97m\33[44m\33[3mYOUR STATS:\33[0m««')


    print(' rotation_period: {} \n '
          'orbital_period: {} \n population: {} \n diameter: {} \n '
          'gravity: {} \n surface_water: {} \n'.format(player_dict['rotation_period'],
                                                        player_dict['orbital_period'],player_dict['population'],player_dict['diameter'],
                                                        player_dict['gravity'],player_dict['surface_water']))

    # *REQUIRED* 4b. Get and print the opponent's planet information
    opponent_planet = star_wars()
    opponent_dict = create_planet_dict(opponent_planet)
    print('\33[32m\33[1mYOUR OPPONENT WAS GIVEN: "{}"\33[0m'.format(opponent_dict['name']))
    print('»»\33[97m\33[44m\33[3mOPPONENT STATS:\33[0m««')
    print(' rotation_period: {} \n '
          'orbital_period: {} \n population: {} \n diameter: {} \n '
          'gravity: {} \n surface_water: {} \n'.format( opponent_dict['rotation_period'],
                                                       opponent_dict['orbital_period'],opponent_dict['population'],
                                                       opponent_dict['diameter'],
                                                       opponent_dict['gravity'], opponent_dict['surface_water']))

    # *REQUIRED* 5. Prompt the user to choose a stat for comparison
    chosen_stat = input("Which stat do you want to use for comparison? population, diameter, gravity or surface_water: ")

    # Get the values of the chosen stat for the player and opponent
    player_stat_value = player_planet[chosen_stat]
    opponent_stat_value = opponent_planet[chosen_stat]

    # Create a dictionary to store the result of the comparison
    result_dict = {"Result": None}

    # *REQUIRED* 6. Compare the chosen stat values and update the result_dict
    # *REQUIRED* 6. Compare the chosen stat values and update the result_dict


    if player_stat_value is None and opponent_stat_value is None: #if player nd opponent value on chosen stat is none
            result_dict["Result"] = f"Both players have 'None' values for the chosen stat: {chosen_stat}. Choose another."
    elif player_stat_value is None: #if only the players value is none
            result_dict["Result"] = f"You lose! You have an 'None' value for the chosen stat: {chosen_stat}."
    elif opponent_stat_value is None: #if my oponent value is none then i win
            result_dict["Result"] = f"You win! Your opponent has an 'None' value for the chosen stat: {chosen_stat} ."

    elif player_stat_value == opponent_stat_value: #if are values are the same
            result_dict["Result"] ="Its a tie! Both players have equal values for the chosen stat."
    elif player_stat_value > opponent_stat_value:
            result_dict["Result"] = "You win! Your {} ({}) is higher than your opponent\'s ({}).".format(chosen_stat,
                                                                                                         player_stat_value,
                                                                                                         opponent_stat_value)
    else:
            result_dict["Result"] = "You lose! Your {} ({}) is lower than your opponent\'s ({}).".format(chosen_stat,
                                                                                                         player_stat_value,
                                                                                                         opponent_stat_value)





        # Print the result of the comparison
    print("\33[97mRESULT:\33[0m", result_dict["Result"])
    time.sleep(1)

    print("\n\n\33[97m\33[46m\33[1m--- Next Round ---\33[0m\n")
    time.sleep(1)

    # *EXTENSION* Randomly choose a stat for the opponent
    opponent_chosen_stat = random.choice(['surface_water', 'gravity', 'population', 'diameter'])
    print("Opponent chose the stat: {}".format(opponent_chosen_stat))
    time.sleep(1)

    # *EXTENSION* Get the values of the opponent's chosen stat for the player and opponent
    player_stat_value = player_planet[opponent_chosen_stat]
    opponent_stat_value = opponent_planet[opponent_chosen_stat]

    # Reset the result_dict for the next round
    result_dict["Result"] = None

    # *EXTENSION* Compare the opponent's chosen stat values and update the result_dict
    # *REQUIRED* 6. Compare the chosen stat values and update the result_dict
    if player_stat_value is None and opponent_stat_value is None:
        result_dict["Result"] = f"Both players have 'None' Values for the chosen stat: {opponent_chosen_stat}. Choose another stat"
    elif player_stat_value is None:
        result_dict["Result"] = f"You lose! You have an 'None' value for the chosen stat: {opponent_chosen_stat}."
    elif opponent_stat_value is None:
        result_dict["Result"] = f"You win! Your opponent has an 'None' values for the chosen stat: {opponent_chosen_stat}."
    elif player_stat_value == opponent_stat_value:
        result_dict["Result"] = "Its a tie! Both players have equal value for the chosen stat."
    elif player_stat_value > opponent_stat_value:
        result_dict["Result"] = "You win! Your {} ({}) is higher than your opponent\'s ({}).".format(opponent_chosen_stat,
                                                                                                     player_stat_value,
                                                                                                     opponent_stat_value)
    else:
        result_dict["Result"] = "You lose! Your {} ({}) is lower than your opponent\'s ({}).".format(opponent_chosen_stat,
                                                                                                     player_stat_value,
                                                                                                     opponent_stat_value)



    # Print the result of the comparison for the next round
    print("\33[97mRESULT:\33[0m", result_dict["Result"])

    # round_number += 1

    record_result(result_dict,player_score,opponent_score,ties)


    print("\n\33[97m\33[43m\33[1mThank you for playing! Until next time! \33[0m")


# Initiates the game
run_game()




