'''
Problem 4:
Accept number from user and calculate the sum of all number from 1 to a given number
'''
input_number = int(input('Enter an Entiger Number = '))
i = 1
sum = 0
for i in range(input_number):
    sum = sum + i

print('The sum of all number from 1 to your given number = ', sum)


