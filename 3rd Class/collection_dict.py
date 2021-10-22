# key diclairation
# Key value pair -> Key:Value
set_2 = {'Key_1': 'value_1', 2: 20, 3: 30.5}
print(set_2)
print(set_2['Key_1'])

# deffrent type of for loop for dict
for i, j in set_2.items():
    print(i, j)

for i, j in set_2.items():
    if i == 'Key-1':
        print(i, j)

print(set_2.get('Key_1'))

# Nested one in side of one
student = {
    '12': {
        'Name': 'Md. Mahfuj Hasan',
        'Dept': 'SWE'
    },
    '13': {
        'Name': 'Md. Shohug',
        'Dept': 'CSE'
    },
    '14': {
        'Name': 'Hasnur',
        'Dept': 'BBA'
    }
}
# search dict using get
print(student.get('12'))
student_info = student.get(input())
if student_info == None:
    print('No data')
else:
    print(student_info['Name'], student_info['Dept'])

# Printing Key and value
print(set_2.keys())
print(set_2.values())

# Updating the set
set_3 = {7: 30}
set_2.update(set_3)
print(set_2)
