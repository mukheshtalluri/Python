def pattern(rows):
    for i in range(rows):
        for j in range((rows - 1) * 2 + 1):
            if i == rows - 1 or i + j == rows - 1 or i + rows - 1 == j:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print(" ")

pattern(5)
