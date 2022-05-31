# Stores Text Data
# Value enclosed inside single quotes (' ') or double quotes (" ") while assigning to variables.
# Triple quotes ('''  ''') can be used to store multiline string value
# If the string has to include special characters line \n we make use of escape characters.

# Examples
print('\n', '-' * 15, 'Representation', '-' * 15)
greeting = 'Hello'                    # Use of Single Quotation
programming_greeting = "Hello World"  # Use of Double Quotation


# Use of Triple Quotation
my_multiline_text = ''' Hello,                  
    This is multiline text on a variable.'''


escape_character_sample = 'Ram Said, \'I love Python\'.'    # Escape Character demo
alternative_approach_sample = "Ram Said, 'I Love Python'."  # Stored Same value without use of escape character
new_line_sample = 'Hi there,\nI love Python'                # New Line Sample
tab_sample = 'Tech\tTutorial'                               # Tab separator Sample
tab_escaped = 'Tech\\tTutorial'                             # \t escaped (Avoided being interpreted as tab character)
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
# indexing: Used to extract character from mentioned index. Starts with 0. Can be positive/negative (denoting from end)
character_p = sample_variable[14]
character_l = sample_variable[5]
character_n = sample_variable[-1]
character_o = sample_variable[-9]
print('Sample Word: ', sample_variable)
print('Character p: ', character_p)
print('Character l: ', character_l)
print('Character n: ', character_n)
print('Character o: ', character_o)


print('\n', '-' * 15, 'slicing', '-' * 15)
# slicing: Used to extract substring from string data
word_python = sample_variable[14:20]    # Extract String from index 14 to 19 (20 is exclusive)
word_fun = sample_variable[-3:]         # Extract Sting from index -3 to end
word_I_am = sample_variable[:4]         # Extract String from beginning to third index
word_lann = sample_variable[5:12:2]     # Extract String from index 5 to 11 with increment of 2
reverse_word = sample_variable[::-1]    # Extracts from beginning to end but in reverse order (Reversing)
print('Sample Word: ', sample_variable)
print('Word Python: ', word_python)
print('Word fun: ', word_fun)
print('Word I am: ', word_I_am)
print('Word lann: ', word_lann)
print('Reverse Word: ', reverse_word)


print('\n', '-' * 15, 'repetition', '-' * 15)
# repetition: Repeats the value of string
my_greet = 'Hello '
print('Sample Word: ', my_greet)
print('Two Times: ', my_greet * 2)      # Prints 'Hello Hello '
print('Three Times: ', my_greet * 3)    # Prints 'Hello Hello Hello '


print('\n', '-' * 15, 'len', '-' * 15)
# len: Calculates length of string
print('Sample Word: ', my_greet)
print('length: ', len(my_greet))  # Displays 6 as it has six characters


print('\n', '-' * 15, 'strip', '-' * 15)
# strip: Removes unwanted characters from either side of string
# Default character to strip is space
message_with_space = '   Hello, I have many spaces.    '
print('Original Message: ', message_with_space)
print('Space Trimmed: ', message_with_space.strip())  # Displays "Hello, I have many spaces."

# stripping with specified character
my_message = 'DangerThis is Super SecretDanger'
print('Sample Word: ', my_message)
print('Danger Stripped: ', my_message.strip('Danger'))              # Displays "This is Super Secret"
print('Danger Stripped at left: ', my_message.lstrip('Danger'))     # Displays "This is Super SecretDanger"
print('Danger Stripped at right: ', my_message.rstrip('Danger'))    # Displays "DangerThis is Super Secret"


print('\n', '-' * 15, 'split', '-' * 15)
# split: Separates string into multiple strings based on the separator
# default separator is space
text_to_split = "I am learning Python. Python is Fun"
print('Sample Word: ', text_to_split)
print('Default Split by space: ', text_to_split.split())
# Splitting with space as default Separator. Prints: ['I', 'am', 'learning', 'Python.', 'Python', 'is', 'Fun']

print('Splitting with . separator: ', text_to_split.split('.'))
# . as a Separator. Prints: ['I am learning Python', ' Python is Fun']


print('\n', '-' * 15, 'join', '-' * 15)
# join: joins the character of string with mentioned separator
string_to_join = 'Python'
print('Sample Word: ', string_to_join)
print('Joined with - : ', '-'.join(string_to_join))     # Displays P-y-t-h-o-n
print('Joined with ... :', '...'.join(string_to_join))   # Displays P...y...t...h...o...n


print('\n', '-' * 15, 'find and index', '-' * 15)
# find, index: Finds index of specified sub-string in a string
# find returns -1 is not match whereas index raises error if not match
my_string = 'I am learning Python'
print('Sample String: ', my_string)
print('Find Python: ', my_string.find('Python'))        # Displays 14, as Python is at 14th index
print('Find Java: ', my_string.find('Java'))            # Displays -1, as Java is not present in the string

print('Index Python: ', my_string.index('Python'))      # Displays 14, as Python is at 14th index
# print('Index Java: ', my_string.index('Java'))        # Raises error, as Java is not present in the string


# count: Counts occurrence of substring in the string
print('\n', '-' * 15, 'count', '-' * 15)
string_to_count = 'I am learning Python. Python is fun'
print('Sample Word: ', string_to_count)
print('Count of Python: ', string_to_count.count('Python'))  # Displays 2, as Python as occurred twice in the string
print('Count of fun: ', string_to_count.count('fun'))        # Displays 1, as fun as occurred once in the string
print('Count of Java: ', string_to_count.count('Java'))      # Displays 0, as Java is not present in the string


# replace: Replaces old value with new value in a string
print('\n', '-' * 15, 'replace', '-' * 15)
string_to_replace = 'I am learning Python. Python is fun'
print('Sample String: ', string_to_replace)
print('Python replaced by java: ', string_to_replace.replace('Python', 'Java'))
# Displays "I am learning Java. Java is fun"

# Replace first occurrence only
print('Python replaced by java(first occurrence only): ', string_to_replace.replace('Python', 'Java', 1))
# Displays "I am learning Java. Python is fun"


# isalpha, isdigit, isspace, isalnum: Checks if string has alphabetical, digit, space or alphanumeric values or not
print('\n', '-' * 15, 'isdigit, isalpha, isspace, isalnum', '-' * 15)
print('Check 123 is digit: ', '123'.isdigit())      # Displays True, as 123 are digits
print('Check 123a is digit: ', '123a'.isdigit())    # Displays False, as 'a' is not digit in 123a
print('Check 123 is alphabet: ', '123'.isalpha())   # Displays False, as 123 are not alphabets
print('Check abc is alphabet: ', 'abc'.isalpha())   # Displays True, as 'abc' is alphabet
print('Check  is space: ', '  '.isspace())          # Displays True, as    is space
print('Check 123a is space: ', '123a'.isspace())    # Displays False, as 'a' is not digit in 123a
print('Check 123p is alphanumeric: ', '123p'.isalnum())     # Displays True, as 123p are alphanumeric
print('Check 1a? is alphanumeric: ', '1a?'.isalnum())       # Displays False, as '1a?' is not alphanumeric

# is_lower, is_upper: Checks if string is in lowercase, uppercase or not
print('\n', '-' * 15, 'is_lower, is_upper', '-' * 15)
print('check python is lower: ', 'python'.islower())
print('check Python is lower: ', 'Python'.islower())
print('check Python is upper: ', 'Python'.isupper())
print('check PYTHON is upper: ', 'PYTHON'.isupper())
print('check python is upper: ', 'python'.isupper())


# lower, upper, capitalize, swapcase, title: Converts string value to lowercase, uppercase, capital case, swaps case
print('\n', '-' * 15, 'is_lower, is_upper', '-' * 15)
sample_word = 'i Am learning Python'
print('Sample Word: ', sample_word)
print('Upper Case: ', sample_word.upper())
print('Lower Case: ', sample_word.lower())
print('Capital Case: ', sample_word.capitalize())
print('Title Case: ', sample_word.title())
print('Swap Case: ', sample_word.swapcase())
print(sample_word.casefold())


# startswith, endswith: Checks if string startswith or endswith specified substring or not
print('\n', '-' * 15, 'startswith, endswith', '-' * 15)
sample_word = 'tech tutorial helps us to learn by doing'
print('Sample Word: ', sample_word)
print('Starts with python: ', sample_word.startswith('python'))
print('Starts with tech: ', sample_word.startswith('tech'))
print('Ends with reading: ', sample_word.endswith('reading'))
print('Ends with doing: ', sample_word.endswith('doing'))


# ord, chr: Generates ascii value from character and character from ascii value
print('\n', '-' * 15, 'ord, chr', '-' * 15)
sample_character = 'a'
sample_ascii = 66
print('Sample Character: ', sample_character)
print('Ascii value: ', ord(sample_character))
print('Sample ASCII: ', sample_ascii)
print('Character from ASCII: ', chr(sample_ascii))


# concatenation
print('\n', '-' * 15, 'concat', '-' * 15)
string_1 = '1'
string_2 = '2'
print('String 1: ', string_1)
print('String 2: ', string_2)
print('Concatenation with + operator: ', string_1 + string_2)
# Stores 12 instead of 3, as 1 and 2 are stored as string and + denotes concatenation in string
