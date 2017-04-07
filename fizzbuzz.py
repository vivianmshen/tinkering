#print 1 to 100
#print fizz for mult 3
#print buzz for mult 5
#print fizzbuzz for mult 3 and 5

for num in range(1,101):
	if num % 3 == 0 and num % 5 == 0:
		print("fizzbuzz")
	elif num % 3 == 0: 
		print("fizz")
	elif num % 5 == 0:
		print("buzz")
	else:
		print(num) 

