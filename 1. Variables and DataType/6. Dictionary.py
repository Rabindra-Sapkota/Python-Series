# Items are enclosed inside {} bracket and separated by comma
# Each item is a key-value pairs where key and values are separated by colon (:)
# Keys can be immutable data type and value can be any valid data type of Python
# Keys are unique in dictionary (i.e multiple not allowed) and dictionary are not sequenced i.e position is invalid
# Thus, index related functions such as index, slicing, insert are invalid
# Generally used for lookups


print('\n', '-' * 15, 'Representation', '-' * 15)
sample_dict = {'channel': 'Tech Tutorial', 'courses_number': 3, 'courses_list': ['AWS', 'Python', 'Git']}
my_dict2 = dict(name='Python', length=35, features={'Course': 'Full', 'Lab': True})
print('First Dictionary: ', sample_dict)
print('Second Dictionary: ', my_dict2)


print('\n', '-' * 15, 'Immutable Concept', '-' * 15)
sample_list = ['Cat', 'Rat', 'Bat']
print('Original List: ', sample_list)
sample_list[0] = 'Hat'
print('List after updating: ', sample_list)

sample_string = 'Cat'
# sample_string[0] = 'R'

sample_tuple = ('Cat', 'Rat', 'Bat')
# sample_tuple[0] = 'Hat'


print('\n', '-' * 15, 'Accessing Element', '-' * 15)
print('Sample Dictionary: ', sample_dict)
channel_value = sample_dict['channel']
print('Accessing Name: ', channel_value)
courses_number = sample_dict.get('courses_number')
print('Courses Number: ', courses_number)
rating = sample_dict.get('rating', 4.9)
print('Rating Value: ', rating)

print('\n', '-' * 15, 'Add/Update Element', '-' * 15)
print('Sample Dictionary: ', sample_dict)
sample_dict['courses_number'] = 6
print('After update: ', sample_dict)
sample_dict['rating'] = 4.8
print('After adding: ', sample_dict)


print('\n', '-' * 15, 'items', '-' * 15)
print('Sample Dictionary: ', sample_dict)
print('Items: ', sample_dict.items())
for key, value in sample_dict.items():
    print('Key: ', key, '& Value: ', value)


print('\n', '-' * 15, 'keys', '-' * 15)
print('Sample Dictionary: ', sample_dict)
print('Keys: ', sample_dict.keys())


print('\n', '-' * 15, 'values', '-' * 15)
print('Sample Dictionary: ', sample_dict)
print('Values: ', sample_dict.values())


print('\n', '-' * 15, 'del', '-' * 15)
print('Sample Dictionary: ', sample_dict)
del sample_dict['courses_list']
print('After Delete: ', sample_dict)
# del sample_dict
# print('After Whole Delete: ', sample_dict)  # Generates Error


print('\n', '-' * 15, 'clear', '-' * 15)
print('Sample Dictionary: ', my_dict2)
my_dict2.clear()
print('After Clear: ', my_dict2)


print('\n', '-' * 15, 'len', '-' * 15)
print('Sample Dictionary: ', sample_dict)
print('Length: ', len(sample_dict))


print('\n', '-' * 15, 'copy', '-' * 15)
dict_1 = {'name': 'Python', 'Type': 'Tutorial', 'Lab': True}
print('Sample Dictionary: ', dict_1)
copied_dict = dict_1
copied_dict['Price'] = 'Free'
print('Copied Dictionary: ', copied_dict)
print('Original Dictionary: ', dict_1)
print()
valid_copy = dict_1.copy()
valid_copy['other_course'] = 'AWS'
print('Valid Copy:', valid_copy)
print('Original Dictionary:', dict_1)


print('\n', '-' * 15, 'containment', '-' * 15)
print('Sample Dictionary: ', sample_dict)
print('Check Channel: ', 'channel' in sample_dict)
print('Check courses_list: ', 'courses_list' in sample_dict)


print('\n', '-' * 15, 'update', '-' * 15)
print('Sample Dictionary: ', sample_dict)
new_dict = {'lab': True, 'price': 'Free'}
print('Dictionary to add: ', new_dict)
sample_dict.update(new_dict)
print('After Update: ', sample_dict)


print('\n', '-' * 15, 'pop', '-' * 15)
print('Sample Dictionary: ', sample_dict)
price_value = sample_dict.pop('price')
print('Price popped: ', price_value)
print('After pop: ', sample_dict)
