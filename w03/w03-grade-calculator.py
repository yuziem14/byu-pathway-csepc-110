'''
Week 03 Team Activity Project: Grade Calculator Progam
CSEPC 110

Authors
@Yuri Nunes
@Gabriely Silveira
@Randy Munõz
'''

# Define Constant Grades Minimum and Signs
A_MINIMUM = 90
B_MINIMUM = 80
C_MINIMUM = 70
D_MINIMUM = 60
PLUS_SIGN_MINIMUM = 7
MINUS_SIGN_MINIMUM = 3
PLUS_SIGN = '+'
MINUS_SIGN = '-'

grade_percentage = float(input('What\'s your grade percentage? '))
grade_last_digit = grade_percentage % 10
grade_letter = ''
grade_sign = ''
final_message = ''

# Define the Grade Sign
if(grade_last_digit >= PLUS_SIGN_MINIMUM):
    grade_sign = PLUS_SIGN
elif(grade_last_digit < MINUS_SIGN_MINIMUM):
    grade_sign = MINUS_SIGN

# Define the Grade Letter
if(grade_percentage >= A_MINIMUM):
    grade_letter = 'A'
    # Apply Sign Rule for A+
    grade_sign = grade_sign if grade_sign != PLUS_SIGN else ''
elif (grade_percentage >= B_MINIMUM and grade_percentage < A_MINIMUM):
    grade_letter = 'B'
elif (grade_percentage >= C_MINIMUM and grade_percentage < B_MINIMUM):
    grade_letter = 'C'
elif (grade_percentage >= D_MINIMUM and grade_percentage < C_MINIMUM):
    grade_letter = 'D'
else:
    grade_letter = 'F'
    grade_sign = ''

# Defines if is approved and set the final message variable
if (grade_percentage >= C_MINIMUM):
    final_message = 'You\'re approved. Congratulations!'
else:
    final_message = 'Sorry! With this grade you can\'t be approved. Make one more try.'

# Display Results
print(f'Your grade is {grade_letter}{grade_sign}')
print(final_message)