# Operations like addition, subtraction, multiplication, division, exponents, modulus, integer division,
# comparison can be performed on numeric data types.

# Examples
integer_sample = 5
negative_integer_sample = -20

float_sample = 2.5423456
negative_float_sample = -3.467
exponential_sample = 2.3e3
print('Exponential Sample:', exponential_sample)

complex_sample_1 = 2 + 5j
complex_sample_2 = 4 - 2j
print('Complex Addition:', complex_sample_1 + complex_sample_2)

binary_sample = 0b100
octal_sample = 0o245
hex_sample = 0xA23F
print('Hex Value:', hex_sample)


# Some Functions Associated
import math
print('\n----------- Function Associated ---------------')
print('Original Number:', float_sample)
print('Rounded Number:', round(float_sample, 2))
print('Floor Value:', math.floor(float_sample))
print('Ceiling Value:', math.ceil(float_sample))
print('Log Base2:', math.log(float_sample, 2))
print('Tan Inverse:', math.atan(float_sample))
print('GCD of 12 and 18:', math.gcd(18, 12))
