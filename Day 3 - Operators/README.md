
![Python Operators](https://www.aipython.in/wp-content/uploads/2020/04/Python-operators-1024x576.jpg)

---

## ✅ Boolean Basics

```python
print(True)   # Output: True
print(False)  # Output: False
🧠 Boolean values must be capitalized in Python (True, False)

🧮 Arithmetic Operators
Operator	Description	Example	Result
+	Addition	3 + 2	5
-	Subtraction	5 - 3	2
*	Multiplication	4 * 2	8
/	Division	6 / 2	3.0
%	Modulus	7 % 3	1
//	Floor Division	7 // 3	2
**	Exponentiation	2 ** 3	8

➗ Quick Math Example
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
# Circle
radius = 10
area = 3.14 * radius ** 2
print("Circle Area:", area)

# Rectangle
length, width = 15, 5
print("Rect Area:", length * width)
print("Rect Perimeter:", 2 * (length + width))
🧩 Comparison Operators
python
Copy
Edit
print(4 > 3)            # True
print(4 == 4)           # True
print(5 != 3)           # True
print('a' in 'banana')  # True
⚡ Logical Operators
Operator	Meaning	Example	Result
and	Both True	True and True	True
or	At least one True	True or False	True
not	Inverts value	not True	False

🧠 Mini Challenges
Declare variables: your age (int), height (float), and a complex number.

Ask user for base & height → calculate triangle area.

Ask user for 3 sides → calculate triangle perimeter.

Write script: pay = hourly_rate × hours_worked.

Build a multiplication power table:

python
Copy
Edit
print("1 1 1 1 1")
print("2 1 2 4 8")
# ...
🧠 Bonus – Slope & Distance
python
Copy
Edit
# Points
x1, y1 = 2, 2
x2, y2 = 6, 10

# Slope
slope = (y2 - y1) / (x2 - x1)
print("Slope:", slope)

# Distance
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Distance:", distance)
