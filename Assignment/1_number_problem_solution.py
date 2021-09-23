'''
Given a range of the first 10 numbers, Iterate from the start number to the end number, 
and In each iteration
print the sum of the current number and previous number
'''

# Solution
sum = 0
for i in range(10):
    print(i)
    sum = sum + i
    print('Sum from the current number and previous number is = ', sum)
