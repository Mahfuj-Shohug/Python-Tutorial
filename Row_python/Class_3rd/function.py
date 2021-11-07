# Reusing the calculation or logic and set the function
student = {
    '12': {
        'Name': 'Md. Mahfuj Hasan',
        'Dept': 'SWE'
    },
    '13': {
        'Name': 'Md. Shohug',
        'Dept': 'CSE'
    },
    '12': {
        'Name': 'Hasnur',
        'Dept': 'BBA'
    }
}


def find_info(id):
    student_info = student.get(id)
    if student_info == None:
        print('No data')
    else:
        print(student_info['Name'], student_info['Dept'])


find_info('12')

# Arguments and parametter


def get_number(num1, numm2):
    print(num1, numm2)


get_number(10, 20)

# Multiple Number


def multiple_num(*num):
    print(num)


multiple_num(10, 20, 30)

# Multiplle argument with keyword
# function(*args, **key)
# Must need to maintains the secquences


def arg_key(*num, **keyword):
    print(num)
    print(keyword)


arg_key(20, 30, name='Mahfuj', age='24')

# Mixed argument in function


def mixed_arg(name, age, *arg, **key):
    return name+''+str(age)


print(mixed_arg('Mahfuj', 24))

# If return any kind of arguments must need to print the argument
# outside the function
