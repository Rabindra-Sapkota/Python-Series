# True, False or expression that yields True/False
# Vital role in control flow statement. If, loop
print('\n', '-'*15, 'Boolean', '-'*15)
true_value = True
false_value = False
print('Boolean True: ', true_value)
print('Boolean False: ', false_value)
print('Comparator Operators: ', 2 < 3)
print('Containment Operators: ', 'AWS' in ['Python', 'AWS'])


# Range
print('\n', '-'*15, 'Range', '-'*15)
my_range = range(1, 10)
skipped_range = range(2, 10, 2)
reversed_range = range(10, 1, -1)
print(my_range)
print(*skipped_range)


# Data Type of variable is known with Type function
# Data Type can be converted into another compatible type
print('\n', '-'*15, 'Data Type', '-'*15)
int_variable = 3
str_variable = 'Python'
list_variable = ['Python', 'AWS']
tuple_variable = (5, 6)
set_variable = {1, 'Rabindra'}
dict_variable = {'Name': 'Code', 'Time': 6}
bool_variable = True

print(type(int_variable))
print(type(str_variable))
print(type(list_variable))
print(type(tuple_variable))
print(type(set_variable))
print(type(dict_variable))
print(type(bool_variable))


# new_data_type = data_type(old_datatype)
print('\n', '-'*15, 'Type Conversion', '-'*15)
print(int('3'))
print(bin(2))
print(oct(10))
print(hex(12))
print(tuple(['AWS', 'Python']))
int_val = int('b', base=16)
print(int_val)
print()

my_list = [1, 2, 3, 1]
print("Original List: ", my_list)
set_converted = set(my_list)
print("Set Converted: ", set_converted)
unique_list = list(set_converted)
print("Unique List: ", unique_list)

print()
str_flt = '10.5'
print('Original String: ', str_flt)
print(type(str_flt))
flt_converted = float(str_flt)
print('Float Converted: ', flt_converted)
print(type(flt_converted))


# On Summary
print('\n', '-'*15, 'Summary Info', '-'*15)
summary_info = '''
Property        List        Tuple       Set         Dictionary      string
ordered         yes         yes         no          no              yes
mutable         yes         no          yes         yes             no
unique          no          no          yes         yes             no
'''
print(summary_info)

# Number System Conversion
# Multiplication Table
