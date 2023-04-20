# Given two integer numbers return their product
# only if the product is equal to or lower than 1000,
# else return their sum.

def multiplication_or_sum (num1, num2):
    if num1 * num2 <= 1000:
        return num1 * num2
    elif num1 * num2 > 1000:
        return num1 + num2


print(multiplication_or_sum(20, 30))
print(multiplication_or_sum(40, 30))