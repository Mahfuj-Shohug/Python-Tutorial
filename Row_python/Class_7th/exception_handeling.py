# This is use for the find out the error
print('Exception Handeling')
# print(6/0)
print(6/2)
# System of exception handeling
try:
    number = int(input())
    print(100/number)
except ZeroDivisionError as error:
    print(error)
# mother class of exception handeling
# multiple exception handeling
print('ok')
try:
    number = int(input())
    print(50/number)
except Exception as error:
    print(error)

#solution of this exception handeling 
# Using Recurtion Function

def error_hand():
    try:
        number = int(input())
        print(50/number)
    except Exception as error:
        print(error)
        # if error then recal then repete
        error_hand()

error_hand()
