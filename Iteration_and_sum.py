# Write a program to iterate the first 10 numbers
# and in each iteration, print the sum of
# the current and previous number.

print("Printing current and previous number sum in a range(10)")

previous_number = 0
border = 10
for i in range(border):
    current_number = i
    sum_of_numbers = current_number + previous_number
    print(f"Current Number: {current_number} Previous Number: {previous_number}  Sum:  {sum_of_numbers}")
    previous_number = current_number
