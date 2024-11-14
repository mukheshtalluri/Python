"""
Error handling : If any error happen it break the program instead of breaking we can use the error handling.
"""
#print(10 / 0)

try:
    x = 10 / int(input("Enter the number you want to divide : "))
except (ValueError, ZeroDivisionError) as e:
    print(f"Error happen in operation : {e}")
else:
    print("Operation executed successfully.")

# Error handling with the all methods.
try:
    file = open("data.txt", "r")
    content = file.read()

except FileNotFoundError:
    print("File not found!")

else:
    print(content)

finally:
    file.close()
    print("File has been closed.")


