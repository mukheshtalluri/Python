def pattern(rows):
    for i in range(rows):
        for j in range(rows):
            if j == 0 or i == rows - 1 or i == j:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print(" ")

pattern(5)