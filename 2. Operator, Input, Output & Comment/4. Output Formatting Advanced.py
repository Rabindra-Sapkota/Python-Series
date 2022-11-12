# .format method and all its implementations

"""
<	⇒	Left align (default for most objects)
>	⇒	right align (default for number)
=	⇒	Padding after sign but before digit for numeric types
^	⇒	Center align

+	⇒	Sign should used for both positive & negative numbers
-	⇒	Sign is only used for negative number (default)
space	⇒	leading space for positive and minus sign for negative

b 	⇒	Binary Format
c	⇒	Convert integer to unicode character before print
d	⇒	Decimal format(default)
o	⇒	Octal format
x	⇒	Hex format. Alphabet in lowercase
X	⇒	Hex format. Alphabet in uppercase
n	⇒	Decimal using current locale setting to insert separator
e	⇒	Exponent notation. Precision is 6. e is used for notation
E	⇒	Same as e but notation is done by E
f	⇒	Fixed-point notation. Default precision is 6
F	⇒	Same as f but uses NAN and INF instead of nan and inf
%	⇒	Multiply the number by 100 and put a% sign. f format
g 	⇒	Generic see doc for detail
G	⇒	Same as g but notation in uppercase
"""
