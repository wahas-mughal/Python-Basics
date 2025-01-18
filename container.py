#  containers
a_tuple = (1,2,3,'str')
a_list = [1,2,3,'str']
a_list.append('another str')
a_set = {1,2,3,4,2}
a_dictionary = {'name': 'XYX', 123: [1,2,3]}
a_dictionary['new key'] = 1.5 # add new key value pair in the dictionary

# print(list(set(a_set)))
# print(a_set)
# print(a_list)
# print(len(a_list))
# print(a_dictionary)

# how to get values from the containers
# we can get the data by two methods: Indexing and Slicing
 
# user_list = ['A', 'B', 'C', 'D', 'E']
# print(user_list[2])
# print(user_list[-2])
# print(user_list[0:3:2]) #0: staring index, 3: ending index (boundary), 2: size of steps
# print(a_dictionary[123])

# exercise
# a_list = [1,2,3,4,5,6,7,8,9,10]
# print(a_list[7::-2]) # output: [8,6,4,2]
