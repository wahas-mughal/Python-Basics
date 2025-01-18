# def print_x_times(parameter = 'value', loop_amount = 8):
#     count = 0
#     print(global_var) # global scope of the variable 
#     while count < loop_amount:
#      print(count, parameter)
#      count += 1
#     return loop_amount

# # call
# global_var = 'global variable'
# test = print_x_times() 
# print(test)

# def hypotenuse_calculator(side_a = 1, side_b = 1):
#     hypotenuse = (side_a ** 2 + side_b ** 2) ** (1/2)
#     return round(hypotenuse, 2)

# print(hypotenuse_calculator(side_a = 5, side_b = 4))

#exercise

# def shouter(string = 'values', number = 1):
#     counter = 1
#     if number > 10:
#         print('you are too loud')
#         return
#     while counter <= number:
#        counter += 1
#        print(string.upper())
#     return 'done'

# test = shouter('test', 10)
# print(test)

# by net ninja

def shout(output_string = 'hello', repition_amount = 2):
    # print(list(range(repition_amount))) if repition_amount = 6, returns [0, 1, 2, 3, 4, 5, 6]
    if repition_amount <= 10:
        for i in range(repition_amount):
            print(output_string.upper())
    else:
        print('you are too loud')
    return 'done'

status = shout()
print(status)