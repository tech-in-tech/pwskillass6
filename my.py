# Q1. What is a tuple in Python?
# In Python, a tuple is an ordered, immutable collection of elements enclosed in parentheses ()
t1 = (1, 5, 3, 2, 9)
print(t1)



# Q2. How do you create a tuple in Python?
t2 = (0, 34, 12, 66, 78)
print(t2)



# Q3. What is the difference between a tuple and a list in Python?
# list are Mutable 
# tuple are immutable
l1 = [1, 2, 3]  # Mutable list
t3 = (1, 2, 3)  # Immutable tuple
l1[0] = 4  # Modifying list element
print(l1)  # Output: [4, 2, 3]
t3[0] = 4  # Raises TypeError: 'tuple' object does not support item assignment



# Q4. Can a tuple be changed in Python?
# No, a tuple cannot be changed in Python.



# Q5. How do you access elements in a tuple?
t4 = (1, 2, 3, 4, 5)
print(t4[0])  # Output: 1
print(t4[2])  # Output: 3



# Q6. How do you unpack a tuple in Python?
t5 = (1, 2, 3)
a, b, c = t5
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3