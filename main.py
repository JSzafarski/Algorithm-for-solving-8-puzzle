import copy
import os
from re import template

matrix_start = []
matrix_end = []
matrix_solution_trace = []  # Stores previous array configurations
blank_space_coordinate = []  # x then y
import os


def populate():  # one fo the spaces needs to be -1
    y = 0
    x = 0
    some_matrix = []
    entered_blank_count = 0
    row = []
    entered_array = []
    while y < 3:
        while x < 3:
            usr_imp = int(input("input numbers"))
            if usr_imp == -1:
                blank_space_coordinate.append(x)  # tells the program where empty space will be
                blank_space_coordinate.append(y)
                entered_blank_count = entered_blank_count + 1
                if entered_blank_count > 1:
                    entered_blank_count = 0
                    break
            else:
                if usr_imp < 1 or usr_imp > 8:
                    entered_blank_count = 0
                    break
                for z in entered_array:
                    if z == usr_imp:
                        entered_blank_count = 0
                        break
                entered_array.append(usr_imp)
            row.append(usr_imp)
            x = x + 1
        some_matrix.append(row)
        row = []
        x = 0  # reset for each row
        y = y + 1
    if entered_blank_count:
        return some_matrix
    else:
        print("error occurred ,check you inputs and use -1 for blank space")


# need a function that will compare positions and check how far is each value from solution
def calculate_distance_to_goal(matrix_start, matrix_end):  # bad heuristic just for proof of concept
    # check for 1,2,3,4,5,6,7,8,-1
    n = -1

    x1 = 0  # row
    x2 = 0  # column

    y1 = 0
    y2 = 0
    found = False

    distance = 0

    while n < 9:
        while y1 < 3:
            while x1 < 3:
                if matrix_start[x1][y1] == n:
                    found = True
                    break
                x1 = x1 + 1
            if found:
                break
            else:
                x1 = 0
                y1 = y1 + 1
        found = False
        while y2 < 3:
            while x2 < 3:
                if matrix_end[x2][y2] == n:
                    found = True
                    break
                x2 = x2 + 1
            if found:
                break
            else:
                x2 = 0
                y2 = y2 + 1

        distance = distance + abs(x1 - x2) + abs(y1 - y2)

        y2 = 0
        x2 = 0
        x1 = 0
        y1 = 0
        found = False
        if n == -1:
            n = n + 2
        else:
            n = n + 1

    return distance


'''
      |     |     
    A |  B  |  C  
 _____|_____|_____
      |     |     
   D  |  E  |  F  
 _____|_____|_____
      |     |     
    G |  H  |  -1  
      |     |     
'''


def print_matrix(matrix):
    print("      |     |     ")
    print("   " + str(matrix[0][0]) + " |  " + str(matrix[1][0]) + "  |  " + str(matrix[2][0]) + "  ")
    print(" _____|_____|_____")
    print("      |     |     ")
    print("   " + str(matrix[0][1]) + "  |  " + str(matrix[1][1]) + "  |  " + str(matrix[2][1]) + "  ")
    print(" _____|_____|_____")
    print("      |     |     ")
    print("    " + str(matrix[0][2]) + " |  " + str(matrix[1][2]) + "  | " + str(matrix[2][2]) + "  ")
    print("      |     |     ")


def main():
    matrix_start = copy.deepcopy(populate())  # populate start and end matrices
    print("next")
    matrix_end = copy.deepcopy(populate())
    print(calculate_distance_to_goal(matrix_start, matrix_end))  # fix this too

    # define legal moves
    # blank_space_coordinate is the starting position

    matrix_solution_trace.append(matrix_start)

    up_move = 0  # variable for weights for doing a move
    down_move = 0
    left_move = 0
    right_move = 0

    updated_1 = False
    updated_2 = False
    updated_3 = False
    updated_4 = False

    temp_matrix = copy.deepcopy(matrix_start)

    iteration_count = 0

    smallest_move_array = []

    previous_move = ""

    while True:

        x = blank_space_coordinate[0]
        y = blank_space_coordinate[1]

        matrix_solution_trace.append(temp_matrix)

        temp_matrix2 = copy.deepcopy(temp_matrix)
        temp_matrix3 = copy.deepcopy(temp_matrix)
        temp_matrix4 = copy.deepcopy(temp_matrix)
        temp_matrix5 = copy.deepcopy(temp_matrix)

        # move down

        if y > 0:
            if previous_move != "up":
                temp_val = temp_matrix2[x][y - 1]
                temp_matrix2[x][y - 1] = -1
                temp_matrix2[x][y] = temp_val
                down_move = calculate_distance_to_goal(temp_matrix2, matrix_end)
                updated_1 = True
            else:
                down_move = 100000
                # this can be optimised by seeing change each move rather than recalculating each time

        # move up
        if y < 2:
            if previous_move != "down":
                temp_val = temp_matrix3[x][y + 1]
                temp_matrix3[x][y + 1] = -1
                temp_matrix3[x][y] = temp_val
                up_move = calculate_distance_to_goal(temp_matrix3, matrix_end)
                updated_2 = True
            else:
                up_move = 100000

        # move left
        if x > 0:
            if previous_move != "right":
                temp_val = temp_matrix4[x - 1][y]
                temp_matrix4[x - 1][y] = -1
                temp_matrix4[x][y] = temp_val
                left_move = calculate_distance_to_goal(temp_matrix4, matrix_end)
                updated_3 = True
            else:
                left_move = 100000

        # move right
        if x < 2:
            if previous_move != "left":
                temp_val = temp_matrix5[x + 1][y]
                temp_matrix5[x + 1][y] = -1
                temp_matrix5[x][y] = temp_val
                right_move = calculate_distance_to_goal(temp_matrix5,
                                                        matrix_end)  ## this will be 0 if not acessed so make it high if not acessed
                updated_1 = True
            else:
                right_move = 100000

        smallest = left_move + right_move + up_move + down_move  # upperbound
        if left_move <= smallest:
            smallest = left_move
            smallest_move_array.clear()
            smallest_move_array.append("left_move")
        if right_move <= smallest:
            smallest = right_move
            smallest_move_array.clear()
            smallest_move_array.append("right_move")
        if up_move <= smallest:
            smallest = up_move
            smallest_move_array.clear()
            smallest_move_array.append("up_move")
        if down_move <= smallest:
            smallest = down_move
            smallest_move_array.clear()
            smallest_move_array.append("down_move")

        if smallest_move_array[0] == "up_move" and updated_1 is True:
            temp_matrix = copy.deepcopy(temp_matrix3)
            blank_space_coordinate[1] = y + 1
            previous_move = "up"
        elif smallest_move_array[0] == "down_move" and updated_2 is True:
            temp_matrix = copy.deepcopy(temp_matrix2)
            blank_space_coordinate[1] = y - 1
            previous_move = "down"
        elif smallest_move_array[0] == "left_move" and updated_3 is True:
            temp_matrix = copy.deepcopy(temp_matrix4)
            blank_space_coordinate[0] = x - 1
            previous_move = "left"
        elif smallest_move_array[0] == "right_move" and updated_4 is True:
            temp_matrix = copy.deepcopy(temp_matrix5)
            blank_space_coordinate[0] = x + 1
            previous_move = "right"
        updated_1 = False  # recently updated
        updated_2 = False
        updated_3 = False
        updated_4 = False

        if smallest == 0:
            print("number of counts: " + str(iteration_count))
            print(matrix_solution_trace)
            print_matrix(temp_matrix)
            break

        iteration_count = iteration_count + 1
        print("iteration_count :" + str(iteration_count) + " heuristic value: " + str(smallest))
        smallest_move_array.clear()
        print_matrix(temp_matrix)


##add a stack to keep track of the moves or create a tree and do some sort of back tracking

if __name__ == '__main__':
    main()
