f = lambda x: x + 1
print(f(4))  # This will output: 5


lambda arguments: expression


# basic arithmetic
add = lambda x, y: x + y
print(add(5, 3))  # Outputs: 8

multiply = lambda x, y: x * y
print(multiply(5, 3))  # Outputs: 15


# sorting lists
people = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
sorted_people = sorted(people, key=lambda person: person[1])
print(sorted_people)  # Outputs: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]


# filtering
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Outputs: [2, 4, 6, 8]




# using with map()
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Outputs: [1, 4, 9, 16]

listiSemSkalVinnaMed = [random.randint(100,200) for tala in range(10)]
annadVeldi = list(map(lambda x: x**2, listiSemSkalVinnaMed))
# For each number in tolurFra100Til200, the lambda function is applied.
# The lambda function squares the number.
# map collects all these squared numbers and produces an iterator.
# list then takes this iterator and turns it into a list.


# Let's say tolurFra100Til200 is: [101, 102, 103]
# map applies the lambda function to 101, resulting in 101**2 = 10201.
# It then applies the lambda to 102, getting 102**2 = 10404.
# And again for 103, getting 103**2 = 10609.
# At this stage, we have a map object that looks something like this (in terms of values): (10201, 10404, 10609)
# Wrapping this map object with list() gives us the list: [10201, 10404, 10609].
# This list becomes the value of annadVeldi.


# checking conditions
is_positive = lambda x: x > 0
print(is_positive(-5))  # Outputs: False
print(is_positive(3))   # Outputs: True


# working with strings
reverse_str = lambda s: s[::-1]
print(reverse_str("hello"))  # Outputs: olleh


# multiple logic
divisible_by_2_and_3 = lambda x: x % 2 == 0 and x % 3 == 0
print(divisible_by_2_and_3(6))  # Outputs: True
print(divisible_by_2_and_3(8))  # Outputs: False
