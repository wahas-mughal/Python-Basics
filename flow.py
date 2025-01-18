# print(4 == 4)

# if 5 > 6:
#     print('true')
# elif 2 > 3:
#     print('true') 
# elif 2 == 2 and 3 > 2:
#     print('true') 
#     if len([1,2,3]) > 2:
#         print('list length is greater than 2')
# else:
#     print('false')

# while loop
# counter = 0
# while counter <= 10:
#     print(counter)
#     counter += 1
#     if counter == 5:
#         print('counter is', counter)
# print('while loop has finished!')

# for loop
# test_list = {1:2, 3:4, 5:6} # we can have tuple, set and dictionaries
# for x in test_list:
#     print(x)
# for x in test_list.keys():
#     print(x)
# for x in test_list.values():
#     print(x)
# for x in test_list.items():
#     print(x[0])
# for k,v in test_list.items():
#     print(k, v)

# empty list, empty string values and 0 is falsy, everthing else is truthy
#truthy and falsy
# if 0:
#     print('truthy')
# else:
#     print('falsy')

#exerice
list_items = [1,2,3,4,5]

for x in list_items:
    if x == 2:
        print('the value is 2')
    else:
        print("the value isn't 2")
counter = 0
if x == 5:
    while counter <= 5:
        counter += 1
        print(x)
