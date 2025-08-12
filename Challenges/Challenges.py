# Task 1: Sum of integers from user input
numbers = input("Enter integers separated by spaces: ").split()
int_list = [int(num) for num in numbers]
print("Sum of all integers:", sum(int_list))



