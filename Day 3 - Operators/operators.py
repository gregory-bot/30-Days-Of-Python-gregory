# 🔢 Arithmetic Operations in Python – by Gregory 🚀

# 👉 Integers
print('Addition:', 1 + 2)
print('Subtraction:', 2 - 1)
print('Multiplication:', 2 * 3)
print('Division (float):', 4 / 2)
print('Another Division:', 7 / 2)
print('Floor Division:', 7 // 2)     # Integer division
print('Modulus (Remainder):', 3 % 2)
print('Exponentiation (3^2):', 3 ** 2)

# 👉 Floating point numbers
print('Pi ≈', 3.14)
print('Gravity ≈', 9.81)

# 👉 Complex numbers
print('Complex number:', 1 + 1j)
print('Complex product:', (1 + 1j) * (1 - 1j))

# 🧠 Variable-based Arithmetic
a, b = 3, 2
print('\nUsing variables a=3, b=2:')
print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a / b =', a / b)
print('a % b =', a % b)
print('a // b =', a // b)
print('a ** b =', a ** b)

# 🎯 Grouped Example
num_one, num_two = 3, 4
print('\nWorking with num_one = 3 and num_two = 4:')
print('Total:', num_one + num_two)
print('Difference:', num_two - num_one)
print('Product:', num_one * num_two)
print('Division:', num_two / num_one)
print('Remainder:', num_two % num_one)

# 🔵 Geometry Time
radius = 10
area_circle = 3.14 * radius ** 2
print('\n🟠 Area of Circle:', area_circle)

length, width = 10, 20
area_rect = length * width
print('🟩 Area of Rectangle:', area_rect)

# 🧲 Physics Time
mass = 75  # kg
gravity = 9.81  # m/s²
weight = mass * gravity
print('\n🪨 Weight =', weight, 'N')

# 🔍 Comparison Operators
print('\n🔍 Basic Comparisons:')
print('3 > 2 →', 3 > 2)
print('3 == 2 →', 3 == 2)
print('3 != 2 →', 3 != 2)
print('len("mango") == len("avocado") →', len('mango') == len('avocado'))

# 🔗 String and Membership
print('\n🔗 String Membership:')
print('"G" in "Gregory" →', 'G' in 'Gregory')
print('"g" in "Gregory" →', 'g' in 'Gregory')
print('"coding" in "coding for all" →', 'coding' in 'coding for all')

# 🤖 Boolean Logic
print('\n🤖 Boolean Logic:')
print('True and False →', True and False)
print('True or False →', True or False)
print('not True →', not True)

# 🔍 Identity and More Fun
print('\n🔁 Identity & Power Check:')
print('1 is 1 →', 1 is 1)
print('1 is not 2 →', 1 is not 2)
print('4 is 2 ** 2 →', 4 is 2 ** 2)

# 💡 Compound Logic
print('\n💡 Compound Logic:')
print('3 > 2 and 4 > 3 →', 3 > 2 and 4 > 3)
print('3 < 2 or 4 > 3 →', 3 < 2 or 4 > 3)
print('not 3 > 2 →', not 3 > 2)
