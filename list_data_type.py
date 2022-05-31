# Items are enclosed inside [] bracket and separated by comma
# Can store any valid data type of python

print('\n', '-' * 15, 'Representation', '-' * 15)
courses_list = ['Python', 'AWS', 'Git', 'Excel', 'Hadoop']
rating_list = [3.4, 3, 2.9]
mixed_list = ['Python', 2.3, {'AWS', 'Git'}, {'Name': 'Tech Tutorial'}, ('Learn', 'Fun'), True]
print('String item only: ', courses_list)
print('Numeric item only: ', rating_list)
print('Mixed item: ', mixed_list)


print('\n', '-' * 15, 'Indexing', '-' * 15)
print('Courses List: ', courses_list)
print('Rating List: ', rating_list)
print('First item of Courses list: ', courses_list[0])
print('Last item of Courses list: ', courses_list[-1])
print('Second item of Rating list: ', rating_list[1])


print('\n', '-' * 15, 'Slicing', '-' * 15)
print('Sample list: ', courses_list)
print('third to fifth item: ', courses_list[2:5])
print('Last Two item: ', courses_list[-2:])
print('Till Second item: ', courses_list[:2])
print('Skipping One item: ', courses_list[::2])
print('Reverse List: ', courses_list[::-1])


print('\n', '-' * 15, 'Repetition', '-' * 15)
print('Sample List: ', rating_list)
print('Repeated Twice: ', rating_list * 2)
print('Repeated Thrice: ', rating_list * 3)


print('\n', '-' * 15, 'len', '-' * 15)
print('Sample List: ', mixed_list)
print('Length: ', len(mixed_list))


print('\n', '-' * 15, 'join', '-' * 15)
print('Sample List: ', courses_list)
print('Joined with space: ', ' '.join(courses_list))
print('Joined with dash: ', '-'.join(courses_list))
print('Joined with dot: ', '.'.join(courses_list))


print('\n', '-' * 15, 'index', '-' * 15)
print('Sample List: ', courses_list)
print('AWS index: ', courses_list.index('AWS'))
# print('Java index: ', courses_list.index('Java'))  # Raises Error


print('\n', '-' * 15, 'count', '-' * 15)
sample_list = ['Learn', 'Fun', 'Eat', 'Fun', 'Travel', 'Fun', 'Eat']
print('Sample List: ', sample_list)
print('Count of item Fun: ', sample_list.count('Fun'))
print('Count of item Eat: ', sample_list.count('Eat'))
print('Count of item Dance: ', sample_list.count('Dance'))


print('\n', '-' * 15, 'containment', '-' * 15)
print('Sample List: ', courses_list)
print('Check Python in List: ', 'Python' in courses_list)
print('Check Java in List: ', 'Java' in courses_list)


print('\n', '-' * 15, 'substitute', '-' * 15)
print('Sample List: ', courses_list)
courses_list[3] = 'Power BI'
print('After Substitution: ', courses_list)


print('\n', '-' * 15, 'append', '-' * 15)
print('Sample List: ', courses_list)
courses_list.append('Java')
print('After Append: ', courses_list)


print('\n', '-' * 15, 'pop', '-' * 15)
print('Sample List: ', courses_list)
popped_value = courses_list.pop()
print('Popped Value: ', popped_value)
print('After pop: ', courses_list)


print('\n', '-' * 15, 'insert', '-' * 15)
print('Sample List: ', courses_list)
courses_list.insert(2, 'Python')
print('After Insert: ', courses_list)


print('\n', '-' * 15, 'remove', '-' * 15)
print('Sample List: ', courses_list)
courses_list.remove('Python')
print('After First Removal', courses_list)
courses_list.remove('Python')
print('After Second Removal', courses_list)


print('\n', '-' * 15, 'extend', '-' * 15)
print('Sample List: ', courses_list)
new_courses = ['Tableau', 'Looker']
print('New Courses: ', new_courses)
courses_list.extend(new_courses)
print('After Extend: ', courses_list)


print('\n', '-' * 15, 'del', '-' * 15)
print('Sample List: ', rating_list)
del(rating_list[1])
print('After Element Delete: ', rating_list)
del rating_list
# print(rating_list)  # raises error as list is already deleted


print('\n', '-' * 15, 'copy', '-' * 15)
print('Sample List: ', courses_list)
copied_list = courses_list
copied_list.append('SQL')
print('Append effect on copied list: ', copied_list)
print('Append effect on original list: ', courses_list)   # Why SQL append here also. Justify

valid_copy = courses_list[:]    # or valid_copy = list(courses_list) is also valid
print()
valid_copy.append('Azure')
print('Append effect on copied list: ', valid_copy)
print('Append effect on original list: ', courses_list)


print('\n', '-' * 15, 'sum, min, max', '-' * 15)
sample_list = [8, 3, 2, 4, 11, 20]
print('Sample List: ', sample_list)
print('Sum of items: ', sum(sample_list))
print('Min Value: ', min(sample_list))
print('Max Value: ', max(sample_list))


print('\n', '-' * 15, 'sort, sorted', '-' * 15)
print('Sample List: ', sample_list)
print('Sorted List: ', sorted(sample_list))
print('Descending Sort: ', sorted(sample_list, reverse=True))
sample_list.sort()
print('Inplace Sort', sample_list)
sample_list.sort(reverse=True)
print('Inplace Descending Sort', sample_list)


print('\n', '-' * 15, 'sort alphabets', '-' * 15)
sample_list = ['a', 'da', 'z', 'ab']
print('Sample List: ', sample_list)
sample_list.sort()
print('Dictionary Sort: ', sample_list)
sample_list.sort(reverse=True)
print('Dictionary Sort (Reverse): ', sample_list)
sample_list.sort(key=len)
print('Length Sort: ', sample_list)
sample_list.sort(key=len, reverse=True)
print('Length Sort (Reverse): ', sample_list)


print('\n', '-' * 15, 'reverse', '-' * 15)
print('Sample List: ', courses_list)
courses_list.reverse()
print('Reversed List: ', courses_list)
