import copy

matrix_start = []
matrix_end = []
matrix_solution_trace = []
blank_space_coordinate = []  # x then y


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
def calculate_distance_to_goal(matrix_start,matrix_end):  # bad heuristic just for proof of concept
    # check for 1,2,3,4,5,6,7,8
    n = 1

    x1 = 0  # row
    x2 = 0  # column

    y1 = 0
    y2 = 0
    found = False

    distance = 0

    while n < 8:
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
    G |  H  |  I  
      |     |     
'''


def main():
    matrix_start = copy.deepcopy(populate())  # populate start and end matrices
    print("next")
    matrix_end = copy.deepcopy(populate())
    print(calculate_distance_to_goal(matrix_start,matrix_end))
    # define legal moves

    # heuristics and A*


if __name__ == '__main__':
    main()
