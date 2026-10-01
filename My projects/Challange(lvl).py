numbers = []
numbers.append(int(input("Enter number 1:")))
numbers.append(int(input("Enter number 2:")))
numbers.append(int(input("Enter number 3:")))
numbers.append(int(input("Enter number 4:")))
numbers.append(int(input("Enter number 5:")))
#total_even = 0 total_odd = 0 total_sum = 0 has_greater = False
def process_numbers(numbers):
    total_even = 0
    total_odd = 0
    total_sum = 0
    has_greater = False
    for number in numbers:
        if number % 2 == 0: 
            total_even += 1
        else:
            total_odd += 1
        total_sum += number
        if number > 15:
            has_greater = True
    return total_even, total_odd, total_sum, has_greater
w,x,y,z = process_numbers(numbers)
print(f"Even: {w}")
print(f"Odd: {x}")
print(f"Sum: {y}")
print(f"Has greater than 15: {z}")