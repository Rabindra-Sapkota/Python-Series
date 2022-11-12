# Items are enclosed inside {} bracket and separated by comma
# Stores unique values only
# Used to perform mathematical set operations like union, intersection, difference, subset
# Only hashable datatype can be used. Example: numeric, string, tuple but tuple's data should be sting or numeric only
# Set are not sequenced i.e position is invalid
# Thus, index related functions such as index, slicing, insert are invalid
# Generally used for lookups


print('\n', '-' * 15, 'Representation', '-' * 15)
int_set = {1, 2, 4}
str_set = {'Python', 'AWS', 'Git'}
mixed_set = {4, 'Python', ('AWS', 'Git'), True}
print('Int Set: ', int_set)
print('Str Set: ', str_set)
print('Mixed Set: ', mixed_set)


# print('\n', '-' * 15, 'Only Hashable Demo', '-' * 15)
# list_set = {['Python', 'AWS'], [3, 4]}   # Generates Error. Invalid Items: List, Set, dict
# Tuple should only contain number and string


print('\n', '-' * 15, 'Unique and Arbitrary Order (index invalid)', '-' * 15)
sample_set = {1, 5, 'Python', 'AWS', 1, 'Python'}
print('Sample Set: ', sample_set)


print('\n', '-' * 15, 'add', '-' * 15)
print('Sample Set: ', sample_set)
sample_set.add('Git')
print('After add (Git): ', sample_set)


print('\n', '-' * 15, 'update from iterable', '-' * 15)
print('Sample Set: ', sample_set)
new_iterable = [7, 'Linux']
print('Iterable List: ', new_iterable)
sample_set.update(new_iterable)
print('After Update: ', sample_set)

print('\n', '-' * 15, 'remove', '-' * 15)
print('Sample Set: ', sample_set)
sample_set.remove(5)
print('After Remove (5): ', sample_set)
# sample_set.remove('Looker')  # Key Error


print('\n', '-' * 15, 'discard', '-' * 15)
print('Sample Set: ', sample_set)
sample_set.discard('Linux')
print('After Discard (Linux): ', sample_set)
sample_set.discard('Azure')
print('After Discard (Azure): ', sample_set)


print('\n', '-' * 15, 'clear', '-' * 15)
print('Sample Set: ', int_set)
int_set.clear()
print('After Clear: ', int_set)


print('\n', '-' * 15, 'containment', '-' * 15)
print('Sample Set: ', sample_set)
print('Check AWS: ', 'AWS' in sample_set)
print('Check Java: ', 'Java' in sample_set)


print('\n', '-' * 15, 'copy', '-' * 15)
print('Sample Set: ', str_set)
invalid_copy = str_set
invalid_copy.add('Java')
print('Copied Set: ', invalid_copy)
print('Original Set: ', str_set)
print()

valid_copy = str_set.copy()
valid_copy.add('Looker')
print('Copied Set: ', valid_copy)
print('Original Set: ', str_set)


print('\n', '-' * 15, 'union', '-' * 15)
planned_set = {'AWS', 'Python', 'Git', 'MySQL', 'Linux'}
current_set = {'AWS', 'Python', 'Personal'}
print('Planned Set: ', planned_set)
print('Current Set: ', current_set)
print('Union: ', planned_set.union(current_set))
print('Union: ', planned_set | current_set)


print('\n', '-' * 15, 'intersection', '-' * 15)
print('Planned Set: ', planned_set)
print('Current Set: ', current_set)
print('Intersection: ', planned_set.intersection(current_set))
print('Intersection: ', planned_set & current_set)


print('\n', '-' * 15, 'difference', '-' * 15)
print('Planned Set: ', planned_set)
print('Current Set: ', current_set)
print('Difference: ', planned_set.difference(current_set))
print('Difference: ', planned_set - current_set)


print('\n', '-' * 15, 'symmetric difference', '-' * 15)
print('Planned Set: ', planned_set)
print('Current Set: ', current_set)
print('Sym Diff: ', planned_set.symmetric_difference(current_set))
print('Sym Diff: ', planned_set ^ current_set)


print('\n', '-' * 15, 'isdisjoint', '-' * 15)
print('Planned Set: ', planned_set)
print('Current Set: ', current_set)
print('Is Disjoint: ', planned_set.isdisjoint(current_set))
print('{1, 2} disjoint {3, 4}: ', {1, 2}.isdisjoint({3, 4}))


print('\n', '-' * 15, 'issubset', '-' * 15)
print('Planned Set: ', planned_set)
print('Current Set: ', current_set)
print('Is Subset: ', planned_set.issubset(current_set))
print('{1} is subset {1, 2}: ', {1}.issubset({1, 2}))
print('{1, 2} is super-set {1}: ', {1,2 }.issuperset({1}))


print('\n', '-' * 15, 'frozen set', '-' * 15)
frozen_planned = frozenset(planned_set)
print('Frozen Set: ', frozen_planned)
# frozen_planned.remove('MySQL')
# Add, update invalid as set is frozen and we cannot add/remove item. Other functions are valid
print('Difference: ', frozen_planned - {'Python'})
