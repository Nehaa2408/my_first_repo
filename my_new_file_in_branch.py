print("Simple Calculator")

n1 = float(input("Enter 1st number: "))
n2 = float(input("Enter 2nd number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1/2/3/4): ")

if choice == '1':
	print("Result:", n1 + n2)
elif choice == '2':
	print("Result:", n1 - n2)

elif choice == '3':
	print("Result:", n1 * n2)

elif choice == '4':
	if n2 != 0:
		print("Result:", n1 / n2)
	else:
		print("Cannot divide by zero")

else:
	print("Invalid choice")
	