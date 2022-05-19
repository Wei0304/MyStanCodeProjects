"""
File: largest_digit.py
Name: Wei
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
	:param n: input as integer
	:return: The biggest digit within the integer
	"""
	return find_largest_digit_helper(n, 0)  # must return to pass to main function



def find_largest_digit_helper(n, current_num):
	if 0 < n < 1:
		# print(current_num)
		return current_num
	elif n <= -1:
		return find_largest_digit(n*(-1))
	else:
		n1 = int(n % 10)
		if n1 > current_num:
			current_num = n1
		return find_largest_digit_helper(n/10, current_num)


if __name__ == '__main__':
	main()
