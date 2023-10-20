'''
Week 05 Team Activity Project: List Of Numbers
CSEPC 110

Authors
@Yuri Nunes
@Gabriely Silveira
@Diana Mera Angulo
@Randy Munõz
'''
# Define Stop number constant
STOP_NUMBER = 0

# Initialize variables
numbers = []
number_input = STOP_NUMBER + 1
total_sum = 0
largest_number = 0
smallest_number = 99999999999

print(f'Enter a list of numbers, type {STOP_NUMBER} when finished.')

while(number_input != STOP_NUMBER):
    # Ask for number
    number_input = int(input('> Enter Number: '))

    # Check if the input is 0
    if(number_input == STOP_NUMBER):
        continue

    # Initialize largest with the first input
    if(len(numbers) == 0):
        largest_number = number_input

    # Add to the list
    numbers.append(number_input)

    # Replace the largest number if the input is largest than the previous one
    if(number_input > largest_number):
        largest_number = number_input

    # Check if number is positive and if it is smallest than the previous one
    if(number_input > 0 and number_input < smallest_number):
        smallest_number = number_input
    
    # Add the number into the total
    total_sum += number_input

# Get avergae
average = total_sum / len(numbers)

print(f'The sum is: {total_sum}')
print(f'The average is: {average}')
print(f'The largest number is: {largest_number}')
print(f'The smallest positive number is: {smallest_number}')
print('The sorted list is:')

# Sort and print numbers
for number in sorted(numbers):
    print(number)