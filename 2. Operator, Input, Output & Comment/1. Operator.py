# Operates on two or more variable and gives the result

# Arithmetic Operator
print('\n', '-'*15, 'Arithmetic Operator', '-'*15)
print('For Numeric (Int, Float, Complex)')
num_1, num_2 = 3, 2
print('num_1 and num_2 are:', num_1, 'and', num_2)
print('Addition with (+):', num_1 + num_2)
print('Difference with (-):', num_1 - num_2)
print('Product with (*):', num_1 * num_2)
print('Division with (/):', num_1 / num_2)
print('Exponent with (**):', num_1 ** num_2)
print('Integer Division with (//):', num_1 // num_2)
print('Remainder with (%):', num_1 % num_2)

print('\nFor String')
str_1, str_2 = 'Hello ', 'World'
print('First String:', str_1)
print('Second String:', str_2)
print('With (+) operator:', str_1 + str_2)

print('\nFor List and Tuple')
list_1 = ['AWS', 'Python']
list_2 = ['Git', 'Excel']
print(list_1 + list_2)

print('\nFor Set')
set_1 = {1, 2}
set_2 = {1, 3}
print(set_1 - set_2)

# Assignment Operator
print('\n', '-'*15, 'Assignment Operator', '-'*15)
num_1 = 4
num_2 = num_1
print(num_1)
print(num_2)
num_1 += 1
print('After addition of 1:', num_1)
num_1 *= 2
print('After multiplication with 2:', num_1)
num_1 -= 4
print('After subtraction by 4:', num_1)
num_1 /= 2
print('After division by 2:', num_1)
num_1 **= 3
print('After Exponent of 3:', num_1)
num_1 %= 4
print('After Modulus of 4:', num_1)
num_1 //= 2
print('After Integer Division of 2:', num_1)
print()
print('Assigning at once')
a = b = c = 55
print('Single Assignment:', a, b, c)
x, y = 10, 15
print('Assignment at once:', x, y)

# Comparison Operator
# Result of these operator is either True or False and used during Control Flow
print('\n', '-'*15, 'Comparison Operator', '-'*15)
num_1, num_2 = 5, 8
print(num_1, num_2)
print('Comparison (==):', num_1 == num_2)
print('Comparison (!=):', num_1 != num_2)
print('Comparison (>):', num_1 > num_2)
print('Comparison (<):', num_1 < num_2)
print('Comparison (>=):', num_1 >= num_2)
print('Comparison (<=):', num_1 <= num_2)


# Logical Operator
# Used to combine multiple comparison operator
print('\n', '-'*15, 'Logical Operator', '-'*15)
num_1, num_2 = 5, 8
print(num_1, num_2)
print('Comparing with > 6 condition')
print('Logical AND:', num_1 > 6 and num_2 > 6)
print('Logical OR:', num_1 > 6 or num_2 > 6)
print('Logical NOT:', not num_1 > 6)


# Bitwise Operator
print('\n', '-'*15, 'Bitwise Operator', '-'*15)
num_1, num_2 = 4, 6
print(num_1, num_2)
print('Bitwise and (&):', num_1 & num_2)
print('Bitwise or (|):', num_1 | num_2)
print('Bitwise not of num_1 (~):', ~num_1)
print('Bitwise xor (^):', num_1 ^ num_2)
print('Binary Left Shift:', num_1 << 1)
print('Binary Right Shift:', num_1 >> 1)

# For Set
representation = '''
For Set Data Type
Notation    Interpretation
---------------------------
&           Intersection
|           Union
-           Set Difference
^           Symmetric Difference
'''
print(representation)
