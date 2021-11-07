# Nested function
def first_func():
    def sec_func():
        print('this id inner function')

    print('This is outer function')
    return sec_func()


first_func()


# for output must need to have secquennce
def func_1(name):
    def func_2():
        print('welcome: ', name)

    return func_2()


func_1('Mahfuj')


#validation instancce
# def fact_2(number):
#     try:
#         if not isinstance(number, int):
#             raise TypeError('sorry, number must have to be integer')
#     except TypeError as e:
#         print(e)
#     try:
#         if number < 0:
#             raise ValueError('Must input getter then 0')
#
#         def cal_fact(num):
#             if num <= 1:
#                 return 1
#             return num * cal_fact(num - 1)
#
#     return cal_fact(num)
# print(fact_2(5))
def factorial(number):
    try:
        if not isinstance(number, int):
            raise TypeError("Sorry, number have to be integer")
        if number < 0:
            raise ValueError("please input number must be bigger then 0")

        def cal_fact(num):
            if num <= 1:
                return 1
            return num * cal_fact(num - 1)

        return cal_fact(number)
    except Exception as e:
        print(e)
#lamda function
num = lambda x: x**2
print(num(10))

# condition function in lambda
num_1 = lambda y: y**3 if y==10 else y**2
print(num_1(10))

# multiple argument
lam_func = lambda a, b: a+b if a == 100 and b == 200 else a-b
print(lam_func(20, 30))