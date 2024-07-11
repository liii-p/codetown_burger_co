# A program to take orders for Codetown Burger Co.
# Author: David Paul <David.Paul@une.edu.au>

# Possible options for the number of burgers
BURGER_RANGE = [f"{i}" for i in range(1, 10 + 1)]

# Possible options for the bun type
BUN_TYPE = ["milk", "gluten free"]

# Possible options for the sauce type
SAUCE_TYPE = ["tomato", "barbecue", "none"]

# Possible options for the number of patties
PATTY_RANGE = [f"{i}" for i in range(0, 3 + 1)]

# Possible options for the number of slices of cheese
CHEESE_RANGE = [f"{i}" for i in range(0, 3 + 1)]

# Possible choices for whether to include tomato
TOMATO_CHOICE = ["yes", "no"]

# Possible choices for whether to include lettuce
LETTUCE_CHOICE = ["yes", "no"]

# Possible choices for whether to include onion
ONION_CHOICE = ["yes", "no"]

# The base cost of a burger
BASE_BURGER_COST = 5

# The extra charge for a gluten free burger
GLUTEN_FREE_COST = 1

# The extra charge for an extra patty
EXTRA_PATTY_COST = 3

# The extra charge for an extra slice of cheese
EXTRA_CHEESE_COST = 1

# The extra charge for an extra salad item
EXTRA_SALAD_COST = 1


def get_choice(prompt, choices):
    """
    Uses the given prompt to ask users to choose one of the valid given choices (case insensitive).
    Will continually prompt the user until they enter a valid choice, which is then returned.

    parameters:
      - prompt: The prompt to display when requesting input from the user
      - choices: A list of valid choices the user can enter

    returns:
      - A valid choice from choices, in lower case
    """
    result = input(prompt)
    while result.lower() not in choices:
        print(f"Please enter a valid choice: {choices}")
        result = input(prompt)
    return result.lower()


def main():
    """ Main program to get user's order """
    print("Welcome to Codetown Burger Co!")

    # Determine number of burgers in the order
    burgers = get_choice(f"How many burgers would you like to order [{BURGER_RANGE[0]}-{BURGER_RANGE[-1]}]? ", BURGER_RANGE)
    num_burgers = int(burgers)

    # The total cost for the order
    total_cost = 0
    
    # Get details for each burger
    for i in range(1, num_burgers + 1):
        print(f"Details for Burger {i}:")

        # Get burger choices
        bun = get_choice(f"\tWhat bun type should be included for Burger {i} {BUN_TYPE}? ", BUN_TYPE)

        sauce = get_choice(f"\tWhat sauce should be included on Burger {i} {SAUCE_TYPE}? ", SAUCE_TYPE)

        patties = get_choice(f"\tHow many patties should be on Burger {i} [{PATTY_RANGE[0]}-{PATTY_RANGE[-1]}]? ", PATTY_RANGE)
        # The number of patties on the burger
        patty_count = int(patties)

        cheese = get_choice(f"\tHow many slices of cheese should be on Burger {i} [{CHEESE_RANGE[0]}-{CHEESE_RANGE[-1]}]? ", CHEESE_RANGE)
        # The number of cheese slices on the burger
        cheese_count = int(cheese)

        # The number of salad items on the burger
        salad_count = 0
        tomato = get_choice(f"\tShould Burger {i} have tomato {TOMATO_CHOICE}? ", TOMATO_CHOICE)
        if "yes" == tomato:
            salad_count += 1

        lettuce = get_choice(f"\tShould Burger {i} have lettuce {LETTUCE_CHOICE}? ", LETTUCE_CHOICE)
        if "yes" == lettuce:
            salad_count += 1

        onion = get_choice(f"\tShould Burger {i} have onion {ONION_CHOICE}? ", ONION_CHOICE)
        if "yes" == onion:
            salad_count += 1

        # Calculate the cost of the burger and add to total
        burger_cost = BASE_BURGER_COST
        if "gluten free" == bun:
            burger_cost += GLUTEN_FREE_COST
        if patty_count > 1:
            burger_cost += EXTRA_PATTY_COST * (patty_count - 1)
        if cheese_count > 1:
            burger_cost += EXTRA_CHEESE_COST * (cheese_count - 1)
        if salad_count > 1:
            burger_cost += EXTRA_SALAD_COST * (salad_count - 1)

        total_cost += burger_cost

    # Output total cost
    print(f"Total cost for the {num_burgers} burger(s): ${total_cost}")

# Program entry point
if __name__ == "__main__":
    main()
