"""
Print Function : This function is used to print something to console.
Arguments in print function
1. values : Any object which we are trying to print.
2. sep : If multiple values want at a time we can separate them by using sep. sep = " - ". Default value : sep = " "
3. end : We want to print multiple print statements in the same line we will use end. end = " ". Default value : end = "\n"
4. file : When we want to print something directly to the file we will use file.
5. flush : when we want print value forcefully after completion of process without buffering will use flush. flush = True. Default value: flush = False
"""
print("This function is used to print.")

"""
Input function : This function is used to take input from the user.
Points to remember while using the input function.
1. If you pass integer or float value also it will be string while using with the input function.
"""
taught = input("Type what you want to type : ")

marks = input("Enter you marks : ")
print(type(marks))
marks = int(marks)
print(type(marks))



