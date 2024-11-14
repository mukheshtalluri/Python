def pattern(rows):
    for i in range(rows):
        for j in range((rows - 1) * 2 + 1):
            if i == 0 or i == j or i + j == (rows -1) * 2:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print(" ")

pattern(5)