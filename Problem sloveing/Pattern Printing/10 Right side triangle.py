def pattern(rows):
    for i in range(rows):
        for j in range(rows - i -1):
            print(" ", end = " ")
        for k in range(i + 1):
            print("*", end = " ")
        print(" ")
    for i in range(rows -1):
        for j in range(i + 1):
            print(" ", end = " ")
        for k in range(rows - i - 1):
            print("*", end = " ")
        print(" ")

pattern(5)