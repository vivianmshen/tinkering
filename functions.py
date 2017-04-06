number1 = 5
number2 = 10

def print_none(one, two):
	return one+two

total = print_none(number1, number2)
print(total)

def uppercase_and_reverse(text):
	return text.upper()[::-1]

print(uppercase_and_reverse("vivian is the greatest"))