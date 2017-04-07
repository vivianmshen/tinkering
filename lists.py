people = ["vivian", "bob", "jan"]
numbers = [0, 3, 5]
things = [True, "pop", 1]
i = 0

while i < len(people):
	things.append(people[i])
	i = i + 1

for person in people:
	numbers.append(person)
	print("person: {}".format(person))

for num in range(1,11):
	print("{} is {} when squared".format(num, num * num))

print(numbers)

