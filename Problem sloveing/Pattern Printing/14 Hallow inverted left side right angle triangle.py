def pattern(rows):
    for i in range(rows):
        for j in range(rows):
            if i == 0 or j == 0 or i + j == rows - 1:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print(" ")

pattern(5)