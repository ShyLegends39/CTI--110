# CTI-110

# P2HW2 - List

# Kelly Bullard

# October 11, 2022

#


# The variables for Modules 1-6 will be name: mod1, mod2, mod3, mod4, mod5, mod6.
# Also, to save time and to them keep simple.

# Inputs/User's inputs
print('Enter grade for Module 1: ', end='')
mod1 = float(input())
print('Enter grade for Module 2: ', end='')
mod2 = float(input())
print('Enter grade for Module 3: ', end='')
mod3 = float(input())
print('Enter grade for Module 4: ', end='')
mod4 = float(input())
print('Enter grade for Module 5: ', end='')
mod5 = float(input())
print('Enter grade for Module 6: ', end='')
mod6 = float(input())
print('') # The in-between spaces

# Calculating the inputs from the User and making them into lists
# List part
mod_grades = [mod1, mod2, mod3, mod4, mod5, mod6] # To store their value(s) for the next part
# Calculating lists part
min(mod_grades)
max(mod_grades)
sum_grades = sum(mod_grades)
avg_grades = sum_grades/len(mod_grades)

# Output
print('------------Results------------')
print(f'Lowest Grade:       {min(mod_grades):.1f}')
print(f'Highest Grade:      {max(mod_grades):.1f}')
print(f'Sum of Grades:      {sum_grades:.1f}')
print(f'Average:            {avg_grades:.2f}')
print('-----------------------------------------')


# Pseudocode for this program's code
# NOTE: For this use the current Python(like Python 3) by using the following inputs and outputs and more for program's code.
# Certain parts were it talks about/uses float and lists, I took shot in the dark and I hope that is okay.
# I did try to them look up but it wasn't clear, so this is what I did for float and lists parts in the pseudocode?!

# START

# The variables for Modules 1-6 will be name: mod1, mod2, mod3, mod4, mod5, mod6.
# Also, to save time and to them keep simple.

# Inputs/User's inputs
# DISPLAY 'Enter grade for Module 1: ', ADD: end='', the user's input is on the prompt line
# INPUT mod1 = Float(input())
# DISPLAY 'Enter grade for Module 2: ', ADD: end='', the user's input is on the prompt line
# INPUT mod2 = Float(input())
# DISPLAY 'Enter grade for Module 3: ', ADD: end='', the user's input is on the prompt line
# INPUT mod3 = Float(input())
# DISPLAY 'Enter grade for Module 4: ', ADD: end='', the user's input is on the prompt line
# INPUT mod4 = Float(input())
# DISPLAY 'Enter grade for Module 5: ', ADD: end='', the user's input is on the prompt line
# INPUT mod5 = Float(input())
# DISPLAY 'Enter grade for Module 6: ', ADD: end='', the user's input is on the prompt line
# INPUT mod6 = Float(input())
# DISPLAY '' # The in-between spaces

# Calculating the inputs from the User and making them into lists
# List part
# LIST: mod_grades = [mod1, mod2, mod3, mod4, mod5, mod6] # To store their value(s) for the next part
# Calculating lists part
# DETERMINE min(mod_grades)
# DETERMINE max(mod_grades)
# COMPUTE sum_grades = sum(mod_grades)
# CALCULATE avg_grades = sum_grades/len(mod_grades)

# Output
# DISPLAY '------------Results------------'
# DISPLAY Float'Lowest Grade:       {min(mod_grades):.1f}'
# DISPLAY Float'Highest Grade:      {max(mod_grades):.1f}'
# DISPLAY Float'Sum of Grades:      {sum_grades:.1f}'
# DISPLAY Float'Average:            {avg_grades:.2f}'
# DISPLAY '-----------------------------------------'

# END

#
