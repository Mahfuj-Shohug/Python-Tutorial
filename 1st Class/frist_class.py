
print('Hello Mahfuj')

# variable, data types, conditions, loops
# variable => Storage, Features, Using for data store
name = 'friend'
print(name)
"""
Multiline 
comment
python case sensetive
"""
# data type
"""
1. primitive: Int, float, bool
2. Non-primitive: string, array (buliding)
"""
print(type(name))
int_variable = 100
float_variable = 10.5
bool_varibale = True
print(type(int_variable))
print(type(float_variable))
print(type(bool_varibale))

# Conditions
con = True
if con == True:
    print('Class will be held')
else:
    print('Not be happend')

# Nested Condition
# User Input
age = int(input('Enter Your Age ='))
if age >= 18:
    print('You are able to have NID')
    nid = input('do you have NID (Y/N) =')
    if nid == 'Y':
        print('Able to get vote')
    else:
        print('Bring your NID')
else:
    print('Cant able to vote you are under 18')

# Condition Ladder
# ==, <=, >=, !=, or(|), and(&)
mark = int(input('Enter your mark = '))
if mark <= 40:
    print('Fail')
elif mark > 40 and mark < 80:
    print('Pass')
elif mark >= 80:
    print('Outstanding')
else:
    print('You must need to inpute your number')
