def move(state, direction):
    state = list(state)

    def check_moves(statiii):
        possible_moves = []
        for line in statiii:
            for i in range(len(line)):
                if line[i] == "o":
                    if statiii.index(line) < len(statiii) - 1:
                        if statiii[statiii.index(line) + 1][i] == " ":
                            possible_moves.append("down")
                    if i > 0:
                        if line[i - 1] == " ":
                            possible_moves.append("left")
                    if i < len(line) - 1:
                        if line[i + 1] == " ":
                            possible_moves.append("right")
                    if statiii.index(line) > 0:
                        if statiii[statiii.index(line) - 1][i] == " ":
                            possible_moves.append("up")
        return possible_moves

    # check if the state is valid, it only contains the defined characters (" ", "#", "o").
    for line in state:
        for char in line:
            if char not in [" ", "#", "o"]:
                raise Warning("Invalid character in state")
    # ceck if  each line has same length
    for line in state:
        if len(line) != len(state[0]):
            raise Warning("Invalid state, lines have different length")
    #  it contains exactly one player.
    player = 0
    for line in state:
        player += line.count("o")
    if player != 1:
        raise Warning("Invalid state, too many players")
    # check it has a sensible size (both dimensions are greater than 0).
    if len(state) == 0 or len(state[0]) == 0:
        raise Warning("Invalid state, too small")
    # check if at least one move is possible
    if not check_moves(state):
        raise Warning("Invalid state, no moves possible")
    # check if the direction is valid
    if direction not in check_moves(state):
        raise Warning("Invalid direction")
    # check that it has a sensible size (both dimensions are greater than 0)
    if len(state) == 0 or len(state[0]) == 0:
        raise Warning("Invalid state, too small")

    # move the player
    for line in state:
        if "o" in line:
            p_line = state.index(line)
            p_index = line.index("o")
    state[p_line] = state[p_line][:p_index] + " " + state[p_line][p_index + 1:]
    if direction == "up":
        state[p_line - 1] = state[p_line - 1][:p_index] + "o" + state[p_line - 1][p_index + 1:]
    elif direction == "down":
        state[p_line + 1] = state[p_line + 1][:p_index] + "o" + state[p_line + 1][p_index + 1:]
    elif direction == "left":
        state[p_line] = state[p_line][:p_index - 1] + "o " + state[p_line][p_index + 1:]
    elif direction == "right":
        state[p_line] = state[p_line][:p_index] + " o" + state[p_line][p_index + 2:]
    return tuple(state), tuple(check_moves(state))


# The following line calls the function and prints the return
# value to the Console.
s1 =(
        "###   ",
        "###o  ",
        "#    #",
        "    ##"
    )
s2 = move(s1, "right")

print("= New State =")
print("\n".join(s2[0]))
print(f"\nPossible Moves: {s2[1]}")

s3 = move(s2[0], "up")
print("= New State =")
print("\n".join(s3[0]))
print(f"\nPossible Moves: {s3[1]}")

s4 = move(s3[0], "left")
print("= New State =")
print("\n".join(s4[0]))
print(f"\nPossible Moves: {s4[1]}")

