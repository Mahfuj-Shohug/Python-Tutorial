'''
8 number problem:
Concatenate two lists index-wise
'''
list_1 = ['Mahfuj:', 'faruk:']
list_2 = ['Anika', 'Shallu']
list_3 = [i + j for i, j in zip(list_1, list_2)]

print(list_3)

'''
9 number problem:
Given a Python list of numbers. Turn every item of a list into its square
'''
list_number = [10, 20, 25, 40, 15, 18, 30]
for i in list_number:
    list_number = i**2
    print(list_number)
