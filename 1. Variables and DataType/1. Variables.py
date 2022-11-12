# Introduction
"""
1.  Containers (reserved memory location) that hold the value.
2.  Values once assigned can be used later for computational purposes.
3.  Declaration not necessary prior to use.
"""

# Naming Convention
'''
1. Variable names can contain only alphabets, numbers or underscores. [A-Za-z0-9_].
2. First character of the variable cannot be a number. Example: list2 is valid but 2list is invalid
3. Variable names cannot be the same as keywords of python and its inbuilt function name. 
4. Keywords are name that has special meaning on programming language
5. Variable name should be proper as per naming convention and should pose a proper message about the value being stored
6. Variables are case-sensitive. Example: my_list and MY_LIST are different
'''

# Printing Reserved Keywords in Python
import keyword
print(keyword.kwlist)

# Left side is variable name and right side is value for it. Different data type used in the example
channel_name_string = 'Tech Tutorial'
series_name = 'Python Tutorial Series'

course_length_int = 10
average_dedication_float = 2.3

other_courses_list = ['AWS', 'MySQL', 'Git', 'MongoDB']
social_medias_tuple = ('Facebook', 'Instagram', 'Twitter', 'LinkedIn')
channel_info_dict = {'name': 'Tech Tutorial', 'category': 'Education', 'courses': ['AWS', 'Python'], 'rating': 9.7,
                     'established_date': 2021}
play_list_set = {'AWS', 'Python', 'MySQL', 'Git'}
is_active_bol = True
