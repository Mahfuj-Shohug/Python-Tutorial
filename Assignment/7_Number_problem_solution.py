'''
7 number problem:
Display “My Name Is James” as “My**Name**Is**James” using output formatting of a print() function
For example: print('My', 'Name', 'Is', 'Tamim') will display MyNameIsJames
So use one of the formatting argument of print() to turn the output into My**Name**Is**Tamim
'''
# Sample
print('My', 'Name', 'Is', 'Tamim')

# solution
arg = '**'
print('My'+arg+'Name'+arg+'Is'+arg+'James')
