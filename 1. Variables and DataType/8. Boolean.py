# True, False or expression that yields True/False
# Vital role in control flow statement. If, loop
true_value = True
false_value = False
print('Boolean True: ', true_value)
print('Boolean False: ', false_value)
print('Comparator Operators: ', 2 < 3)
print('Containment Operators: ', 'AWS' in ['Python', 'AWS'])


# Range
my_range = range(1, 10)
skipped_range = range(2, 10, 2)
reversed_range = range(10, 1, -1)
print(my_range)
print(*skipped_range)


# Data Type of variable is known with Type function
# Data Type can be converted into another compatible type
int_variable = 3
str_variable = 'Python'
list_variable = ['Python', 'AWS']
print(type(int_variable))

# new_data_type = data_type(old_datatype)
print(int('3'))
print(bin(2))
print(tuple(['AWS', 'Python']))
int_val = int('10', base=15)
# float, set, str

# On Summary
'''
Property        List        Tuple       Set         Dictionary      string
ordered         yes         yes         no          no              yes
mutable         yes         no          yes         yes             no
unique          no          no          yes         yes             no
'''

# Number System Conversion
# Multiplication Table
