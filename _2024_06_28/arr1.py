import array

# Целые числа со знаком (signed char)
array_signed_char = array.array('b', [1, -2, 3])
print(array_signed_char)  # Output: array('b', [1, -2, 3])

# Целые числа без знака (unsigned char)
array_unsigned_char = array.array('B', [1, 2, 3])
print(array_unsigned_char)  # Output: array('B', [1, 2, 3])

# Короткие целые числа со знаком (signed short)
array_signed_short = array.array('h', [1, -2, 3])
print(array_signed_short)  # Output: array('h', [1, -2, 3])

# Короткие целые числа без знака (unsigned short)
array_unsigned_short = array.array('H', [1, 2, 3])
print(array_unsigned_short)  # Output: array('H', [1, 2, 3])

# Целые числа со знаком (signed int)
array_signed_int = array.array('i', [1, -2, 3])
print(array_signed_int)  # Output: array('i', [1, -2, 3])

# Целые числа без знака (unsigned int)
array_unsigned_int = array.array('I', [1, 2, 3])
print(array_unsigned_int)  # Output: array('I', [1, 2, 3])

# Длинные целые числа со знаком (signed long)
array_signed_long = array.array('l', [1, -2, 3])
print(array_signed_long)  # Output: array('l', [1, -2, 3])

# Длинные целые числа без знака (unsigned long)
array_unsigned_long = array.array('L', [1, 2, 3])
print(array_unsigned_long)  # Output: array('L', [1, 2, 3])

# Длинные длинные целые числа со знаком (signed long long)
array_signed_long_long = array.array('q', [1, -2, 3])
print(array_signed_long_long)  # Output: array('q', [1, -2, 3])

# Длинные длинные целые числа без знака (unsigned long long)
array_unsigned_long_long = array.array('Q', [1, 2, 3])
print(array_unsigned_long_long)  # Output: array('Q', [1, 2, 3])

# Числа с плавающей запятой (float)
array_float = array.array('f', [1.0, -2.0, 3.0])
print(array_float)  # Output: array('f', [1.0, -2.0, 3.0])

# Числа с плавающей запятой двойной точности (double)
array_double = array.array('d', [1.0, -2.0, 3.0])
print(array_double)  # Output: array('d', [1.0, -2.0, 3.0])

