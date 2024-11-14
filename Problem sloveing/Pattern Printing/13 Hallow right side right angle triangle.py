def pattern(rows):
    for i in range(rows):
        for j in range(rows):
            if j == rows - 1 or i == rows - 1 or i + j == rows - 1:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print(" ")

pattern(5)