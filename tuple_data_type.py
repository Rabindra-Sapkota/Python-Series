# Items are enclosed inside () bracket and separated by comma
# Can store any valid data type of python

print('\n', '-' * 15, 'Representation', '-' * 15)
courses_tuple = ('Python', 'AWS', 'Git', 'Excel', 'Hadoop')
rating_tuple = (3.4, 3, 2.9)
mixed_tuple = ('Python', 2.3, {'AWS', 'Git'}, {'Name': 'Tech Tutorial'}, ('Learn', 'Fun'), True)
print('String item only: ', courses_tuple)
print('Numeric item only: ', rating_tuple)
print('Mixed item: ', mixed_tuple)


print('\n', '-' * 15, 'Indexing', '-' * 15)
print('Courses Tuple: ', courses_tuple)
print('Rating Tuple: ', rating_tuple)
print('First item of Courses Tuple: ', courses_tuple[0])
print('Last item of Courses Tuple: ', courses_tuple[-1])
print('Second item of Rating Tuple: ', rating_tuple[1])


print('\n', '-' * 15, 'Slicing', '-' * 15)
print('Sample Tuple: ', courses_tuple)
print('third to fifth item: ', courses_tuple[2:5])
print('Last Two item: ', courses_tuple[-2:])
print('Till Second item: ', courses_tuple[:2])
print('Skipping One item: ', courses_tuple[::2])
print('Reverse Tuple: ', courses_tuple[::-1])


print('\n', '-' * 15, 'Repetition', '-' * 15)
print('Sample Tuple: ', rating_tuple)
print('Repeated Twice: ', rating_tuple * 2)
print('Repeated Thrice: ', rating_tuple * 3)


print('\n', '-' * 15, 'len', '-' * 15)
print('Sample Tuple: ', mixed_tuple)
print('Length: ', len(mixed_tuple))


print('\n', '-' * 15, 'join', '-' * 15)
print('Sample Tuple: ', courses_tuple)
print('Joined with space: ', ' '.join(courses_tuple))
print('Joined with dash: ', '-'.join(courses_tuple))
print('Joined with dot: ', '.'.join(courses_tuple))


print('\n', '-' * 15, 'index', '-' * 15)
print('Sample Tuple: ', courses_tuple)
print('AWS index: ', courses_tuple.index('AWS'))
# print('Java index: ', courses_tuple.index('Java'))  # Raises Error


print('\n', '-' * 15, 'count', '-' * 15)
sample_tuple = ('Learn', 'Fun', 'Eat', 'Fun', 'Travel', 'Fun', 'Eat')
print('Sample Tuple: ', sample_tuple)
print('Count of item Fun: ', sample_tuple.count('Fun'))
print('Count of item Eat: ', sample_tuple.count('Eat'))
print('Count of item Dance: ', sample_tuple.count('Dance'))


print('\n', '-' * 15, 'containment', '-' * 15)
print('Sample List: ', courses_tuple)
print('Check Python in List: ', 'Python' in courses_tuple)
print('Check Java in List: ', 'Java' in courses_tuple)


print('\n', '-' * 15, 'del', '-' * 15)
print('Sample Tuple: ', rating_tuple)
del rating_tuple
# print(rating_tuple)  # raises error as tuple is already deleted


print('\n', '-' * 15, 'sum, min, max', '-' * 15)
sample_tuple = (8, 3, 2, 4, 11, 20)
print('Sample Tuple: ', sample_tuple)
print('Sum of items: ', sum(sample_tuple))
print('Min Value: ', min(sample_tuple))
print('Max Value: ', max(sample_tuple))


print('\n', '-' * 15, 'sort, sorted', '-' * 15)
print('Sample Tuple: ', sample_tuple)
print('Sorted List: ', sorted(sample_tuple))
print('Descending Sort: ', sorted(sample_tuple, reverse=True))


print('\n', '-' * 15, 'sort alphabets', '-' * 15)
sample_tuple = ('a', 'da', 'z', 'ab')
print('Sample Tuple: ', sample_tuple)
print('Dictionary Sort: ', sorted(sample_tuple))
print('Dictionary Sort (Reverse): ', sorted(sample_tuple, reverse=True))
print('Length Sort: ', sorted(sample_tuple, key=len))
print('Length Sort (Reverse): ',  sorted(sample_tuple, key=len, reverse=True))
