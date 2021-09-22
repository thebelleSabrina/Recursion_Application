"""
File: largest_digit.py
Name: Sabrina Wang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: integers
	:return: the biggest digit of the integer
	"""
	lar = 0
	return helper(n, lar)


def helper(n, lar):
	if n < 0:   # turns negative integer into positive
		n *= -1
	if n == 0:  # base-case
		return lar
	else:
		r = n % 10  # gets every digit
		if lar < r:
			lar = r
		return helper(n // 10, lar)


if __name__ == '__main__':
	main()
