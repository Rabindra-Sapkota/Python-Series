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

# In Example Below, left side of equal sign denotes name of variable and right denotes the value stored for it
channel_name = 'Tech Tutorial'              # String Value
series_name = 'Python Tutorial Series'

course_length = 10                          # Integer Value (Numeric)
average_dedication = 2.3                    # Float Value

other_courses = ['AWS', 'MySQL', 'Git', 'MongoDB']      # List Value

social_medias = ('Facebook', 'Instagram', 'Twitter', 'LinkedIn')    # Tuple Value

channel_info = {'name': 'Tech Tutorial', 'category': 'Education', 'courses': ['AWS', 'Python'], 'rating': 9.7,
                'established_date': 2021}               # Dictionary Value

play_list = {'AWS', 'Python', 'MySQL', 'Git'}           # Set Value

is_active = True                                        # Boolean Value
