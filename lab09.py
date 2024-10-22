A = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

user_input = input("Введіть цифри (через пробіл): ").split()

B = tuple(A[int(digit)] for digit in user_input if digit.isdigit())

print("\nКортеж B:")
print(B)
