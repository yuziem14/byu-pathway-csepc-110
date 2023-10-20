'''
Week 06 Team Activity Project: HR System
CSEPC 110

Authors
@Yuri Nunes
@Gabriely Silveira
@Diana Mera Angulo
@Randy Munõz
'''
# Import OS library to get the current path
import os

# Define Constants
NAME_INDEX = 0
ID_INDEX = 1
TITLE_INDEX = 2
SALARY_INDEX = 3
MONTHS_PER_YEAR = 12
TIMES_PAID_PER_MONTH = 2

employees = []

FILE_PATH = f'{os.path.dirname(__file__)}/data/hr_system.txt'

with open(FILE_PATH) as employees_file:
    for employee_line in employees_file:
        employee_line = employee_line.strip()
        employee = employee_line.split(' ')
        employees.append(employee)

for employee in employees:
    name = employee[NAME_INDEX]
    id_number = employee[ID_INDEX]
    title = employee[TITLE_INDEX]
    yearly_salary = float(employee[SALARY_INDEX])
    pay_amount = (yearly_salary / (MONTHS_PER_YEAR * TIMES_PAID_PER_MONTH))

    if(title.lower() == 'engineer'):
        bonus = 1000
        pay_amount += bonus 

    print(f'{name} (ID: {id_number}), {title} - ${pay_amount:.2f}')
