'''
@author Yuri Nunes

Week 06 Project: Data Analysis

Exceed Requirement: None
'''
# Import OS library to get the current path
import os

# Get full path from file
FILE_PATH = f'{os.path.dirname(__file__)}/data/life-expectancy.csv'

# Define Constants
ENTITY_INDEX = 0
CODE_INDEX = 1
YEAR_INDEX = 2
LE_YEARS_INDEX = 3

# Initalize variables
dataset_list = []
country_interest = []
year_interest = 0
sum_year_interest = 0
# Highest and Lowest List has [name, life_expectancy, year]
highest_country = ['', 0, 0]
lowest_country = ['', 0, 0]

# Open file, parse it and store all data in the dataset_list
with open(FILE_PATH) as dataset_file:
    for line in dataset_file:
        clear_line = line.strip()
        dataset = clear_line.split(',')
        dataset_list.append(dataset)

# Remove first line dataset (Legend)
dataset_list.remove(dataset_list[0])

year_interest = int(input('Enter the year of interest: '))

for index in range(len(dataset_list)):
    dataset = dataset_list[index]

    # Extract name, year and life expectancy from dataset
    name = dataset[ENTITY_INDEX]
    year = int(dataset[YEAR_INDEX])
    life_expectancy = float(dataset[LE_YEARS_INDEX])

    if(index == 0):
        highest_country[1] = life_expectancy
        lowest_country[1] = life_expectancy

    highest_le = highest_country[1]
    lowest_le = lowest_country[1]

    if(life_expectancy > highest_le):
        highest_country[0] = name
        highest_country[1] = life_expectancy
        highest_country[2] = year

    if(life_expectancy < lowest_le):
        lowest_country[0] = name
        lowest_country[1] = life_expectancy
        lowest_country[2] = year

    if(year == year_interest):
        country_interest.append(dataset)

# Display Highest and Lowest Life Expectancy
print()
print(f'The overall max life expectancy is: {highest_country[1]} from {highest_country[0]} in {highest_country[2]}')
print(f'The overall min life expectancy is: {lowest_country[0]} from {lowest_country[0]} in {lowest_country[2]}\n')

for index in range(len(country_interest)):
    dataset = country_interest[index]

    # Extract name, year and life expectancy from dataset
    name = dataset[ENTITY_INDEX]
    year = int(dataset[YEAR_INDEX])
    life_expectancy = float(dataset[LE_YEARS_INDEX])

    if(index == 0):
        highest_country[1] = life_expectancy
        lowest_country[1] = life_expectancy

    highest_le = highest_country[1]
    lowest_le = lowest_country[1]

    if(life_expectancy > highest_le):
        highest_country[0] = name
        highest_country[1] = life_expectancy
        highest_country[2] = year

    if(life_expectancy < lowest_le):
        lowest_country[0] = name
        lowest_country[1] = life_expectancy
        lowest_country[2] = year

    sum_year_interest += life_expectancy

# Display Average, Highest and Lowest Life Expectancy For Interest Year
average_interest = sum_year_interest / len(country_interest)

print(f'For the year {year_interest}:')
print(f'The average life expectancy across all countries was {average_interest:.2f}')
print(f'The max life expectancy was in {highest_country[0]} with {highest_country[1]}')
print(f'The min life expectancy was in {lowest_country[0]} with {lowest_country[1]}')
