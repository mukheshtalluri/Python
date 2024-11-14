def pattern(rows):
    for i in range(rows):
        for j in range(i):
            print(" ", end = " ")
        for k in range((rows - i -1) * 2 + 1):
            print("*", end = " ")
        print(" ")

pattern(5)
