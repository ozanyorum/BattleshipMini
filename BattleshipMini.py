import random


def generate_matrix(rows, cols, battleships, hidden_matrix=0):

    """Create a list of the matrix contents according to user input values and shuffle it.
    If hidden_matrix == 1, create a list with question marks that the user will see, instead of the real cpu_matrix."""

    matrix = []
    matrix_contents = []

    if hidden_matrix == 0:
        for _ in range((rows * cols) - battleships):
            matrix_contents.append(" ")
        for _ in range(battleships):
            matrix_contents.append("O")
        random.shuffle(matrix_contents)

    else:
        for _ in range(rows * cols):
            matrix_contents.append("?")

    # Create a nested list to initialize the matrix

    for _ in range(cols):
        list = []
        for _ in range(rows):
            list.append(matrix_contents[0])
            del matrix_contents[0]
        matrix.append(list)

    return matrix


def vertical_matrix(matrix):
    """Convert the horizontal nested list into a vertical matrix-like list"""
    return_value = ""
    row_number = 1
    for i in matrix:
        return_value += f"{row_number}: {str(i)} \n"
        row_number += 1
    return return_value


def main():

    rows = 10
    cols = 10
    battleships = 20

    # Uncomment the code below to allow manuel row, column, and battleship amount input.

    # while True:
    #     try:
    #         rows = int(input("Please enter the amount of rows (Default: 5): "))
    #     except:
    #         print("Please enter a correct value")
    #     try:
    #         cols = int(input("Please enter the amount of columns (Default: 5): "))
    #     except:
    #         print("Please enter a correct value")
    #     try:
    #         battleships = int(
    #             input("Please enter the amount of battleships (Default: 6): ")
    #         )
    #     except:
    #         print("Please enter a correct value")
    #     break

    # Generate the user's and the CPU's nested lists with the given values.
    user_matrix = generate_matrix(rows, cols, battleships)
    cpu_matrix = generate_matrix(rows, cols, battleships)

    # This list will be used to display CPU's grid as question marks to the user
    cpu_hidden_matrix = generate_matrix(rows, cols, battleships, 1)

    user_ships = cpu_ships = battleships

    while user_ships > 0 and cpu_ships > 0:

        # User's Turn

        print("Your turn!")
        print("\nCPU's Board:")
        print(vertical_matrix(cpu_hidden_matrix))

        while True:
            try:
                user_attack_row = int(input("Select a row to strike: ")) - 1
                break
            except:
                print("Please enter a correct value")
        while True:
            try:
                user_attack_col = int(input("Select a column to strike: ")) - 1
                break
            except:
                print("Please enter a correct value")
        if cpu_matrix[user_attack_row][user_attack_col] == "O":
            print("\nShip sunk!")
            cpu_matrix[user_attack_row][user_attack_col] = "X"
            cpu_hidden_matrix[user_attack_row][user_attack_col] = "X"
            cpu_ships -= 1
            print("Remaining CPU Ships: ", cpu_ships)
        else:
            print("\nMissed")
            cpu_hidden_matrix[user_attack_row][user_attack_col] = "/"

        print("\nCPU's Board:")
        print(vertical_matrix(cpu_hidden_matrix))

        input("Press Enter to continue.")

        # CPU's Turn

        # Randomly select a square on the user's matrix.
        # If the square was selected before, select a new one until its a unique selection

        unique_selection = False
        while unique_selection == False:
            cpu_random_row = random.randrange(0, rows)
            cpu_random_col = random.randrange(0, cols)
            cpu_random_selection = user_matrix[cpu_random_row][cpu_random_col]
            if cpu_random_selection != "X" and cpu_random_selection != "/":
                unique_selection = True

        if cpu_random_selection == "O":
            print("\nCPU sunk one of your ships")
            user_ships -= 1
            print("Your remaining ships: ", user_ships)
            user_matrix[cpu_random_row][cpu_random_col] = "X"
        else:
            print("\nCPU failed to sink your ship")
            user_matrix[cpu_random_row][cpu_random_col] = "/"

        print("\nYour Board")
        print(vertical_matrix(user_matrix))

        input("Press Enter to continue.")

    print("\nGame Over\n")

    if cpu_ships == 0:
        print("You Won")
    else:
        print("You lost")
    input()


if __name__ == "__main__":
    main()
