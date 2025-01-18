# f strings
# user_name = 'Bob'
# user_age = 10
# user_information = f'{user_name} is {user_age} years old' # correct approach
# bad_approach = user_name + ' is ' + str(user_age) + ' years old' #bad approach
# print(user_information)

# single line if statements
# user_name = 'Anna'
# user_age = 17
# user_status = 'Adult' if user_age >= 18 else 'Child'
# if user_age < 18:
#     user_status = 'Child'
# else:
#     user_status = 'Adult'
# print(f'{user_name} is {user_age} years old and person is {user_status}')

# list comprehension
# simple_list = [f'{i}{j}' for i in range(0,11,1) for j in ('a', 'b, c') if j == 'a']
# for i in range(0, 10, 1):
#     simple_list.append(i)
# print(simple_list)

#lambda function
# def double_value(num):
#     return num * 2
# double_value = lambda num: num  * 2
# print(double_value(20))

# some functions wants a function as an argument
# random_list = [('Anna', 25), ('Paul', 40), ('Angela', 26)]
# sorted_list = sorted(random_list, key = lambda tuple_list: tuple_list[1])
# print(sorted_list)

# exercise

# simple_list = [f'{j}{i}' for i in range(1,6,1) for j in ('A', 'B', 'C', 'D', 'E') if f'{j}{i}' != 'C3']
# print(simple_list)