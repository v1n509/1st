
#
data = [("A", 10), ("B", 20), ("C", 30)]
print(data[1][0])
print(data[2][1])

#Count how many times each fruit appears
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
counts = {}

for fruit in fruits:
    counts[fruit] = counts.get(fruit, 0) + 1

print(counts)

#
marks = {"Math": 85, "Science": 90, "English": 78}
print(marks.get("Math"))
print(marks.get("History", 0))

