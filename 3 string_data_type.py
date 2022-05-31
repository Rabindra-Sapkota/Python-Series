# Stores Text Data
# Value enclosed inside single quotes (' ') or double quotes (" ") while assigning to variables.
# Triple quotes ('''  ''') can be used to store multiline string value
# If the string has to include special characters line \n we make use of escape characters.

# Use of Single, Double and Triple Quotation
print('\n', '-' * 15, 'Representation', '-' * 15)
greeting = 'Hello'
programming_greeting = "Hello World"
my_multiline_text = ''' Hello,                  
    This is multiline text on a variable.'''


# Use of escape character, alternative approach and special characters
escape_character_sample = 'Ram Said, \'I love Python\'.'
alternative_approach_sample = "Ram Said, 'I Love Python'."
new_line_sample = 'Hi there,\nI love Python'
tab_sample = 'Tech\tTutorial'
tab_escaped = 'Tech\\tTutorial'

print('Greeting: ', greeting)
print('Programming Greeting: ', programming_greeting)
print('Multiline text: ', my_multiline_text)
print('Escape Character Sample: ', escape_character_sample)
print('Alternative approach Sample: ', alternative_approach_sample)
print('New Line Sample: ', new_line_sample)
print('Tab Sample: ', tab_sample)
print('Tab escaped Sample: ', tab_escaped)

# Functions for String Data Type
sample_variable = 'I am learning Python from Tech Tutorial. Python is fun'


print('\n', '-' * 15, 'indexing', '-' * 15)
print('Sample Word: ', sample_variable)
print('Character p: ', sample_variable[14])
print('Character l: ', sample_variable[5])
print('Character n: ', sample_variable[-1])
print('Character o: ', sample_variable[-9])


print('\n', '-' * 15, 'slicing', '-' * 15)
print('Sample Word: ', sample_variable)
print('Word Python: ', sample_variable[14:20])
print('Word fun: ', sample_variable[-3:])
print('Word I am: ', sample_variable[:4])
print('Word lann: ', sample_variable[5:12:2])
print('Reverse Word: ', sample_variable[::-1])


print('\n', '-' * 15, 'repetition', '-' * 15)
my_greet = 'Hello '
print('Sample Word: ', my_greet)
print('Repeat Twice: ', my_greet * 2)
print('Repeat Thrice: ', my_greet * 3)


print('\n', '-' * 15, 'len', '-' * 15)
print('Sample Word: ', my_greet)
print('length: ', len(my_greet))


print('\n', '-' * 15, 'strip', '-' * 15)
message_with_space = '   Hello, I have many spaces.    '
print('Original Message: ', message_with_space)
print('Space Trimmed: ', message_with_space.strip())

# stripping with specified character
my_message = 'DangerThis is Super SecretDanger'
print('Sample Word: ', my_message)
print('Danger Stripped: ', my_message.strip('Danger'))
print('Danger Stripped at left: ', my_message.lstrip('Danger'))
print('Danger Stripped at right: ', my_message.rstrip('Danger'))


print('\n', '-' * 15, 'split', '-' * 15)
text_to_split = "I am learning Python. Python is Fun"
print('Sample Word: ', text_to_split)
print('Default Split by space: ', text_to_split.split())
print('Splitting with . separator: ', text_to_split.split('.'))


print('\n', '-' * 15, 'join', '-' * 15)
string_to_join = 'Python'
print('Sample Word: ', string_to_join)
print('Joined with - : ', '-'.join(string_to_join))
print('Joined with ... :', '...'.join(string_to_join))


print('\n', '-' * 15, 'find and index', '-' * 15)
my_string = 'I am learning Python'
print('Sample String: ', my_string)
print('Find Python: ', my_string.find('Python'))
print('Find Java: ', my_string.find('Java'))

print('Index Python: ', my_string.index('Python'))
# print('Index Java: ', my_string.index('Java'))        # Raises error, as Java is not present in the string


print('\n', '-' * 15, 'count', '-' * 15)
string_to_count = 'I am learning Python. Python is fun'
print('Sample Word: ', string_to_count)
print('Count of Python: ', string_to_count.count('Python'))
print('Count of fun: ', string_to_count.count('fun'))
print('Count of Java: ', string_to_count.count('Java'))


print('\n', '-' * 15, 'replace', '-' * 15)
string_to_replace = 'I am learning Python. Python is fun'
print('Sample String: ', string_to_replace)
print('Python replaced by java: ', string_to_replace.replace('Python', 'Java'))
print('Python replaced by java(first occurrence only): ', string_to_replace.replace('Python', 'Java', 1))


print('\n', '-' * 15, 'isdigit, isalpha, isspace, isalnum', '-' * 15)
print('Check 123 is digit: ', '123'.isdigit())
print('Check 123a is digit: ', '123a'.isdigit())
print('Check 123 is alphabet: ', '123'.isalpha())
print('Check abc is alphabet: ', 'abc'.isalpha())
print('Check  is space: ', '  '.isspace())
print('Check 123a is space: ', '123a'.isspace())
print('Check 123p is alphanumeric: ', '123p'.isalnum())
print('Check 1a? is alphanumeric: ', '1a?'.isalnum())


print('\n', '-' * 15, 'is_lower, is_upper', '-' * 15)
print('check python is lower: ', 'python'.islower())
print('check Python is lower: ', 'Python'.islower())
print('check Python is upper: ', 'Python'.isupper())
print('check PYTHON is upper: ', 'PYTHON'.isupper())
print('check python is upper: ', 'python'.isupper())


print('\n', '-' * 15, 'uppercase, lowercase, capital case, title case, swap case', '-' * 15)
sample_word = 'i Am learning Python'
print('Sample Word: ', sample_word)
print('Upper Case: ', sample_word.upper())
print('Lower Case: ', sample_word.lower())
print('Capital Case: ', sample_word.capitalize())
print('Title Case: ', sample_word.title())
print('Swap Case: ', sample_word.swapcase())
print(sample_word.casefold())


print('\n', '-' * 15, 'startswith, endswith', '-' * 15)
sample_word = 'tech tutorial helps us to learn by doing'
print('Sample Word: ', sample_word)
print('Starts with python: ', sample_word.startswith('python'))
print('Starts with tech: ', sample_word.startswith('tech'))
print('Ends with reading: ', sample_word.endswith('reading'))
print('Ends with doing: ', sample_word.endswith('doing'))


print('\n', '-' * 15, 'ord, chr', '-' * 15)
sample_character = 'a'
sample_ascii = 66
print('Sample Character: ', sample_character)
print('Ascii value: ', ord(sample_character))
print('Sample ASCII: ', sample_ascii)
print('Character from ASCII: ', chr(sample_ascii))


print('\n', '-' * 15, 'concat', '-' * 15)
string_1 = '1'
string_2 = '2'
print('String 1: ', string_1)
print('String 2: ', string_2)
print('Concatenation with + operator: ', string_1 + string_2)
