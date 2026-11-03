def multiply(a, b):
	return a * b


def divide(a, b):
	if b == 0:
		return "Cannot divide by zero"
	return a / b


if __name__ == "__main__":
	print("Multiplication:", multiply(10, 5))
	print("Division:", divide(10, 5))
