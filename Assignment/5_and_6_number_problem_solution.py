'''
Problem 5:
Given a list, iterate it, and display numbers divisible by five, 
and if you find a number greater than 150, stop the loop iteration.
'''
list_num = [20, 33, 40, 54, 60, 70, 82, 88, 90, 122, 130, 142, 155]
for i in list_num:
    if i < 150:
        if (i % 5 == 0):
            print('Number is divided by 5 = ', i)
    else:
        print('Oh no this is gatter then 150')
        break


'''
Problem 6
Reverse the following list using for loop
'''
for i in reversed(list_num):
    print(i)


