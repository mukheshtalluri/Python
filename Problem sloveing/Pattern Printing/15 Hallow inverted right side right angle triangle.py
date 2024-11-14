def pattern(rows):
    for i in range(rows):
        for j in range(rows):
            if i == 0 or j == rows - 1 or i == j:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print(" ")

pattern(5)