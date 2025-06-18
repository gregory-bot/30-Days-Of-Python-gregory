![Python Operators](https://www.aipython.in/wp-content/uploads/2020/04/Python-operators-1024x576.jpg)


✅ Boolean Basics

✅ Arithmetic, Comparison & Logical Operators

✅ Real-world Math Calculations

✅ A bunch of fun hands-on exercises 🚀

🔘 Boolean Data Type
python
Copy
Edit
print(True)   # Outputs: True
print(False)  # Outputs: False
🧠 Boolean values are either True or False and are case-sensitive in Python.

🧮 Arithmetic Operators
Operator	Description	Example	Result
+	Addition	3 + 2	5
-	Subtraction	5 - 3	2
*	Multiplication	4 * 2	8
/	Division	6 / 2	3.0
%	Modulus	7 % 3	1
//	Floor Division	7 // 3	2
**	Exponentiation	2 ** 3	8

🔧 Tip: Use // to avoid decimals when dividing whole numbers.

➗ Example: Quick Math
python
Copy
Edit
a, b = 5, 2

print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a / b =', a / b)
print('a % b =', a % b)
print('a // b =', a // b)
print('a ** b =', a ** b)
📏 Real-World Calculations
python
Copy
Edit
# Circle area
radius = 10
area = 3.14 * radius ** 2
print("Circle Area:", area)

# Rectangle area and perimeter
length, width = 15, 5
print("Rect Area:", length * width)
print("Rect Perimeter:", 2 * (length + width))
💡 Try applying this to triangles, distance, or volume!

🧩 Comparison Operators
python
Copy
Edit
print(4 > 3)      # True
print(4 == 4)     # True
print(5 != 3)     # True
print('a' in 'banana')  # True
⚡ Logical Operators
Operator	Meaning	Example	Result
and	True if both true	True and True	True
or	True if one is true	True or False	True
not	Inverts value	not True	False

🧠 Mini Challenges
Try solving these:

Declare your age (int), height (float), and a complex number.

Ask user for base & height and compute triangle area.

Ask for 3 sides and compute triangle perimeter.

Write a Python script to calculate pay based on hourly rate.

Build a table like:

python-repl
Copy
Edit
1 1 1 1 1
2 1 2 4 8
...
🧠 Bonus Exercise (Slope & Distance)
python
Copy
Edit
# Points
x1, y1 = 2, 2
x2, y2 = 6, 10

# Slope
slope = (y2 - y1) / (x2 - x1)
print("Slope:", slope)

# Euclidean Distance
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("Distance:", distance)
🎉 You’ve completed Day 3!
Tomorrow is all about Strings – the fun stuff! Stay consistent and keep coding!
