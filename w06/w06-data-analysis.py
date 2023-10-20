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
FIRST_LINE_STRING = 'Entity,Code,Year,Life expectancy (years)'.lower()

# Initalize variables
dataset_list = []
highest_le = 0
lowest_le = 0

# Open file, parse it and store all data in the dataset_list
with open(FILE_PATH) as dataset_file:
    for line in dataset_file:
        clear_line = line.strip()
        dataset = clear_line.split(',')
        dataset_list.append(dataset)

# Remove first line dataset (Legend)
first_line_dataset = dataset_list[0]
dataset_list.remove(first_line_dataset)

for index in range(len(dataset_list)):
    dataset = dataset_list[index]
    life_expectancy = float(dataset[LE_YEARS_INDEX])
    
    # initialize max and low with the first value
    if(index == 0):
        highest_le = life_expectancy
        lowest_le = life_expectancy

    # Check if current value is higher than the previous one
    if(life_expectancy > highest_le):
        highest_le = life_expectancy

    # Check if current value is lowest than the previous one
    if(life_expectancy < lowest_le):
        lowest_le = life_expectancy

# Display Highest and Lowest Life Expectancy
print(f'The overall max life expectancy is: {highest_le:.2f}')
print(f'The overall min life expectancy is: {lowest_le:.2f}')