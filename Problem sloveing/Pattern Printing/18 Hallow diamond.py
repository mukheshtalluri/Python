def pattern(rows):
    for i in range(rows - 1):
        for j in range(rows * 2 + 1):
            if j == (i + rows - 1) or i + j == rows - 1:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print(" ")

    for i in range(rows):
        for j in range( rows * 2 + 1):
            if i == j or i + j == ((rows - 1) * 2):
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print(" ")
pattern(5)